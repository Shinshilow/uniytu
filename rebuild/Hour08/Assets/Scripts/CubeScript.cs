using UnityEngine;

// Book p.182. Per-frame values are intentional in this specific experiment.
public class CubeScript : MonoBehaviour
{
    void Update()
    {
        transform.Translate(.05f, 0f, 0f);
        transform.Rotate(0f, 0f, 1f);
        transform.localScale = new Vector3(1.5f, 1.5f, 1.5f);
    }
}
