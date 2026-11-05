using UnityEngine;
// Printed pp.197,201-202: same callbacks, with trigger-name mode for the exercise.
public class TriggerScript : MonoBehaviour
{
    public bool reportTriggerName;
    void OnTriggerEnter(Collider other)
    {
        if (reportTriggerName)
            print(gameObject.name + ": вход — " + other.gameObject.name);
        else
            print(other.gameObject.name + " has entered the cube");
    }
    void OnTriggerStay(Collider other)
    {
        if (reportTriggerName)
            print(gameObject.name + ": нахождение внутри — " + other.gameObject.name);
        else
            print(other.gameObject.name + " is still in the cube");
    }
    void OnTriggerExit(Collider other)
    {
        if (reportTriggerName)
            print(gameObject.name + ": выход — " + other.gameObject.name);
        else
            print(other.gameObject.name + " has left the cube");
    }
}
