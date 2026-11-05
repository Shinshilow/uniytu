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
