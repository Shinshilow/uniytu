# Audit of original publisher material and terrain assets (hours 3–4)

Source: `/workspace/book-originals/extracted`, compared with `audit/book-requirements.json`. This is read-only source inspection. Original files were not changed. Full machine-readable findings, source hashes, scene references, material properties and binary TerrainData summaries are in `originals-03-04-detail.json`. Supplementary hour 6 terrain evidence is also in `originals-06-terrain-detail.json`.

## Hour 3: actual model mapping and brick materials

Both supplied projects were saved in Unity **2018.1.0b4**.

- `Hour 3 TIY/Assets/Models/Torus.fbx.meta` has `ModelImporter.globalScale=100`, `useFileScale=1`; it is an importer setting, not a substituted scene scale. The import scene references the actual FBX.
- `Applying textures.unity` uses the original `Brick_Texture.png` through `BrickWall.mat`, **Standard** shader (built-in fileID 46), Main Texture tiling **(3,1)**, offset (0,0). The original wall's saved transform is available in the JSON scene evidence.
- `Assets from the asset store.unity` instantiates the actual `Robot Kyle.fbx` prefab. Its binary FBX contains **4,934 UV pairs**, all coordinate values nonzero, range 0.004623–0.996013, and **12,796 UV indices**. The original `Robot_Color.mat` resolves to `Robot_Color.tga` and `Robot_Normal.tga`; the normal texture has `textureType=1`, `sRGBTexture=0`, and the color texture has `textureType=0`, `sRGBTexture=1`. The supplied Kyle material uses its original built-in legacy shader reference (fileID 2), which is independent of the Standard requirement for the brick exercise.
- `Hour 3 Exercise/Assets/Scenes/Main.unity` saves four actual spheres at (1,2,-5), (-1,0,-5), (1,0,-5), (-1,2,-5), all scale (2,2,2), each with its own material reference. Directional Light is at (0,10,-10), Euler hint (30,-180,0).
- All four brick materials use **Standard/Opaque**, metallic 0, original `Brick_Texture.png`, Main Texture tiling **(3,3)** and zero offsets. Smoothness is 0 for DiffuseBrick/BumpedBrick and 0.6 for SpecularBrick/BumpedSpecularBrick. Both Bumped materials link the original `Brick_Normal.png`, bump strength 1, `_NORMALMAP` keyword. Albedo importer has **aniso=3**. Normal importer has **textureType=1**, **sRGBTexture=0**, no convert-to-normal operation.

These are actual source assets and assigned GUID references; no procedural replacement textures or robot primitives are necessary. The built-in sphere/cube UVs are sufficient for the book's exercise. No new UV unwrap is prescribed.

## Hour 4: genuine binary TerrainData and painted maps

The publisher supplies **only `Hour 4 TIY`**, with four saved scenes. The four `.asset` TerrainData files are **binary Unity serialized files, version 2018.1.0b4**, not YAML. Preserve these files byte-for-byte with their matching `.meta` GUIDs. Each scene's Terrain and TerrainCollider references the same TerrainData GUID.

| TerrainData | Size | Native painted splats | Native vegetation |
| --- | --- | --- | --- |
| Heightmapped Terrain | 50×60×50 | none, appropriate to import stage | none |
| Scultped Terrain (publisher spelling) | 50×60×50 | none, appropriate to sculpt stage | none |
| Textured Terrain | 50×60×50 | GrassHill, GrassRocky, Cliff, Sand | no instances |
| Trees and Grass | 50×60×50 | same four original image textures | 37 trees; grass detail layer |

All four heightmaps are **513×513**. The original `terrain.raw` is **526,338 bytes**, 263,169 big-endian uint16 samples. Every imported Heightmapped Terrain sample matches `floor(raw/2)` after accounting for transposed binary height storage axes: **263,169/263,169 matches**, with no vertical flip. This distinguishes the original import from generated noise.

For Textured/Trees and Grass:

- Native `m_SplatDatabase.m_Splats` resolves to original `GrassHillAlbedo.psd`, `GrassRockyAlbedo.psd`, `CliffAlbedoSpecular.psd`, `SandAlbedo.psd`, with tile sizes (10,10), (10,10), (8,8), (15,15). Normal slots are empty in these source terrain layers; chapter 4 first-layer normal maps are optional.
- The native embedded **512×512 RGBA splat alphamap** contains **6,893 distinct values**. Channels span R13–255, G0–154, B0–177, A0–182. Every pixel's channel sum is **254–256**, consistent with normalized four-layer weights quantized to bytes. Textured and Trees/Grass share the same decoded map pixels. This is genuine spatial texture painting with blends, not one material or flat color.
- Trees and Grass contains **29 Conifer_Desktop + 8 Broadleaf_Desktop** native TreeInstances, matching two actual `.spm` tree prototypes. Their width scales span 0.13152–0.43775; there are no substitute primitive trees.
- The native grass DetailPrototype points to **GrassFrond01AlbedoAlpha.psd**, renderMode 0 (billboard), width and height ranges 1–2. There are **341 nonempty detail patches**, density sum **543**, plus saved wind settings. These are actual terrain detail records.
- Every referenced external terrain image/tree GUID resolves to an asset inside the supplied project. No missing external terrain reference was found.

## Required additions beyond the publisher's finished examples

The supplied chapter 4 examples do not by themselves complete every book requirement:

1. **H04-P04** asks for a horizontal 100×100 terrain, but the source Trees/Grass TerrainData is actually 50×50. Save an independent corrected practice copy at (100,60,100), preserving its native painted terrain/vegetation data and framing the new extent appropriately.
2. **H04-P06** is absent from the four source scenes: each scene contains only Main Camera, Directional Light and Terrain. The original `Standard Assets/Characters/FirstPersonCharacter/Prefabs/FPSController.prefab` and supporting scripts are available. Create a separate saved practice scene with that real prefab above the actual terrain, remove the old camera/listener, and verify walking/jumping/collision in Unity.
3. **H04-E** has no supplied Exercise project or final scene. Save an independently completed terrain with recognizable beach, mountain ridge and flat plain, Sand→GrassRocky transitions, GrassHill plains, Cliff high/steep portions, plus native tree/detail layers. A simple renamed copy of Trees/Grass should not be represented as this final exercise.

A valid implementation should use the **Unity 2018.1 `SplatPrototype`/`splatPrototypes` API**, original images, `SetAlphamaps`, native TreeInstances and `SetDetailLayer`, and save the actual assets before Play. `TerrainLayer` is a later API. The FPS scene must use actual TerrainCollider/TerrainData and exactly one AudioListener.

## Hour 6 supplementary terrain evidence

`Amazing Racer/Assets/Terrains/New Terrain.asset` is a binary TerrainData saved with **Unity 2017.3.0b10**. Its heightmap is 513×513, scale (0.390625,100,0.390625), so the actual size is **200×100×200**. It contains original GrassHill, Cliff, GrassRocky and MudRocky splats, each tiled 15×15; all four source GUIDs resolve. There are no native terrain trees or details in this racer source. Do not shrink the Z dimension to 100 without reconciling the saved course, whose player starts at Z125.

## Validation limits

The audit read YAML/importer references, direct original FBX UV arrays and UnityPy 1.25.4 binary TerrainData type trees and splat textures. It did **not** run Unity 2018.1.0f1, perform Editor imports, compile against the Editor, compare rendered visuals, enter Play mode or build Windows executables. Source compatibility and runtime checks remain to be performed in the actual target Editor.
