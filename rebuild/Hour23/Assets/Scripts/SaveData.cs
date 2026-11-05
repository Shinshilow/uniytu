using UnityEngine;

// Book p.437: this component belongs to Scene1's Main Camera, not the Cube.
public class SaveData : MonoBehaviour
{
    public string playerName = "";

    void OnGUI()
    {
        playerName = GUI.TextField(new Rect(5, 120, 100, 30), playerName);
        if (GUI.Button(new Rect(5, 180, 50, 50), "Save"))
        {
            PlayerPrefs.SetString("name", playerName);
            // Explicit disk flush makes the chapter's relaunch check repeatable.
            PlayerPrefs.Save();
        }
    }
}
