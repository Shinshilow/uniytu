using UnityEngine;

// Book p.180: standalone saved variant of the PlayerInput example.
public class MouseInputScript : MonoBehaviour
{
    void Update()
    {
        float mxVal = Input.GetAxis("Mouse X");
        float myVal = Input.GetAxis("Mouse Y");
        if (mxVal != 0)
            print("Mouse X movement selected: " + mxVal);
        if (myVal != 0)
            print("Mouse Y movement selected: " + myVal);
    }
}
