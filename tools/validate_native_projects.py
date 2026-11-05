#!/usr/bin/env python3
"""Structural validation for saved Unity scenes, not Unity runtime validation.

Checks YAML deserialization, local references, bidirectional component/parent
links, GUID resolution, actual saved renderer objects and script dependencies.
"""
from pathlib import Path
import argparse,json,re
import yaml
from inspect_unity_assets import inspect
HEADER=re.compile(r'^--- !u!(\d+) &(\d+).*$',re.M)

def documents(path):
    raw=path.read_text();parts=list(HEADER.finditer(raw));docs={}
    for i,match in enumerate(parts):
        fileid=int(match.group(2));assert fileid not in docs,('duplicate fileID',path,fileid)
        stop=parts[i+1].start() if i+1<len(parts) else len(raw)
        docs[fileid]=yaml.safe_load(raw[match.end():stop])
    assert docs,('No saved YAML objects',path)
    return docs

def refs(value):
    if isinstance(value,dict):
        if 'fileID' in value and 'guid' not in value:yield value['fileID']
        for child in value.values():yield from refs(child)
    elif isinstance(value,list):
        for child in value:yield from refs(child)

def validate(project):
    report=inspect(project);assert not report['unresolved_guids'],report['unresolved_guids'];assert not report['duplicate_guids'],report['duplicate_guids']
    counts={}
    for path in sorted((project/'Assets/Scenes').glob('*.unity')):
        docs=documents(path)
        for fileid,doc in docs.items():
            for ref in refs(doc):assert ref==0 or ref in docs,('dangling local ref',path,fileid,ref)
            if 'GameObject' in doc:
                go=doc['GameObject']
                for component in go.get('m_Component',[]):
                    cid=component['component']['fileID'];c=next(iter(docs[cid].values()))
                    assert c.get('m_GameObject',{}).get('fileID')==fileid,('wrong component owner',path,fileid,cid)
            if 'Transform' in doc or 'RectTransform' in doc:
                t=doc.get('Transform',doc.get('RectTransform'))
                if 'm_Father' not in t:
                    # Classic linked-prefab stripped Transform: state comes from
                    # the external prefab, not duplicated local serialized fields.
                    target=t.get('m_PrefabParentObject',{})
                    assert target.get('guid') and target.get('fileID'),('invalid stripped transform',path,fileid)
                    owner=t.get('m_PrefabInternal',{}).get('fileID')
                    assert owner in docs and 'Prefab' in docs[owner],('stripped transform owner',path,fileid)
                    prefab=docs[owner]['Prefab']['m_ParentPrefab']
                    assert prefab['guid']==target['guid'],('stripped prefab target mismatch',path,fileid)
                    continue
                parent=t['m_Father']['fileID']
                if parent:
                    pd=docs[parent];children=pd.get('Transform',pd.get('RectTransform'))['m_Children']
                    assert any(c['fileID']==fileid for c in children),('missing child in parent',path,fileid)
                for child in t['m_Children']:
                    cd=docs[child['fileID']];assert cd.get('Transform',cd.get('RectTransform'))['m_Father']['fileID']==fileid,('wrong child parent',path,fileid)
        cameras=[v for v in docs.values() if 'Camera' in v]
        listeners=[v for v in docs.values() if 'AudioListener' in v]
        assert len(cameras)==len(listeners)==1,('camera/listener count',path)
        counts[path.name]={'serialized_objects':len(docs),'renderers':sum('MeshRenderer' in d for d in docs.values()),'behaviours':sum('MonoBehaviour' in d for d in docs.values()),'prefab_instances':sum('Prefab' in d and d['Prefab'].get('m_IsPrefabParent')==0 for d in docs.values())}
    assert counts,('No scenes',project)
    build=documents(project/'ProjectSettings/EditorBuildSettings.asset')
    settings=next(iter(build.values()))['EditorBuildSettings']
    guid_map={p['path']:p['guid'] for p in settings['m_Scenes']}
    for name in counts:
        scene=project/'Assets/Scenes'/name
        meta=Path(str(scene)+'.meta').read_text()
        assert guid_map['Assets/Scenes/'+name] in meta,('Wrong scene BuildSettings GUID',scene)
    assert (project/'ProjectSettings/ProjectVersion.txt').read_text().strip()=='m_EditorVersion: 2018.1.0f1'
    return {'hour':int(project.name[4:]),'scene_count':len(counts),'scenes':counts,'structural_check':'PASS','unity_import':'UNRUN','unity_compilation':'UNRUN','play':'UNRUN'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('projects',type=Path,nargs='+');p.add_argument('--output',type=Path);a=p.parse_args();reports=[validate(path.resolve()) for path in a.projects]
    result=json.dumps(reports,ensure_ascii=False,indent=2)
    if a.output:a.output.write_text(result+'\n')
    else:print(result)
    print(f"PASS: structural validation of {sum(r['scene_count'] for r in reports)} saved scenes across {len(reports)} projects. Unity checks UNRUN.")
if __name__=='__main__':main()
