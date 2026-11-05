using UnityEngine;

// End exercise, pp.187-188. Arrow motion stays along world X/Z after yaw.
public class CubeControlScript : MonoBehaviour
{
    public Camera controlledCamera;
    public float movementSpeed = 4f;
    public float mouseSensitivity = 2f;
    Vector3 originalScale;
    bool doubleSize;

    void Start()
    {
        originalScale = transform.localScale;
    }

    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");
        transform.Translate(new Vector3(horizontal, 0f, vertical)
            * movementSpeed * Time.deltaTime, Space.World);

        float mouseX = Input.GetAxis("Mouse X");
        float mouseY = Input.GetAxis("Mouse Y");
        transform.Rotate(0f, mouseX * mouseSensitivity, 0f, Space.World);
        controlledCamera.transform.Rotate(-mouseY * mouseSensitivity, 0f, 0f,
            Space.Self);

        if (Input.GetKeyDown(KeyCode.M))
        {
            doubleSize = !doubleSize;
            transform.localScale = originalScale * (doubleSize ? 2f : 1f);
        }
    }
}
