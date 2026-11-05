using UnityEngine;

// Book p.178 modifies PlayerInput. Distinct class keeps each variant available.
public class KeyInputScript : MonoBehaviour
{
    void Update()
    {
        if (Input.GetKey(KeyCode.M))
            print("The 'M' key is pressed down");
        if (Input.GetKeyDown(KeyCode.O))
            print("The 'O' key was pressed");
    }
}
