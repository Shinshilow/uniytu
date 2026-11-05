using UnityEngine;
public class TouchScript : MonoBehaviour
{
    void OnGUI()
    {
        if (Input.touchCount == 0) GUI.Label(new Rect(5, 5, 500, 30), "No touch data. Connect a real Unity Remote device.");
        for (int i = 0; i < Input.touchCount; i++)
        {
            Touch touch = Input.GetTouch(i);
            float x = 5 + i * 130;
            GUI.Label(new Rect(x, 5, 130, 25), "ID: " + touch.fingerId);
            GUI.Label(new Rect(x, 30, 130, 25), "Phase: " + touch.phase);
            GUI.Label(new Rect(x, 55, 130, 25), "Taps: " + touch.tapCount);
            GUI.Label(new Rect(x, 80, 130, 25), "X: " + touch.position.x);
            GUI.Label(new Rect(x, 105, 130, 25), "Y: " + touch.position.y);
        }
    }
}
