#!/usr/bin/env python3
"""Write native, dependency-free Unity 2018.1 scenes for book hours 1 and 2.

Only rebuild/Hour01 and rebuild/Hour02 are written. No editor/runtime generation,
external materials, MonoBehaviours, or modifications to the previous archive.
"""
from pathlib import Path
import hashlib, math, json, re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'rebuild'
MESH_GUID='0000000000000000e000000000000000'
MATERIAL_GUID='0000000000000000f000000000000000'
HEADER='%YAML 1.1\n%TAG !u! tag:unity3d.com,2011:\n'

def guid(name):return hashlib.md5(('uniytu/native-intro/'+name).encode()).hexdigest()
def vec(values, names='xyz'):
    return '{'+', '.join(f'{k}: {v:.9g}' for k,v in zip(names,values))+'}'
def quat(euler):
    # Unity Quaternion.Euler applies rotations in Z, X, Y order.
    x,y,z=(math.radians(v)*.5 for v in euler)
    sx,cx=math.sin(x),math.cos(x);sy,cy=math.sin(y),math.cos(y);sz,cz=math.sin(z),math.cos(z)
    return (cy*sx*cz+sy*cx*sz,sy*cx*cz-cy*sx*sz,cy*cx*sz-sy*sx*cz,cy*cx*cz+sy*sx*sz)

def metadata(path, scene=False, folder=False):
    key=str(path.relative_to(OUT));g=guid(key)
    content=f'fileFormatVersion: 2\nguid: {g}\n'
    if folder:content+='folderAsset: yes\n'
    content+='DefaultImporter:\n  externalObjects: {}\n  userData:\n  assetBundleName:\n  assetBundleVariant:\n'
    Path(str(path)+'.meta').write_text(content)
    return g

def gameobject(i,name,components,tag='Untagged'):
    return f'''--- !u!1 &{i}
GameObject:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  serializedVersion: 5
  m_Component:
'''+''.join(f'  - component: {{fileID: {c}}}\n' for c in components)+f'''  m_Layer: 0
  m_Name: {name}
  m_TagString: {tag}
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
'''

def transform(i,go,pos=(0,0,0),euler=(0,0,0),scale=(1,1,1),parent=0,children=(),order=0):
    return f'''--- !u!4 &{i}
Transform:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_LocalRotation: {vec(quat(euler),'xyzw')}
  m_LocalPosition: {vec(pos)}
  m_LocalScale: {vec(scale)}
  m_Children:'''+ ('\n'+''.join(f'  - {{fileID: {c}}}\n' for c in children) if children else ' []\n')+f'''  m_Father: {{fileID: {parent}}}
  m_RootOrder: {order}
  m_LocalEulerAnglesHint: {vec(euler)}
'''

def camera(pos=(0,1,-10)):
    return gameobject(100,'Main Camera',[101,102,103],'MainCamera')+transform(101,100,pos,order=0)+'''--- !u!20 &102
Camera:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {fileID: 0}
  m_PrefabInternal: {fileID: 0}
  m_GameObject: {fileID: 100}
  m_Enabled: 1
  serializedVersion: 2
  m_ClearFlags: 1
  m_BackGroundColor: {r: 0.1921569, g: 0.3019608, b: 0.4745098, a: 0}
  m_NormalizedViewPortRect:
    serializedVersion: 2
    x: 0
    y: 0
    width: 1
    height: 1
  near clip plane: 0.3
  far clip plane: 1000
  field of view: 60
  orthographic: 0
  orthographic size: 5
  m_Depth: -1
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_RenderingPath: -1
  m_TargetTexture: {fileID: 0}
  m_TargetDisplay: 0
  m_TargetEye: 3
  m_HDR: 1
  m_AllowMSAA: 1
  m_AllowDynamicResolution: 0
  m_ForceIntoRT: 0
  m_OcclusionCulling: 1
  m_StereoConvergence: 10
  m_StereoSeparation: 0.022
--- !u!81 &103
AudioListener:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {fileID: 0}
  m_PrefabInternal: {fileID: 0}
  m_GameObject: {fileID: 100}
  m_Enabled: 1
'''

def light(i=200,name='Directional Light',point=False,pos=(0,3,0),order=1):
    return gameobject(i,name,[i+1,i+2])+transform(i+1,i,pos,euler=(0,0,0) if point else (50,-30,0),order=order)+f'''--- !u!108 &{i+2}
Light:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {i}}}
  m_Enabled: 1
  serializedVersion: 8
  m_Type: {2 if point else 1}
  m_Color: {{r: 1, g: 0.95686275, b: 0.8392157, a: 1}}
  m_Intensity: 1
  m_Range: 10
  m_SpotAngle: 30
  m_CookieSize: 10
  m_Shadows:
    m_Type: {0 if point else 2}
    m_Resolution: -1
    m_CustomResolution: -1
    m_Strength: 1
    m_Bias: 0.05
    m_NormalBias: 0.4
    m_NearPlane: 0.2
  m_Cookie: {{fileID: 0}}
  m_DrawHalo: 0
  m_Flare: {{fileID: 0}}
  m_RenderMode: 0
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_Lightmapping: 4
  m_LightShadowCasterMode: 0
  m_AreaSize: {{x: 1, y: 1}}
  m_BounceIntensity: 1
  m_ColorTemperature: 6570
  m_UseColorTemperature: 0
  m_ShadowRadius: 0
  m_ShadowAngle: 0
'''

def primitive(i,name,kind='Cube',pos=(0,0,0),parent=0,children=(),order=2,euler=(0,0,0),scale=(1,1,1)):
    mesh=10202 if kind=='Cube' else 10207
    result=gameobject(i,name,[i+1,i+2,i+3,i+4])+transform(i+1,i,pos,euler,scale,parent,children,order)
    result+=f'''--- !u!33 &{i+2}
MeshFilter:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {i}}}
  m_Mesh: {{fileID: {mesh}, guid: {MESH_GUID}, type: 0}}
--- !u!23 &{i+3}
MeshRenderer:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {i}}}
  m_Enabled: 1
  m_CastShadows: 1
  m_ReceiveShadows: 1
  m_DynamicOccludee: 1
  m_MotionVectors: 1
  m_LightProbeUsage: 1
  m_ReflectionProbeUsage: 1
  m_RenderingLayerMask: 1
  m_Materials:
  - {{fileID: 10303, guid: {MATERIAL_GUID}, type: 0}}
  m_StaticBatchInfo:
    firstSubMesh: 0
    subMeshCount: 0
  m_StaticBatchRoot: {{fileID: 0}}
  m_ProbeAnchor: {{fileID: 0}}
  m_LightProbeVolumeOverride: {{fileID: 0}}
  m_ScaleInLightmap: 1
  m_PreserveUVs: 0
  m_IgnoreNormalsForChartDetection: 0
  m_ImportantGI: 0
  m_StitchLightmapSeams: 0
  m_SelectedEditorRenderState: 3
  m_MinimumChartSize: 4
  m_AutoUVMaxDistance: 0.5
  m_AutoUVMaxAngle: 89
  m_LightmapParameters: {{fileID: 0}}
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 0
'''
    if kind=='Cube':result+=f'''--- !u!65 &{i+4}
BoxCollider:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {i}}}
  m_Material: {{fileID: 0}}
  m_IsTrigger: 0
  m_Enabled: 1
  serializedVersion: 2
  m_Size: {{x: 1, y: 1, z: 1}}
  m_Center: {{x: 0, y: 0, z: 0}}
'''
    else:result+=f'''--- !u!135 &{i+4}
SphereCollider:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {i}}}
  m_Material: {{fileID: 0}}
  m_IsTrigger: 0
  m_Enabled: 1
  serializedVersion: 2
  m_Radius: 0.5
  m_Center: {{x: 0, y: 0, z: 0}}
'''
    return result

SETTINGS='''--- !u!104 &2
RenderSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 9
  m_Fog: 0
  m_FogColor: {r: 0.5, g: 0.5, b: 0.5, a: 1}
  m_FogMode: 3
  m_FogDensity: 0.01
  m_LinearFogStart: 0
  m_LinearFogEnd: 300
  m_AmbientSkyColor: {r: 0.212, g: 0.227, b: 0.259, a: 1}
  m_AmbientEquatorColor: {r: 0.114, g: 0.125, b: 0.133, a: 1}
  m_AmbientGroundColor: {r: 0.047, g: 0.043, b: 0.035, a: 1}
  m_AmbientIntensity: 1
  m_AmbientMode: 0
  m_SubtractiveShadowColor: {r: 0.42, g: 0.478, b: 0.627, a: 1}
  m_SkyboxMaterial: {fileID: 10304, guid: 0000000000000000f000000000000000, type: 0}
  m_HaloStrength: 0.5
  m_FlareStrength: 1
  m_FlareFadeSpeed: 3
  m_HaloTexture: {fileID: 0}
  m_SpotCookie: {fileID: 10001, guid: 0000000000000000e000000000000000, type: 0}
  m_DefaultReflectionMode: 0
  m_DefaultReflectionResolution: 128
  m_ReflectionBounces: 1
  m_ReflectionIntensity: 1
  m_CustomReflection: {fileID: 0}
  m_Sun: {fileID: 202}
  m_IndirectSpecularColor: {r: 0.446, g: 0.496, b: 0.575, a: 1}
  m_UseRadianceAmbientProbe: 0
'''

def save_scene(project,name,content):
    path=project/'Assets/Scenes'/f'{name}.unity'
    path.write_text(HEADER+SETTINGS+content)
    metadata(path,scene=True)
    return {'path':'Assets/Scenes/'+path.name,'guid':guid(str(path.relative_to(OUT)))}

def build_project(hour,scenes,readme):
    p=OUT/f'Hour{hour:02d}';(p/'Assets/Scenes').mkdir(parents=True,exist_ok=True);(p/'ProjectSettings').mkdir(exist_ok=True)
    metadata(p/'Assets/Scenes',folder=True)
    specs=[save_scene(p,name,content) for name,content in scenes]
    (p/'ProjectSettings/ProjectVersion.txt').write_text('m_EditorVersion: 2018.1.0f1\n')
    (p/'ProjectSettings/EditorBuildSettings.asset').write_text(HEADER+'''--- !u!1045 &1
EditorBuildSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_Scenes:
'''+''.join(f'  - enabled: 1\n    path: {s["path"]}\n    guid: {s["guid"]}\n' for s in specs)+ '  m_configObjects: {}\n')
    (p/'ОТКРЫТЬ.md').write_text(readme)
    (p/'scene_manifest.json').write_text(json.dumps({'hour':hour,'version':'2018.1.0f1','runtime_scripts':0,'scenes':specs,'validation':'Static serialized-reference checks only; Unity deserialization and Play have not run.'},ensure_ascii=False,indent=2)+'\n')
    (p/'.gitignore').write_text('Library/\nTemp/\nObj/\nLogs/\n*.csproj\n*.sln\n')
    return p

def validate(project):
    for path in (project/'Assets/Scenes').glob('*.unity'):
        text=path.read_text();ids=set(re.findall(r'^--- !u!\d+ &(\d+)',text,re.M))
        assert len(ids)==len(re.findall(r'^--- !u!',text,re.M))
        for match in re.finditer(r'\{fileID: (\d+)([^}]*)\}',text):
            value,tail=match.groups()
            assert value=='0' or 'guid:' in tail or value in ids,(path,value)
        assert 'MonoBehaviour:' not in text
        assert text.count('AudioListener:')==1
        assert text.count('Camera:')==1
        assert 'm_Mesh: {fileID: 10202,' in text or path.stem=='01_NewProject'
        assert guid(str(path.relative_to(OUT))) in Path(str(path)+'.meta').read_text()
    return len(list((project/'Assets/Scenes').glob('*.unity')))

def main():
    default=camera()+light()
    p1=build_project(1,[
        ('03_Exercise_Cube',default+primitive(1000,'Cube')),
        ('01_NewProject',default),
        ('02_EditorNavigation',default+primitive(1000,'Cube')),
    ],'''# Час 1 — введение в Unity

Открытие без Unity Hub: File → Open Project → выберите папку Hour01. Затем в Project откройте Assets/Scenes/03_Exercise_Cube.unity. Сцена уже сохранена: Cube, Main Camera, Directional Light. Нажмите Play. Здесь ещё нет управления игроком: глава посвящена самому редактору.

| Книга | Сохранённый результат |
|---|---|
| Практикум «Создание первого проекта», стр. 29–30 | 01_NewProject: новая 3D-сцена с камерой и направленным светом, без дополнительных пакетов. Имя папки поставки Hour01; книга предлагает имя проекта Hour 1 TIY. |
| Панели Project, Hierarchy, Inspector, Scene, Game, стр. 31–42 | 02_EditorNavigation: куб для выделения и изучения Inspector; папка Scenes. Layout редактора пользовательский и в проект не встраивается. |
| Hand, Flythrough, сочетания клавиш, стр. 42–44 | 02_EditorNavigation: ориентир Cube. Q — Hand; F — фокус; ПКМ+WASD — Flythrough; Alt+мышь — орбита. Эти действия нужно выполнить в Scene лично. |
| Итоговое упражнение, стр. 46–47 | 03_Exercise_Cube: сохранённая сцена в Assets/Scenes, куб со стандартными MeshFilter, MeshRenderer и BoxCollider. |

Текстуры, UV-развёртка и normal mapping в первом часе ещё не задаются; здесь оставлен стандартный материал Unity, как при Create → 3D Object → Cube. Дополнительный интерфейс и скрипты не добавлены.

Статически проверены локальные fileID, встроенные ссылки на меш/материал и scene GUID. Фактический импорт и Play в Unity 2018.1.0f1 здесь не запускались. Готовность к сдаче этим не подтверждается.
''')
    objects=default+gameobject(300,'GameObject',[301])+transform(301,300,order=2)+primitive(1000,'Cube',order=3)+light(400,'Point Light',True,(0,3,-2),4)
    hierarchy=camera((0,2.5,-12))+light()+primitive(1000,'Cube',pos=(0,2,-5),children=(1101,))+primitive(1100,'Sphere','Sphere',pos=(0,1,0),parent=1001,order=0)
    transformed=camera((0,2.5,-12))+light()+primitive(1000,'Cube',pos=(0,2,-5),children=(1101,),euler=(0,0,45),scale=(1.5,1.5,1.5))+primitive(1100,'Sphere','Sphere',pos=(0,1,0),parent=1001,order=0)
    p2=build_project(2,[
        ('03_Exercise_ParentChild',hierarchy),
        ('01_GameObjects',objects),
        ('02_TransformTools',default+primitive(1000,'Cube',pos=(1,0,0),euler=(0,0,90),scale=(1,1,1))),
        ('04_ParentTransformExperiment',transformed),
    ],'''# Час 2 — игровые объекты и преобразования

Откройте папку Hour02 через File → Open Project. Откройте Assets/Scenes/03_Exercise_ParentChild.unity: Cube — корневой объект, Sphere — дочерний. Объекты уже сохранены в сцене, их не создаёт скрипт при Play.

| Книга | Сцена и точные свойства |
|---|---|
| Практикум «Создание игровых объектов», стр. 52–53 | 01_GameObjects: пустой GameObject с одним Transform; Cube с MeshFilter, MeshRenderer, BoxCollider; дополнительный Point Light; стандартные камера и Directional Light. |
| Перемещение, вращение, масштаб, Local/Global и Pivot/Center, стр. 53–60 | 02_TransformTools: Cube в (1,0,0), Z=90°. Сцена даёт объект для инструментов W/E/R и сравнения порядка преобразований. Local/Global и Pivot/Center нужно переключать лично в редакторе. |
| Итоговое упражнение, стр. 63 | 03_Exercise_ParentChild: Cube world (0,2,-5), Rotation (0,0,0), Scale (1,1,1). Sphere local (0,1,0), Rotation (0,0,0), Scale (1,1,1); её мировое положение (0,3,-5). |
| Эксперимент с родительским преобразованием, пункт 6, стр. 63 | 04_ParentTransformExperiment: родитель Cube повёрнут на Z=45° и равномерно увеличен до 1.5, а числовые локальные значения дочерней Sphere сохранены. Сравните с 03_Exercise_ParentChild. |

Текстурирование и normal mapping рассматриваются в следующем часе, поэтому первые два часа используют стандартный материал Unity. Никакие общие скрипты, UI, Timeline или пакеты других глав в проект не включены.

Проверены структура локальных fileID, ссылки на встроенные меши Cube (10202) / Sphere (10207), GUID сцен, parent/children и числовые transform. Десериализация и Play в Unity 2018.1.0f1 здесь не запускались.
''')
    print(json.dumps({'projects':2,'native_scenes':validate(p1)+validate(p2),'MonoBehaviour_count':0,'unity_run':False}))
if __name__=='__main__':main()
