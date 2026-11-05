using UnityEngine;
// Final exercise 2, printed p.167. Exactly one output for each integer 1..100.
public class ProgrammingNumbers : MonoBehaviour
{
    void Start()
    {
        for (int number = 1; number <= 100; number++)
        {
            if (number % 3 == 0 || number % 5 == 0)
            {
                print("Программирование — это прекрасно!");
            }
            else
            {
                print(number);
            }
        }
    }
}
