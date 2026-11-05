#!/usr/bin/env python3
"""Saved Unity 2018.1.0f1 scenes for all Hour09 physics practica.
No runtime geometry factories, no UI overlays, no cross-hour scripts.
PhysicMaterial experiments use clearly named independently authored assets.
"""
from pathlib import Path
import json,re,shutil
import build_native_intro as n
from build_native_scripting import write_script,behaviour,validate_project
ROOT=Path(__file__).resolve().parents[1]
P=n.OUT/'Hour09'


def rigidbody(i,go,gravity=True,constraints=0,drag=0):
    return f'''--- !u!54 &{i}
Rigidbody:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  serializedVersion: 2
  m_Mass: 1
  m_Drag: {drag}
  m_AngularDrag: 0.05
  m_UseGravity: {int(gravity)}
  m_IsKinematic: 0
  m_Interpolate: 0
  m_Constraints: {constraints}
  m_CollisionDetection: 0
'''


def add_component(text,go,component):
    anchor=f'  - component: {{fileID: {go+4}}}\n'
    assert anchor in text
    return text.replace(anchor,anchor+f'  - component: {{fileID: {component}}}\n',1)


def shape(i,name,kind='Cube',pos=(0,0,0),scale=(1,1,1),euler=(0,0,0),body=False,gravity=True,constraints=0,drag=0,trigger=False,material=None,sphere_collider=False,script=None,fields=''):
    t=n.primitive(i,name,kind=kind,pos=pos,scale=scale,euler=euler)
    if sphere_collider and kind=='Cube':
        t=t[:t.index('--- !u!65')]+n.primitive(i,name,kind='Sphere')[n.primitive(i,name,kind='Sphere').index('--- !u!135'):]
    if trigger:t=t.replace('  m_IsTrigger: 0','  m_IsTrigger: 1')
    if material:t=t.replace('  m_Material: {fileID: 0}',f'  m_Material: {{fileID: 13400000, guid: {material}, type: 2}}')
    if body:t=add_component(t,i,i+5)+rigidbody(i+5,i,gravity,constraints,drag)
    if script:t=add_component(t,i,i+6)+behaviour(i+6,i,script,fields)
    return t


def physical_material(name,dynamic,static,bounce,friction_combine,bounce_combine):
    path=P/'Assets/PhysicsMaterials'/(name+'.physicMaterial')
    path.parent.mkdir(parents=True,exist_ok=True);n.metadata(path.parent,folder=True)
    path.write_text(n.HEADER+f'''--- !u!134 &13400000
PhysicMaterial:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_Name: {name}
  dynamicFriction: {dynamic}
  staticFriction: {static}
  bounciness: {bounce}
  frictionCombine: {friction_combine}
  bounceCombine: {bounce_combine}
''')
    g=n.guid(str(path.relative_to(n.OUT)))
    Path(str(path)+'.meta').write_text(f'''fileFormatVersion: 2
guid: {g}
NativeFormatImporter:
  externalObjects: {{}}
  mainObjectFileID: 13400000
  userData: Independently authored study material; not the Standard Assets original.
  assetBundleName:
  assetBundleVariant:
''')
    return g


def build():
    scripts={
    'MovementScript':'''using UnityEngine;
// Printed p.197: the mouse-trigger practicum uses Transform motion as shown.
public class MovementScript : MonoBehaviour
{
    void Update()
    {
        float mX = Input.GetAxis("Mouse X") / 10f;
        float mY = Input.GetAxis("Mouse Y") / 10f;
        transform.Translate(mX, mY, 0f);
    }
}''',
    'TriggerScript':'''using UnityEngine;
// Printed pp.197,201-202: same callbacks, with trigger-name mode for the exercise.
public class TriggerScript : MonoBehaviour
{
    public bool reportTriggerName;
    void OnTriggerEnter(Collider other)
    {
        if (reportTriggerName)
            print(gameObject.name + ": вход — " + other.gameObject.name);
        else
            print(other.gameObject.name + " has entered the cube");
    }
    void OnTriggerStay(Collider other)
    {
        if (reportTriggerName)
            print(gameObject.name + ": нахождение внутри — " + other.gameObject.name);
        else
            print(other.gameObject.name + " is still in the cube");
    }
    void OnTriggerExit(Collider other)
    {
        if (reportTriggerName)
            print(gameObject.name + ": выход — " + other.gameObject.name);
        else
            print(other.gameObject.name + " has left the cube");
    }
}''',
    'RaycastScript':'''using UnityEngine;
// Printed pp.199-200: cast every frame, without a click-to-fire requirement.
public class RaycastScript : MonoBehaviour
{
    void Update()
    {
        float dirX = Input.GetAxis("Mouse X");
        float dirY = Input.GetAxis("Mouse Y");
        transform.Rotate(dirY, dirX, 0f);
        CheckForRaycastHit();
    }
    void CheckForRaycastHit()
    {
        RaycastHit hit;
        if (Physics.Raycast(transform.position, transform.forward, out hit))
        {
            print(hit.collider.gameObject.name + " destroyed!");
            Destroy(hit.collider.gameObject);
        }
    }
}''',
    'MotionScript':'''using UnityEngine;
// Final exercise p.201-202: world X/Z arrow input through the physics step.
[RequireComponent(typeof(Rigidbody))]
public class MotionScript : MonoBehaviour
{
    public float speed = 2f;
    Rigidbody body;
    void Awake()
    {
        body = GetComponent<Rigidbody>();
    }
    void FixedUpdate()
    {
        Vector3 movement = new Vector3(Input.GetAxisRaw("Horizontal"), 0f,
            Input.GetAxisRaw("Vertical"));
        body.MovePosition(body.position + movement * speed * Time.fixedDeltaTime);
    }
}'''
    }
    gs={name:write_script(P,name,source) for name,source in scripts.items()}
    default=n.camera()+n.light()
    scenes=[]
    # First scene is the final exercise, ready to inspect before Play.
    exercise=default
    for i,x,name in [(1000,-1.5,'LTrigger'),(1100,1.5,'RTrigger')]:
        exercise+=shape(i,name,pos=(x,0,-5),scale=(.1,2,2),trigger=True,script=gs['TriggerScript'],fields='  reportTriggerName: 1\n')
    exercise+=shape(1200,'Sphere',kind='Sphere',pos=(0,0,-5),body=True,gravity=False,script=gs['MotionScript'],fields='  speed: 2\n')
    scenes.append(('06_Exercise_TwoTriggers',exercise))
    for label,body,drag,constraints in [('01a_Rigidbody_Baseline',False,0,0),('01b_Rigidbody_Gravity',True,0,0),('01c_Rigidbody_DragStudy',True,5,0),('01d_Rigidbody_FreezeYStudy',True,0,4)]:
        scenes.append((label,default+shape(1000,'Cube',pos=(0,1,-5),body=body,drag=drag,constraints=constraints)))
    for name,constraints,sphere,euler in [('02a_Colliders_Unrestrained',0,False,(0,0,15)),('02b_Colliders_FreezeAll',126,False,(0,0,15)),('02c_CubeWithSphereCollider',126,True,(0,0,350)),('02d_LowerCube_FreezeYStudy',4,True,(0,0,350))]:
        objects=default+shape(1000,'UpperCube',pos=(0,1,-5),body=True,sphere_collider=sphere)
        objects+=shape(1100,'LowerCube',pos=(0,-1,-5),scale=(4,.1,4),euler=euler,body=True,gravity=False,constraints=constraints)
        scenes.append((name,objects))
    # Chapter expressly allows creating one's own material experiments. These
    # values are documented study choices, not copied/guessed Standard Assets.
    values=[('Authored_BouncyStudy',0,0,1,0,3),('Authored_IceStudy',0,0,0,0,0),('Authored_MetalStudy',.2,.3,.05,0,0),('Authored_RubberStudy',.9,1,.7,3,3),('Authored_TreeStudy',.5,.6,.1,0,0)]
    mats={v[0]:physical_material(*v) for v in values}
    friction=n.camera((0,6,-16))+n.light()
    bounce=n.camera((0,4,-15))+n.light()
    for index,v in enumerate(values):
        x=-6+index*3;i=1000+index*100
        friction+=shape(i,v[0]+'_Ramp',pos=(x,-1,-2),scale=(2,.2,7),euler=(15,0,0),material=mats[v[0]])
        friction+=shape(i+20,v[0]+'_SlidingCube',pos=(x,1.5,-3),body=True,material=mats[v[0]])
        bounce+=shape(i,v[0]+'_Surface',pos=(x,-1,-3),scale=(2,.2,4),material=mats[v[0]])
        bounce+=shape(i+20,v[0]+'_FallingSphere',kind='Sphere',pos=(x,2,-3),body=True,material=mats[v[0]])
    scenes.append(('03a_AuthoredPhysicMaterials_Friction',friction));scenes.append(('03b_AuthoredPhysicMaterials_Bounce',bounce))
    mouse=default+shape(1000,'Cube',pos=(-1,1,-5),trigger=True,script=gs['TriggerScript'],fields='  reportTriggerName: 0\n')
    mouse+=shape(1100,'Sphere',kind='Sphere',pos=(1,1,-5),body=True,gravity=False,script=gs['MovementScript'])
    scenes.append(('04_MouseTrigger',mouse))
    cam=n.camera();cam=cam.replace('  - component: {fileID: 103}\n','  - component: {fileID: 103}\n  - component: {fileID: 104}\n')
    rays=cam+behaviour(104,100,gs['RaycastScript'])+n.light()
    for index,pos in enumerate([(-1,1,-5),(1,1.5,-5),(-1,-2,5),(1.5,0,0)]):
        rays+=shape(1000+index*100,'Sphere'+str(index+1),kind='Sphere',pos=pos)
    scenes.append(('05_Raycast',rays))
    p=n.build_project(9,scenes,'''# Час 9 — столкновения, физика, триггеры и рейкастинг

Unity **2018.1.0f1**, как на вашем скриншоте. Откройте папку Hour09 через File → Open Project. Сцены уже сохранены в Assets/Scenes: видимые объекты, Rigidbody, коллайдеры и привязки скриптов существуют до Play. Нет CourseSetup, общего Lesson.cs, UI-накладок или создания геометрии при запуске.

Начните с **06_Exercise_TwoTriggers.unity**: стрелки или WASD перемещают Sphere по мировым X/Z. В Console видны LTrigger/RTrigger и тип события: вход, нахождение внутри, выход. Для каждого повтора остановите Play и запустите снова: сцена вернётся к сохранённым координатам.

## Соответствие книге

| Блок книги | Сцена | Сохранённый результат и проверка |
|---|---|---|
| 09-P01, стр.191, до Rigidbody | 01a_Rigidbody_Baseline | Cube (0,1,-5), Rigidbody отсутствует; при Play не должен падать. |
| 09-P01, стр.191, после Rigidbody | 01b_Rigidbody_Gravity | Тот же Cube с Rigidbody, Use Gravity включён; должен падать. Плоскость не добавлена, как в практикуме. |
| 09-P01, эксперимент с Drag | 01c_Rigidbody_DragStudy | Тот же объект, Drag=5 — собственное выбранное значение для сравнения скорости падения. |
| 09-P01, эксперимент с Constraints | 01d_Rigidbody_FreezeYStudy | Freeze Position Y, Use Gravity включён; сравните с 01b. Выбор оси — исследовательский вариант, не фиксированная константа книги. |
| 09-P02, стр.193, пункт3 | 02a_Colliders_Unrestrained | Верхний Cube (0,1,-5) с гравитацией; нижний (0,-1,-5), Scale(4,.1,4), Z15°, Rigidbody без гравитации и без ограничений. |
| 09-P02, стр.194, пункты4–5 | 02b_Colliders_FreezeAll | У нижнего Rigidbody заморожены все позиции и вращения; оба куба с BoxCollider. |
| 09-P02, стр.194, пункты6–7 | 02c_CubeWithSphereCollider | Видимый верхний куб теперь имеет SphereCollider вместо BoxCollider; нижний Z350° и FreezeAll. Проверить скатывание. |
| 09-P02, стр.194, пункт8 | 02d_LowerCube_FreezeYStudy | У нижнего заморожен только PositionY; остальные степени свободы оставлены свободными. |
| 09-A01, стр.194–196 | 03a_AuthoredPhysicMaterials_Friction / 03b_AuthoredPhysicMaterials_Bounce | Пять настоящих .physicMaterial-ассетов назначены Collider.sharedMaterial, не MeshRenderer. Это собственные опыты по свойствам Dynamic/Static Friction, Bounciness и Combine. Не оригинальные Bouncy/Ice/Metal/Rubber/Tree из Standard Assets. |
| 09-P03, стр.197 | 04_MouseTrigger | Cube(-1,1,-5) с IsTrigger=true и TriggerScript; Sphere(1,1,-5) с Rigidbody без гравитации и MovementScript. Мышь сдвигает сферу на MouseX/10,MouseY/10; три сообщения книги печатаются в Console. |
| 09-P04, стр.199–200 | 05_Raycast | Четыре сферы в(-1,1,-5),(1,1.5,-5),(-1,-2,5),(1.5,0,0). RaycastScript на Main Camera поворачивает её от мыши; каждый кадр проверяет луч и уничтожает объект попадания. Кнопка стрельбы не добавлена. |
| 09-E01, стр.201–202 | 06_Exercise_TwoTriggers | LTrigger(-1.5,0,-5), RTrigger(1.5,0,-5), Scale(.1,2,2), оба IsTrigger=true. Sphere(0,0,-5), Rigidbody без гравитации, MotionScript. Rigidbody.MovePosition вызывается в FixedUpdate. |

В сценах MouseTrigger и итогового упражнения OnTriggerStay печатается на каждом физическом шаге, как в книжном примере. Для чтения можно включить Collapse в Console; при необходимости увидеть отдельные события выключите его. Это не сообщение об ошибке.

## Собственные физические материалы

В книге прямо разрешено создавать свои материалы, однако готовый пакет также упоминается. Стандартные оригиналы не получены из заблокированного архива и не выдаются за приложенные. Для изучения сохранены следующие явно выбранные значения:

| Файл Authored_* | Dynamic Friction | Static Friction | Bounciness | Friction Combine | Bounce Combine |
|---|---:|---:|---:|---|---|
| BouncyStudy |0|0|1|Average|Maximum|
| IceStudy |0|0|0|Average|Average|
| MetalStudy |.2|.3|.05|Average|Average|
| RubberStudy |.9|1|.7|Maximum|Maximum|
| TreeStudy |.5|.6|.1|Average|Average|

Откройте материалы в Inspector и изменяйте параметры, затем сравнивайте поведение в Play. Значения названий здесь учебные, не измеренные физические характеристики реальных веществ. Для точного выполнения шага Import Package → Characters → Physics Materials нужен оригинальный пакет; этот шаг остаётся внешним ограничением.

Глава посвящена физическим материалам, а не текстурным картам. Использован стандартный рендер-материал Unity; PhysicMaterial назначен именно коллайдерам. Пустые текстуры не выдаются за выполненный UV/normal mapping другой главы.

**Проверки:** сохранённые YAML-сцены, локальные fileID, ссылки на скрипты/физические материалы, точные координаты и флаги проверены статически. Синтаксис C# проверен парсером. Импорт, компиляция Unity API, физическое поведение в Play и EXE-сборка здесь НЕ выполнялись. Готовность к сдаче без этих проверок не утверждается.
''')
    # These four standard axes are the complete input requirements of this hour.
    axes=[]
    for name,negative,positive,altnegative,altpositive,typ,axis in [('Horizontal','left','right','a','d',0,0),('Vertical','down','up','s','w',0,0),('Mouse X','','','','',1,0),('Mouse Y','','','','',1,1)]:
        axes.append(f'''  - serializedVersion: 3
    m_Name: {name}
    descriptiveName:
    descriptiveNegativeName:
    negativeButton: {negative}
    positiveButton: {positive}
    altNegativeButton: {altnegative}
    altPositiveButton: {altpositive}
    gravity: 3
    dead: 0.001
    sensitivity: {1 if typ else 3}
    snap: 0
    invert: 0
    type: {typ}
    axis: {axis}
    joyNum: 0
''')
    (p/'ProjectSettings/InputManager.asset').write_text(n.HEADER+'''--- !u!13 &1
InputManager:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_Axes:
'''+''.join(axes))
    (p/'Семинар.md').write_text('''# Час 9 — контрольные вопросы, стр.201

1. Для физических свойств объекта, в том числе падения под действием гравитации, нужен Rigidbody.
2. У объекта может быть несколько Collider, поэтому утверждение «только один» неверно.
3. Raycast позволяет определить объект по направлению луча и получить данные попадания, например для прицеливания или измерения расстояния.

Физический материал влияет на столкновение и трение; обычный Material с текстурой влияет на отображение. Это разные ассеты и разные поля компонентов.
''')
    validate_project(p,len(scripts))
    mp=p/'scene_manifest.json';manifest=json.loads(mp.read_text());manifest.update(source_requirements=['09-P01','09-P02','09-A01','09-P03','09-P04','09-E01'],native_physic_materials=len(mats),companion_assets_obtained=False,original_package_import='BLOCKED: original Standard Assets PhysicsMaterials not obtained; custom authored experiments explicitly identified.',runtime_geometry_creation=False)
    mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'project':str(p),'scenes':len(scenes),'scripts':len(scripts),'physic_materials':len(mats),'unity_run':False},ensure_ascii=False))
    return p
if __name__=='__main__':build()
