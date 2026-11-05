using UnityEngine;
// Book practicum, printed pp.153-154. Stop Play after a short observation.
public class ImportantFunctions : MonoBehaviour
{
    void Start()
    {
        print("Start runs before an object Updates");
    }
    void Update()
    {
        print("This is called once a frame");
    }
}
