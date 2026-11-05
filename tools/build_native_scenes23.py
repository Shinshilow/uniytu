#!/usr/bin/env python3
"""Saved Unity 2018.1.0f1 scenes for chapter23; no runtime/editor scene generator.

Only rebuild/Hour23 is written. Uses primitive/native helpers, with an independent
scene pair for the scene-order and persistent-object demonstrations. Exact Scene1
and Scene2 names are retained for the cumulative PlayerPrefs result.
"""
from pathlib import Path
import json,re,hashlib
import build_native_intro as native
from build_native_scripting import write_script,behaviour

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT/'rebuild/Hour23'

RUNTIME={
'DontDestroy':r'''using UnityEngine;
using UnityEngine.SceneManagement;

// Book pp.435-436. The target differs only for the independent comparison pair.
public class DontDestroy : MonoBehaviour
{
    public int targetSceneIndex = 1;
    // Auxiliary observation: this field stays on the SAME Cube after scene load.
    public int clickCount;

    void Start()
    {
        DontDestroyOnLoad(gameObject);
    }

    void OnMouseDown()
    {
        clickCount++;
        if (SceneManager.GetActiveScene().buildIndex != targetSceneIndex)
            SceneManager.LoadScene(targetSceneIndex);
    }
}
''',
'SaveData':r'''using UnityEngine;

// Book p.437: this component belongs to Scene1's Main Camera, not the Cube.
public class SaveData : MonoBehaviour
{
    public string playerName = "";

    void OnGUI()
    {
        playerName = GUI.TextField(new Rect(5, 120, 100, 30), playerName);
        if (GUI.Button(new Rect(5, 180, 50, 50), "Save"))
        {
            PlayerPrefs.SetString("name", playerName);
            // Explicit disk flush makes the chapter's relaunch check repeatable.
            PlayerPrefs.Save();
        }
    }
}
''',
'LoadData':r'''using UnityEngine;

// Book pp.437-438: Scene2's independent Main Camera reads the saved value.
public class LoadData : MonoBehaviour
{
    string playerName = "";

    void Start()
    {
        playerName = PlayerPrefs.GetString("name", "");
    }

    void OnGUI()
    {
        GUI.Label(new Rect(5, 220, 200, 30), playerName);
    }
}
''',
'SceneOrderInput':r'''using UnityEngine;
using UnityEngine.SceneManagement;

// Small navigation aid for the separate scene-order practicum. No objects are
// generated and no DontDestroyOnLoad is used in this comparison scene pair.
public class SceneOrderInput : MonoBehaviour
{
    public int targetSceneIndex;

    void OnGUI()
    {
        if (GUI.Button(new Rect(5, 120, 180, 35), "Load other scene"))
            SceneManager.LoadScene(targetSceneIndex);
    }
}
''',
'SceneObservation':r'''using UnityEngine;
using UnityEngine.SceneManagement;

// Additional readout to observe the book's saved object and click counter.
// It does not create objects or change any of the book's primitive transforms.
public class SceneObservation : MonoBehaviour
{
    public string instructions;

    void OnGUI()
    {
        GUI.Label(new Rect(5, 5, Screen.width - 10, 80), instructions);
        var cube = FindObjectOfType<DontDestroy>();
        if (cube != null)
        {
            GUI.Label(new Rect(5, 85, Screen.width - 10, 25),
                "Persistent Cube: " + cube.GetInstanceID() +
                " | clicks: " + cube.clickCount +
                " | scene index: " + SceneManager.GetActiveScene().buildIndex);
        }
        else if (SceneManager.GetActiveScene().name == "Scene2")
        {
            GUI.Label(new Rect(5, 85, Screen.width - 10, 25),
                "Cube is absent because Scene2 was opened directly. Start Scene1 first.");
        }
    }
}
''',
}

BUILD=r'''using System;
using System.IO;
using System.Collections.Generic;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEditor.SceneManagement;
using UnityEngine;

// Build only: the supplied scenes are ALREADY saved, no CourseSetup is needed.
public static class BuildHour23
{
    [MenuItem("Book/Hour 23/Build Windows x64")]
    public static void BuildWindows()
    {
        if (Application.isPlaying)
            throw new InvalidOperationException("Stop Play Mode before building.");
        if (!BuildPipeline.IsBuildTargetSupported(BuildTargetGroup.Standalone,
                BuildTarget.StandaloneWindows64))
            throw new InvalidOperationException(
                "Windows Build Support for Unity 2018.1.0f1 is required.");

        var scenes = new List<string>();
        foreach (var scene in EditorBuildSettings.scenes)
        {
            if (!scene.enabled) continue;
            if (!File.Exists(scene.path))
                throw new FileNotFoundException("Configured scene not found", scene.path);
            scenes.Add(scene.path);
        }
        if (scenes.Count == 0)
            throw new InvalidOperationException("Scenes In Build is empty.");

        PlayerSettings.companyName = "Unity Book Study";
        PlayerSettings.productName = "Hour23 - Scenes and Save Data";
        PlayerSettings.defaultScreenWidth = 1000;
        PlayerSettings.defaultScreenHeight = 700;
        PlayerSettings.runInBackground = true;
        PlayerSettings.displayResolutionDialog = ResolutionDialogSetting.Enabled;

        var output = Path.GetFullPath("Builds/Hour23/Hour23.exe");
        Directory.CreateDirectory(Path.GetDirectoryName(output));
        var report = BuildPipeline.BuildPlayer(new BuildPlayerOptions
        {
            scenes = scenes.ToArray(),
            locationPathName = output,
            target = BuildTarget.StandaloneWindows64,
            options = BuildOptions.None
        });
        if (report.summary.result != BuildResult.Succeeded)
            throw new InvalidOperationException("Build failed: " + report.summary.result);
        Debug.Log("HOUR23_BUILD_SUCCEEDED " + output);
    }

    [MenuItem("Book/Hour 23/Bake active scene lighting")]
    public static void BakeActiveSceneLighting()
    {
        if (Application.isPlaying)
            throw new InvalidOperationException("Stop Play Mode before baking.");
        Lightmapping.giWorkflowMode = Lightmapping.GIWorkflowMode.OnDemand;
        if (!Lightmapping.Bake())
            throw new InvalidOperationException("Lighting bake did not finish successfully.");
        EditorSceneManager.SaveOpenScenes();
        Debug.Log("HOUR23_LIGHTING_BAKED");
    }
}
'''


def write_editor(source):
    folder=PROJECT/'Assets/Editor';folder.mkdir(parents=True,exist_ok=True)
    native.metadata(folder,folder=True)
    file=folder/'BuildHour23.cs';file.write_text(source)
    g=native.guid(str(file.relative_to(native.OUT)))
    Path(str(file)+'.meta').write_text(f'''fileFormatVersion: 2
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


def camera_with(guids,components):
    text=native.camera()
    ids=[150+i for i in range(len(components))]
    text=text.replace('  - component: {fileID: 103}\n',
        '  - component: {fileID: 103}\n'+''.join(f'  - component: {{fileID: {i}}}\n' for i in ids),1)
    for i,(name,fields) in zip(ids,components):text+=behaviour(i,100,guids[name],fields)
    return text+native.light()


def observation(message):
    return ('SceneObservation','  instructions: '+json.dumps(message,ensure_ascii=True)+'\n')


def cube_with(guids,index):
    text=native.primitive(1000,'Cube')
    text=text.replace('  - component: {fileID: 1004}\n','  - component: {fileID: 1004}\n  - component: {fileID: 1050}\n')
    return text+behaviour(1050,1000,guids['DontDestroy'],f'  targetSceneIndex: {index}\n  clickCount: 0\n')


README='''# Час 23 — сцены, сохранение объектов/данных и сборка

Версия **Unity 2018.1.0f1** подтверждена вашим скриншотом. Unity Hub не нужен: **File → Open Project → Hour23**. В Project откройте **Assets/Scenes/Scene1.unity**, затем Play.

Это нативные сохранённые сцены. Cube, Sphere, Main Camera, Directional Light, компоненты и ссылки уже записаны в .unity/.meta. Нет общего Lesson.cs, CourseSetup, построения геометрии при Play или импорта пакетов других глав. Для часа23 внешние текстуры и UV-маппинг не нужны: книга использует стандартные куб и сферу. Стандартный материал соответствует этому заданию.

## Итоговый результат и проверка PlayerPrefs

1. Откройте **Scene1** и нажмите Play.
2. В текстовом поле введите короткое имя и нажмите **Save**.
3. Щёлкните по Cube в Game. Загрузится **Scene2** (индекс1), появится Sphere в (0,2,0).
4. Куб сохраняется: тот же объект, тот же InstanceID и его счётчик clicks. Камера Scene1 и её SaveData уничтожаются; у Scene2 собственная камера с LoadData. Камера не является дочерним объектом куба и не сохраняется между сценами.
5. В Scene2 на y=220 отобразится сохранённое имя. Остановите Play, снова откройте Scene1, запустите, щёлкните по кубу: имя должно загрузиться из PlayerPrefs без повторного Save.
6. В готовой сборке повторите после полного закрытия и повторного запуска процесса.

`clickCount` и строка InstanceID — дополнительные средства наблюдения, а не замена задания. PlayerPrefs-ключ `name` соответствует книге. Нажатие Save выполняет также PlayerPrefs.Save() для явной записи на диск. Скрипты не удаляют существующие PlayerPrefs пользователя. В LoadData ширина поля увеличена с50 до200, чтобы видеть короткие имена целиком.

Если открыть Scene2 напрямую, сохранённого Cube там не будет: он переносится из Scene1, как предусмотрено заданием. Начинайте проверку с Scene1.

## Все практикумы и соответствие книге

| Страницы книги | Сцены / исходники | Что выполнено в файлах |
|---|---|---|
| 433: добавление сцен в сборку | Scene1, Scene2 | Точные имена из книги. В EditorBuildSettings они стоят первыми:0 и1. |
| 433–434: переключение сцен | 01_SceneOrder_Scene1, 01_SceneOrder_Scene2 | Отдельная пара для сравнения обычной загрузки. Кнопка Load other scene вызывает SceneManager.LoadScene по явному индексу. В первой сцене Cube, во второй Sphere; Cube здесь не сохраняется. Кнопка — дополнительный способ воспроизвести учебный вызов LoadScene. |
| 435–436: DontDestroyOnLoad | 02_Persistent_Scene1, 02_Persistent_Scene2, DontDestroy.cs | Независимая пара без PlayerPrefs. Cube в (0,0,0); Sphere назначения в (0,2,0). Start сохраняет Cube, щелчок загружает заданный индекс. |
| 437–438: PlayerPrefs | Scene1/Scene2, SaveData.cs/LoadData.cs | Итоговая сцена расширяет перенос куба. SaveData на Main Camera Scene1; LoadData на Main Camera Scene2. Поле ввода и Save в координатах книги. |
| 436: освещение загружаемой сцены | каждая сцена назначения, Book → Hour 23 → Bake active scene lighting | Предоставлена команда для настоящего bake в редакторе. Данные запекания здесь не сгенерированы: это нужно выполнить в Unity, затем сохранить. В исходных сценах уже есть направленный свет и настройки окружения. |
| 438–443: Player Settings и Build Settings | ProjectSettings/EditorBuildSettings.asset, Assets/Editor/BuildHour23.cs | Список семи готовых сцен. Скрипт сборки задаёт Company/Product,1000×700 и обычное окно выбора параметров Unity2018. Отладочные сцены доступны отдельно в Project. |
| 444–445: итоговое упражнение — собрать выбранный проект и запустить | Book → Hour 23 → Build Windows x64; Build-Windows.ps1 | Реальный вызов BuildPipeline, проверка результата. Никакого EXE пока нет. Дополнительная 04_BuildExample_Cube — сохранённый простой куб из первого часа, если хотите собрать вместо демонстрации данных. |

Разные практикумы имеют отдельные пары, поэтому названия сравнения содержат префиксы. Точные имена **Scene1/Scene2** и индексы0/1 сохранены у накопленного итогового результата. Целевые индексы остальных пар явно записаны в Inspector и соответствуют поставленному BuildSettings; не переставляйте сцены без обновления `targetSceneIndex`.

### Список сборки

0. Scene1 — ввод и сохранение имени, сохраняемый Cube.
1. Scene2 — Sphere, чтение имени.
2. 02_Persistent_Scene1 — Cube с DontDestroy без PlayerPrefs.
3. 02_Persistent_Scene2 — Sphere и наблюдение сохранённого Cube.
4. 01_SceneOrder_Scene1 — обычный Cube, переход без сохранения.
5. 01_SceneOrder_Scene2 — Sphere, обратный переход.
6. 04_BuildExample_Cube — отдельная простая сцена куба из часа1.

В начале сборки запускается Scene1. Если для итогового упражнения хотите только куб, в File → Build Settings оставьте включённой только 04_BuildExample_Cube и поставьте её первой. Остальные учебные пары требуют исходных индексов, поэтому не запускайте их из такой изменённой конфигурации; восстановите EditorBuildSettings из поставки для полной демонстрации.

## Освещение и Windows-сборка без Hub

Для проверки правила со стр.436 откройте сцену назначения, выберите Window → Lighting → Settings, отключите Auto Generate и нажмите Generate Lighting, либо используйте **Book → Hour 23 → Bake active scene lighting**. Проверьте переход из её первой сцены после запекания. Генератор данных освещения здесь не запускался, и LightingData.asset не подделан.

Выберите **Book → Hour 23 → Build Windows x64**. Нужен компонент Windows Build Support той же версии Unity; Windows Editor обычно имеет встроенную поддержку своей платформы. Результат: **Hour23/Builds/Hour23/Hour23.exe** вместе с папкой данных и DLL.

Для командной сборки закройте открытый экземпляр этого проекта и запустите PowerShell:

```powershell
./Build-Windows.ps1 -UnityPath 'C:\\Program Files\\Unity\\Editor\\Unity.exe'
```

Укажите фактический путь установленного обычного Unity.exe. Hub не требуется. Скрипт ждёт завершения процесса, проверяет его код, новый журнал с маркером успеха и наличие EXE. Если модуль платформы отсутствует или есть ошибка компиляции/сборки, выполнение останавливается.

Для передачи игры упакуйте **всю** папку Builds/Hour23. Один EXE без *_Data/DLL не является полной Unity-игрой.

## Статус проверки

Статически сверены YAML, локальные fileID, GUID скриптов, подключения компонентов, конфигурация сцен и целевые индексы. Проверка синтаксиса C# при наличии анализатора — отдельная от компиляции с Unity API. **Импорт, десериализация самим Unity, компиляция, Play, bake, PowerShell-скрипт, сборка и запуск EXE здесь НЕ ВЫПОЛНЯЛИСЬ.** После открытия в Unity требуется проверить Console и пройти пункты выше. Работа не объявляется полностью проверенной или готовой к сдаче без этой проверки.
'''

POWERSHELL=r'''param([Parameter(Mandatory=$true)][string]$UnityPath)
$ErrorActionPreference = 'Stop'
if (!(Test-Path -LiteralPath $UnityPath -PathType Leaf)) { throw 'Unity.exe not found.' }
$project = $PSScriptRoot
$log = Join-Path $project 'build-windows.log'
if (Test-Path -LiteralPath $log) { Remove-Item -LiteralPath $log }
$arguments = '-batchmode -nographics -quit -projectPath "{0}" -executeMethod BuildHour23.BuildWindows -logFile "{1}"' -f $project, $log
$process = Start-Process -FilePath $UnityPath -ArgumentList $arguments -Wait -PassThru
if ($process.ExitCode -ne 0) { throw "Unity failed: $($process.ExitCode). See $log" }
if (!(Test-Path -LiteralPath $log)) { throw 'No build log was produced.' }
if (!(Select-String -LiteralPath $log -Pattern 'HOUR23_BUILD_SUCCEEDED' -Quiet)) { throw "Build success not confirmed. See $log" }
$exe = Join-Path $project 'Builds/Hour23/Hour23.exe'
if (!(Test-Path -LiteralPath $exe -PathType Leaf)) { throw "Output missing: $exe" }
Write-Host "Build completed: $exe. Distribute its entire folder, including _Data and DLLs."
'''


def main():
    (PROJECT/'Assets/Scripts').mkdir(parents=True,exist_ok=True)
    guids={name:write_script(PROJECT,name,source) for name,source in RUNTIME.items()}
    main1=camera_with(guids,[('SaveData','  playerName: \n'),observation('Chapter 23: type your name, Save, then click the Cube. Scene2 must retain the Cube and show the saved name.')])+cube_with(guids,1)
    main2=camera_with(guids,[('LoadData',''),observation('Scene2: the Sphere belongs to this scene; the Cube arrived from Scene1. Saved name appears below.')])+native.primitive(1000,'Sphere','Sphere',pos=(0,2,0))
    persistent1=camera_with(guids,[observation('DontDestroyOnLoad practicum: click Cube to load 02_Persistent_Scene2. No PlayerPrefs is involved in this pair.')])+cube_with(guids,3)
    persistent2=camera_with(guids,[observation('Persistent-object destination: the same Cube remains, and Sphere appears at (0,2,0).')])+native.primitive(1000,'Sphere','Sphere',pos=(0,2,0))
    order1=camera_with(guids,[('SceneOrderInput','  targetSceneIndex: 5\n'),observation('Scene order comparison: ordinary LoadScene replaces all current scene objects. Cube is not marked DontDestroyOnLoad.')])+native.primitive(1000,'Cube')
    order2=camera_with(guids,[('SceneOrderInput','  targetSceneIndex: 4\n'),observation('Scene order destination: Sphere replaces Cube. Load other scene returns to the first scene of this pair.')])+native.primitive(1000,'Sphere','Sphere',pos=(0,2,0))
    build_example=camera_with(guids,[observation('Chapter 23 final exercise may build any prior project. This simple saved cube matches the introductory hour1 example.')])+native.primitive(1000,'Cube')
    native.build_project(23,[('Scene1',main1),('Scene2',main2),('02_Persistent_Scene1',persistent1),('02_Persistent_Scene2',persistent2),('01_SceneOrder_Scene1',order1),('01_SceneOrder_Scene2',order2),('04_BuildExample_Cube',build_example)],README)
    write_editor(BUILD)
    (PROJECT/'Build-Windows.ps1').write_text(POWERSHELL)
    (PROJECT/'.gitignore').write_text('Library/\nTemp/\nObj/\nLogs/\nBuilds/\n*.csproj\n*.sln\nbuild-windows.log\n')
    manifest=json.loads((PROJECT/'scene_manifest.json').read_text());manifest.update(runtime_scripts=len(RUNTIME),editor_scripts=1,book_printed_pages='431–445',unity_import='UNRUN',unity_compilation='UNRUN',play='UNRUN',lighting_bake='UNRUN',windows_build='UNRUN',windows_launch='UNRUN',external_assets_required=False)
    (PROJECT/'scene_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    for folder in [PROJECT/'Assets',PROJECT/'ProjectSettings']:
        if folder.name=='Assets':native.metadata(folder,folder=True)
    # Do not pretend YAML structure is a Unity-engine deserialization test.
    from validate_native_projects import validate
    report=validate(PROJECT)
    # Explicitly cross-check the index-based assignments against the saved scene list.
    scenes=manifest['scenes']
    assert scenes[1]['path']=='Assets/Scenes/Scene2.unity'
    assert scenes[3]['path']=='Assets/Scenes/02_Persistent_Scene2.unity'
    assert scenes[4]['path']=='Assets/Scenes/01_SceneOrder_Scene1.unity'
    assert scenes[5]['path']=='Assets/Scenes/01_SceneOrder_Scene2.unity'
    report['target_indices']='PASS';report['external_assets_required']=False;report['lighting_bake']='UNRUN';report['windows_build']='UNRUN';report['windows_launch']='UNRUN'
    (PROJECT/'structural_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
