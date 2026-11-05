using UnityEngine;
// Independently authored study examples for chapter 7 pp.157-165.
// This is NOT the original companion file EqualityAndOperations.cs.
public class OperatorsStudy : MonoBehaviour
{
    void Start()
    {
        int sum = 0;
        for (int count = 1; count <= 100; count++)
        {
            sum += count;
        }
        print("Sum 1..100 (for): " + sum);
        int total = 0;
        int number = 1;
        while (number <= 100)
        {
            total += number;
            number++;
        }
        print("Sum 1..100 (while): " + total);
        print("10 % 2 = " + (10 % 2));
        print("6 % 5 = " + (6 % 5));
        print("24 % 7 = " + (24 % 7));
        int x = 5;
        x += 5;
        x++;
        print("x = 5; x += 5; x++; result: " + x);
        print("5 == 6: " + (5 == 6));
        print("9 == 9: " + (9 == 9));
        print("true && false: " + (true && false));
        print("true || false: " + (true || false));
        print("!false: " + (!false));
    }
}
