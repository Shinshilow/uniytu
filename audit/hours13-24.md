# Аудит книги: часы13–24

Это карта требований, а не отметка о выполнении. Источник — предоставленный пользователем PDF. Номер страницы PDF на1 больше печатного. Оригинальные примеры указаны в книге: http://addons.eksmo.ru/it/Unity.zip. Для маппинга текстур и ригов необходимы исходные материалы и .meta; замена цветными примитивами не воспроизводит упражнения.

## Час 13. Тайлмапы в 2D-играх — печатные страницы248–264

Оригинальные ассеты: GrassPlatform_TileSet / GrassPlatform_Tileset; Jungle_Tileset; Standard Assets/2D/Prefabs/CharacterRobotBoy.prefab; CameraFollow.cs.

### 13.1 Добавление тайлмапа (стр.249–250)

- 2D-project, Scenes folder and saved scene. One Grid with Background and Platforms child Tilemaps; do not create a second Grid. Grid default Cell Size=(1,1,0), Tilemap+TilemapRenderer on each.

### 13.2 Создание палитры (стр.252–253)

- Persist real palette assets Jungle Tiles and Grass Tiles in Palettes, both accessible in Tile Palette window.

### 13.3 Настройка спрайтов и создание тайлов (стр.254–256)

- Sprites folder. GrassPlatform_Tileset SpriteMode=Multiple, PPU=64, Slice GridByCellSize64x64. Jungle_Tileset sliced128x128; corresponding PPU must match tile size per CellSize1 (text says repeat settings; inspect original importer/meta before overwriting). Preserve every source sprite and create real Tile assets in Tiles; put correct tiles into respective Grass Tiles/Jungle Tiles palettes.

### 13.4 Рисуем тайлами (стр.258–259)

- Paint Jungle background and Grass platforms into their own maps. Scene must contain recognizable textured terrain rather than solid square substitutes. Arrange tiles inside palettes for practical editing.

### 13.5 Тайлмапы и физика (стр.260–263)

- Import real CharacterRobotBoy above platform, scale=(1,1,1) if needed. TilemapCollider2D on Platforms, offset.y=-0.1. Add CompositeCollider2D with Rigidbody2D BodyType=Static, enable UsedByComposite on TilemapCollider2D. Consider Continuous collision for fast actor.

### 13.E Итоговое упражнение (стр.264)

- Finish both painted maps; optional Foreground plants/rocks; follow camera via CameraFollow.cs; move Background farther on z and use perspective camera to show real parallax; tint Background paler.

Проверки:

- After save/reopen all sprite, Tile, palette references survive.
- Robot lands on grass and can jump between platforms; collision offset correct; composite map static.
- Follow camera and actual parallax under motion, layer sorting correct.

Недостатки прежнего архива:

- Prior scene used single-color generated square sprites; no imported tile sheets, no real palettes.
- Called maps Ground/Decoration instead of Platforms/Foreground; omitted original RobotBoy, composite collider and offset.

## Час 14. Пользовательские интерфейсы — печатные страницы265–286

Оригинальные ассеты: BackgroundSpace.png; Hour14Package.unitypackage; clouds.jpg; LevelManager prefab including original dependencies.

### 14.1 Добавление холста (стр.267)

- Canvas plus EventSystem; preserve proper RectTransform/CanvasScaler/GraphicRaycaster.

### 14.2 Использование Rect Transform (стр.269–270)

- Image on Canvas; demonstrate unified anchor vs split/stretch anchors; different Game aspect/resolution affects layout correctly. Separate demonstration scenes or clearly named examples preserve both states.

### 14.3 Использование изображений (стр.273–274)

- Import BackgroundSpace.png as Sprite2D/UI and use as actual UI background SourceImage, properly anchored/stretched.

### 14.4 Использование кнопок (стр.277–279)

- UI Button ColorTransition, HighlightedColor=red, PressedColor=green. Serialized/persistent OnClick modifies its child Text.text to Released. Verify it remains wired after scene reopen.

### 14.5 Изучение режимов рендеринга (стр.283)

- 3D demonstration Canvas modes ScreenSpaceOverlay, ScreenSpaceCamera with MainCamera assigned, and WorldSpace. Make the modes inspectable; moving camera and toggling Perspective/Orthographic demonstrates differences.

### 14.E Система меню (стр.284–286)

- 2D scene UI Panel; import Hour14Package.unitypackage. clouds.jpg must be Sprite and assigned to Panel Source Image. Title/subtitle; button object name Start, child label Start Game. Save Menu plus separate empty placeholder game scene; ScenesInBuild has Menu first. Original LevelManager prefab in scene; Start persistent OnClick calls LoadGame(). Original splash/fade/background music assets and behaviour from package should be kept, not replaced with a flat blue panel.

Проверки:

- Button hover/pressed colors and Released label actually work.
- Inspect anchor behavior across two aspect ratios.
- Start Game transitions from textured Menu to empty placeholder scene; no missing event target after reopen.
- Original LevelManager fades/music work and survive scene load as authored.

Недостатки прежнего архива:

- Old project only synthesized menu, blue rectangle, generated tone and race as Game; missing other practicum scenes and source assets.
- Assigning runtime callbacks is not equivalent to saved inspector OnClick task.

## Час 15. Игра третья: Капитан Бластер — печатные страницы287–307

Оригинальные ассеты: Star_Sky.png; spaceship.png; meteor.png (19 frames); bullet.png; Original completed project/assets in hour15 examples.

### 15.1 Подготовка мира и фона (стр.288–291)

- 2D project Captain Blaster, Scenes/Main.unity, Game aspect5:4, orthographic camera Size6. Background folder; Star_Sky Sprite PPU50, two instances positions(0,0,0),(0,20,0). ScrollBackground speed=-2, lowerYValue=-20, upperYValue=40; translate downward and wrap.

### 15.2 Корабль (стр.291–293)

- Spaceship folder, spaceship.png SpriteModeMultiple; grid slice116x140. All frames produce Ship.anim and AnimatorController. Ship pos(0,-5,0), scale(1,-1,1), SpriteRenderer.OrderInLayer1. PolygonCollider2D IsTrigger=true. Visible animated engines required.

### 15.3 Метеор (стр.293–294)

- Meteor folder, meteor.png sliced Automatic into19frames, Meteor animation/controller. CircleCollider2D non-trigger, Rigidbody2D GravityScale0, OrderInLayer1. Saved Meteor.prefab and no initial orphan instance in scene.

### 15.4 Снаряд и дробилки (стр.295–296)

- Bullet folder, bullet.png PPU400, tint green, OrderInLayer1, CircleCollider2D+Rigidbody2D GravityScale0; real Bullet.prefab. Two empty Shredder objects at(0,-10,0),(0,10,0), BoxCollider2D IsTrigger=true size(16,1), DestroyOnTrigger.cs deletes passing bullets/meteors.

### 15.5 UI и GameManager (стр.296–299)

- Canvas/Text Score upper-left anchor, anchoredPosition(100,-30,0), initial0, white. Game Over center pos0, width200,height100, red centered BestFit, Text.enabled=false. GameManager.scoreText/gameOverText connected. AddScore increments one and writes label; PlayerDied enables GameOver text and freezes Time.timeScale0.

### 15.6 Скрипты метеора и спауна (стр.299–301)

- MeteorMover sets Rigidbody2D velocity(0,-2). Meteor Spawn empty pos(0,8,0), MeteorSpawn.meteorPrefab connected, minSpawnDelay1,max3,spawnXLimit6; Invoke repeatedly spawns at random x[-6,6].

### 15.7 ShipControl и Bullet (стр.302–305)

- ShipControl references GameManager/BulletPrefab; speed10,xLimit7,reloadTime0.5. Base movement ONLY Horizontal; clamp x; press Jump/Space spawns at ship+(0,1.2,0) at most2shots/s. Bullet speed10 upward via Rigidbody2D; OnCollisionEnter2D destroys Meteor and self and calls AddScore exactly once. Nontrigger meteor/bullet vs trigger ship deliberate.

### 15.E Внешний плейтест и улучшения (стр.305–307)

- Let real diverse users play and record actual feedback; then choose improvements. Suggested alternatives: bullets/shot trajectories, double shot, increasing spawn, meteor variants, shield, movement in two axes. Keep base book scene separately if modifying rules.

Проверки:

- Background uses original art and scrolls continuously; ship/meteor animation visible.
- Ship stays within screen; never exceeds2shots/s in base scene.
- One bullet hit gives exactly one point; meteor-ship collision displays GameOver and stops.
- Shredders remove offscreen objects; no runaway count.
- Real feedback recorded, not fabricated.

Недостатки прежнего архива:

- Old implementation used square colors, independent tiny stars, omitted all 19frame animation and collider shape.
- Old fire .17s (~6shots/s) and vertical movement differ from book baseline.
- No authored shredder/score GameOver states, no real feedback.

Внешние/визуальные требования:

- External players needed for final exercise.

## Час 16. Системы частиц — печатные страницы308–327

Оригинальные ассеты: Standard Assets/ParticleSystems package; Standard Assets/ParticleSystems/Prefabs/FireComplex.prefab; Smoke.prefab; Explosion and fireworks prefabs and textures/materials.

### 16.1 Создание системы (стр.309)

- Default ParticleSystem scene; editable rotation/scale and inspectable emission.

### 16.2 Настройка столкновения (стр.320–321)

- Sphere at(0,5,0),scale(3,3,3),Rigidbody. ParticleSystem pos0, EmissionRateOverTime100. Collision enabled TypeWorld, ColliderForce20; particles collide and can support sphere. Book intro mentions Plane too; preserve explicit World setup and an inspectable Plane variant.

### 16.3 Curves Editor (стр.325–326)

- Separate ParticleSystem at0; Main.StartSize mode Curve range2, normalized keys start0/middle peak/end0 over default5second duration. This is start size over emitter cycle, not SizeOverLifetime substitution.

### 16.E Стандартные эффекты (стр.327)

- Import full ParticleSystems package. Use actual FireComplex and Smoke prefabs; inspect explosion/firework too. Keep referenced texture sheets/materials/shaders. Additional own effects allowed.

Проверки:

- No pink/missing material particles after save/reload.
- World collision force interacts with Rigidbody sphere.
- StartSize curve visibly modulates emitted particles over 5seconds.
- Original FireComplex,Smoke present and functional.

Недостатки прежнего архива:

- Old project has four generic emitters with no original standard particle textures/prefabs and omits physics and start-size curve practicums.

## Час 17. Анимация — печатные страницы329–344

Оригинальные ассеты: RobotBoyRunSprite.png from 2D Standard Assets or hour17 examples.

### 17.1 Нарезка спрайтов и анимация (стр.332–334)

- New2D project/scene, import RobotBoyRunSprite.png, Multiple, grid slice64x64,Offset0,Padding0,PivotCenter (visually verified fig17.3). Build actual sprite animation and AnimatorController, RobotRun sample12fps. SpriteRenderer.sprite changes through full frames.

### 17.2 Пусть объект вращается (стр.337–338)

- New3D scene Cube at0, ObjectSpinAnim.anim, Rotation.y0->360 between0:00 and1:00(60fps). Save actual clip/controller.

### 17.3 Режим записи цвета (стр.339–340)

- CubeColor material assigned; animate RGBA colors in spinning animation; initial red(1,0,0,1), other colors allowed, last at1sec matches first for loop.

### 17.4 Curves Editor (стр.342)

- Rotation.y curve edited to straight smooth continuous spin; inspect actual saved tangents rather than only transform.Rotate script.

### 17.E Песочница (стр.343–344)

- Additional saved clips demonstrate wide arc flight, Renderer enabled/disabled blinking, local scale and material property changes.

Проверки:

- Actual sprite run clip cycles original frames, no static rectangle.
- Cube rotates full turn seamlessly and color loops; saved animation clips editable in Animation window.
- Renderer blinking/arc/scale clips visibly work after scene reload.

Недостатки прежнего архива:

- Old project only arc/blink/scale cube, omits RobotBoy sprite animation and rotating ObjectSpinAnim/CubeColor practicum.

## Час 18. Аниматоры и гуманоидный mapping — печатные страницы345–368

Оригинальные ассеты: Standard Assets/Characters/ThirdPersonCharacter/Models/Ethan.fbx plus EthanBody/EthanGlasses textures/materials; Animations/Idles.fbx; Animations/WalkForward.fbx; Animations/WalkForwardTurns.fbx; Checker.tga; Standard Assets/Characters/ThirdPersonCharacter/Prefabs/ThirdPersonController.prefab (investigation exercise).

### 18.1 Скелет Ethan (стр.347–351)

- Import entire Characters package, actual textured Ethan model. Rig.AnimationTypeHumanoid; valid Avatar mapping. Configure window Mapping binds body/head/arms/legs correctly. This cannot be fulfilled by replacing humanoid with capsule.

### 18.2 Подготовка клипов (стр.351–356)

- Import original Animations. All FBX RigHumanoid. Idles: Idle frame128–1100 (visually verified fig18.6), LoopTime and LoopPose true, all RootTransform BakeIntoPose true. WalkForward clip renamed WalkForwardStraight, first215.2,last244.9, loop time/pose true, bake rotation+Y, preserve XZ movement; RotationOffset3.53 makes AverageVelocity.x0 (visually verified fig18.9). Turns: WalkForwardTurnRight frames122–152,loopTime/loopPose true,rotation BakeIntoPosefalse/BodyOrientation/offset0,YBakeIntoPosetrue/Feet,XZBakeIntoPosefalse/CenterOfMass (visually verified fig18.10); duplicate WalkForwardTurnLeft with identical settings+Mirror=true.

### 18.3 Настройка сцены (стр.357–359)

- Ethan pos(0,0,-5), MainCamera child of Ethan local(0,1.5,-1.5),rot(20,0,0). AnimatorController Animators/PlayerAnimator assigned with Avatar. Plane pos(0,0,-5),scale(10,1,10). Checker material uses original Checker.tga Albedo; actual texture mapping retained.

### 18.4 Контроллер (стр.359–364)

- Idle default state from Idles.fbx, FootIK=true. Float parameters Speed and Direction. Walking state is1DBlendTree by Direction, thresholds -1/0/1 map WalkForwardTurnLeft/Straight/Right. Idle->Walking condition SpeedGreater0.1; Walking->Idle SpeedLess0.1; disable HasExitTime.

### 18.5 AnimationControl (стр.365–366)

- AnimationControl.cs attached to Ethan. Get Animator then SetFloat Speed=Input.GetAxis(Vertical), Direction=Input.GetAxis(Horizontal). WASD/arrows drive walk/turn and root motion; retain correct root motion behavior.

### 18.E Изучение Mecanim (стр.367–368)

- Read Mecanim docs and inspect actual ThirdPersonController.prefab with Grounded/Airborne/Crouching trees. This is additional study of Standard Assets, not replacement of the authored Idle/Walking controller.

Проверки:

- Valid humanoid Avatar in Configure Mapping; textured skinned humanoid, no missing bones/materials.
- Clip trimming and mirror/root-motion settings persisted; feet not skating in Idle (FootIK).
- Speed/Direction drive Idle/Walking/turn blending; camera follows as child.
- Plane Checker Albedo mapped; actual ThirdPersonController investigation separately accessible.

Недостатки прежнего архива:

- Old capsule and fake vertical-bob clips entirely omit humanoid mapping, FBX clip preparation, retargeting, skins, Checker map.
- Old controller Speed+Crouch+Jump/Grounded trees incorrectly substitutes optional prefab inspection for main exercise.

Внешние/визуальные требования:

- Figures18.6,18.9,18.10,18.11 visually inspected; frame ranges/root settings recorded.

## Час 19. Timeline — печатные страницы369–383

Оригинальные ассеты: Hour19/Animations/{Red,Orange,Yellow,Green,Blue,Indigo,Violet} clips; Hour19/Audio/Beep High clip.

### 19.1 Ассет таймлайна (стр.372)

- Timelines folder, real TimelineAsset and empty Director GameObject with PlayableDirector pointing to asset.

### 19.2 Треки (стр.375)

- Cube at0. AnimationTrack bound to Cube Animator; AudioTrack present (can be unbound).

### 19.3 Последовательности (стр.376–377)

- Import actual Animations and Audio folders. Seven color clips ordered Red,Orange,Yellow,Green,Blue,Indigo,Violet; one BeepHigh per color, audio starts aligned with color changes. Persistent track bindings, timeline audio plays in PlayMode.

### 19.4 Смешивание (стр.379–380)

- Overlap adjacent color clips by50%. Orange begins frame30 ends90; continue continuous mix through rainbow; beeps move to new start of corresponding color clips. Preserve unblended sequence as separate timeline/scene if showing whole lesson.

### 19.5 InputControl (стр.381)

- Director.PlayOnAwake=false; InputControl reads Jump/Space; if director.state Paused calls Play otherwise Stop. No auto-start when entering Play.

### 19.E Опыты (стр.383)

- Additional dynamic UI animation, guard patrol, camera animation series, activation-light strobe as suggested extension. These do not replace rainbow/audio main timeline.

Проверки:

- Seven colors and synchronized beeps work, actual overlap creates interpolation.
- Space starts/stops, no auto-start.
- Every timeline binding restored after reload; audio output audible.
- At least selected optional extension is explicit and visible.

Недостатки прежнего архива:

- Old scene only guard/camera/strobe. Missing whole main rainbow+audio sequence, overlap task and Space control; PlayOnAwake wrong.

## Час 20. Игра четвёртая: Бег с препятствиями — печатные страницы384–403

Оригинальные ассеты: Hour20/Materials (Ground,Wall,Dark Sky); Hour20/Textures (all referenced Albedo/normal maps); Hour20/Models/Player.fbx and textured Player material; Hour20/Animations/Runs.fbx; PhasedOut material and Hologram shader from hour20 Models; Source project Adventure/Unity (assetstore76216); HologramShader github.com/andydbc/HologramShader.

### 20.1 Сцена и текстурированный коридор (стр.385–388)

- Gauntlet Runner3D project, Scene/Main.unity. Camera pos(0,3,-10.7),rot(33,0,0). Import original Materials/Textures with.meta preserving GUID texture bindings. Dark Sky Skybox/Procedural applied. Ground cube pos(0,0,15.5),rot(0,180,0),scale(10,.5,50). Walls quads at(-5.25,1.2,15.5),(5.25,1.2,15.5),rot(0,-90,0),scale(50,2,1); inspect visual facing. Apply original metallic tiled Ground material and glowing Wall material.

### 20.2 UV-прокрутка (стр.388)

- TextureScroller.cs on Ground speed.5, increment offset by deltaTime*speed, wrap >1 subtract1; renderer.material.mainTextureOffset=(0,offset). Mesh stays stationary. This explicit texture mapping/tiling exercise is mandatory.

### 20.3 Powerup (стр.389–390)

- Sphere pos(0,1.5,42),scale(.5,.5,.5),Rigidbody UseGravityfalse. Powerup yellow material Metallic0 Smoothness1; yellow PointLight. ParticleSystem lifetime.5,speed-5,size.3,light-yellow; emission30,shapeSphere radius1,StretchedBillboard LengthScale5,Default-Particle material. Save Prefabs/Powerup.prefab and remove scene instance.

### 20.4 Obstacle и TriggerZone (стр.390–391)

- Obstacle cube pos(0,.4,42),scale(1,.2,1),RigidbodyNoGravity,red Light; red material with darkred Emission. Save Prefabs/Obstacle.prefab, remove scene instance. TriggerZone cube pos(0,1,-20),scale(10,1,1),BoxCollider IsTriggertrue; TriggerZone.cs destroys passing objects.

### 20.5 Игрок и Run (стр.391–393)

- Import actual Models/Animations. Player.fbx RigHumanoid; scene pos(0,.25,-8.5),tagPlayer. CapsuleCollider IsTriggertrue centerY.7 radius.3 height1.5. Runs.fbx Humanoid, Run frames302–319,LoopTime/LoopPose true,RootRotation BakeIntoPosetrue/BodyOrientation/Offset-4.81,YBakeIntoPosetrue/Original,XZBakeIntoPosefalse/CenterOfMass,AverageVelocity.x0 (visually verified fig20.6). PlayerAnimator.Run speed.7,FootIKtrue,Animator.ApplyRootMotionfalse.

### 20.6 GameManager и Player (стр.394–398)

- GameManager.ground references TextureScroller; gameTime10; elapsed/time countdown; AdjustTime(amount), amount<0 sets Time.timeScale.5 then returns1 after1scaledsec via Invoke, CancelInvoke handles repeated hits. End only when time<=0, not on collision. Player references normalMatPlayer/phasedMatPhasedOut and manager; bounds3,strafeSpeed4,phaseCooldown2; Horizontal movement clamps[-3,3]; Jump phases via material swap and disabling collider, reenable after2sec. Cannot collect bonuses while phased.

### 20.7 Collidable и Spawner (стр.398–401)

- Collidable.moveSpeed20; powerup.timeAmount+1.5,obstacle.timeAmount-.5. OnTriggerEnter taggedPlayer adjusts manager and deletes self. Spawner on GameManager.spawnCycle.5; alternate bonus/obstacle, retain prefab positions atz42, randomx[-3,3], assign manager reference on instance. Wire all references.

### 20.E Улучшения (стр.402–403)

- Optional more bonus/obstacle types, modern UGUI instead of legacy OnGUI, tune spawn/time/slowdown, richer particle/textures, distance and increasing speed. Keep base rules scene separate.

Проверки:

- Floor geometry stationary, original tiling texture visibly scrolls via UV offset; textured illuminated walls and DarkSky.
- Actual rigged skinned Player runs in place at correct speed; no side drift.
- Space swaps to visible Hologram and disables collider2sec; no bonuses taken while phased.
- Powerup adds1.5sec; obstacle removes.5sec and halves world speed then restores; collision does not directly end game.
- Spawn alternates every.5sec; old objects destroyed at TriggerZone; game starts10sec.

Недостатки прежнего архива:

- Old colored floor and capsule omit all UV mapping/TextureScroller, original textures/walls/sky and custom Hologram shader.
- Old collision immediately loses and green bonus+5sec/time60 differs from mandatory main rules; no phase or slowdown.

Внешние/визуальные требования:

- Real external feedback encouraged; do not fabricate.
- Preserve original .meta for texture-material-model bindings.

## Час 21. Работа со звуком — печатные страницы404–418

Оригинальные ассеты: Sounds/looper.ogg; Sounds/quick_laser.ogg; Sounds/xxplosion.ogg.

### 21.1 Проверка звука (стр.408)

- Import real Sounds folder; Cube at0 AudioSource.cliplooper.ogg,PlayOnAwaketrue, loop off. It plays original roughly20sec track and stops.

### 21.2 Звук на Scene и3D (стр.409–410)

- Scene audio switch enables listening while navigating. Demonstrate defaultSpatialBlend0 unchanged by distance thenSpatialBlend1 with attenuation by distance; keep separate inspectable variants.

### 21.3 Запуск и остановка (стр.412)

- Cube AudioSource.PlayOnAwakefalse,Looptrue, AudioScript.cs toggles Stop/Play on Jump/Space; each restart from beginning.

### 21.4 Аудиомикшер (стр.413–415)

- Create actual AudioMixer asset, Master and chosen groups; route AudioSource.Output to group; mixer controls shared volume/effects. Material demonstration irrelevant here; no need invented textures.

### 21.E Звуковая карта (стр.417–418)

- New scene Cube pos(0,0,-10),AudioSource.PlayOnAwakefalse; AudioScript public clip1/2/3 assigned actual looper/quick_laser/xxplosion; Start choosesclip1; 1/2/3 Stop,swap,Play; Space toggles PlayStop; L togglesloop.

Проверки:

- Original clips audible, switching sounds really changes content.
- Play/Stop starts at beginning; Loop toggle works.
- 3D variant attenuates by camera distance; mixer routing survives scene reload.

Недостатки прежнего архива:

- Old synthetic sine/noise tones are not original clips and omit spatial/mixer practicums.

## Час 22. Разработка для мобильных устройств — печатные страницы419–430

Оригинальные ассеты: Unity Remote5 app on real device; SDK and Unity build module if building to Android/iOS.

### 22.1 Настройка Remote (стр.422–423)

- Scene with central UI Button, PressedColorred. Device viaUSB, openUnityRemote; EditorSettings UnityRemote.Device appropriate. Confirm desktop click then real-device tap changes button color.

### 22.2 Акселерометр (стр.425)

- Cube at0; AccelerometerScript Update x=Input.acceleration.x*deltaTime,z=-Input.acceleration.z*deltaTime; Translate(x,0,z). Device parallel toground; demonstrate actual tilt movement.

### 22.3 Отслеживание касаний (стр.427)

- TouchScript on MainCamera; show per-touch fingerId,phase,tapCount,positionX/Y. OnGUI labels laid out130px apart by ID in book; touch data must remain visible for real fingers.

### 22.E Независимое управление3кубами (стр.429–430)

- Cube1(-3,1,-5),Cube2(0,1,-5),Cube3(3,1,-5). InputScript per cube maps fingers and deltaPosition*.05 into X/Y. Book code assumes IDs0/1/2; robust equivalent may retain stable arbitrary finger mapping if explicitly documented. Lift/readd fingers does not move the other cubes.

Проверки:

- Actual Remote device interaction button+accelerometer+multitouch.
- Three independent cube control and persistent finger identity across lifting middle finger.
- Mouse fallback must be labeled fallback, cannot constitute device verification.

Недостатки прежнего архива:

- Old only cube demo with mouse fallback; omitted Remote button, accelerometer and touch-information scenes.

Внешние/визуальные требования:

- Real compatible phone/USB/Remote required; external blocker if unavailable.

## Час 23. Доработка и развертка — печатные страницы431–445

Оригинальные ассеты: Any earlier playable project for final deployment; No completed final build project supplied by book for this exercise.

### 23.1 Сцены в сборке (стр.433)

- Scenes/Scene1.unity index0,Scene2.unity index1 inBuildSettings.

### 23.2 Переключение и сохранение объекта (стр.435–436)

- Scene2 Sphere(0,2,0),Scene1 Cube(0,0,0). DontDestroy.cs attachedCube,Start DontDestroyOnLoad(this); OnMouseDown loadsScene1index=1 (Scene2). Saved cube remains and sphere appears. For correct dynamic-scene lighting disableAutoGenerate and GenerateLighting; preserve generated lighting data.

### 23.3 PlayerPrefs (стр.437–438)

- Scene1 MainCamera SaveData.cs with playerName,TextField rect(5,120,100,30), Save buttonrect(5,180,50,50) usesPlayerPrefs.SetString(name,playerName). Scene2 camera LoadData StartGetString(name), GUI.Labelrect(5,220,50,30). Enter/save name,clickcube to change scene, name displays; persists across relaunch.

### 23.4 PlayerSettings/BuildSettings (стр.438–443)

- Company/ProductName, squareicon and appropriate display/platform settings; PCMacLinuxStandalone, correct scene order. Use Input axes remappable via legacy standalone Input config, not all hard-coded keys.

### 23.E Сборка и запуск (стр.444–445)

- Build actual executable for target machine and run independently of Editor, experiment with player/game settings. Distribute full datafolder and required DLL, not nakedEXE.

Проверки:

- ClickCube changes Scene1->Scene2 and retains same Cube; no duplicate camera/audio errors.
- Saved name loads inScene2 and after process restart.
- Scene2 lighting correct after dynamic load.
- Actual Windows build succeeds and launches with scenes+input.

Недостатки прежнего архива:

- Old chapter23 simply cloned racer; omitted every mandatory scene/persistence/PlayerPrefs practicum.
- No EXE created or launched.

Внешние/визуальные требования:

- Native executable must be built and launched for readiness; Linux local syntax checks insufficient.

## Час 24. Подведение итогов — печатные страницы446–451

Оригинальные ассеты: не требуются.

### 24.E Письменный разбор (стр.451)

- Deliver actual written postmortem about ONE game made earlier: what worked, what did not, encountered pitfalls and lessons. Reflect real development and test evidence; no fictional user interviews/performance results. Suggested printout placed inbook. No unique3Dscene or EXE prescribed for this hour.

Проверки:

- Written document exists and refers to actual implementation and results; clearly separates unresolved issues and observations.

Недостатки прежнего архива:

- Old menu/game copy irrelevant to actual writing exercise; blank placeholders alone do not constitute completed report.

Внешние/визуальные требования:

- Personal observations require user input or transparent agent-authored development facts.
