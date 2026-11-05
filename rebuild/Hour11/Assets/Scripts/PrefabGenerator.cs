using UnityEngine;
// Book Hour11, printed pp.230-231. Reference is assigned to the real Lamp asset.
public class PrefabGenerator : MonoBehaviour
{
    public GameObject prefab;
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.B))
        {
            Instantiate(prefab);
        }
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Instantiate(prefab, transform.position, transform.rotation);
        }
    }
}
