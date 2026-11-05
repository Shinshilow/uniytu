using System;
using System.IO;
using System.Collections.Generic;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEditor.SceneManagement;
using UnityEngine;

// Build only: the supplied scenes are ALREADY saved, no CourseSetup is needed.
public static class BuildHour23
{
    [MenuItem("Book/Hour 23/Build Windows x64")]
    public static void BuildWindows()
    {
        if (Application.isPlaying)
            throw new InvalidOperationException("Stop Play Mode before building.");
        if (!BuildPipeline.IsBuildTargetSupported(BuildTargetGroup.Standalone,
                BuildTarget.StandaloneWindows64))
            throw new InvalidOperationException(
                "Windows Build Support for Unity 2018.1.0f1 is required.");

        var scenes = new List<string>();
        foreach (var scene in EditorBuildSettings.scenes)
        {
            if (!scene.enabled) continue;
            if (!File.Exists(scene.path))
                throw new FileNotFoundException("Configured scene not found", scene.path);
            scenes.Add(scene.path);
        }
        if (scenes.Count == 0)
            throw new InvalidOperationException("Scenes In Build is empty.");

        PlayerSettings.companyName = "Unity Book Study";
        PlayerSettings.productName = "Hour23 - Scenes and Save Data";
        PlayerSettings.defaultScreenWidth = 1000;
        PlayerSettings.defaultScreenHeight = 700;
        PlayerSettings.runInBackground = true;
        PlayerSettings.displayResolutionDialog = ResolutionDialogSetting.Enabled;

        var output = Path.GetFullPath("Builds/Hour23/Hour23.exe");
        Directory.CreateDirectory(Path.GetDirectoryName(output));
        var report = BuildPipeline.BuildPlayer(new BuildPlayerOptions
        {
            scenes = scenes.ToArray(),
            locationPathName = output,
            target = BuildTarget.StandaloneWindows64,
            options = BuildOptions.None
        });
        if (report.summary.result != BuildResult.Succeeded)
            throw new InvalidOperationException("Build failed: " + report.summary.result);
        Debug.Log("HOUR23_BUILD_SUCCEEDED " + output);
    }

    [MenuItem("Book/Hour 23/Bake active scene lighting")]
    public static void BakeActiveSceneLighting()
    {
        if (Application.isPlaying)
            throw new InvalidOperationException("Stop Play Mode before baking.");
        Lightmapping.giWorkflowMode = Lightmapping.GIWorkflowMode.OnDemand;
        if (!Lightmapping.Bake())
            throw new InvalidOperationException("Lighting bake did not finish successfully.");
        EditorSceneManager.SaveOpenScenes();
        Debug.Log("HOUR23_LIGHTING_BAKED");
    }
}
