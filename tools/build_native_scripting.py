#!/usr/bin/env python3
"""Native, self-contained Unity 2018.1.0f1 scripting practica (Hour07).
No Lesson.cs, no editor-generation dependency, no fabricated texture requirement.
"""
from pathlib import Path
import json,re
import build_native_intro as native
ROOT=Path(__file__).resolve().parents[1]

def write_script(project,name,source):
    folder=project/'Assets/Scripts';folder.mkdir(parents=True,exist_ok=True)
    native.metadata(folder,folder=True)
    path=folder/(name+'.cs');path.write_text(source.strip()+'\n')
    g=native.guid(str(path.relative_to(native.OUT)))
    Path(str(path)+'.meta').write_text(f'''fileFormatVersion: 2
guid: {g}
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
    return g

def behaviour(i,go,guid,fields=''):
    return f'''--- !u!114 &{i}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {guid}, type: 3}}
  m_Name:
  m_EditorClassIdentifier:
'''+fields

def attach_camera(scripts):
    camera=native.camera()
    extra=''.join(f'  - component: {{fileID: {104+i}}}\n' for i in range(len(scripts)))
    camera=camera.replace('  - component: {fileID: 103}\n','  - component: {fileID: 103}\n'+extra)
    return camera+native.light()+''.join(behaviour(104+i,100,guid) for i,guid in enumerate(scripts))

def validate_project(project,expected_scripts):
    script_guids={}
    for meta in (project/'Assets/Scripts').glob('*.cs.meta'):
        g=re.search(r'^guid: (\w+)',meta.read_text(),re.M).group(1);script_guids[g]=meta
    assert len(script_guids)==expected_scripts
    for path in (project/'Assets/Scenes').glob('*.unity'):
        text=path.read_text();ids=re.findall(r'^--- !u!\d+ &(\d+)',text,re.M)
        assert len(ids)==len(set(ids))
        for value,tail in re.findall(r'\{fileID: (\d+)([^}]*)\}',text):
            assert value=='0' or 'guid:' in tail or value in ids,(path,value)
        for g in re.findall(r'm_Script: \{fileID: 11500000, guid: (\w+)',text):
            assert g in script_guids,(path,g)
        assert text.count('Camera:')==1 and text.count('AudioListener:')==1
    manifest=json.loads((project/'scene_manifest.json').read_text());manifest['runtime_scripts']=expected_scripts;manifest['unity_api_compilation']='UNRUN';manifest['play_mode']='UNRUN'
    (project/'scene_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')


def build7():
    p=native.OUT/'Hour07'
    sources={
      'HelloWorldScript':'''using UnityEngine;
// Book practicum, printed pp.149-150. Attached to Main Camera.
public class HelloWorldScript : MonoBehaviour
{
    void Start()
    {
        print("Hello World");
    }
}''',
      'ImportantFunctions':'''using UnityEngine;
// Book practicum, printed pp.153-154. Stop Play after a short observation.
public class ImportantFunctions : MonoBehaviour
{
    void Start()
    {
        print("Start runs before an object Updates");
    }
    void Update()
    {
        print("This is called once a frame");
    }
}''',
      'OperatorsStudy':'''using UnityEngine;
// Independently authored study examples for chapter 7 pp.157-165.
// This is NOT the original companion file EqualityAndOperations.cs.
public class OperatorsStudy : MonoBehaviour
{
    void Start()
    {
        int sum = 0;
        for (int count = 1; count <= 100; count++)
        {
            sum += count;
        }
        print("Sum 1..100 (for): " + sum);
        int total = 0;
        int number = 1;
        while (number <= 100)
        {
            total += number;
            number++;
        }
        print("Sum 1..100 (while): " + total);
        print("10 % 2 = " + (10 % 2));
        print("6 % 5 = " + (6 % 5));
        print("24 % 7 = " + (24 % 7));
        int x = 5;
        x += 5;
        x++;
        print("x = 5; x += 5; x++; result: " + x);
        print("5 == 6: " + (5 == 6));
        print("9 == 9: " + (9 == 9));
        print("true && false: " + (true && false));
        print("true || false: " + (true || false));
        print("!false: " + (!false));
    }
}''',
      'EvenSum':'''using UnityEngine;
// Final exercise 1, printed p.167. Sum even integers from 2 through 499.
public class EvenSum : MonoBehaviour
{
    void Start()
    {
        int sum = 0;
        for (int number = 2; number <= 499; number += 2)
        {
            sum += number;
        }
        print(sum);
    }
}''',
      'ProgrammingNumbers':'''using UnityEngine;
// Final exercise 2, printed p.167. Exactly one output for each integer 1..100.
public class ProgrammingNumbers : MonoBehaviour
{
    void Start()
    {
        for (int number = 1; number <= 100; number++)
        {
            if (number % 3 == 0 || number % 5 == 0)
            {
                print("Программирование — это прекрасно!");
            }
            else
            {
                print(number);
            }
        }
    }
}''',
      'Fibonacci':'''using UnityEngine;
// Final exercise 3, printed p.167. First twenty terms, beginning with 0 and 1.
public class Fibonacci : MonoBehaviour
{
    void Start()
    {
        int first = 0;
        int second = 1;
        for (int index = 0; index < 20; index++)
        {
            print(first);
            int next = first + second;
            first = second;
            second = next;
        }
    }
}'''
    }
    guids={name:write_script(p,name,code) for name,code in sources.items()}
    scenes=[('04_Exercise_ThreeScripts',attach_camera([guids['EvenSum'],guids['ProgrammingNumbers'],guids['Fibonacci']])),('01_HelloWorld',attach_camera([guids['HelloWorldScript']])),('02_ImportantFunctions',attach_camera([guids['ImportantFunctions']])),('03_OperatorsStudy',attach_camera([guids['OperatorsStudy']]))]
    native.build_project(7,scenes,'''# Час 7 — скрипты, часть 1

Версия из вашего скриншота: Unity 2018.1.0f1. Unity Hub не требуется: File → Open Project → папка Hour07. Сцены и привязки скриптов уже сохранены. Нет CourseSetup, Lesson.cs, скриптов других часов, RuntimeInitializeOnLoad или построения сцены при Play.

Откройте **Assets/Scenes/04_Exercise_ThreeScripts.unity**. Выделите Main Camera: к ней прикреплены три независимых скрипта. Откройте Window → Console, выключите Collapse для просмотра всех строк, нажмите Play. В Game в этом часе нет игрового интерфейса: результат задач — Console, как в книге.

| Практикум и страница книги | Сохранённая сцена | Что проверить |
|---|---|---|
| Создание и назначение скрипта, стр.149–150 | 01_HelloWorld | HelloWorldScript на Main Camera; при Play один Hello World. В книге до прикрепления скрипта сообщения нет; этот промежуточный редакторный шаг не выдаётся за отдельную выполненную программу. |
| Start и Update, стр.153–154 | 02_ImportantFunctions | Start runs before an object Updates появляется один раз; This is called once a frame — каждый кадр. Запускайте ненадолго, затем Stop. |
| Операторы и циклы, стр.157–165 | 03_OperatorsStudy | Собственные учебные примеры по выражениям книги: цикл for/while даёт 5050, остатки 0/1/3, инкремент и логические выражения. Это не оригинальный EqualityAndOperations.cs. |
| Итоговое упражнение1, стр.167 | 04_Exercise_ThreeScripts | EvenSum выводит 62250: чётные числа 2…498. |
| Итоговое упражнение2, стр.167 | 04_Exercise_ThreeScripts | ProgrammingNumbers делает100 выводов:47 замен фразой «Программирование — это прекрасно!»,53 числа. Кратность3 ИЛИ5. |
| Итоговое упражнение3, стр.167 | 04_Exercise_ThreeScripts | Fibonacci выводит20 членов:0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181. |

Порядок Start между разными компонентами Unity не фиксирует. Оценивайте выход каждого скрипта, а не порядок трёх блоков; двойной щелчок по Console-строке открывает соответствующий источник.

Текстуры и UV-маппинг в этой главе не требуются. Никакие материалы других часов не подменяют задания на программирование.

Ссылка на оригинальный EqualityAndOperations.cs есть на стр.160, но сам файл относится к отдельному архиву примеров. Он здесь не объявлен полученным или проверенным. Все три итоговые задачи и два явных исполняемых практикума реализованы по тексту книги; самостоятельные операторные примеры отмечены отдельно.

**Проверки:** статически сверены GUID скриптов, локальные fileID, компоненты Main Camera, синтаксис C# и структура сцен. Импорт, компиляция с Unity API, Play и Windows EXE в этой облачной среде не выполнялись. После открытия нужно подтвердить отсутствие красных ошибок и сверить Console с таблицей; готовность к сдаче пока не подтверждена.
''')
    (p/'Семинар.md').write_text('''# Час7 — контрольные вопросы (стр.166–167)

1. Язык программирования этой книги — C#.
2. Start выполняется один раз при запуске активного компонента; Update — каждый кадр.
3. Тип с плавающей точкой, используемый Unity по умолчанию, — float.
4. Остаток от деления возвращает оператор %.
5. Условный оператор выбирает ветвь кода по логическому условию.
6. Для подсчёта удобно использовать цикл for.

Это письменные ответы; факт чтения и понимания не доказывается наличием EXE.
''')
    validate_project(p,len(sources))
    manifest_path=p/'scene_manifest.json'
    manifest=json.loads(manifest_path.read_text())
    manifest['source_requirements']=['07-P01','07-P02','07-A01','07-E01']
    manifest['written_work']='Семинар.md'
    manifest['companion_file_unavailable']='EqualityAndOperations.cs; OperatorsStudy is an explicitly independent reading aid.'
    manifest['expected_exercise_outputs']={'even_sum':62250,'numbers_count':100,'replacement_count':47,'fibonacci_terms':20,'fibonacci_last':4181}
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return p
if __name__=='__main__':
    p=build7();print(json.dumps({'project':str(p),'scenes':4,'scripts':6,'unity_run':False},ensure_ascii=False))
