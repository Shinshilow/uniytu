using UnityEngine;
// Final exercise 3, printed p.167. First twenty terms, beginning with 0 and 1.
public class Fibonacci : MonoBehaviour
{
    void Start()
    {
        int first = 0;
        int second = 1;
        for (int index = 0; index < 20; index++)
        {
            print(first);
            int next = first + second;
            first = second;
            second = next;
        }
    }
}
