#!/usr/bin/env python3
"""Native old-format Unity 2018.1 Prefab assets and connected Hour11 scenes.
Format cross-checked with the official Unity Standard-Assets-Characters repository
build-10 c241d4d003e1aa6854ced6f83e7b87f7c7d98a23, retained OldBase examples.
No assets from that reference repository are copied into the deliverable.
"""
from pathlib import Path
import json,re
import build_native_intro as n
from build_native_scripting import write_script,behaviour
ROOT=Path(__file__).resolve().parents[1]
P=n.OUT/'Hour11'
PREFAB_ID=100100000


def rigidbody(i,go):
    return f'''--- !u!54 &{i}
Rigidbody:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  serializedVersion: 2
  m_Mass: 1
  m_Drag: 0
  m_AngularDrag: 0.05
  m_UseGravity: 1
  m_IsKinematic: 0
  m_Interpolate: 0
  m_Constraints: 0
  m_CollisionDetection: 0
'''


def sphere_light(color):
    text=n.light(1103,'unused',True)
    text=text[text.index('--- !u!108'):]
    # Light component ID1105, on Sphere GO1100 rather than a separate light GO.
    text=text.replace('m_GameObject: {fileID: 1103}','m_GameObject: {fileID: 1100}')
    text=text.replace('m_Color: {r: 1, g: 0.95686275, b: 0.8392157, a: 1}',f'm_Color: {{r: {color[0]}, g: {color[1]}, b: {color[2]}, a: 1}}')
    return text


def lamp_objects(pos=(-1,0,-5),color=(1,1,1)):
    lamp=n.primitive(1000,'Lamp',pos=pos,scale=(.5,2,.5),children=(1101,),order=0)
    lamp=lamp.replace('  - component: {fileID: 1004}\n','  - component: {fileID: 1004}\n  - component: {fileID: 1005}\n')
    sphere=n.primitive(1100,'Sphere',kind='Sphere',pos=(0,.6,0),scale=(2,.5,2),parent=1001,order=0)
    sphere=sphere.replace('  - component: {fileID: 1104}\n','  - component: {fileID: 1104}\n  - component: {fileID: 1105}\n')
    return lamp+rigidbody(1005,1000)+sphere+sphere_light(color)


def write_prefab(name,color):
    path=P/'Assets/Prefabs'/name;path.parent.mkdir(parents=True,exist_ok=True)
    n.metadata(path.parent,folder=True)
    objects=lamp_objects(color=color)
    # All objects/components belong to this asset's classic Prefab object.
    objects=objects.replace('m_PrefabInternal: {fileID: 0}',f'm_PrefabInternal: {{fileID: {PREFAB_ID}}}')
    # As in Unity's own old native prefab serialization: only root GO has hideFlags0.
    docs=re.split(r'(?=^--- !u!)',objects,flags=re.M)
    for k,doc in enumerate(docs):
        if doc and not doc.startswith('--- !u!1 &1000\n'):
            docs[k]=doc.replace('m_ObjectHideFlags: 0','m_ObjectHideFlags: 1',1)
    objects=''.join(docs)
    text=n.HEADER+f'''--- !u!1001 &{PREFAB_ID}
Prefab:
  m_ObjectHideFlags: 1
  serializedVersion: 2
  m_Modification:
    m_TransformParent: {{fileID: 0}}
    m_Modifications: []
    m_RemovedComponents: []
  m_ParentPrefab: {{fileID: 0}}
  m_RootGameObject: {{fileID: 1000}}
  m_IsPrefabParent: 1
'''+objects
    path.write_text(text)
    g=n.guid(str(path.relative_to(n.OUT)))
    Path(str(path)+'.meta').write_text(f'''fileFormatVersion: 2
guid: {g}
NativeFormatImporter:
  externalObjects: {{}}
  mainObjectFileID: {PREFAB_ID}
  userData:
  assetBundleName:
  assetBundleVariant:
''')
    return g


def modification(guid,target,path,value):
    return f'''    - target: {{fileID: {target}, guid: {guid}, type: 2}}
      propertyPath: {path}
      value: {value}
      objectReference: {{fileID: 0}}
'''


def instance(i,guid,pos,order=2,name='Lamp',white_override=False):
    mods=''
    for axis,value in zip('xyz',pos):mods+=modification(guid,1001,'m_LocalPosition.'+axis,value)
    mods+=modification(guid,1001,'m_RootOrder',order)
    mods+=modification(guid,1000,'m_Name',name)
    if white_override:
        for axis in 'rgba':mods+=modification(guid,1105,'m_Color.'+axis,1)
    return f'''--- !u!1001 &{i}
Prefab:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_Modification:
    m_TransformParent: {{fileID: 0}}
    m_Modifications:
'''+mods+f'''    m_RemovedComponents: []
  m_ParentPrefab: {{fileID: {PREFAB_ID}, guid: {guid}, type: 2}}
  m_IsPrefabParent: 0
--- !u!4 &{i+1} stripped
Transform:
  m_PrefabParentObject: {{fileID: 1001, guid: {guid}, type: 2}}
  m_PrefabInternal: {{fileID: {i}}}
'''


def plane(i,name,pos=(0,0,0),euler=(0,0,0)):
    text=n.primitive(i,name,pos=pos,euler=euler)
    text=text[:text.index(f'--- !u!65 &{i+4}')]
    text=text.replace('m_Mesh: {fileID: 10202,','m_Mesh: {fileID: 10209,')
    return text+f'''--- !u!64 &{i+4}
MeshCollider:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {i}}}
  m_Material: {{fileID: 0}}
  m_IsTrigger: 0
  m_Enabled: 1
  serializedVersion: 3
  m_Convex: 0
  m_CookingOptions: 30
  m_Mesh: {{fileID: 10209, guid: {n.MESH_GUID}, type: 0}}
'''


def lamps(guid,override=False):
    content=n.camera((0,4,-12))+n.light()+plane(2000,'Floor')
    for k,(x,z) in enumerate([(-3,-3),(3,-3),(-3,3),(3,3)]):
        content+=instance(6000+k*10,guid,(x,1,z),order=3+k,name='Lamp '+str(k+1),white_override=override and k==0)
    return content


def validate():
    metas={}
    for meta in (P/'Assets').rglob('*.meta'):
        match=re.search(r'^guid: (\w+)',meta.read_text(),re.M)
        if match:metas[match.group(1)]=Path(str(meta)[:-5])
    builtins={n.MESH_GUID,n.MATERIAL_GUID}
    documents=list((P/'Assets').rglob('*.unity'))+list((P/'Assets').rglob('*.prefab'))
    instances=0
    for path in documents:
        text=path.read_text();ids=re.findall(r'^--- !u!\d+ &(\d+)',text,re.M)
        assert len(ids)==len(set(ids)),path
        for value,tail in re.findall(r'\{fileID: (\d+)([^}]*)\}',text):
            if value=='0':continue
            match=re.search(r'guid: (\w+)',tail)
            if match:
                g=match.group(1);assert g in metas or g in builtins,(path,g)
                if g in metas and metas[g].suffix=='.prefab':
                    external=metas[g].read_text();assert re.search(r'^--- !u!\d+ &'+value+r'(?:\s|$)',external,re.M),(path,value,g)
            else:assert value in ids,(path,value)
        if path.suffix=='.unity':instances+=text.count('m_IsPrefabParent: 0')
    main=(P/'Assets/Prefabs/Lamp.prefab').read_text()
    assert 'Rigidbody:' in main and 'm_GameObject: {fileID: 1000}' in main
    assert 'm_LocalPosition: {x: -1, y: 0, z: -5}' in main
    assert 'm_LocalScale: {x: 0.5, y: 2, z: 0.5}' in main
    assert 'm_LocalPosition: {x: 0, y: 0.6, z: 0}' in main
    assert 'm_LocalScale: {x: 2, y: 0.5, z: 2}' in main
    final=(P/'Assets/Scenes/06_Exercise_Spawn.unity').read_text()
    assert 'Directional Light' not in final
    assert 'prefab: {fileID: 1000, guid:' in final
    assert 'm_LocalPosition: {x: 1, y: 1, z: -5}' in final
    assert 'm_LocalEulerAnglesHint: {x: 270, y: 0, z: 0}' in final
    return {'hour':11,'native_scenes':6,'old_format_prefab_assets':2,'connected_instances':instances,'native_external_and_internal_refs':'PASS','unity_import':'UNRUN','unity_api_compile':'UNRUN','play_mode':'UNRUN'}


def main():
    prefab_guid=write_prefab('Lamp.prefab',(1,1,1))
    red_guid=write_prefab('UpdateStages/Lamp_RedSnapshot.prefab',(1,0,0))
    script_guid=write_script(P,'PrefabGenerator','''using UnityEngine;
// Book Hour11, printed pp.230-231. Reference is assigned to the real Lamp asset.
public class PrefabGenerator : MonoBehaviour
{
    public GameObject prefab;
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.B))
        {
            Instantiate(prefab);
        }
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Instantiate(prefab, transform.position, transform.rotation);
        }
    }
}''')
    final=n.camera((0,1,-12))+plane(2000,'Plane',(0,0,-4),(270,0,0))
    final+=n.gameobject(3000,'Spawn Point',[3001,3002])+n.transform(3001,3000,(1,1,-5),order=2)+behaviour(3002,3000,script_guid,f'  prefab: {{fileID: 1000, guid: {prefab_guid}, type: 2}}\n')
    # Avoid a dangling RenderSettings Sun reference in a scene without DirectionalLight.
    scenes=[('06_Exercise_Spawn',final),('01_CreateLamp',n.camera((0,1.5,-10))+n.light()+instance(6000,prefab_guid,(0,1,0))),('Lamps',lamps(prefab_guid)),('03_AssetRedSnapshot',lamps(red_guid)),('04_OneWhiteOverride',lamps(red_guid,True)),('05_AfterApplyWhite',lamps(prefab_guid))]
    n.build_project(11,scenes,'''# Час 11 — настоящие префабы Unity 2018.1

Открытие без Hub: File → Open Project → папка Hour11. Откройте **Assets/Scenes/06_Exercise_Spawn.unity**. В сцене уже есть Main Camera, Plane и Spawn Point; Directional Light удалён, как в задании. На Spawn Point назначен PrefabGenerator с прямой ссылкой на Assets/Prefabs/Lamp.prefab. Play: B создаёт префаб в его сохранённой позиции (−1,0,−5), Space — в позиции Spawn Point (1,1,−5). Создаваемый объект содержит Rigidbody, дочернюю Sphere и её Light. Из-за гравитации координаты начнут меняться после создания; для проверки поставьте Pause/Step.

Это native `.prefab` и связанные экземпляры старого формата Unity до 2018.3, а не копии отдельных GameObject и не фабрика сцены на старте.

| Практикум книги | Сохранённый результат |
|---|---|
| Создание префаба, стр.224–225 | 01_CreateLamp: связанный Lamp в (0,1,0), scale(.5,2,.5), Rigidbody; Sphere — дочерняя, world(0,2.2,0), её локальная позиция(0,.6,0), localScale(2,.5,2), что сохраняет её мировой масштаб1. Light находится на самой Sphere. |
| Несколько экземпляров, стр.226 | Lamps: Plane Floor в начале координат и четыре связанных экземпляра по углам. Точные координаты углов книга не задаёт; выбраны ±3 по X/Z. Floor использует встроенный Plane mesh и MeshCollider. |
| Изменить ассет на красный, стр.227–228 | 03_AssetRedSnapshot: четыре экземпляра отдельного исторического Lamp_RedSnapshot.prefab; свет наследует красный из ассета. Это явно сохранённый этап, а не новый механизм prefab variants. |
| Один локальный белый override, стр.227 | 04_OneWhiteOverride: тот же красный ассет, первая лампа имеет реальные Prefab property modifications m_Color.r/g/b/a=1 на дочернем Light; остальные наследуют красный. |
| Результат Apply белого, стр.227–228 | 05_AfterApplyWhite: четыре экземпляра основного белого Lamp.prefab, без локальных цветовых override. Реальную последовательность редактирования/Apply выполните по памятке ниже. |
| Итоговое упражнение, стр.230–231 | 06_Exercise_Spawn: PrefabGenerator из двух вызовов Instantiate, Plane (0,0,−4), rotation(270,0,0), Spawn Point(1,1,−5), prefab root(−1,0,−5). |

Основной Lamp.prefab сохранён в конечной позиции итогового упражнения. Более ранние сцены сохраняют позиции их экземпляров через штатные prefab overrides. Красный ассет — отдельный снимок промежуточного этапа только для демонстрации, не заявленный оригинальный файл автора.

## Редакторные действия наследования

Откройте Lamps. Выберите основной Lamp.prefab в Project, разверните Sphere и сделайте её Light красным: все четыре лампы должны обновиться. Выберите Sphere только одной лампы в Hierarchy и верните белый: три другие должны остаться красными. Выберите корневой экземпляр Lamp и нажмите Apply в Inspector: после этого все станут белыми. Эти взаимодействия с редактором здесь не выполнялись; готовые снимки показывают нужные состояния для сравнения.

Для связанной темы «Разрыв связи» (стр.228) сначала сохраните копию сцены. Выберите экземпляр, GameObject → Break Prefab Instance; проверьте, что дальнейшее изменение ассета его не затрагивает. Используйте Revert в Inspector, чтобы восстановить связь. Не выдавайте обычную несвязанную копию объекта за результат проверки prefab inheritance.

В главе 11 для Lamp не заданы текстуры/normal mapping. Оставлены стандартные встроенные меши/материал; это не отсутствие требуемого текстурирования.

## Что проверено

Проверены GUID и локальные/внешние fileID, принадлежность всех частей Prefab asset, поля старой связанной prefab instance, реальный Light override, Rigidbody, transforms и ссылка скрипта на основной Prefab. Формат сопоставлен с сохранёнными старыми native файлами официального Unity Standard-Assets-Characters. Импорт, разрешение prefab connections в Inspector, компиляция и Play в Unity 2018.1.0f1 **не запускались**; применять результат как проверенную работу для сдачи пока нельзя.
''')
    final_path=P/'Assets/Scenes/06_Exercise_Spawn.unity'
    final_path.write_text(final_path.read_text().replace('m_Sun: {fileID: 202}','m_Sun: {fileID: 0}'))
    result=validate()
    manifest_path=P/'scene_manifest.json';manifest=json.loads(manifest_path.read_text());manifest.update(result);manifest['runtime_scripts']=1;manifest['source_requirements']=['11-P01','11-P02','11-P03','11-E01'];manifest['prefab_assets']=['Assets/Prefabs/Lamp.prefab','Assets/Prefabs/UpdateStages/Lamp_RedSnapshot.prefab'];manifest['source_format_reference']='Unity-Technologies/Standard-Assets-Characters @ c241d4d003e1aa6854ced6f83e7b87f7c7d98a23, OldBase native files (no third-party assets copied)';manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'audit').mkdir(parents=True,exist_ok=True)
    (ROOT/'audit/native-hour11-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
