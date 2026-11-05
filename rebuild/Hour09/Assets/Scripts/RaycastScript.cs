using UnityEngine;
// Printed pp.199-200: cast every frame, without a click-to-fire requirement.
public class RaycastScript : MonoBehaviour
{
    void Update()
    {
        float dirX = Input.GetAxis("Mouse X");
        float dirY = Input.GetAxis("Mouse Y");
        transform.Rotate(dirY, dirX, 0f);
        CheckForRaycastHit();
    }
    void CheckForRaycastHit()
    {
        RaycastHit hit;
        if (Physics.Raycast(transform.position, transform.forward, out hit))
        {
            print(hit.collider.gameObject.name + " destroyed!");
            Destroy(hit.collider.gameObject);
        }
    }
}
