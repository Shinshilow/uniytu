using UnityEngine;
using System.Collections.Generic;

// Separate comparison variant: fingers retain their Cube until released.
// This is deliberately not a silent change to the printed InputScript example.
public class StableInputScript : MonoBehaviour
{
    void Update()
    {
        TouchRouting.UpdateRouting();
        foreach (Touch touch in Input.touches)
        {
            int index = TouchRouting.CubeFor(touch.fingerId);
            if (name == "Cube" + (index + 1) && touch.phase == TouchPhase.Moved)
                transform.Translate(touch.deltaPosition.x * .05f,
                    touch.deltaPosition.y * .05f, 0f);
        }
    }
}

public static class TouchRouting
{
    static readonly Dictionary<int, int> fingers = new Dictionary<int, int>();
    static int frame = -1;

    public static void UpdateRouting()
    {
        // Three Cube components share one update of the mapping per frame.
        if (frame == Time.frameCount) return;
        frame = Time.frameCount;
        if (Input.touchCount == 0) { fingers.Clear(); return; }

        var remove = new List<int>();
        foreach (var pair in fingers)
        {
            bool found = false;
            foreach (Touch touch in Input.touches)
                if (touch.fingerId == pair.Key && touch.phase != TouchPhase.Ended
                        && touch.phase != TouchPhase.Canceled)
                    found = true;
            if (!found) remove.Add(pair.Key);
        }
        foreach (int id in remove) fingers.Remove(id);

        foreach (Touch touch in Input.touches)
        {
            if (touch.phase == TouchPhase.Ended || touch.phase == TouchPhase.Canceled
                    || fingers.ContainsKey(touch.fingerId)) continue;
            for (int cube = 0; cube < 3; cube++)
            {
                if (fingers.ContainsValue(cube)) continue;
                fingers.Add(touch.fingerId, cube);
                break;
            }
        }
    }

    public static int CubeFor(int id)
    {
        int result;
        return fingers.TryGetValue(id, out result) ? result : -1;
    }
}
