#!/usr/bin/env python3
"""Inspect serialized Unity assets; never substitute this for Unity compilation/Play.

Finds broken GUID references and material/normal-map import links. Only files on
 disk count: runtime-generated flat materials do not count as textured assets.
"""
import argparse,json,re
from pathlib import Path
GUID=re.compile(r'\bguid:\s*([a-fA-F0-9]{32})\b')
# Unity 2018 built-in UI scripts reside in the editor's UI module, not Assets.
UNITY_UI_GUIDS={
 'dc42784cf147c0c48a680349fa168899', # GraphicRaycaster
 'fe87c0e1cc204ed48ad3b37840f39efcb', # Image
 '4e29b1a8efbd4b44bb3f3716e73f07ff', # Button
 '5f7201a12d95ffc409449d95f23cf332',  # Text
 '76c392e42b5098c458856cdf6ecaaaaa1', # EventSystem
 '4f231c4fb786f3946a6b90b886c48677', # StandaloneInputModule
}
TEXT_EXT={'.unity','.prefab','.mat','.asset','.controller','.anim','.playable'}

def inspect(project):
    assets=project/'Assets'
    if not assets.is_dir(): raise ValueError(f'Not a Unity project: {project}')
    guid_paths={};duplicates=[]
    for meta in sorted(assets.rglob('*.meta')):
        match=GUID.search(meta.read_text(errors='replace'))
        if not match:continue
        guid=match.group(1).lower()
        if guid in guid_paths:duplicates.append([guid,str(guid_paths[guid]),str(meta)])
        else:guid_paths[guid]=Path(str(meta)[:-5])
    missing=[];materials=[];scenes=[]
    for path in sorted(assets.rglob('*')):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXT:continue
        data=path.read_bytes()
        if not data.startswith(b'%YAML'):continue
        text=data.decode('utf-8',errors='replace')
        for guid in set(GUID.findall(text)):
            guid=guid.lower()
            if guid.startswith('0000000000000000') or guid in UNITY_UI_GUIDS:continue # Unity built-ins.
            if guid not in guid_paths:missing.append({'file':str(path.relative_to(project)),'guid':guid})
        if path.suffix=='.unity':
            scenes.append({'path':str(path.relative_to(project)),'gameobjects':len(re.findall(r'^GameObject:',text,re.M)),'renderers':len(re.findall(r'^(?:MeshRenderer|SkinnedMeshRenderer|SpriteRenderer|Terrain|Tilemap):',text,re.M))})
        if path.suffix=='.mat':
            maps={}
            for name in ['_MainTex','_BumpMap','_MetallicGlossMap','_OcclusionMap','_EmissionMap']:
                m=re.search(r'- '+re.escape(name)+r':\s*\n\s*m_Texture:\s*\{([^}]+)\}',text)
                if not m:continue
                g=GUID.search(m.group(1))
                if not g:continue
                target=guid_paths.get(g.group(1).lower())
                maps[name]={'guid':g.group(1),'asset':str(target.relative_to(project)) if target else None}
                if target and name=='_BumpMap':
                    meta=Path(str(target)+'.meta')
                    imp=meta.read_text(errors='replace') if meta.exists() else ''
                    maps[name]['normal_import']=bool(re.search(r'^\s*textureType:\s*1\s*$',imp,re.M))
            materials.append({'path':str(path.relative_to(project)),'maps':maps})
    return {'project':str(project),'scenes':scenes,'materials':materials,
            'textured_materials':sum('_MainTex' in m['maps'] for m in materials),
            'normal_materials':sum('_BumpMap' in m['maps'] for m in materials),
            'duplicate_guids':duplicates,'unresolved_guids':missing,
            'unity_compilation':'UNRUN','play_mode':'UNRUN'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('projects',type=Path,nargs='+')
    parser.add_argument('--output',type=Path)
    parser.add_argument('--require-textures',action='store_true',help='Use only for chapters whose checklist requires textured materials.')
    args=parser.parse_args();reports=[inspect(p.resolve()) for p in args.projects]
    result=json.dumps(reports,ensure_ascii=False,indent=2)
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(result+'\n')
    else:print(result)
    for report in reports:
        if report['duplicate_guids'] or report['unresolved_guids']:raise SystemExit(1)
        if args.require_textures and not report['textured_materials']:raise SystemExit(2)
if __name__=='__main__':main()
