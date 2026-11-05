# Audit of the previous Unity24 implementation

Scope: static inspection of `Unity24/SharedSource` and `tools/package_lessons.py` for the user's Unity **2018.1.0f1** and full book workflow. No Unity Editor run or semantic API compilation was available. This report does not claim any runtime check passed.

## Main conclusion

The current archive is a generic procedural lesson launcher copied into 24 folders. It implements simplified versions of selected final exercises, not the complete practical work in each chapter. Fixing compiler errors or adding arbitrary textures cannot make it match the book. Reconstruct real chapter projects using the publisher's original files, `.meta` GUIDs, scenes, model importers, materials and animator data; complete missing practice scenes against the book's checklist.

The companion download is explicitly named in the book: `http://addons.eksmo.ru/it/Unity.zip` (introduction). The lack of a PDF attachment containing those files did not justify substituting every asset before checking this link.

## Confirmed texture and mapping defects

| Source | Finding | Required correction |
|---|---|---|
| `Runtime/Lesson.cs:34` | `Shape()` creates a Standard material containing **only a color**. Most 3D scenes therefore have no albedo/normal maps assigned. Built-in primitive UVs exist, but no meaningful texture mapping is demonstrated. | Use the actual model/mesh UVs and original material/texture assets specified for each scene. Do not invent mapping requirements in chapters 1–2 where none are assigned. |
| `Runtime/Lesson.cs:141` | Chapter 3 uses generated 64×64 blocks instead of Brick_Texture.png / Brick_Normal.png. No actual `Textures` import settings are configured. | Import original maps, set albedo Aniso Level 3, normal texture importer type NormalMap and reimport; connect the maps to Diffuse/Specular/Bumped Diffuse/Bumped Specular materials. Check material references after reopening. |
| `Runtime/Lesson.cs:151` | `Brick(true)` keeps R/G at .5 and varies only B for mortar. It does not encode brick edge slopes in tangent X/Y. Under RGB normal unpack the normals point straight out everywhere; under packed/DXT5nm expectations the data is also not imported/encoded correctly. Merely assigning it to `_BumpMap` does not produce the requested normal mapping. | Preserve the original normal image plus its NormalMap importer `.meta`; verify visible relief under grazing light and identical geometry/UVs across four comparison materials. |
| `Runtime/Lesson.cs:156` | Terrain uses three 8×8 near-solid noise colors. Terrain splat weights are present, but original SandAlbedo, GrassRockyAlbedo, GrassHillAlbedo etc. are absent. No normal maps or original Terrain Assets material setup. | Restore original texture layers, tiling and terrain data from examples, then complete the named beach/ridge/plain and vegetation exercises. |
| `Runtime/Lesson.cs:170` | Trees are separate primitive cylinders/spheres; no Terrain `treePrototypes`, `TreeInstance`, `detailPrototypes` or grass are configured. | Use the actual terrain painting systems demonstrated by the chapter. |
| `Runtime/Lesson.cs:218` | Every sprite is one solid 16×16 color. RobotBoy, Ranger, Jungle tiles, clouds, space background, ship and meteor art are not imported. | Restore original image files, sprite slicing, pivots, pixels-per-unit, draw order and sprite animation clips. |
| `Runtime/Lesson.cs:246` | Menu panel is a solid color and has no source sprite despite being named Clouds panel. | Assign clouds.jpg through its Sprite importer and preserve original LevelManager/fade setup. |
| `Runtime/Lesson.cs:267` | Named FireComplex/Smoke/Explosion/Fireworks are newly configured generic cone emitters with an untextured particle material. They are not the Standard Assets prefabs. | Use the supplied particle prefab/material/texture network and inspect missing dependencies. |
| `Runtime/Lesson.cs:274` | Ethan is replaced by a capsule with vertical translation clips. No Humanoid Avatar, model rig, original skin/UV/material, root motion or original character controller exists. | Restore model, Avatar mapping, original imported animations and material/Checker.tga exercise. Capsule motion is not equivalent to Mecanim retargeting. |

## Structural and behavioral problems

1. **Chapter isolation is missing.** `package_lessons.py` copies every runtime script and Timeline/Animator editor code into every project. An error for any chapter prevents even Hour01 entering Play. Each project should contain its own required scripts/assets and directly openable chapter scenes.
2. **Only bootstrap scenes are distributed.** The `.unity` files contain a Lesson component; actual content depends on `CourseSetup.AutoPrepare()` successfully compiling and running. Saved normal maps, materials, terrain, prefab, controllers and timelines are not in the archive until generated on the user's machine. Deliver serialized completed scenes/assets, not a promise to generate them.
3. **Automatic regeneration can destroy work.** `Prepare()` unconditionally creates new scenes and saves over fixed paths. Re-running the menu overwrites scene edits, creates more assets via GenerateUniqueAssetPath and uses an unversioned marker. There is no dirty-scene confirmation. Avoid this mechanism for the revised completed projects.
4. **Marker is not verification.** `prepared.txt` confirms commands reached the end, not model/texture completeness or runtime correctness; it also prevents updated content rebuilding when the marker is stale.
5. **Runtime/Editor mixed persistence is fragile.** The editor calls runtime scene-creation methods and attempts to discover dependencies afterwards. `CreateScene()` never reloads the saved scene to confirm material/texture/sprite/tile/prefab references survive. Verify exact GUID/fileID dependency graphs and reopen scenes in the actual editor.
6. **Chaos initial movement is set in Edit Mode.** `Body(ball,true).velocity=...` occurs during editor generation. Velocity is physics state rather than a reliable scene-serialized initial condition. Set initial velocities in an actual Start/OnEnable script (or original ChaosBall script), and verify initial motion after scene reload.
7. **Games are materially different.** The race is a colored top-down platform course rather than the supplied terrain/first-person project; the runner has a capsule and random colored blocks rather than the original level/objects/materials; the shooter uses colored rectangles rather than the sprites/prefabs/background workflow. Their existence does not fulfill the chapter procedures.
8. **UI connections are hidden from Inspector.** Button callbacks are reattached by matching string names at runtime. Saved OnClick entries are empty; the chapter's explicit LevelManager event wiring is not demonstrated. Use persistent serialized button events as specified.
9. **Audio assets are substituted.** Three synthesized tones/noise clips replace the original OGG clips and no original Mixer workflow is present. Preserve clips and their import settings, AudioMixer groups/effects and the chapter's separate practice scenes.
10. **Animator demonstration is insufficient.** Three trees contain generic vertical translations. The jump clip loops; the Airborne tree blends the same jump with itself; neither reproduces a rigged character/retargeted motions. This is not a meaningful completion of chapter 18.
11. **No Animator/Timeline validation.** Bindings are created with APIs consistent with the general 2018.1 era, but the exact 2018.1.0f1 assemblies were never used to compile them. Track offsets/default clip duration/state transitions/material animation need actual scene runs.
12. **Full book work is missing by design.** Documentation explicitly says only final exercises are represented. Chapter 24 is a placeholder report; chapter 15's external playtest and chapter 22's phone test have never happened. Keep those truthful instead of marking them done.

## Compatibility observations

- The now-added `using UnityEngine.Tilemaps;` resolves the **specific reported** TileBase namespace error. Syntax parsing could not have caught it because it does not resolve types.
- `SplatPrototype`, old `PrefabUtility.CreatePrefab`, built-in UI and Tilemap are appropriate APIs to investigate for 2018.1; do not replace them blindly with TerrainLayer or SaveAsPrefabAsset from newer Unity versions.
- BuildReport-era build calls, Timeline track APIs and AnimationUtility bindings still require semantic compilation against **the actual 2018.1.0f1** editor libraries. No new incompatible API was definitively demonstrated in this audit.
- Exact imported project metadata from the publisher is preferable to hand-written incomplete settings, if its version and source are verified. A project upgrade must be reviewed for changed serialization/materials/rig import settings.

## What existing checks do and do not establish

`validate_sources.py` verifies folder count, matching duplicate scripts, the one Lesson GUID, axis-name presence and ZIP CRCs. The optional parser checks C# grammar. These do **not** establish Unity compilation, scene deserialization, shader availability, UVs, normal-map importer type, material texture references, terrain layers/vegetation, Animator rig mapping, Timeline bindings, gameplay, or EXE builds. Repeating these checks is insufficient evidence for another ready-to-submit claim.

## Recommended replacement delivery and acceptance

1. Inspect/unpack trusted original companion ZIP safely, preserving all paths and `.meta` files. Inventory complete Unity projects versus unitypackages versus loose assets. Identify exact per-hour source files and native Unity version.
2. For each chapter, include all practical scenes and the final exercise in a separate project or a documented set of scenes, with the original dependencies. A shared per-hour selection switch does not meet this.
3. Preserve original meshes/UVs, material shader choice, texture slots and scale/offset, TextureImporter types, model rig/Avatar mappings, sprite slicing, terrain splat/tree/detail layers, prefabs, animator controllers and Timeline bindings.
4. Add a table linking every book procedure to its scene and relevant objects/assets. Distinguish complete-in-source, checked in editor, externally unverified, and absent.
5. In Unity 2018.1.0f1: compile all scripts, open every listed scene, check missing references and unsupported shaders, save/reopen, run required representative interactions, verify all maps visually, then build and launch Windows players where requested.
6. Deliver the 24 projects with **baked native assets and scenes**. If an editor/license/network requirement prevents testing, report the exact blocker and source-only state. Do not publish another generic colored substitute archive as complete.
