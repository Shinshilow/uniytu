# Original publisher projects: hours 9–16

Read-only audit of the original archive against `book-requirements.json`. The 14 original projects target **2018.1.0b4**; user target is **2018.1.0f1**. Original `.meta` files, sprite subasset IDs and prefab links are the source of truth. Unity Editor import, API compilation, Play and Windows builds are **UNRUN**. All 18 custom C# sources and the separate Hour10 extension parse without syntax errors; this is not an engine compilation result.

| Hour | Original scenes/assets | Missing or differing book work |
|---|---|---|
|9|TIY Rigidbody, Colliders, Triggers, Raycasting; Exercise Main with two real trigger planes and arrow sphere.|No physical-material assets/comparison scene. No intermediate no-body/unconstrained snapshots. Triggers Rigidbody on Cube instead of printed Sphere.|
|10|Actual closed Chaos Ball arena, SandAlbedo wall mapping10×, original water/FPS bumper, five yellow +four colored balls, matching goals, SuperBouncy.|No final modification; initial GameOver bool true; source gravity1 vs printed0 withY frozen. Separate authored timer/restart overlay supplied.|
|11|True Lamp prefabs, four linked Lamps instances, Complex Object and correct B/Space spawning Exercise.|Final snapshot cannot prove override/Apply/Break/Revert sequence. Original DirectionalLight is inactive, equivalent visually to removing it.|
|12|Original ranger/rangerTalking90-slice sheet, Hexagon, sorting/2Dpolygon-collision scenes; real animated RobotBoy/platform Exercise.|No dedicated Ranger/SpriteSheet snapshots. Unused RobotBoyFalling animation has two absent-sprite references.|
|13|Original Jungle32 +Grass26 slices,58Tile assets,two editable palettes, painted maps and RobotBoy follow/parallax Exercise.|Exercise Platform TilemapCollider2D has UsedByComposite0; set1 in copy. Same unused falling sprite defect.|
|14|Canvas/Anchors/Image/Button/Camera Modes, saved Released callback, textured clouds Menu+Game, Start→LoadGame persistent call.|Original Hour14Package contains clouds+manager loader, no fade/music/splash implementation. Earlier requirement prose overstated those supplied assets.|
|15|Original star background,4ship/19meteor animation frames, true Bullet/Meteor prefabs, matching horizontal movement/reload/spawning/score/gameover.|No external-player feedback. Possible simultaneous collision duplicate scoring needs runtime verification.|
|16|World collision force20/emission100, real Main.StartSize curve, original FireComplex and full particle package with18mapped materials.|Main lacks actual Smoke instance though prefab exists. Optional disabled fire AudioSources reference missing audio.|

## Hour 9 details

The saved collider final variant matches the written example: lower cube at(0,-1,-5),scale(4,.1,4),rotZ350,FreezeAll126,no gravity; upper cube uses SphereCollider and gravity Rigidbody. Raycasting destroys the ray hit every Update; adding a click requirement would change the printed exercise. Exercise Main has L Trigger/R Trigger at±1.5,y0,z-5 with correct(.1,2,2)scale and actual trigger colliders. Its MotionScript moves X/Y using Horizontal/Vertical, and logs identify each trigger. Names contain spaces, a cosmetic source difference.

Physical materials are not visual renderer materials. Both original H9 projects have zero `.physicMaterial` assets and all collider material refs0. A supplemental real comparison is required for the chapter activity. Sequential gravity/constraint transitions should be documented or preserved as snapshots.

## Hour 10 mapping and gameplay

Original Wall.mat uses real SandAlbedo GUID`bfd675cc0db1d4656b75dc6d6ba91142`, main tiling(10,1),Smoothness0. Blue/Green/Orange/Red/Chaos/BumperColor are intentionally plain colored materials. DynamicsManager DefaultMaterial resolves to SuperBouncy GUID`b9d3fc8be54911f4b9ffd5b525098342`: friction0,bounciness1,Average friction combine,Maximum bounce combine.

Water4Advanced uses FX/Water4 with real normal and shore maps. Nine stale saved texture properties refer to absent GUIDs; most are not declared by this shader, and its quality passes use bump/shore/reflection data. MainTex could affect the legacy fallback path. Preserve actual water mapping and inspect rendering in the target Editor; a global missing-GUID count alone is not evidence that the source scene has no mapping.

The original GoalScript checks matching tags, disables the correct goal light and destroys its colored ball. GameManager references all four goals and ANDs their solved states. It does not have the incorrect prior scaffold's falling-ball defeat objective. The source GameManager initializes gameOver true, which can briefly display victory before the first Update.

`course_additions/Hour10/Assets/Scripts/GameManager.cs` is an explicitly authored final-exercise overlay: timer, R restart and victory Restart button. It keeps the original public blue/green/red/orange GoalScript fields and must retain the publisher meta. On victory it disables FirstPersonController and unlocks the cursor so the button is usable; no Time.timeScale changes. Main must be enabled in Build Settings. Its source is syntax-checked, engine checks remain unrun.

## Prefabs, sprites and later chapters

Hour11 uses genuine linked Lamp assets: cube root scale(.5,2,.5) with Rigidbody, child Sphere localY.6 and compensating scale(2,.5,2), real white point Light. Exercise prefab root is(-1,0,-5); Spawn Point(1,1,-5); Plane(0,0,-4),rotX270. B and Space preserve the two Instantiate overloads.

Hour12 ranger is Single/PPU100; rangerTalking is Multiple/PPU100 with90 saved subSprites. Sorting layers are Background,Player,Default in original TagManager. Exercise retains original animated RobotBoy and level/angled PlatformWhiteSprite objects rather than colored primitive substitutes. RobotBoyFalling.anim has absent GUID`76d13a61287547d4fb40bfa27eca4e94`,fileID21300014 twice. Available RobotBoyJump07 has the same fileID under GUID`9e1a2edf6149977479db158e4fbf9671`; using it is an inferred repair, not recovered source art. The broken clip is not reached by conservative traversal from the actual Exercise scene/controller.

Hours13–16 exact GUIDs, callback targets, importer values and per-unit mapping are preserved in `originals-13-16-detail.json`. H13 Exercise collider fileID586025270 must enable UsedByComposite. H14 Button's persistent Text.set_text argument is Released; Start persists LoadGame and Menu precedes Game. H16 Smoke prefab GUID`921a3ff88856fe04ebc86b196fd8cc59` is available for the missing scene instance.

## Reference/version limits

Legacy GUID`f5f67c52d1564df4a8936ccd202a3bd8` is UnityEngine.UI.dll: Text/Image/Button/CanvasScaler/GraphicRaycaster/EventSystem/inputmodule class fileIDs. Preserve it; it is not absent user art. Old version4 materials encode maps using first/second rather than modern property keys; all18 particle materials have textures (16 assets,2 builtin), despite generic scanner zero-map reports. SpriteLit receives sprite textures per renderer.

Fonts`01cd679a1b9ee48bf9c546f6ce2cb97e`/`b51a3e520f9164da198dc59c8acfccd6` and optional fire audio`537536d187c5b2d409581d8728efa012` are absent from the archive; these occur in unused/optional Standard Assets prefabs. Do not remove all art based on a blanket unresolved-reference count.

Most original BuildSettings contain no scenes; delivered copies need explicit enabled scenes. Keep TIY and Exercise separate or deliberately resolve same-name class/GUID conflicts (notably H9 TriggerScript). Version metadata edits alone cannot establish compatibility. Actual Editor reopening, preserved palettes/UI events, RobotBoy motion/parallax, collision/scoring and particle visuals still require target Unity checks. External playtest feedback cannot be fabricated.
