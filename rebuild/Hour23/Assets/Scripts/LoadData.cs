using UnityEngine;

// Book pp.437-438: Scene2's independent Main Camera reads the saved value.
public class LoadData : MonoBehaviour
{
    string playerName = "";

    void Start()
    {
        playerName = PlayerPrefs.GetString("name", "");
    }

    void OnGUI()
    {
        GUI.Label(new Rect(5, 220, 200, 30), playerName);
    }
}
