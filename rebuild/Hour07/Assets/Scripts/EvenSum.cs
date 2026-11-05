using UnityEngine;
// Final exercise 1, printed p.167. Sum even integers from 2 through 499.
public class EvenSum : MonoBehaviour
{
    void Start()
    {
        int sum = 0;
        for (int number = 2; number <= 499; number += 2)
        {
            sum += number;
        }
        print(sum);
    }
}
