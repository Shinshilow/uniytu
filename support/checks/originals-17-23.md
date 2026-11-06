# Publisher originals, hours 17–23

Target: **Unity 2018.1.0f1**. Source: `/workspace/book-originals/extracted`, read without modification. Author projects were saved with Unity 2018.1.0b3 or b4. This audit inspected serialized scenes, materials, import settings, controllers and scripts. Unity import, API compilation, Play Mode, sound playback, phone input and executable builds have **not** been run.

The JSON report contains complete scene component summaries, custom script sources, material texture references, humanoid mappings, FBX clip settings and controller graph data. Separate C# syntax parsing passed for 18 original/custom preparation scripts; it does not certify Unity API compatibility.

## Hour 17 — animation

Original project: `Hour 17 Files Final/Completed Projects/Hour 17 TIY` (2018.1.0b4).

Scenes:

- `Assets/Scenes/2D Animation.unity`
- `Assets/Scenes/Custom Animation.unity`

Coverage:

- **17.1:** The original 2048×2048 RobotBoy sheet has 16 native sprite rectangles of 275×275, centered pivots. `Robot Run.anim` references 16 sprite frames at 12 fps; a real Animator Controller is assigned. This differs from the book's stated 64×64 slicing example. Cutting the supplied artwork into 64×64 rectangles would fragment the character; preserve the original 275×275 frame definitions and document the discrepancy.
- **17.2:** Cube is at the origin, with an actual ObjectSpinAnim clip and controller. Euler Y goes from 0 to 360 over one second, sampled at 60 fps, with looping enabled.
- **17.3:** CubeColor is assigned. Saved RGBA material animation starts and ends red, with intermediate colors.
- **17.4:** The author clip has zero Y tangents at both endpoints, causing easing. The final straight rotation curve exercise remains unfinished in the original.
- **17.E:** Arc flight, Renderer blinking and scale/material transformations are absent from the original.

Addition supplied in `course_additions/Hour17`: an Editor preparer that saves native arc, discrete Renderer blink, scale/color clips, controllers, materials and `Assets/Scenes/Exercise.unity`; it also sets the source spin Y curve to linear. These generated assets remain pending until Unity executes the preparer. Original scenes are retained.

## Hour 18 — Mecanim

Original project: `Hour 18 Files Final/Completed Projects/Hour 18 TIY` (2018.1.0b4).

Scene: `Assets/Scenes/Main.unity`.

Coverage:

- **18.1:** Actual Ethan FBX, Humanoid rig, populated human bone map and configured Avatar are present. EthanNormals.png and EthanOcclusion.png are 4096×4096. Runtime Avatar validity still requires Unity import.
- **18.2:** Custom animation FBXs use Humanoid with 54 mapped bones. Idle: frames 128–1100. WalkForwardStraight: 215.2–244.9, orientation offset 3.53. Right and mirrored left turns: 122–152. Loop and root bake metadata match the book.
- **18.3:** Checker.mat uses original Checker.tga in `_MainTex`, tiling 10×10, offset zero. Plane is at (0,0,-5), scale (10,1,10). Camera is parented to Ethan, local position (0,1.5,-1.5), X rotation 20 degrees.
- **18.4:** The authored PlayerAnimator has float Speed and Direction, default Idle with Foot IK, Walking 1D blend thresholds -1/0/1, and Speed greater/less than 0.1 transitions without exit time. Active custom motion references resolve.
- **18.5:** Original AnimationControl sets Speed from Vertical and Direction from Horizontal.
- **18.E:** The real Standard Assets ThirdPersonController prefab and Grounded/Airborne/Crouching controller are available, but no separate exploration scene is saved.

Material/reference concerns:

- EthanGrey/EthanWhite retain unresolved `_MainTex`, `_SpecGlossMap` and `_Cube` references from the author archive. Normal and occlusion references resolve. Do not describe every original material property as complete without checking the actual shader output.
- The Standard Assets controller has nine missing external GUIDs in **unreachable orphan BlendTrees**. Graph traversal from all three real states found no missing active motion references. Replacing the active controller is unnecessary.
- Several `lastHumanDescriptionAvatarSource` fields reference absent historical imports, while the FBX contains its human description. This does not prove that its active Avatar is broken.
- References to Unity UI DLL GUIDs are engine references, not missing project assets.

Minimal addition: save a separate exploration scene using the original ThirdPersonController prefab, a plane and camera, retaining the custom Idle/Walking scene.

## Hour 19 — Timeline

Original project: `Hour 19 Files Final/Completed Projects/Hour 19 TIY` (2018.1.0b3).

Scenes:

- `Assets/Scenes/Creating a Timeline.unity`
- `Assets/Scenes/Adding tracks.unity`
- `Assets/Scenes/Scripting.unity`

Coverage:

- **19.1–19.2:** Real TimelineAsset assigned to a PlayableDirector. Adding tracks binds the AnimationTrack to Cube Animator. AudioTrack exists; its binding is null in the original.
- **19.3:** Seven actual color AnimationClips and original Beep High.wav exist. Seven audio clips align with color starts.
- **19.4:** Shared final timeline has one-second Red/Orange/Yellow/Green/Blue/Indigo/Violet clips starting at 0,0.5,1,1.5,2,2.5,3 seconds: correct 50% overlaps. No separate unblended version is saved.
- **19.5:** Scripting scene disables Play On Awake and uses original InputControl: Space plays when paused, otherwise stops.
- **19.E:** Additional UI, patrol, camera and activation/light experiments are absent.

Timeline DLL GUID `6a10b2909283487f913b00d94cd3faf5` belongs to Unity Timeline. Preserve it. A stale null binding to old asset GUID `155288b2422ec8f47be05ab7a96973e2` is harmless leftover data, not a reason to replace the Timeline asset.

Addition supplied in `course_additions/Hour19`: an Editor preparer saves a separate native Exercise timeline with guard patrol, two camera movements, animated UI, light ActivationTrack and original beep AudioTrack. It also saves Unblended.unity with seven one-second original color clips without overlaps and explicitly binds AudioSource in the delivery copy's Adding tracks/Scripting scenes. These changes remain pending until Unity executes the preparer.

## Hour 20 — Gauntlet Runner

Original project: `Hour 20 Files Final/Completed Projects/Gauntlet Runner` (2018.1.0b4).

Scene: `Assets/Scenes/Main.unity`.

Texture/UV mapping is materially present:

- Ground.mat uses MarketFloorMetalAlbedo.tif, tiling (2,10), offset (0,0).
- Wall.mat uses SecurityRoomLazerGateAlpha.png, tiling (1,5), offset (0,0), with red tint.
- Player.mat uses original 2048×2048 PlayerAlbedo.png, tiling (1,1), offset (0,0). Original FBX and its UV data are retained.
- PhasedOut.mat uses actual Hologram.shader with blue main/rim colors.
- Dark Sky is an assigned procedural sky material.

Coverage:

- **20.1:** Ground, walls, camera and native materials follow the book corridor. Main camera position is (0,3,-10.7).
- **20.2:** TextureScroller changes material texture Y offset using deltaTime × 0.5, subtracting one when it exceeds one; the ground mesh stays in place.
- **20.3–20.4:** Actual Powerup/Obstacle prefabs, Rigidbody without gravity, materials, lights, particles and cleanup TriggerZone are included. Powerup position/scale: (0,1.5,42)/(.5,.5,.5). Obstacle: (0,.4,42)/(1,.2,1). TriggerZone: (0,1,-20)/(10,1,1), trigger enabled.
- **20.5:** Actual Player Humanoid FBX and Runs FBX. Run uses frames 302–319, orientation offset -4.81, loop/bake fields from the book. Controller Run speed is 0.7, Foot IK enabled. Scene override disables root motion and tags Player.
- **20.6:** Ten-second timer, horizontal speed 4 clamped to ±3, Space phase for two seconds by material/collider swap. Negative hits set time scale to 0.5, restoring 1 after one scaled second. Game ends when the timer expires, not on collision.
- **20.7:** Collidable speed 20; powerup +1.5 seconds, obstacle -0.5 seconds. Spawner alternates every 0.5 seconds at random X in [-3,3] and assigns manager references.
- **20.E:** Optional enhancements are not supplied; base game matches the mandatory exercise.

The game-over GUI sets Time.timeScale to zero. Any added restart/course scene navigation must restore it to one before loading a scene.

## Hour 21 — audio

Original projects: `Hour 21 Files Final/Completed Projects/Hour 21 TIY` and `Hour 21 Exercise` (both 2018.1.0b4).

Scenes:

- TIY: Adding Audio Source, Audio in Scene View, Audio Scripting, Audio Mixer.
- Exercise: `Assets/Scenes/Main.unity`.

Coverage:

- **21.1:** Original looper.ogg, Play On Awake true and Loop false.
- **21.2:** Adding Audio Source supplies the 2D spatial-blend-zero version; Audio in Scene View supplies spatial blend one. Both are native inspectable scenes.
- **21.3:** Audio Scripting has Play On Awake false, Loop true and original Space Play/Stop code.
- **21.4:** Actual NewAudioMixer asset is present. Cube routes to a real group through serialized field **OutputAudioMixerGroup**. The lack of `m_OutputAudioMixerGroup` is not an error.
- **21.E:** Separate exercise Cube at (0,0,-10), real looper/quick_laser/xxplosion clips, Space toggle, L loop toggle and 1/2/3 stop/swap/play controls.

The two projects define different classes named AudioScript. Keep them as separate practice projects or rename the exercise class and filename while preserving its meta GUID when merging.

## Hour 22 — mobile input

Original projects: `Hour 22 Files Final/Completed Projects/Hour 22 TIY` and `Hour 22 Exercise` (2018.1.0b4).

Scenes:

- TIY: Unity Remote, Accelerometer, Touches.
- Exercise: `Assets/Scenes/Main.unity`.

Coverage:

- **22.1:** Native central UI Button/Remote scene. Unity UI DLL GUID `f5f67c52d1564df4a8936ccd202a3bd8` is an engine reference.
- **22.2:** Actual accelerometer script translates by acceleration.x × deltaTime and -acceleration.z × deltaTime.
- **22.3:** Actual touch IDs, phase, tap count and position are displayed in columns 130 pixels apart.
- **22.E:** Original three-cube exercise maps finger IDs 0/1/2 using deltaPosition × 0.05, exactly as the book.

Real devices can assign arbitrary finger IDs after fingers lift/rejoin. A documented stable finger-to-cube assignment is an optional robustness improvement. Remote connection, tilt and multitouch require physical-device checks.

## Hour 23 — scenes, preferences and builds

Original project: `Hour 23 Files Final/Completed Projects/Hour 23 DIY` (2018.1.0b3).

Scenes: `Assets/Scenes/Scene1.unity`, `Assets/Scenes/Scene2.unity`.

Coverage:

- **23.1:** Build Settings correctly enables Scene1 at index zero, Scene2 at index one.
- **23.2:** Cube at origin uses DontDestroyOnLoad(this), click loads index one. Scene2 Sphere is at (0,2,0). LightingDataAsset is null; the book's Generate Lighting step is not proven complete.
- **23.3:** Original SaveData writes PlayerPrefs key `name`; LoadData reads it and displays the label with the specified GUI rectangles. Calling PlayerPrefs.Save on Save is an optional durability improvement.
- **23.4:** Original PlayerSettings exist; standalone icon/display settings need delivery review.
- **23.E:** No built executable is supplied in the author project. An actual Windows build and external run remain necessary.

## Delivery constraints

Copy complete Assets folders and their meta files. Preserve binary FBX UVs and GUIDs. Set the target Editor version in delivery copies, not the read-only source archive. Build Settings are empty in author projects 17–22 and must be populated. Keep class-name collisions isolated. Generated exercise scenes should be reported as pending Editor preparation until Unity saves them; do not claim existing EXEs or successful engine tests from these files.
