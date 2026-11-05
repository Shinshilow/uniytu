#!/usr/bin/env python3
"""Native serialized Unity 2018.1.0f1 project for EVERY hour-8 practicum.

Rewrites only rebuild/Hour08. No editor or runtime scene generator is included in
that project. Scene objects and component references are persisted in YAML.
"""
from pathlib import Path
import hashlib,json,re
import build_native_intro as u
ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT/'rebuild/Hour08'

SCRIPTS={
'FireBallScript':'''using UnityEngine;

// Book pp.171-174: all three overloads coexist in one class.
public class FireBallScript : MonoBehaviour
{
    int TakeDamageFromFireball()
    {
        int playerHealth = 100;
        return playerHealth - 5;
    }

    int TakeDamageFromFireball(int damage)
    {
        int playerHealth = 100;
        return playerHealth - damage;
    }

    int TakeDamageFromFireball(int damage, int playerHealth)
    {
        return playerHealth - damage;
    }

    void Start()
    {
        int x = TakeDamageFromFireball();
        print("Player health: " + x);
        int y = TakeDamageFromFireball(25);
        print("Player health: " + y);
        int z = TakeDamageFromFireball(30, 50);
        print("Player health: " + z);
    }
}
''',
'PlayerInput':'''using UnityEngine;

// Book p.177: axes can be remapped in Project Settings > Input.
public class PlayerInput : MonoBehaviour
{
    void Update()
    {
        float hVal = Input.GetAxis("Horizontal");
        float vVal = Input.GetAxis("Vertical");
        if (hVal != 0)
            print("Horizontal movement selected: " + hVal);
        if (vVal != 0)
            print("Vertical movement selected: " + vVal);
    }
}
''',
'KeyInputScript':'''using UnityEngine;

// Book p.178 modifies PlayerInput. Distinct class keeps each variant available.
public class KeyInputScript : MonoBehaviour
{
    void Update()
    {
        if (Input.GetKey(KeyCode.M))
            print("The 'M' key is pressed down");
        if (Input.GetKeyDown(KeyCode.O))
            print("The 'O' key was pressed");
    }
}
''',
'MouseInputScript':'''using UnityEngine;

// Book p.180: standalone saved variant of the PlayerInput example.
public class MouseInputScript : MonoBehaviour
{
    void Update()
    {
        float mxVal = Input.GetAxis("Mouse X");
        float myVal = Input.GetAxis("Mouse Y");
        if (mxVal != 0)
            print("Mouse X movement selected: " + mxVal);
        if (myVal != 0)
            print("Mouse Y movement selected: " + myVal);
    }
}
''',
'CubeScript':'''using UnityEngine;

// Book p.182. Per-frame values are intentional in this specific experiment.
public class CubeScript : MonoBehaviour
{
    void Update()
    {
        transform.Translate(.05f, 0f, 0f);
        transform.Rotate(0f, 0f, 1f);
        transform.localScale = new Vector3(1.5f, 1.5f, 1.5f);
    }
}
''',
'TargetCubeScript':'''using UnityEngine;

// Book pp.185-186. Script is on Main Camera, not Cube.
public class TargetCubeScript : MonoBehaviour
{
    private GameObject target;

    void Start()
    {
        target = GameObject.Find("Cube");
    }

    void Update()
    {
        target.transform.Translate(.05f, 0f, 0f);
        target.transform.Rotate(0f, 0f, 1f);
        target.transform.localScale = new Vector3(1.5f, 1.5f, 1.5f);
    }
}
''',
'CubeControlScript':'''using UnityEngine;

// End exercise, pp.187-188. Arrow motion stays along world X/Z after yaw.
public class CubeControlScript : MonoBehaviour
{
    public Camera controlledCamera;
    public float movementSpeed = 4f;
    public float mouseSensitivity = 2f;
    Vector3 originalScale;
    bool doubleSize;

    void Start()
    {
        originalScale = transform.localScale;
    }

    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");
        transform.Translate(new Vector3(horizontal, 0f, vertical)
            * movementSpeed * Time.deltaTime, Space.World);

        float mouseX = Input.GetAxis("Mouse X");
        float mouseY = Input.GetAxis("Mouse Y");
        transform.Rotate(0f, mouseX * mouseSensitivity, 0f, Space.World);
        controlledCamera.transform.Rotate(-mouseY * mouseSensitivity, 0f, 0f,
            Space.Self);

        if (Input.GetKeyDown(KeyCode.M))
        {
            doubleSize = !doubleSize;
            transform.localScale = originalScale * (doubleSize ? 2f : 1f);
        }
    }
}
'''
}

def script_guid(name):
    return hashlib.md5(('uniytu/native-hour08/'+name).encode()).hexdigest()

def write_script(name,code):
    p=PROJECT/'Assets/Scripts'/f'{name}.cs';p.write_text(code)
    Path(str(p)+'.meta').write_text(f'''fileFormatVersion: 2
guid: {script_guid(name)}
MonoImporter:
  externalObjects: {{}}
  serializedVersion: 2
  defaultReferences: []
  executionOrder: 0
  icon: {{instanceID: 0}}
  userData:
  assetBundleName:
  assetBundleVariant:
''')

def mono(component,go,name,fields=''):
    return f'''--- !u!114 &{component}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {script_guid(name)}, type: 3}}
  m_Name:
  m_EditorClassIdentifier:
'''+fields

def camera_script(name):
    text=u.camera()+u.light()
    text=text.replace('  - component: {fileID: 103}\n','  - component: {fileID: 103}\n  - component: {fileID: 150}\n',1)
    return text+mono(150,100,name)

def cube_script(name,pos):
    text=u.camera()+u.light()+u.primitive(1000,'Cube',pos=pos)
    text=text.replace('  - component: {fileID: 1004}\n','  - component: {fileID: 1004}\n  - component: {fileID: 1050}\n',1)
    fields='  controlledCamera: {fileID: 102}\n  movementSpeed: 4\n  mouseSensitivity: 2\n' if name=='CubeControlScript' else ''
    return text+mono(1050,1000,name,fields)

def input_settings():
    axes=[]
    for name,negative,positive,altnegative,altpositive,typ,axis in [
        ('Horizontal','left','right','a','d',0,0),
        ('Vertical','down','up','s','w',0,0),
        ('Mouse X','','','','',1,0),
        ('Mouse Y','','','','',1,1),
    ]:
        axes.append(f'''  - serializedVersion: 3
    m_Name: {name}
    descriptiveName:
    descriptiveNegativeName:
    negativeButton: {negative}
    positiveButton: {positive}
    altNegativeButton: {altnegative}
    altPositiveButton: {altpositive}
    gravity: {3 if typ==0 else 0}
    dead: {0.001 if typ==0 else 0}
    sensitivity: {3 if typ==0 else 0.1}
    snap: {1 if typ==0 else 0}
    invert: 0
    type: {typ}
    axis: {axis}
    joyNum: 0
''')
    return u.HEADER+'''--- !u!13 &1
InputManager:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_Axes:
'''+''.join(axes)

README='''# Час 8 — Скрипты, часть 2

Unity **2018.1.0f1**. Откройте папку Hour08 через File → Open Project, затем двойным щелчком нужную сцену в Assets/Scenes. Начните с **07_Exercise**. Куб, камера, источник света и компоненты уже находятся в файлах сцен; создавать сцену кодом или нажимать Course/Prepare не нужно. Отдельных пакетов и Unity Hub не требуется.

| Книга, печатные страницы | Сохранённый результат | Как проверить в Unity |
|---|---|---|
| Практикум 1 «Идентификация частей метода», 170–171 | Ответы_методы.md | TakeDamage, тип int, один параметр int damageAmount, блок с health и return. |
| Практикум 2 «Вызов методов», 173–174 | 01_Methods; FireBallScript на Main Camera | Play → Console: Player health: 95, 75, 20, в таком порядке. |
| Практикум 3 «Считывание ввода игрока», 177 | 02_PlayerInput; PlayerInput на Main Camera | Щёлкните Game, нажмите стрелки/WASD; в Console значения Horizontal/Vertical. |
| Практикум 4 «Определённые клавиши», 178 | 03_KeyInput; KeyInputScript на Main Camera | M логирует каждый кадр удержания, O один раз на нажатие. |
| Практикум 5 «Движение мыши», 180 | 04_MouseInput; MouseInputScript на Main Camera | С фокусом Game водите мышью: Console показывает Mouse X/Y. |
| Практикум 6 «Преобразование объекта», 182 | 05_LocalCube; Cube в (0,-1,0), CubeScript на кубе | Play: движение .05 по локальной X и поворот Z на1° каждый кадр, масштаб постоянно1.5. |
| Практикум 7 «Целевой объект», 185–186 | 06_TargetCube; Cube в (0,-1,0), TargetCubeScript на Main Camera | Куб движется так же, хотя скрипт расположен на камере. |
| Итоговое упражнение, 187–188 | 07_Exercise; Cube в (0,0,-5), CubeControlScript на кубе | Стрелки: world X/Z; Mouse X: yaw куба; Mouse Y: pitch камеры; два нажатия M восстанавливают исходный масштаб. |

Книга предлагает изменять один PlayerInput последовательно. Чтобы все три варианта можно было открыть одновременно в одном проекте, варианты определённых клавиш и мыши названы KeyInputScript и MouseInputScript. Их логика сохранена; одинаковых классов PlayerInput в проекте нет.

У сцен 01–04 нет игровой геометрии: результат этих практикумов выводится в Console. Это соответствует книге. В сценах 05–06 исходная скорость намеренно задана **на кадр**, как в книге; при разной частоте кадров скорость различается. Чтобы увидеть целый круг, можно отдалить камеру либо наблюдать из Scene. В итоговом контроллере используется deltaTime.

Назначения осей сохранены в ProjectSettings/InputManager.asset. Текстурирование и normal mapping глава 8 не задаёт; здесь стандартный куб и материал Unity, без декоративных ассетов. Их нельзя выдавать за практику материала из часа 3.

Проверены статические ссылки fileID/GUID, соответствие классов именам файлов, наличие всех восьми заданий и входных осей. **Импорт, компиляция API и Play в Unity здесь не выполнялись.** По этим проверкам нельзя утверждать готовность к сдаче.
'''

def main():
    (PROJECT/'Assets/Scripts').mkdir(parents=True,exist_ok=True)
    for name,code in SCRIPTS.items():write_script(name,code)
    scenes=[
        ('07_Exercise',cube_script('CubeControlScript',(0,0,-5))),
        ('01_Methods',camera_script('FireBallScript')),
        ('02_PlayerInput',camera_script('PlayerInput')),
        ('03_KeyInput',camera_script('KeyInputScript')),
        ('04_MouseInput',camera_script('MouseInputScript')),
        ('05_LocalCube',cube_script('CubeScript',(0,-1,0))),
        ('06_TargetCube',camera_script('TargetCubeScript')+u.primitive(1000,'Cube',pos=(0,-1,0))),
    ]
    u.build_project(8,scenes,README)
    u.metadata(PROJECT/'Assets/Scripts',folder=True)
    (PROJECT/'ProjectSettings/InputManager.asset').write_text(input_settings())
    (PROJECT/'Ответы_методы.md').write_text('''# Практикум «Идентификация частей метода» — страницы170–171

```csharp
int TakeDamage(int damageAmount)
{
    int health = 100;
    return health - damageAmount;
}
```

1. Имя метода — TakeDamage.
2. Возвращаемый тип — int (целое число).
3. Единственный параметр — int damageAmount, количество урона.
4. Блок метода создаёт локальную переменную health со значением100 и возвращает разность health-damageAmount.

Например, TakeDamage(25) возвращает75. Переменная health при каждом вызове вновь равна100; этот демонстрационный метод сам не хранит здоровье между вызовами.

Сигнатуры трёх перегрузок в следующем практикуме отличаются набором параметров; возвращаемый тип у всех int. FireBallScript в сцене01 показывает вызов каждой перегрузки.
''')
    manifest=json.loads((PROJECT/'scene_manifest.json').read_text())
    manifest['runtime_scripts']=len(SCRIPTS)
    manifest['source_requirements']=['08-P01','08-P02','08-P03','08-P04','08-P05','08-P06','08-P07','08-E01']
    manifest['written_work']='Ответы_методы.md'
    manifest['input_mappings']={'Horizontal':['left','right','a','d'],'Vertical':['down','up','s','w'],'Mouse X':'X axis','Mouse Y':'Y axis','direct_keys':['M','O']}
    (PROJECT/'scene_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(validate(),ensure_ascii=False))

def validate():
    script_guids={script_guid(name) for name in SCRIPTS}
    for path in (PROJECT/'Assets/Scenes').glob('*.unity'):
        text=path.read_text()
        ids=set(re.findall(r'^--- !u!\d+ &(\d+)',text,re.M))
        assert len(ids)==len(re.findall(r'^--- !u!',text,re.M)),path
        for value,tail in re.findall(r'\{fileID: (\d+)([^}]*)\}',text):
            assert value=='0' or 'guid:' in tail or value in ids,(path,value)
        for guid in re.findall(r'm_Script: \{fileID: 11500000, guid: ([a-f0-9]+)',text):
            assert guid in script_guids,(path,guid)
        assert len(re.findall(r'^Camera:',text,re.M))==1 and len(re.findall(r'^AudioListener:',text,re.M))==1
        assert text.count('MonoBehaviour:')==1
    for name in SCRIPTS:
        path=PROJECT/'Assets/Scripts'/f'{name}.cs'
        assert f'class {name} : MonoBehaviour' in path.read_text()
        assert script_guid(name) in Path(str(path)+'.meta').read_text()
    exercise=(PROJECT/'Assets/Scenes/07_Exercise.unity').read_text()
    assert 'm_LocalPosition: {x: 0, y: 0, z: -5}' in exercise
    assert 'controlledCamera: {fileID: 102}' in exercise
    assert 'Space.World' in SCRIPTS['CubeControlScript']
    assert 'Time.deltaTime' in SCRIPTS['CubeControlScript']
    assert len(list((PROJECT/'Assets/Scenes').glob('*.unity')))==7
    return {'hour':8,'native_scenes':7,'runtime_scripts':7,'written_practicums':1,'static_reference_checks':'passed','Unity_import_and_Play':'unrun'}

if __name__=='__main__':main()
