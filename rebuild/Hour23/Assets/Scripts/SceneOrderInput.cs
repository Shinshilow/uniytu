using UnityEngine;
using UnityEngine.SceneManagement;

// Small navigation aid for the separate scene-order practicum. No objects are
// generated and no DontDestroyOnLoad is used in this comparison scene pair.
public class SceneOrderInput : MonoBehaviour
{
    public int targetSceneIndex;

    void OnGUI()
    {
        if (GUI.Button(new Rect(5, 120, 180, 35), "Load other scene"))
            SceneManager.LoadScene(targetSceneIndex);
    }
}
