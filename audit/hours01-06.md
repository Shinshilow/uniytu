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
