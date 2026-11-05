using UnityEngine;
// Printed p.197: the mouse-trigger practicum uses Transform motion as shown.
public class MovementScript : MonoBehaviour
{
    void Update()
    {
        float mX = Input.GetAxis("Mouse X") / 10f;
        float mY = Input.GetAxis("Mouse Y") / 10f;
        transform.Translate(mX, mY, 0f);
    }
}
