using UnityEngine;
using UnityEngine.SceneManagement;

// Additional readout to observe the book's saved object and click counter.
// It does not create objects or change any of the book's primitive transforms.
public class SceneObservation : MonoBehaviour
{
    public string instructions;

    void OnGUI()
    {
        GUI.Label(new Rect(5, 5, Screen.width - 10, 80), instructions);
        var cube = FindObjectOfType<DontDestroy>();
        if (cube != null)
        {
            GUI.Label(new Rect(5, 85, Screen.width - 10, 25),
                "Persistent Cube: " + cube.GetInstanceID() +
                " | clicks: " + cube.clickCount +
                " | scene index: " + SceneManager.GetActiveScene().buildIndex);
        }
        else if (SceneManager.GetActiveScene().name == "Scene2")
        {
            GUI.Label(new Rect(5, 85, Screen.width - 10, 25),
                "Cube is absent because Scene2 was opened directly. Start Scene1 first.");
        }
    }
}
