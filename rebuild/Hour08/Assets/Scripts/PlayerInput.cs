using UnityEngine;

// Book p.177: axes can be remapped in Project Settings > Input.
public class PlayerInput : MonoBehaviour
{
    void Update()
    {
        float hVal = Input.GetAxis("Horizontal");
        float vVal = Input.GetAxis("Vertical");
        if (hVal != 0)
            print("Horizontal movement selected: " + hVal);
        if (vVal != 0)
            print("Vertical movement selected: " + vVal);
    }
}
