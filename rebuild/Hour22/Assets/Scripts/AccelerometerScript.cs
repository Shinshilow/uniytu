using UnityEngine;
public class AccelerometerScript : MonoBehaviour
{
    void Update()
    {
        float xMove = Input.acceleration.x * Time.deltaTime;
        float zMove = -Input.acceleration.z * Time.deltaTime;
        transform.Translate(xMove, 0f, zMove);
    }
}
