# LeetCode solutions

Historical Java solution notes. `Kth largest` contains two independent `Solution` alternatives for finding the kth-largest element: an insertion-based approach and a sort-based approach.

Copy one `class Solution` block at a time into the online judge; the notes are not one compilable Java file. Both alternatives validate `k`. The insertion variant handles negative numbers; the sort variant mutates the input array.

Examples: `[-5, -2, -8], k=2 → -5`; `[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4 → 4`.

With Python 3 and a JDK on `PATH`, run `python tests/verify_solutions.py` to compile each answer separately and check negative values, duplicates, the minimum integer and invalid `k`.
