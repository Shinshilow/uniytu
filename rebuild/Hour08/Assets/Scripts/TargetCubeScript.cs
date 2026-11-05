using UnityEngine;

// Book pp.185-186. Script is on Main Camera, not Cube.
public class TargetCubeScript : MonoBehaviour
{
    private GameObject target;

    void Start()
    {
        target = GameObject.Find("Cube");
    }

    void Update()
    {
        target.transform.Translate(.05f, 0f, 0f);
        target.transform.Rotate(0f, 0f, 1f);
        target.transform.localScale = new Vector3(1.5f, 1.5f, 1.5f);
    }
}
