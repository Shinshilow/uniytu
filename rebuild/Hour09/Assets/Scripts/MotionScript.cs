using UnityEngine;
// Final exercise p.201-202: world X/Z arrow input through the physics step.
[RequireComponent(typeof(Rigidbody))]
public class MotionScript : MonoBehaviour
{
    public float speed = 2f;
    Rigidbody body;
    void Awake()
    {
        body = GetComponent<Rigidbody>();
    }
    void FixedUpdate()
    {
        Vector3 movement = new Vector3(Input.GetAxisRaw("Horizontal"), 0f,
            Input.GetAxisRaw("Vertical"));
        body.MovePosition(body.position + movement * speed * Time.fixedDeltaTime);
    }
}
