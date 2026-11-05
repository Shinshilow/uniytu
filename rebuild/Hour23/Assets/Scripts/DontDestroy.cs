using UnityEngine;
using UnityEngine.SceneManagement;

// Book pp.435-436. The target differs only for the independent comparison pair.
public class DontDestroy : MonoBehaviour
{
    public int targetSceneIndex = 1;
    // Auxiliary observation: this field stays on the SAME Cube after scene load.
    public int clickCount;

    void Start()
    {
        DontDestroyOnLoad(gameObject);
    }

    void OnMouseDown()
    {
        clickCount++;
        if (SceneManager.GetActiveScene().buildIndex != targetSceneIndex)
            SceneManager.LoadScene(targetSceneIndex);
    }
}
