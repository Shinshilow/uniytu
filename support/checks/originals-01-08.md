# Аудит оригинальных проектов: часы1–8

Это проверка исходного архива издателя, а не отчёт о завершённой сборке курса. Все14проектов сохранены в Unity2018.1.0b4; целевой редактор пользователя —2018.1.0f1. Архив/оригинальные файлы не изменены.

Проверены YAML сцены, материалы, importer metadata, GUID-ссылки и бинарные TerrainData. Компиляция в Unity, Play Mode и WindowsEXE-сборка **не запускались**.

|Час|Оригинальные проекты|Сохранённые сцены|
|---|---|---|
|1|Hour 1 Exercise; Hour 1 TIY|Hour 1 Exercise: Main.unity; Hour 1 TIY: пустой проект|
|2|Hour 2 Exercise; Hour 2 TIY|Hour 2 Exercise: Main.unity; Hour 2 TIY: Creating Objects.unity|
|3|Hour 3 Exercise; Hour 3 TIY|Hour 3 Exercise: Main.unity; Hour 3 TIY: Applying textures.unity, Assets from the asset store.unity, Importing a model.unity|
|4|Hour 4 TIY|Hour 4 TIY: Adding Trees and Grass.unity, Applying Heightmap.unity, Sculpting Terrain.unity, Texturing Terrain.unity|
|5|Hour 5 Exercise; Hour 5 TIY|Hour 5 Exercise: Main.unity; Hour 5 TIY: Cookie.unity, Directional Light.unity, Layers.unity, Multiple Cameras.unity, Picture in Picture.unity, Point Light.unity, Spot Light.unity|
|6|Amazing Racer|Amazing Racer: Main.unity|
|7|Hour 7 Exercise; Hour 7 TIY|Hour 7 Exercise: Main.unity; Hour 7 TIY: Main.unity|
|8|Hour 8 Exercise; Hour 8 TIY|Hour 8 Exercise: Main.unity; Hour 8 TIY: Main.unity|

## Главное для сборки

- Сохранить Assets, ProjectSettings, все .meta и бинарные TerrainData. Library первых часов не переносить. Все сцены добавить в BuildSettings явно.
- Час3: настоящие Torus/RobotKyle/кирпичные карты доступны. BrickWall MainTex tiling(3,1); итоговые четыре Standard материала tiling(3,3), smoothness0/.6 и две normal map. Это не процедурная имитация текстур.
- Час4: оригинал имеет только четыре TIY-сцены и **не содержит итогового Exercise или поставленного FPSController**. Нативный TerrainData содержит настоящие splats/alphamap, деревья и траву; TIFF/YAML material scanner не измеряет это. В AddingTreesAndGrass37нативных деревьев,GrassFrond billboard и341непустойdetailpatch. Размер исходного terrain50×60×50; для печатного практикума деревьев нужен отдельный100×100terrain.
- Час5: нет отдельной Halo и исходной полноэкранной TwoCameras/Depth сцены. В Exercise все четыре AudioListener выключены: включить ровно один. В исходных Split/PiP два компонента, но только один включён. Cookie импортирован настоящим Cookie и назначен Light.cookie.
- Час6: копировать оригинальные RAW, бинарный TerrainData, Water4Advanced и FPSController prefab. Main связан с исходными тремя скриптами и legacyOnGUI. Реальный TerrainData размер200×100×200; в печати длина100, ноPlayerZ125. Четыре реальных splat слоя tiling15×15; исходных деревьев/травы нет — добавить TerrainTreeInstances по книге. Отдельного творческого Exercise нет. Доступность маршрута/возврат после воды и границы требуют Play.
- Час7: EqualityAndOperations.cs найден в оригиналах. Сохранить отдельные HelloWorld/callback/operator примеры. Итоговые три скрипта издателя висят на трёх объектах, а книга просит на MainCamera; текст кратных3/5 у издателя английский.
- Час8: издатель сохранил только объединённую TIY-сцену. Нужны отдельные стадии методов/осей/клавиш/мыши/localCube/targetCube и письменный ответ. Итоговое перемещение исходного CubeControlScript localSpace; для фиксированных осейX/Z после yaw нужен Space.World.
- В часах4/6 одинаковые51ссылки на31отсутствующийGUID в основном среди неиспользуемых ThirdPersonCharacter ассетов. Во всех других исходных часах этихGUID нет. Ссылки настоящих terrain слоёв/деревьев разрешаются. Не заменять из-за этого реальные terrain текстуры.

## Соответствие каждому блоку книги

### Час1 — Введение в Unity

- `H01-P01` **source_covered**. Hour 1 TIY is an intentionally empty 3D project with ProjectSettings and Assets; the first creation exercise does not require a saved game scene.
- `H01-E` **source_covered**. Hour 1 Exercise/Assets/Scenes/Main.unity contains Camera, Directional Light and built-in Cube at origin. Исправление/проверка: Retain editor scene; navigation/Inspector actions remain manual verification.

### Час2 — Игровые объекты

- `H02-P01` **source_covered**. Hour 2 TIY/Assets/Scenes/Creating Objects.unity contains Empty GameObject, Cube, Point Light and defaults.
- `H02-LAB` **source_partial**. Original package preserves the baseline creating-objects scene and parent-child result; no independent local/global, pivot/center or transformed experiment scenes. Исправление/проверка: Retain baseline and add clearly named, separate editable Transform examples; do not change the specified final hierarchy.
- `H02-E` **source_covered**. Exercise Main: Cube at (0,2,-5), Sphere parented to Cube with localPosition (0,1,0); expected worldPosition (0,3,-5).

### Час3 — Модели, материалы и текстуры

- `H03-P01` **source_covered**. TIY Importing a model.unity and original Torus.fbx with ModelImporter globalScale=100; this is importer scale, not a substitute scene Transform.
- `H03-P02` **source_covered**. TIY Assets from the asset store.unity plus original Robot Kyle model, Robot_Color material and texture; GUID references resolve.
- `H03-P03` **source_covered**. TIY Applying textures.unity and BrickWall.mat: Standard, original Brick_Texture, MainTex scale (3,1), zero offset.
- `H03-E` **source_covered**. Four original Standard materials use MainTex scale (3,3). Smoothness 0/.6 and normal-map assignments match the specified four variants. Importer metadata marks Brick_Normal as NormalMap and Brick_Texture aniso=3.

### Час4 — Ландшафт и элементы окружающей среды

- `H04-P01` **source_covered**. Applying Heightmap.unity contains binary native TerrainData with 513x513 height samples, size (50,60,50); source terrain.raw is 16-bit big-endian and matches every native height sample after Unity half-range serialization.
- `H04-P02` **source_covered**. Sculpting Terrain.unity contains independent sculpted native TerrainData, size (50,60,50). Исправление/проверка: Editor brush actions and original flatten operation cannot be proven from final data alone.
- `H04-P03` **source_covered**. Texturing Terrain.unity plus original Terrain Assets; native splat prototypes and nonuniform alphamap exist.
- `H04-P04` **source_partial**. Adding Trees and Grass.unity has 37 native tree instances (29 Conifer_Desktop,8 Broadleaf_Desktop) and genuine source prefabs; TerrainData size remains50x60x50. Исправление/проверка: Preserve original TIY and add a separate100x100 terrain tree-practice scene to match printed setup.
- `H04-P05` **source_covered**. Adding Trees and Grass native TerrainData has GrassFrond01AlbedoAlpha billboard prototype and nonempty native detail patches, plus genuine terrain splats.
- `H04-P06` **source_missing**. All four original Hour4 scenes contain Camera/Light/Terrain, but no FPSController instance. Original Standard Assets Characters/FPS prefab is available. Исправление/проверка: Compose a separate scene with the original FPSController placed above sampled terrain height; remove/disable standalone camera/listener. Verify movement and collision in Unity.
- `H04-E` **source_missing**. Publisher archive has only Hour4 TIY; no Hour4 Exercise project/scene. Existing TIY has four genuine terrain layers and native trees/details but is not a distinct beach/ridge/plain exercise. Исправление/проверка: Create independent native TerrainData and beach/ridge/plain heightmap plus spatial Sand/GrassRocky/GrassHill/Cliff alphamap using original textures; populate native trees/details and appropriate FPS. Preserve all original asset GUIDs.

### Час5 — Источники света и камеры

- `H05-P01` **source_covered**. Point Light.unity preserves Plane(0,.5,0), two Cubes at x+-1.5,y1,z-5 and Point Light(0,1,-7).
- `H05-P02` **source_covered**. Spot Light.unity contains the spotlight at(0,1,-13).
- `H05-P03` **source_covered**. Directional Light.unity is independent; directional light at(50,50,50).
- `H05-P04` **source_missing**. No dedicated Halo scene in original seven TIY scenes. Исправление/проверка: Add separate Halo practice scene based on the book, preserving the baseline point-light scene.
- `H05-P05` **source_covered**. Cookie.unity uses SpotLight component on MainCamera and assigns genuine biohazard texture GUID118aa29c603cee044adf838b223e51f0; importer textureType4(Cookie), alphaUsage2(FromGrayScale), borderMipMap1.
- `H05-P06` **source_partial**. Original Multiple Cameras.unity is already split-screen, not a separately preserved full-viewport two-camera/depth example. Исправление/проверка: Add dedicated Two Cameras/depth scene, retain split-screen source.
- `H05-P07` **source_covered**. Multiple Cameras.unity camera rects(0,0,1,.5) and(0,.5,1,.5); two listener components but only one enabled.
- `H05-P08` **source_covered**. Picture in Picture.unity camera rects(0,0,1,1) and(.75,.75,.2,.2); two listener components but only one enabled.
- `H05-P09` **source_covered**. Layers.unity retains camera/light culling masks and separate objects at x+-2,y1,z-5.
- `H05-E` **source_partial**. Original Main scene has sphere at origin, four colored Point Lights at cardinal distance4 and four cameras at cardinal distance2 with distinct quarter rects. However all four AudioListeners are disabled. Default Ultra quality has pixelLightCount4. Исправление/проверка: Enable exactly one AudioListener; retain camera composition. Ensure chosen/default quality supports four pixel lights.

### Час6 — Игра первая: Великолепный гонщик

- `H06-WORLD` **source_partial**. Amazing Racer contains original binary TerrainData, TerrainHeightmap.raw and four painted native splat layers, but no tree prototypes/instances or detail layers; original Water4Advanced legacy prefab overrides position(100,29,100),scale(2,1,2). Исправление/проверка: Preserve native terrain binaries and texture/prefab GUIDs. Add native terrain trees on flat areas. Actual source size is(200,100,200), while print says length100 and PlayerZ125; document source-versus-print discrepancy and do not truncate a playable original route silently.
- `H06-ENV` **source_covered**. Original scene includes procedural skybox material and RenderSettings fog/environment.
- `H06-PLAYER` **source_covered**. Original FPSController prefab instance named Player at(165,32,125),yaw260; CharacterController slopeLimit30. No active standalone camera; Water4 reflection camera is disabled. Исправление/проверка: Movement, route accessibility and boundary behavior require Unity Play validation.
- `H06-OBJECTS` **source_covered**. SpawnPoint(165,32,125),yaw260; WaterHazardDetector(100,27,100),scale(20,1,20); FinishZone(26,32,37),PointLight range35,intensity3; GameManager object.
- `H06-SCRIPTS` **source_covered**. Original FinishZone.cs, GameManager.cs, PlayerRespawn.cs present; scene links manager, Player and SpawnPoint correctly; GUI uses original OnGUI.
- `H06-TEST` **requires_play**. No Unity Editor execution in this audit. Source assets and serialized connections inspected only. Исправление/проверка: Run in Unity2018.1.0f1: finish route, water respawn, restart, terrain collisions and edge/slope restrictions.
- `H06-E` **source_missing**. Only original Main scene exists; no independent creative Exercise scene. Исправление/проверка: Keep Main as baseline and create Exercise with a concrete documented change, e.g. a second alternate finish zone using original manager.

### Час7 — Скрипты, часть 1

- `07-P01` **source_covered**. Original HelloWorldScript.cs attached to Main Camera in TIY Main. Исправление/проверка: Preserve dedicated HelloWorld scene so other scripts do not obscure its single output.
- `07-P02` **source_covered**. Original ImportantFunctions.cs also attached to Main Camera in TIY Main; Start and Update print required English strings. Исправление/проверка: Preserve dedicated callbacks scene for independent verification.
- `07-A01` **source_covered**. Original EqualityAndOperations.cs is present alongside VariableScript, Conditionals and Loops; no replacement operator file needed.
- `07-E01` **source_partial**. Original AddEvenNumbers produces62250; AvoidMultiples covers1..100 but English Programming is Awesome!; Fibonacci produces first20terms0..4181. Scripts are attached to three separate Exercise GameObjects rather than MainCamera. Исправление/проверка: Attach the three independent scripts to Main Camera in final exercise; use requested translated phrase; remove redundant header logs if exactly100/20 entries are intended.

### Час8 — Скрипты, часть 2

- `08-P01` **source_missing**. No written TakeDamage-method analysis document in original project. Исправление/проверка: Provide concise answers: name TakeDamage; return int; one int damageAmount parameter; body declares health and returns health-damageAmount.
- `08-P02` **source_partial**. Original FireBallScript.cs has overloads and expected health95,75,20 but is not attached in the sole saved TIY scene. Исправление/проверка: Create Methods scene with original script on MainCamera.
- `08-P03` **source_covered**. Original PlayerInput on MainCamera reads Horizontal/Vertical and logs nonzero values; default InputManager retained.
- `08-P04` **source_partial**. Original PlayerInput combines key and axis/mouse examples in one Update; M GetKey and O GetKeyDown are present. Исправление/проверка: Preserve separate Key Input practice scene/script variant so each book stage can be opened independently.
- `08-P05` **source_partial**. Original PlayerInput combines MouseX/MouseY with axes/keys. Исправление/проверка: Preserve separate Mouse Input practice scene/script variant.
- `08-P06` **source_partial**. TIY Cube at(0,-1,0) has ComponentScript; publisher final code is an input-driven expanded example, not the printed fixed Translate(.05,0,0),Rotate(0,0,1),scale1.5 stage. Исправление/проверка: Create separate Local Cube scene implementing the printed stage; retain original code as reference without duplicate class compilation.
- `08-P07` **source_partial**. Original TargetComponentScript exists but is not attached. Start overwrites Find(Cube) with FindWithTag(TargetObject), and Update uses input-driven transforms. Исправление/проверка: Create separate Target Cube scene with only camera controlling Cube through Find(Cube), fixed local move/rotate and1.5scale.
- `08-E01` **source_partial**. Original CubeControlScript on Cube(0,0,-5) references camera, controls yaw/camera pitch and toggles original/double scale with M. Translation uses localSpace, so yaw alters movement axes. Исправление/проверка: Use Space.World for intended fixed X/Z exercise motion; check before/after mouse rotation and M twice in Unity.

## Доказательства и ограничения

Машиночитаемый результат: [originals-01-08.json](originals-01-08.json). Инвентарь: [originals-01-08-assets.json](originals-01-08-assets.json). Подробная проверка материалов/terrain: [originals-03-04-detail.json](originals-03-04-detail.json), [originals-03-04-detail.md](originals-03-04-detail.md). Terrain гонщика: [originals-06-terrain-detail.json](originals-06-terrain-detail.json). Поиск отсутствующихGUID во всём архиве: [originals-01-08-missing-guid-crosscheck.json](originals-01-08-missing-guid-crosscheck.json).

Статусы source_covered означают наличие исходных данных/связей, а не доказательство реального запуска. Изменение версии в ProjectVersion.txt само по себе не подтверждает совместимость; необходим Unity2018.1.0f1 import/compile/Play.
