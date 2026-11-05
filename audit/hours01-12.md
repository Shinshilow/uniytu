# Аудит книги: часы 1–6

Источник: Разработка игр на Unity 2018 за 24 часа, Майк Гейг, Эксмо, 2020
Номер PDF = печатная страница + 1.
Сопроводительные файлы: http://addons.eksmo.ru/it/Unity.zip

Это требования и сверка, не отчёт о запуске. Визуально прочитаны рис.3.9 (PDF80) и4.3 (PDF85).

## Час 1: Введение в Unity (печатные 25–47)

Книга в этом часе не требует пользовательских текстур или UV; не добавлять их как вымышленное требование.

Ассеты: Внешних ассетов нет.

### H01-P01 — Создание первого проекта (стр. 29–30)

- Проект Hour 1 TIY, режим 3D; без добавочных Asset Packages и Analytics.
- Существующий проект можно открыть напрямую Unity File > Open Project; Hub не требуется.

### H01-E — Итоговое упражнение (стр. 46–47)

- Новая сцена, папка Assets/Scenes, сохранить сцену под описательным именем.
- Добавить Cube; исследовать Transform/Inspector.
- Освоить Hand, Flythrough и навигацию вокруг куба. Это действия пользователя в редакторе, их невозможно доказать наличием EXE.

### Проверка

- Assets/Scenes содержит сохранённую открываемую сцену; Cube, Camera и свет доступны сразу в edit mode.
- Нет compile errors; Play отображает куб, но наличие Play не заменяет редакторные шаги.

### Несоответствия старого варианта

- Добавлены лишние общие runtime-скрипты всех часов и UI; нет подтверждения пользовательской практики.
- Одноцветный куб сам по себе для упражнения 1 допустим: «нет текстуры» не является нарушением этого часа.

## Час 2: Игровые объекты (печатные 48–63)

Тема — Transform/иерархия; UV/карты материалов не заданы.

Ассеты: Внешних ассетов нет.

### H02-P01 — Создание игровых объектов (стр. 52–53)

- Новая сцена; добавить Empty, Cube и Point Light.
- Empty содержит только Transform. Cube содержит Transform, MeshFilter, MeshRenderer, BoxCollider. Point Light имеет Transform и Light.
- Сохранить отдельный пример позволяет проверить компоненты, не смешивая с итоговой иерархией.

### H02-LAB — Перемещение, вращение, масштаб, global/local, pivot/center (стр. 54–61)

- Показать работу Move/Rotate/Scale, изменения через Transform.
- Порядок операций имеет значение: локальные оси меняются после поворота.
- Для связанных объектов родительские Transform влияют на ребёнка.
- В числовом примере обсуждаются перенос (1,0,0) и поворот 90 градусов вокруг Z; это объяснение систем координат, а не отдельный фиксированный результат сцены.

### H02-E — Родитель/ребёнок (стр. 63–63)

- Cube world Position (0,2,-5).
- Добавить Sphere, сделать ребёнком Cube, затем Sphere.localPosition=(0,1,0).
- Проверить изменение положения, вращения и масштаба у обоих объектов; сохранить исходное упражнение.

### Проверка

- Cube и Sphere реально находятся в сохранённой сцене, а не создаются лишь после Play.
- Sphere.parent == Cube; локальные координаты (0,1,0), мировые (0,3,-5) при исходных Transform.
- Есть отдельная сцена практикума Empty/Cube/Point Light.

### Несоответствия старого варианта

- В старом варианте создана только итоговая пара Cube/Sphere, отсутствует отдельный практикум компонентов и демонстрация local/global.

## Час 3: Модели, материалы и текстуры (печатные 64–79)

Обязательны настоящие файлы текстур, назначенные материалам; импорт нормалей, tiling Main Maps, корректные Standard shaders. Fig3.9 визуально прочитан из PDF p80.

Ассеты: Torus.fbx, Robot Kyle package/model and its original texture assets, Brick_Texture.png, Brick_Normal.png

### H03-P01 — Импорт Torus (стр. 67–68)

- Assets/Models; импортировать оригинальный Torus.fbx из Час 3.
- Перенести Torus на сцену.
- На самом ModelImporter изменить Scale Factor с 1 на 100 и Apply. Это не transform.localScale=100.

### H03-P02 — Robot Kyle из Asset Store (стр. 68–70)

- Отдельная новая сцена. Найти официальный Robot Kyle Unity Technologies.
- Импортировать весь пакет; запасной вариант — пакет в сопроводительных файлах книги.
- Перетащить модель из Assets/Robot Kyle/Model на сцену; при необходимости подобрать масштаб для обзора.
- Импорт текстур/материалов модели должен сохранить ссылки и UV модели; не заменять робота капсулой.

### H03-P03 — Кирпичная стена (стр. 75–76)

- Создать Assets/Textures и Assets/Materials.
- Импортировать Brick_Texture.png.
- Cube Position (0,1,-5), Scale (5,2,1).
- Создать материал BrickWall, Shader Standard; Brick_Texture назначить Main Maps > Albedo.
- Назначить BrickWall стене.
- Main Maps > Tiling X=3, Y оставлен 1. Нельзя менять Secondary Maps вместо Main Maps.

Материалы (точные значения):

- {"name": "BrickWall", "shader": "Standard", "albedo": "Brick_Texture.png", "mainTextureScale": [3, 1]}

### H03-E — Четыре варианта кирпичных сфер (стр. 78–79)

- Assets/Materials и Assets/Textures; оригинальные Brick_Texture.png и Brick_Normal.png.
- Brick_Texture TextureImporter.anisoLevel=3.
- Brick_Normal TextureImporter.textureType=NormalMap; Apply.
- Directional Light Position(0,10,-10), Euler(30,-180,0).
- Четыре Sphere, все Scale(2,2,2), позиции (1,2,-5),(-1,0,-5),(1,0,-5),(-1,2,-5).
- Назначить по одному материалу каждой сфере. Порядок material↔sphere в тексте не зафиксирован.
- Вопреки названиям материалов, все четыре используют Standard/Opaque, не Legacy shader.

Материалы (точные значения):

- {"name": "DiffuseBrick", "shader": "Standard", "renderingMode": "Opaque", "metallic": 0, "smoothness": 0, "albedo": "Brick_Texture.png", "normal": null, "mainTextureScale": [3, 3], "mainTextureOffset": [0, 0]}
- {"name": "SpecularBrick", "shader": "Standard", "renderingMode": "Opaque", "metallic": 0, "smoothness": 0.6, "albedo": "Brick_Texture.png", "normal": null, "mainTextureScale": [3, 3], "mainTextureOffset": [0, 0]}
- {"name": "BumpedBrick", "shader": "Standard", "renderingMode": "Opaque", "metallic": 0, "smoothness": 0, "albedo": "Brick_Texture.png", "normal": "Brick_Normal.png", "normalStrength": 1, "mainTextureScale": [3, 3], "mainTextureOffset": [0, 0]}
- {"name": "BumpedSpecularBrick", "shader": "Standard", "renderingMode": "Opaque", "metallic": 0, "smoothness": 0.6, "albedo": "Brick_Texture.png", "normal": "Brick_Normal.png", "normalStrength": 1, "mainTextureScale": [3, 3], "mainTextureOffset": [0, 0]}

### Проверка

- После закрытия и повторного открытия сцены материалы и текстуры сохранены как ассеты, Renderer.sharedMaterials ссылаются на них.
- Для сферы есть ненулевая UV-развёртка (у built-in sphere она уже существует); albedo видно на всей сфере. Не требуется изобретать новую UV-развёртку.
- В Inspector правильный tiling, _Metallic, _Glossiness и normal import; Bumped-материалы имеют _NORMALMAP keyword.
- Сравнить блики и рельеф в одинаковом освещении с рис.3.9; выполнить Play без ошибок.

### Несоответствия старого варианта

- Старый MaterialsDemo создавал процедурную кирпичную картинку и не импортировал реальный normal map.
- Legacy Shaders/Diffuse, Specular, Bumped Diffuse, Bumped Specular не соответствуют рис.3.9; там Standard.
- Старые tiling=(1,1), отсутствует обязательный (3,3); Wall, Torus и Robot Kyle отсутствуют.

## Час 4: Ландшафт и элементы окружающей среды (печатные 80–104)

TerrainData.splatPrototypes в Unity2018.1 с настоящими albedo/normal maps; spatial alpha/splat map, плавные переходы по рельефу; Terrain trees/detail layers, не нарисованные поверх примитивы.

Ассеты: terrain.raw, Standard Assets Environment/Terrain Assets, GrassHillAlbedo, GrassRockyAlbedo, CliffAlbedoSpecular (текст итогового упражнения сокращает до Cliff), SandAlbedo, Conifer_Desktop, GrassFrond01AlbedoAlpha, Standard Assets Characters/FPSController

### H04-P01 — Terrain и импорт карты высот (стр. 81–84)

- Новый Terrain; width/length 50. Импорт оригинального terrain.raw.
- Рис.4.3 (визуально проверен): Depth Bit16, Width513, Height513, ByteOrder Mac, Flip Vertically выключен; TerrainSize X50 Y600 Z50 при импорте.
- После импорта изменить максимальную высоту Terrain на60, конечный размер (50,60,50).
- Декодировать RAW как big-endian 16-bit, а не Perlin Noise.

### H04-P02 — Ручной ландшафт (стр. 87–88)

- Отдельный Terrain 50×50, максимальная высота60.
- Paint Height: Height20, Flatten; затем создать рельеф, похожий на рис.4.7 инструментами Raise/Lower, Paint Height, Smooth Height.
- Конкретный рельеф допускает вариации; исходная базовая высота20 должна быть осознанно задана.

### H04-P03 — Текстурирование (стр. 88–92)

- Импортировать Environment/TerrainAssets (сопроводительный пакет, если встроенного нет).
- Добавить GrassHillAlbedo как первый Terrain splat: покроет весь Terrain.
- Добавить GrassRockyAlbedo и выбрать его; BrushSize30, Opacity20, TargetStrength0.6.
- Нанести GrassRockyAlbedo на крутые склоны и трещины.
- Дополнительные предложенные текстуры: CliffAlbedoSpecular на крутых частях, SandAlbedo для тропы.
- Normal Map необязателен для первого слоя, но если добавляется, должен быть импортирован как NormalMap.

### H04-P04 — Terrain Trees (стр. 93–95)

- Сцена с Terrain width/length100, уже сформированным и текстурированным.
- Terrain Edit Trees > Add Tree, оригинальный Conifer_Desktop.
- BrushSize2, Density10; Random Width/Height с уменьшенным средним размером.
- Деревья наносятся Terrain TreeInstances; Draw в TerrainSettings включён.
- Допускается свободное размещение и плотность после начальной практики.

### H04-P05 — Трава и настройки Terrain (стр. 95–100)

- Terrain Edit Details > Add Grass Texture: GrassFrond01AlbedoAlpha.
- Подобрать цвета травы к земле; использовать irregular brush.
- Совет книги: Opacity0.01, TargetStrength0.0625 как начальные значения.
- Сохранить DetailPrototype/DetailLayers, подходящие texture alpha и renderMode billboard, настройки ветра; реальное количество не фиксировано.

### H04-P06 — FPSController (стр. 101–102)

- Импортировать Characters и поставить FPSController на Terrain чуть выше земли.
- WASD, мышь для обзора, Space для прыжка.
- Удалить Main Camera либо её AudioListener, т.к. FPSController содержит камеру/listener.
- Проверить, что персонаж не застревает в Terrain и не проваливается.

### H04-E — Пляж, горный хребет, равнина (стр. 103–104)

- Ландшафт с пляжем, горным хребтом, плоской равниной; форма свободная.
- Пляж SandAlbedo плавно переходит в GrassRockyAlbedo.
- Плоские участки GrassHillAlbedo. По мере крутизны GrassHillAlbedo→GrassRockyAlbedo; наиболее высокие/скалистые участки→Cliff.
- В тексте напечатано GlassRockyAlbedo; это опечатка относительно уже используемого GrassRockyAlbedo.
- Завершить деревьями и травой, используя Terrain paint layers.

### Проверка

- TerrainCollider.data == Terrain.terrainData; heightmap фактически имеет рельеф.
- Все splat textures назначены и asset-файлы существуют, alpha weights >=0 и сумма слоёв≈1.
- Terrain treePrototypes/treeInstances и detailPrototypes/слои не пустые.
- На пляже/равнине/склонах видны разные текстуры; ближний вид не выглядит одноцветной заливкой.
- FPS может ходить по реальному рельефу, прыгать; ровно один AudioListener.

### Несоответствия старого варианта

- Вместо terrain.raw использовалась процедурная формула.
- Использовались маленькие одноцветные текстуры; трёх цветов недостаточно для всех требуемых слоёв.
- Деревья были Cylinder/Sphere, Terrain tree/detail layers отсутствовали.
- Нет травы, FPSController, связанных практикумов.

## Час 5: Источники света и камеры (печатные 105–127)

Особая текстура biohazard.png назначается Light.cookie с TextureImporter Cookie/Spotlight и alphaFromGrayscale, а не обычным albedo.

Ассеты: biohazard.png

### H05-P01 — Point Light (стр. 108–109)

- Отключить default Directional Light.
- Plane Position(0,0.5,0),Euler(270,0,0).
- Cube1 Position(-1.5,1,-5); Cube2 Position(1.5,1,-5).
- Point Light Position(0,1,-7), Shadows Hard; исследовать цвет/range/intensity.

### H05-P02 — Spotlight (стр. 110–110)

- Дубликат Point Light сцены. Переименовать Point Light→Spotlight, Type=Spot, Position(0,1,-13).
- Изучить distance/intensity/spot angle.

### H05-P03 — Directional Light (стр. 110–111)

- Дубликат Spotlight сцены. Переименовать свет Directional Light, Type=Directional, Euler(75,0,0).
- Затем Position(50,50,50): освещение от переноса не должно измениться.
- Процедурное небо зависит от направления света.

### H05-P04 — Halo (стр. 112–113)

- Объяснение/эксперимент DrawHalo для света. Книга здесь не фиксирует отдельную сцену или численные параметры.

### H05-P05 — Cookie (стр. 114–115)

- Новая сцена, удалить Directional Light.
- Plane Position(0,1,0),Euler(270,0,0).
- На Main Camera добавить Light Spot, range18, spotAngle40, intensity3.
- Импорт biohazard.png: TextureType Cookie, LightType Spotlight, AlphaSource FromGrayscale.
- Light.cookie=biohazard; белые области пропускают свет, чёрные блокируют.

### H05-P06 — Две камеры и Depth (стр. 118–118)

- Cube1 Position(-2,1,-5); Cube2 Position(2,1,-5).
- Main Camera Position(-3,1,-8),Euler(0,45,0).
- Camera2 Position(3,1,-8),Euler(0,315,0); AudioListener Camera2 выключен.
- Показать, что верхняя по Depth камера перекрывает нижнюю; затем Main.depth=1.

### H05-P07 — Разделение экрана (стр. 119–119)

- На базе двух камер. Main depth=-1, rect=(0,0,1,0.5).
- Camera2 depth=-1, rect=(0,0.5,1,0.5).
- Образы двух камер одновременно, горизонтальное разделение.

### H05-P08 — Картинка-в-картинке (стр. 120–120)

- На базе двух камер. Main depth=-1, rect=(0,0,1,1).
- Camera2 depth=0, rect=(0.75,0.75,0.2,0.2).
- Маленькое изображение сверху справа; отдельная сохранённая сцена от split screen.

### H05-P09 — Слои Ignore Lights / Ignore Cameras (стр. 124–125)

- Новая сцена с двумя кубами. Текст печатает обе позиции как(2,1,-5); это вероятная опечатка, для демонстрации следует разнести и отметить поправку, а не скрывать.
- Создать пользовательские слои Ignore Lights и Ignore Cameras.
- Первый куб на Ignore Lights, второй на Ignore Cameras.
- DirectionalLight.cullingMask исключает Ignore Lights; MainCamera.cullingMask исключает Ignore Cameras.
- В Game один неосвещённый куб, второй отсутствует.

### H05-E — Четыре Point Light и четыре камеры (стр. 126–127)

- Новая сцена, удалить DirectionalLight. Sphere Position(0,0,0).
- Point Lights Position(-4,0,0),(4,0,0),(0,0,-4),(0,0,4); четыре разных цвета. Range/Intensity свободно подобрать.
- Удалить default MainCamera. Camera positions(2,0,0),(-2,0,0),(0,0,2),(0,0,-2); каждая смотрит в центр сферы.
- AudioListener включён ровно у одной камеры.
- Каждая camera.rect занимает свою четверть (width0.5,height0.5); четыре разных угла.

### Проверка

- Сохранены отдельные Point/Spot/Directional/Cookie/TwoCameras/Split/PiP/Layers/Exercise сцены.
- Cookie импортирован корректно, biohazard виден как проекция, а не просто файл в папке.
- Камеры не перекрывают чужие viewport там, где это не цель практикума; AudioListener count=1.
- Для четырёх Point Lights нужен достаточный QualitySettings.pixelLightCount, иначе часть цветного света может уходить в vertex lighting.

### Несоответствия старого варианта

- Реализовано только итоговое четыре камеры; остальные восемь практикумов пропущены.
- Нет biohazard cookie, слоёв CullingMask и сцены PiP.

## Час 6: Игра первая: Великолепный гонщик (печатные 128–145)

Настоящий Terrain с импортированной RAW-картой; terrain splat maps с Grass/Cliff/Mud; вода Water4Advanced, procedural skybox, fog. Плоская цветная арена не соответствует главе.

Ассеты: TerrainHeightmap.raw, Standard Assets Environment, GrassHillAlbedo, CliffAlbedoSpecular, GrassRockyAlbedo, MudRockyAlbedoSpecular, Water4Advanced.prefab, Standard Assets Characters/FirstPersonCharacter/Prefabs/FPSController.prefab, FinishZone.cs, GameManager.cs, PlayerRespawn.cs

### H06-WORLD — Мир гонщика (стр. 131–133)

- Amazing Racer; Terrain at(0,0,0). Оригинальный TerrainHeightmap.raw, big-endian Mac, default Depth/Width/Height.
- TerrainSize width200,length100,maxHeight100. Сохранить Assets/Scenes/Main.unity.
- Текстуры: GrassHillAlbedo для равнин; CliffAlbedoSpecular на крутых участках; GrassRockyAlbedo между ними; MudRockyAlbedoSpecular в ямах. Оттенки/размещение творческие.
- Немного Terrain trees преимущественно на ровных участках.
- Water4Advanced prefab Position(100,29,100),Scale(2,1,2).

### H06-ENV — Туман и небо (стр. 133–135)

- Lighting Settings Fog включён, пример white,density0.005; в книге явно допускается изменить или удалить эти параметры.
- Отдельный Material Shader Skybox/Procedural, назначить RenderSettings.skybox. Настроить sun/atmosphere/sky tint/exposure на вкус.

### H06-PLAYER — Игрок (стр. 135–136)

- Импортировать Characters, поставить настоящий FPSController prefab.
- Переименовать в Player. Position(165,32,125),Euler(0,260,0).
- Удалить Main Camera, т.к. Player имеет свою.
- Проверить края карты: в исходной RAW специально оставлены выходы. Исправить Terrain/границы или SlopeLimit так, чтобы нельзя было выпасть.

### H06-OBJECTS — Игровые зоны и менеджер (стр. 137–139)

- Empty Spawn Point Position(165,32,125),Euler(0,260,0).
- Plane Water Hazard Detector Position(100,27,100),Scale(20,1,20), MeshCollider.convex=true,isTrigger=true; MeshRenderer.enabled=false.
- Empty Finish Zone Position(26,32,37), Point Light range35,intensity3; CapsuleCollider.isTrigger=true,radius9.
- Empty Game Manager.

### H06-SCRIPTS — Импорт и связи (стр. 140–142)

- Assets/Scripts с оригинальными FinishZone.cs, GameManager.cs, PlayerRespawn.cs.
- FinishZone на Finish Zone; GameManager на Game Manager; PlayerRespawn на Water Hazard Detector.
- PlayerRespawn.gameManager→Game Manager; FinishZone.gameManager→Game Manager.
- GameManager.spawnPoint→Spawn Point; GameManager.player→Player.
- GUI здесь именно предоставленный legacy OnGUI script; новая UI система изучается позже.
- Условие конца — вход в Finish Zone; нет отдельного win/lose, цель — улучшать время. Водная опасность возвращает к спауну.

### H06-TEST — Тестирование (стр. 142–143)

- Проверить возможность завершить маршрут, возврат после воды, отсутствие выхода за границы.
- Проверить взаимодействие SlopeLimit с холмами; подобрать скорость ходьбы/бега при необходимости.
- Нельзя выдавать правки реального плейтеста за выполненные без запуска.

### H06-E — Авторская модификация (стр. 145–145)

- Это свободное улучшение базовой игры. Книга перечисляет предложения, а не требует реализовать все одновременно.
- Варианты: альтернативные Finish Zones; новые опасности в рельефе; несколько spawn points, на которые отправляют разные опасности; другое небо/текстуры.
- Сохранить базовый Main как контрольную сцену и отдельный Exercise с явно описанным выбранным изменением.

### Проверка

- Оригинальная RAW высотная карта применена, size/позиция Terrain соответствуют сцене.
- Все Terrain splat textures, вода, FPS prefab ссылки сохранены.
- Игрок видит сцену от первого лица, ходит, бежит, прыгает и не выходит из мира.
- Water respawn сохраняет нужную позицию/ориентацию; Finish уведомляет GameManager; restart повторяет цикл.
- Доступность маршрута и корректность размеров коллайдеров проверены в Play, не только синтаксисом.

### Несоответствия старого варианта

- Старая Race была плоской ареной с видом сверху и капсулой, без TerrainHeightmap.raw, FPSController, воды Water4, текстур и legacy GUI.
- Исходные GameManager/FinishZone/PlayerRespawn отсутствовали и заменены универсальным LessonActor.
- Две finish зоны/checkpoint сами по себе допустимы как Exercise, но не заменяют базовую игру и предусмотренные связи.


# Аудит книги: часы 7–12

Источник: предоставленный PDF. Печатная страница = PDF страница − 1. Чтение требований не означает проверку проекта в Unity.

Все указанные ниже имена сцен с числовым префиксом — предлагаемые названия для разделения практикумов; обязательные названия книги Main и Lamps указаны отдельно.

## Час 7: Скрипты, часть 1

Печатные страницы 146–167.

### 07-P01 — Создание и назначение скрипта

Вид: practicum; стр. 149, 150; сцена `01_HelloWorld`.

- Assets/Scripts/HelloWorldScript.cs; class HelloWorldScript : MonoBehaviour.
- Start prints exactly Hello World; attach component to Main Camera.
- Before attaching script nothing runs; retain a short explanation or separate inactive example instead of fake output.

Проверка: Enter Play: exactly one Hello World per camera component; verify component exists in Inspector; stop and rerun.

### 07-P02 — Использование встроенных методов

Вид: practicum; стр. 153, 154; сцена `02_ImportantFunctions`.

- ImportantFunctions.cs on Main Camera.
- Start prints Start runs before an object Updates.
- Update prints This is called once a frame. Must demonstrate frame callback; do not replace with unrelated GUI label.

Проверка: Run briefly: initial Start line before repeated Update lines; stop quickly to avoid excessive logs.

### 07-A01 — Операторы

Вид: additional_practice; стр. 160; сцена `03_EqualityAndOperations`.

- Book explicitly recommends EqualityAndOperations.cs from original Hour7 files; preserve original file and inspect examples.
- Examples should cover arithmetic, assignment, comparison, logical conditions; explanatory examples are not separate required games.

Проверка: Open script and identify operator cases; actual output must match cases if attached.

### 07-E01 — Три отдельные задачи

Вид: final_exercise; стр. 167; сцена `04_Exercise`.

- Three separate scripts, all attached to Main Camera.
- Task1 sums even integers 2 through499 inclusive and logs result62250.
- Task2 visits all integers1..100; for multiples of3 OR5 prints Программирование — это прекрасно!, otherwise number.
- Task3 prints first20 Fibonacci terms beginning0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181.

Проверка: Console shows sum62250 once; task2 emits100 entries including47 replacements and53 numeric entries; Fibonacci task emits20 terms with final4181.

### Оригинальные ассеты

- EqualityAndOperations.cs; ImportantFunctions.cs original examples

### Маппинг и материалы

- This chapter does not require texture mapping or textured scenery; focus is C# and Console.

### Недостатки прежнего архива

- Only final exercise was provided previously; HelloWorldScript, ImportantFunctions and EqualityAndOperations examples were omitted.

## Час 8: Скрипты, часть 2

Печатные страницы 168–188.

### 08-P01 — Идентификация частей метода

Вид: written_practicum; стр. 170, 171; сцена `01_Methods`.

- Analyze int TakeDamage(int damageAmount) { int health=100; return health-damageAmount; }.
- Answers: name TakeDamage, return int, one int parameter damageAmount, block declares health and returns subtraction.

Проверка: Keep answers in a short document; no invented 3D requirement.

### 08-P02 — Вызов перегруженных методов

Вид: practicum; стр. 173, 174; сцена `01_Methods`.

- FireBallScript.cs attached to Main Camera.
- Implement int TakeDamageFromFireball() returning100-5; overload(int damage) returning100-damage; overload(int damage,int playerHealth) returning playerHealth-damage.
- Start calls all three with(),(25),(30,50), logs Player health:95,75,20 respectively.

Проверка: Play emits health95,75,20 in order; all overloads present as class methods.

### 08-P03 — Считывание осей игрока

Вид: practicum; стр. 177; сцена `02_PlayerInput`.

- PlayerInput.cs attached to Main Camera; read Input.GetAxis("Horizontal") and("Vertical") in Update.
- Log Horizontal movement selected: hVal / Vertical movement selected: vVal only when nonzero.
- Default mappings include arrows and WASD; retain InputManager axes so remapping remains possible.

Проверка: Arrows and WASD yield positive/negative values; releasing returns zero; inspect Edit Project Settings Input.

### 08-P04 — Считывание определённых клавиш

Вид: practicum; стр. 178; сцена `03_KeyInput`.

- PlayerInput variant on Main Camera: Input.GetKey(KeyCode.M) logs while held; Input.GetKeyDown(KeyCode.O) logs once per press.

Проверка: Hold M several frames vs hold O; verify different Console counts.

### 08-P05 — Считывание движения мыши

Вид: practicum; стр. 180; сцена `04_MouseInput`.

- PlayerInput variant reads Mouse X and Mouse Y every Update; logs nonzero values for each axis.

Проверка: Move mouse horizontally/vertically with Game focus; corresponding signed values appear.

### 08-P06 — Преобразование локального объекта

Вид: practicum; стр. 182; сцена `05_LocalCube`.

- Cube at(0,-1,0); CubeScript.cs attached to Cube.
- Update: transform.Translate(.05f,0f,0f); transform.Rotate(0f,0f,1f); transform.localScale=new Vector3(1.5f,1.5f,1.5f).
- This intentionally demonstrates cumulative per-frame local-space motion; retain book example separately from deltaTime-based controller.

Проверка: Cube follows a broad circle due to rotating local axes; scale stays1.5 rather than accumulating.

### 08-P07 — Преобразование целевого объекта

Вид: practicum; стр. 185, 186; сцена `06_TargetCube`.

- Cube at(0,-1,0); TargetCubeScript.cs attached to Main Camera.
- Start target=GameObject.Find("Cube"); Update performs same Translate(.05,0,0),Rotate(0,0,1),localScale1.5 on target.

Проверка: Only camera has controlling script; cube still follows circular path; verify target found and no null references.

### 08-E01 — Управление кубом

Вид: final_exercise; стр. 187, 188; сцена `07_Exercise`.

- Cube at(0,0,-5); CubeControlScript.cs in Scripts attached to cube.
- Left/right moves along worldX negative/positive; down/up moves along worldZ negative/positive.
- MouseY rotates CAMERA aboutX; MouseX rotates CUBE aboutY.
- M toggles cube between original scale and double original scale.

Проверка: Check all four arrows both before and after mouse rotation; motion must remain intended axes; two M presses restore original size; camera pitch and cube yaw change independently.

### Маппинг и материалы

- No textured model is required in this chapter; appropriate input mappings are required.

### Недостатки прежнего архива

- Prior project only implements final CubeControlScript; six runtime practica and written method analysis omitted.

## Час 9: Столкновения

Печатные страницы 189–202.

### 09-P01 — Использование твёрдых тел

Вид: practicum; стр. 191; сцена `01_Rigidbody`.

- Cube at(0,1,-5); first observe without Rigidbody, then add Rigidbody and observe gravity.
- Explore Drag and Constraints; preserve baseline and gravity variant or explain change in scene notes.

Проверка: Without Rigidbody stays in place; with gravity falls; Inspector contains correct3D Rigidbody.

### 09-P02 — Эксперименты с коллайдерами

Вид: practicum; стр. 193, 194; сцена `02_Colliders`.

- UpperCube at(0,1,-5) with Rigidbody.
- LowerCube at(0,-1,-5),scale(4,.1,4),rot(0,0,15),Rigidbody useGravityfalse.
- Observe two unrestrained bodies; then freeze ALL lowerCube position/rotation axes.
- Final demonstrated variant removes upper BoxCollider, adds SphereCollider; lower rotation changed to(0,0,350).
- Optional variant freeze only lower positionY and leave rest free.

Проверка: Before constraints both move; after FreezeAll lower fixed; upper cube with SphereCollider rolls like sphere.

### 09-A01 — Физические материалы

Вид: chapter_activity; стр. 194, 195, 196; сцена `03_PhysicMaterials`.

- Import Characters/PhysicsMaterials original assets: Bouncy,Ice,Metal,Rubber,Tree, or create PhysicsMaterial assets matching investigated behavior.
- Demonstrate Dynamic/StaticFriction,Bounciness,FrictionCombine,BounceCombine on Collider materials; do not confuse renderer Material with PhysicMaterial.

Проверка: Collider.sharedMaterial assigned; behavior differs under friction and bounce settings.

### 09-P03 — Работа с триггером

Вид: practicum; стр. 197; сцена `04_MouseTrigger`.

- Cube(-1,1,-5),Sphere(1,1,-5).
- Cube BoxCollider.isTrigger=true with TriggerScript; sphere Rigidbody gravityfalse with MovementScript.
- MovementScript.Update translates MouseX/10,MouseY/10,0.
- TriggerScript logs enter,stay,exit with other.gameObject.name; callbacks declared at class level.

Проверка: Sphere responds to mouse; passes through cube without physical collision; logs all3 callback types.

### 09-P04 — Рейкастинг

Вид: practicum; стр. 199, 200; сцена `05_Raycast`.

- Four spheres at(-1,1,-5),(1,1.5,-5),(-1,-2,5),(1.5,0,0).
- RaycastScript.cs on Main Camera; Update reads MouseX,MouseY,rotates camera and calls CheckForRaycastHit().
- Method uses Physics.Raycast(transform.position,transform.forward,out hit); logs hit object name, destroys hit.gameObject.
- No shooting mouse-click requirement in printed practicum; hit is checked every frame.

Проверка: Aim camera centre at sphere: matching sphere destroyed and logged; RaycastHit type is correct.

### 09-E01 — Два триггера и управляемая сфера

Вид: final_exercise; стр. 201, 202; сцена `06_Exercise`.

- LTrigger cube(-1.5,0,-5),scale(.1,2,2); RTrigger duplicate at(1.5,0,-5).
- Sphere(0,0,-5),Rigidbody useGravityfalse; MotionScript on sphere.
- TriggerScript on both cubes, BoxCollider.isTrigger=true (the omitted step is the exercise trick).
- Arrow movement; log TRIGGER name plus entry/stay/exit type.

Проверка: Pass through both trigger planes using arrows; Console identifies LTrigger vs RTrigger and all events; no physical blocking.

### Оригинальные ассеты

- Standard Assets/PhysicsMaterials: Bouncy,Ice,Metal,Rubber,Tree

### Маппинг и материалы

- Physical materials mandatory for investigated examples; texture mapping not specifically required.

### Недостатки прежнего архива

- Prior scaffold final trigger scene approximately matches end exercise, but omits gravity/collider/physical-material/mouse-trigger/raycast practica.

## Час 10: Игра вторая: Шар хаоса

Печатные страницы 203–218.

### 10-G01 — Замкнутая арена

Вид: game_world; стр. 205, 206, 207, 208; сцена `Main`.

- New project Шар хаоса; import Environment and Characters; save Scenes/Main.unity.
- Plane origin scale(5,1,5) =>50×50 floor. Delete default Main Camera.
- Wall1 Cube(-25,1.5,0),scale(1.5,3,51); Wall2(25,1.5,0); Wall3(0,1.5,25),rot(0,90,0); Wall4(0,1.5,-25),rot(0,90,0); group Walls origin.
- Material Wall Standard with Sand Albedo on Albedo; Smoothness0; TilingX10; assign to all four walls.
- Water4Advanced from Standard Assets/Environment/Water/Water4/Prefabs at(0,.5,0).
- SuperBouncy PhysicMaterial from fig10.3; assign PhysicsManager Default Material or explicitly to every colliding surface/body to preserve effect.

Проверка: Arena closed: balls cannot leave; wall texture visibly repeats10 times; floor water reflects as asset permits; spheres keep moving after bounces.

### 10-G02 — Контроллер и бампер

Вид: game_player; стр. 209, 210; сцена `Main`.

- FPSController prefab at(0,1,0); FirstPersonCharacter camera child localPosition(0,5,-3.5),rotation(43,0,0).
- Cube named Bumber (book typo),scale(3.5,3,1),parent FPSController; localPosition(0,0,1),localRotation0.
- Material BumperColor with chosen Albedo color; FPSController movement configuration from fig10.5.

Проверка: Move and steer controller; camera remains above/behind; physical bumper pushes colored balls.

### 10-G03 — Шары хаоса и цветные шары

Вид: game_entities; стр. 210, 211, 212, 213; сцена `Main`.

- First Chaos sphere(12,2,12),scale(.5,.5,.5),yellow ChaosBall material,tag Chaos.
- Rigidbody gravityfalse,CollisionDetection ContinuousDynamic,FreezePositionY.
- VelocityScript startSpeed50; Start rigidbody.velocity=new Vector3(startSpeed,0,startSpeed).
- Five Chaos spheres total (original plus4 duplicates),all y2; group Chaos Balls at origin.
- Blue Ball,Red Ball,Orange Ball,Green Ball: each y2,default sphere scale1,matching colored materials BlueBall/Redball/GreenBall/OrangeBall and tags Blue/Red/Green/Orange.
- Colored ball Rigidbody same gravity/collision/Y constraints; VelocityScript startSpeed25.

Проверка: Five fast yellow plus four slower colored balls move within arena; color/name/tag correctly match; no ball changesY.

### 10-G04 — Четыре угловые цели

Вид: game_logic; стр. 213, 214, 215, 216; сцена `Main`.

- Blue Goal empty(-22,2,-22),tagBlue; BoxCollider size(3,2,3),isTriggertrue; PointLight Blue intensity3 indirectMultiplier0.
- Other goals tags/colors Red,Green,Orange at other corners(22,2,-22),(22,2,22),(-22,2,22); group Goals.
- GoalScript has bool isSolved; OnTriggerEnter compares collided tag to own, marks solved,disables Light,destroys correct colored ball.
- Game Manager with GameManager refs blue/green/red/orange GoalScript; gameover only when all4 isSolved; display Game Over.
- Base book rules: player cannot lose. Do not add defeat by falling as substitute for objective.

Проверка: Wrong-colored sphere does not solve goal; matching ball solves exactly corresponding goal/light; victory only after all4 solved.

### 10-E01 — Модификация игры

Вид: final_exercise; стр. 218; сцена `Exercise`.

- Choose and document an improvement; printed suggestions: restart button,timer,varied Chaos balls,additional Chaos goal,modified bumper shape,hide water beyond arena.
- Keep Main faithful to base chapter; separate Exercise scene may add restart/timer without replacing objective.

Проверка: At least one documented improvement runs; base matching-goal game remains intact.

### Оригинальные ассеты

- Standard Assets Environment (SandAlbedo texture,Water4Advanced prefab)
- Standard Assets Characters (FPSController)

### Маппинг и материалы

- Wall material Albedo Sand Albedo; Smoothness0; texture scaleX10.
- Water4Advanced floor at y.5.
- BumperColor,ChaosBall,BlueBall,Redball,GreenBall,OrangeBall are colored renderer materials; color matching is part of gameplay.

### Недостатки прежнего архива

- Previous Chaos() is a different game:20×20 unbounded platform,5 balls to knock off,top-down cylinder player.
- Missing all four matching colored balls/goals,tags,SuperBouncy,water shader,wall textures,and FPS bumper.

### Замечания

- Values only present in figures10.3 and10.5 must be inspected visually or recovered from original companion project; do not invent and claim exact.

## Час 11: Префабы

Печатные страницы 220–231.

### 11-P01 — Создание префаба Lamp

Вид: practicum; стр. 224, 225; сцена `01_CreateLamp`.

- Cube named Lamp worldPosition(0,1,0),scale(.5,2,.5),Rigidbody.
- Sphere worldPosition(0,2.2,0),Light on Sphere; parent sphere under Lamp preserving world pose.
- Save real Assets/Prefabs/Lamp.prefab; cube+sphere must remain linked prefab assets,not mere generated GameObjects.

Проверка: Prefab asset exists; cube Rigidbody present; child world pose maintained despite parent scaling.

### 11-P02 — Несколько экземпляров

Вид: practicum; стр. 226; сцена `Lamps`.

- Scene Lamps in same project; Plane named Floor at origin; optional grey material to reveal shadows.
- Four linked instances of Lamp across floor corners (book text says place one then three more); positions not numerically specified.

Проверка: Hierarchy instances linked to Lamp asset; play physics reacts to Floor collider.

### 11-P03 — Обновление префаба

Вид: practicum; стр. 227, 228; сцена `02_PrefabUpdates`.

- On Lamp asset change Sphere Light red; every instance inherits.
- Override one instance Sphere Light back towhite; others remainred.
- Apply that override to prefab; all inherited instances become white.
- Can preserve three demonstration snapshots/scenes or a small editor guide because sequential edit operations cannot all be one final scene.
- Related chapter step: demonstrate Break Prefab Instance then Revert link in2018.1 workflow.

Проверка: Changing asset updates linked instances; local override isolated until Apply; no fake disconnected duplicates.

### 11-E01 — Instantiate в двух позициях

Вид: final_exercise; стр. 230, 231; сцена `03_Exercise`.

- Same Lamp prefab; saved root position(-1,0,-5). Delete Directional Light.
- Empty Spawn Point position(1,1,-5); Plane position(0,0,-4),rotation(270,0,0).
- PrefabGenerator.cs on Spawn Point,public GameObject prefab reference Lamp.
- B:Instantiate(prefab); Space:Instantiate(prefab,transform.position,transform.rotation).

Проверка: B spawns root at prefab position(-1,0,-5); Space at(1,1,-5); both are full Lamp with Rigidbody/light.

### Оригинальные ассеты

- Lamp.prefab created in chapter

### Маппинг и материалы

- Grey Floor material is optional; no textured Lamp requirement.

### Недостатки прежнего архива

- Prior Lamp root empty,cylinder stem,missing Rigidbody,incorrect transforms.
- Prior backdrop is Cube instead of specified Plane rotation270.
- Multiple linked instances,updates/override/Apply practice absent.

## Час 12: Инструменты создания 2D-игр

Печатные страницы 232–247.

### 12-P01 — Создание и размещение спрайта

Вид: practicum; стр. 234; сцена `01_SimpleSprite`.

- 2D project (orthographic camera,no Directional Light). Assets/Sprites/Hexagon via Create Sprites Hexagon.
- Place Hexagon in scene and change SpriteRenderer.color; preserve source sprite asset.

Проверка: Sprite visible and tinted; Camera projection Orthographic;2D editor mode.

### 12-A01 — Импорт одиночного спрайта

Вид: chapter_activity; стр. 237, 238; сцена `02_Ranger`.

- Import ranger.png from book examples or own image explicitly permitted by book; TextureImporter textureTypeSprite.
- Place sprite on scene at z in front of camera; nonzeroZ from3D scene view can hide sprites.

Проверка: Imported sprite type correct; visible inGame; image aspect and alpha preserved.

### 12-P02 — Режимы Single и Multiple

Вид: practicum; стр. 238, 239; сцена `03_SpriteSheet`.

- Import rangerTalking.png (own sheet permitted); show Single baseline and Multiple sliced variant via Sprite Editor.
- Save actual Sprite subassets and importer spritesheet rectangles; naming/slices need source/image examination.
- Do not replace sprite sheet with one flat color rectangle; the exercise is importer/slicing practice.

Проверка: Project expansion shows one sprite inSingle and multiple subSprites inMultiple; slice frames cover intended cells.

### 12-P03 — Слои сортировки

Вид: practicum; стр. 241, 242; сцена `04_SortingLayers`.

- Import2D Standard Assets. BackgroundGreyGridSprite pos(-2.5,-2.5,0),scale(2,2,1).
- Sorting layers Background and Player; BackgroundGreyGridSprite onBackground; RobotBoyCrouch00 atorigin onPlayer.
- Default moved to render last if preserving book recommendation; demonstrate reordering makes background cover robot.

Проверка: Renderer.sortingLayerName correct and layers stored in TagManager; robot appears over grid whenPlayer renders later.

### 12-P04 — Столкновение двух спрайтов

Вид: practicum; стр. 244, 245; сцена `05_2DPhysics`.

- RobotBoyCrouch00 at(0,0,0),PolygonCollider2D.
- Duplicate at(.3,-1,0),PolygonCollider2D; top Rigidbody2D dynamic,gravity as in figure12.12.
- Upper falls onto lower;3D BoxCollider/Rigidbody must not substitute.

Проверка: Upper robot falls and collides; polygon matches alpha silhouette; both render in front of camera.

### 12-E01 — Платформы и RobotBoy

Вид: final_exercise; стр. 246, 247; сцена `06_Exercise`.

- CharacterRobotBoy prefab original at(3,1.8,0); keep animator/controller and actual robot artwork.
- PlatformWhiteSprite at(0,0,0),scale(3,1,1),BoxCollider2D.
- Duplicate at(7.5,0,0),rotation(0,0,30),same scale(3,1,1).
- MainCamera position(11,4,-10),orthographicSize7,rotationdefault; arrows movement andSpace jumping.

Проверка: Actual animated RobotBoy moves/jumps; lands on both level and angled platforms; no3D physics mismatch.

### Оригинальные ассеты

- ranger.png
- rangerTalking.png
- Standard Assets/2D/Prefabs/CharacterRobotBoy.prefab
- Standard Assets/2D/Sprites/PlatformWhiteSprite
- BackgroundGreyGridSprite
- RobotBoyCrouch00

### Маппинг и материалы

- Sprite art must be imported as Sprite (2D and UI); slicing and source alpha are material to the exercises.
- SpriteRenderer sorting layers/order required; do not replace sprites with primitive colored squares and claim fidelity.

### Недостатки прежнего архива

- Prior green rectangle player is not CharacterRobotBoy and has no original animation.
- Sprite generation/import,sprite sheet slicing,sorting layers,polygon collider examples omitted.
- Platform width hardcoded6 may happen to resemble graphic but must preserve actual sprite plus transform scale3.

## Уточнение по рисункам часа10

Рис10.3 (печатная207/PDF208) визуально проверен: SuperBouncy DynamicFriction0,StaticFriction0,Bounciness1,FrictionCombine Average,BounceCombine Maximum.

Рис10.5 (печатная210/PDF211): IsWalking=false,WalkSpeed5,RunSpeed20,RunstepLengthen0.7,JumpSpeed0,StickToGroundForce10,GravityMultiplier2; MouseLook Xsensitivity3,Ysensitivity2,ClampVerticalRotation=true,MinimumX0,MaximumX60,Smooth=false,SmoothTime5,LockCursor=true;UseFovKick=true,UseHeadBob=false,StepInterval5,FootstepSounds Size0.
