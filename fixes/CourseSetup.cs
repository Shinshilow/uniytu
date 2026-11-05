using System;
using System.IO;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Tilemaps;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEditor.Animations;
using UnityEngine.Playables;
using UnityEngine.Timeline;
using UnityEngine.SceneManagement;
using UnityEditor.Build.Reporting;

[InitializeOnLoad]
public static class CourseSetup
{
    const string Marker="Assets/Generated/prepared.txt";
    static CourseSetup(){EditorApplication.delayCall+=AutoPrepare;}
    static void AutoPrepare()
    {
        if(EditorApplication.isPlayingOrWillChangePlaymode||EditorApplication.isCompiling)return;
        if(!File.Exists(Marker))Prepare();
    }
    static int Hour(){return int.Parse(File.ReadAllText("Assets/Resources/hour.txt").Trim());}
    [MenuItem("Course/Prepare lesson scenes")]
    public static void Prepare()
    {
        if(EditorApplication.isPlaying)throw new InvalidOperationException("Stop Play Mode first.");
        Directory.CreateDirectory("Assets/Scenes");Directory.CreateDirectory("Assets/Generated");AssetDatabase.Refresh();
        int hour=Hour();var scenes=new List<EditorBuildSettingsScene>();
        if(hour==14||hour==24)
        {
            CreateScene(6,"Game");
            CreateScene(hour,"Menu");
            scenes.Add(new EditorBuildSettingsScene("Assets/Scenes/Menu.unity",true));
            scenes.Add(new EditorBuildSettingsScene("Assets/Scenes/Game.unity",true));
        }
        else {CreateScene(hour,"Lesson");scenes.Add(new EditorBuildSettingsScene("Assets/Scenes/Lesson.unity",true));}
        EditorBuildSettings.scenes=scenes.ToArray();
        PlayerSettings.companyName="Unity24 Learning";PlayerSettings.productName="Hour"+hour.ToString("00");
        PlayerSettings.defaultScreenWidth=1000;PlayerSettings.defaultScreenHeight=700;PlayerSettings.runInBackground=true;
        File.WriteAllText(Marker,"Generated from supplied lesson sources. Unity runtime validation still required.\n");
        AssetDatabase.SaveAssets();AssetDatabase.Refresh();
        Debug.Log("COURSE_PREPARED Hour "+hour);
    }
    static void CreateScene(int hour,string sceneName)
    {
        var scene=EditorSceneManager.NewScene(NewSceneSetup.EmptyScene,NewSceneMode.Single);
        var root=new GameObject("Hour "+hour.ToString("00"));var lesson=root.AddComponent<Lesson>();lesson.hour=hour;
        if(hour==11)
        {
            var lamp=Lesson.Lamp();Persist(scene);var path=AssetDatabase.GenerateUniqueAssetPath("Assets/Generated/Lamp.prefab");
            // Unity 2018.1 API (the prefab API changed in 2018.3).
            lesson.lampPrefab=PrefabUtility.CreatePrefab(path,lamp);UnityEngine.Object.DestroyImmediate(lamp);
        }
        lesson.Generate();
        if(hour==17)Animated(lesson.player);
        if(hour==18)Mecanim(lesson.player);
        if(hour==19)Timeline(lesson.player);
        Persist(scene);
        EditorSceneManager.SaveScene(scene,"Assets/Scenes/"+sceneName+".unity");
        SceneView.RepaintAll();
    }
    static string AssetPath(string name,string ext){return AssetDatabase.GenerateUniqueAssetPath("Assets/Generated/"+name+ext);}
    static void Animated(GameObject go)
    {
        var clip=new AnimationClip();clip.name="ArcBlinkScaleColor";
        clip.SetCurve("",typeof(Transform),"localPosition.x",AnimationCurve.Linear(0,-4,4,4));
        clip.SetCurve("",typeof(Transform),"localPosition.y",new AnimationCurve(new Keyframe(0,0),new Keyframe(2,4),new Keyframe(4,0)));
        foreach(string axis in new[]{"x","y","z"})clip.SetCurve("",typeof(Transform),"localScale."+axis,new AnimationCurve(new Keyframe(0,1),new Keyframe(2,2),new Keyframe(4,1)));
        var blink=new AnimationCurve(new Keyframe(0,1),new Keyframe(1,0),new Keyframe(1.5f,1),new Keyframe(3,0),new Keyframe(3.5f,1),new Keyframe(4,1));
        for(int i=0;i<blink.length;i++){AnimationUtility.SetKeyLeftTangentMode(blink,i,AnimationUtility.TangentMode.Constant);AnimationUtility.SetKeyRightTangentMode(blink,i,AnimationUtility.TangentMode.Constant);}
        clip.SetCurve("",typeof(MeshRenderer),"m_Enabled",blink);
        clip.SetCurve("",typeof(MeshRenderer),"material._Color.r",AnimationCurve.Linear(0,.1f,4,1));
        var settings=AnimationUtility.GetAnimationClipSettings(clip);settings.loopTime=true;AnimationUtility.SetAnimationClipSettings(clip,settings);
        AssetDatabase.CreateAsset(clip,AssetPath(clip.name,".anim"));
        var controller=AnimatorController.CreateAnimatorControllerAtPath(AssetPath("ArcAnimator",".controller"));controller.AddMotion(clip);go.AddComponent<Animator>().runtimeAnimatorController=controller;
    }
    static AnimationClip Motion(string name,float amplitude,float duration)
    {
        var clip=new AnimationClip();clip.name=name;
        clip.SetCurve("",typeof(Transform),"localPosition.y",new AnimationCurve(new Keyframe(0,0),new Keyframe(duration*.5f,amplitude),new Keyframe(duration,0)));
        var settings=AnimationUtility.GetAnimationClipSettings(clip);settings.loopTime=true;AnimationUtility.SetAnimationClipSettings(clip,settings);AssetDatabase.CreateAsset(clip,AssetPath(name,".anim"));return clip;
    }
    static BlendTree Tree(AnimatorController controller,string name,AnimationClip slow,AnimationClip fast)
    {
        var tree=new BlendTree();tree.name=name;tree.blendParameter="Speed";tree.blendType=BlendTreeType.Simple1D;tree.useAutomaticThresholds=false;
        AssetDatabase.AddObjectToAsset(tree,controller);tree.AddChild(slow,0);tree.AddChild(fast,1);return tree;
    }
    static void Mecanim(GameObject go)
    {
        var controller=AnimatorController.CreateAnimatorControllerAtPath(AssetPath("Mecanim",".controller"));controller.AddParameter("Speed",AnimatorControllerParameterType.Float);controller.AddParameter("Crouch",AnimatorControllerParameterType.Bool);controller.AddParameter("Jump",AnimatorControllerParameterType.Trigger);
        var idle=Motion("Idle",.02f,2);var walk=Motion("Walk",.15f,.6f);var run=Motion("Run",.3f,.35f);var jump=Motion("Jump",1.8f,1);var crouch=Motion("Crouch",-.3f,1);
        var sm=controller.layers[0].stateMachine;var grounded=sm.AddState("Grounded");grounded.motion=Tree(controller,"Grounded",idle,run);
        var groundTree=(BlendTree)grounded.motion;groundTree.AddChild(walk,.5f);
        var air=sm.AddState("Airborne");air.motion=Tree(controller,"Airborne",jump,jump);
        var low=sm.AddState("Crouching");low.motion=Tree(controller,"Crouching",crouch,walk);
        sm.defaultState=grounded;
        var t=grounded.AddTransition(low);t.hasExitTime=false;t.duration=.1f;t.AddCondition(AnimatorConditionMode.If,0,"Crouch");
        t=low.AddTransition(grounded);t.hasExitTime=false;t.AddCondition(AnimatorConditionMode.IfNot,0,"Crouch");
        t=sm.AddAnyStateTransition(air);t.hasExitTime=false;t.canTransitionToSelf=false;t.AddCondition(AnimatorConditionMode.If,0,"Jump");
        t=air.AddTransition(grounded);t.hasExitTime=true;t.exitTime=.95f;t.duration=.1f;
        go.GetComponent<Animator>().runtimeAnimatorController=controller;
    }
    static void Timeline(GameObject go)
    {
        var director=new GameObject("Timeline Director").AddComponent<PlayableDirector>();director.playOnAwake=true;director.extrapolationMode=DirectorWrapMode.Loop;
        var timeline=ScriptableObject.CreateInstance<TimelineAsset>();AssetDatabase.CreateAsset(timeline,AssetPath("GuardSequence",".playable"));
        var clip=new AnimationClip();clip.name="GuardPatrol";clip.SetCurve("",typeof(Transform),"localPosition.x",new AnimationCurve(new Keyframe(0,-3),new Keyframe(3,3),new Keyframe(6,-3)));AssetDatabase.CreateAsset(clip,AssetPath("GuardPatrol",".anim"));
        var animator=go.AddComponent<Animator>();var track=timeline.CreateTrack<AnimationTrack>(null,"Guard animation");var tc=track.CreateClip<AnimationPlayableAsset>();tc.start=0;tc.duration=6;((AnimationPlayableAsset)tc.asset).clip=clip;director.SetGenericBinding(track,animator);
        var light=GameObject.Find("Timeline spotlight");var activation=timeline.CreateTrack<ActivationTrack>(null,"Strobe lights");for(int i=0;i<6;i++){var c=activation.CreateDefaultClip();c.start=i;c.duration=.45f;}director.SetGenericBinding(activation,light);
        var cam=Camera.main;var camAnimator=cam.gameObject.AddComponent<Animator>();var cameraClip=new AnimationClip();cameraClip.name="CameraDolly";cameraClip.SetCurve("",typeof(Transform),"localPosition.x",new AnimationCurve(new Keyframe(0,-2),new Keyframe(3,2),new Keyframe(6,-2)));AssetDatabase.CreateAsset(cameraClip,AssetPath("CameraDolly",".anim"));
        var cameraTrack=timeline.CreateTrack<AnimationTrack>(null,"Camera movement");tc=cameraTrack.CreateClip<AnimationPlayableAsset>();tc.duration=6;((AnimationPlayableAsset)tc.asset).clip=cameraClip;director.SetGenericBinding(cameraTrack,camAnimator);
        director.playableAsset=timeline;EditorUtility.SetDirty(timeline);
    }
    static void Persist(Scene scene)
    {
        // Generated materials/textures/terrain/tiles must be assets, or scene reload
        // loses them. Built-in assets and existing references are left intact.
        var roots=scene.GetRootGameObjects();var dependencies=EditorUtility.CollectDependencies(roots);
        foreach(var obj in dependencies)
        {
            if(obj==null||EditorUtility.IsPersistent(obj)||obj is GameObject||obj is Component||obj is Shader||obj is MonoScript)continue;
            if(obj is Material||obj is Texture2D||obj is Sprite||obj is TerrainData||obj is TileBase||obj is AnimationClip)
            {
                var name=System.Text.RegularExpressions.Regex.Replace(obj.name??"Generated","[^a-zA-Z0-9_-]","_");
                AssetDatabase.CreateAsset(obj,AssetPath(name,".asset"));
            }
        }
        AssetDatabase.SaveAssets();
    }
    [MenuItem("Course/Build Windows x64")]
    public static void BuildWindows()
    {
        if(!File.Exists(Marker))Prepare();
        if(!BuildPipeline.IsBuildTargetSupported(BuildTargetGroup.Standalone,BuildTarget.StandaloneWindows64))throw new InvalidOperationException("Install Windows Build Support for this Unity Editor.");
        var paths=new List<string>();foreach(var scene in EditorBuildSettings.scenes)if(scene.enabled)paths.Add(scene.path);
        var folder=Path.GetFullPath(Path.Combine(Application.dataPath,"../../Builds/Hour"+Hour().ToString("00")));Directory.CreateDirectory(folder);
        var report=BuildPipeline.BuildPlayer(new BuildPlayerOptions{scenes=paths.ToArray(),locationPathName=Path.Combine(folder,"Hour"+Hour().ToString("00")+".exe"),target=BuildTarget.StandaloneWindows64,options=BuildOptions.None});
        if(report.summary.result!=BuildResult.Succeeded)throw new Exception("Windows build failed: "+report.summary.result);
        Debug.Log("COURSE_BUILD_SUCCEEDED "+folder);
    }
}
