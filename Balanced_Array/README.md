# Balanced Array
You are given a positive integer n, it is guaranteed that n is even (i.e. divisible by 2).
You want to construct the array a of length n such that:

- The first n2 elements of a are even (divisible by 2); 
- the second n2 elements of a are odd (not divisible by 2);
- all elements of a are distinct and positive;
- the sum of the first half equals to the sum of the second half.

If there are multiple answers, you can print any. It is not guaranteed that the answer exists.
You have to answer t independent test cases.

Input: he first line of the input contains one integer t (1≤t≤10^4) — the number of test cases. Then t test cases follow.
The only line of the test case contains one integer n (2≤n≤2⋅10^5) — the length of the array. It is guaranteed that that n is even (i.e. divisible by 2).

Output: For each test case, print the answer — "NO" (without quotes), if there is no suitable answer for the given test case or "YES" in the first line and any suitable array a1,a2,…,an (1≤ai≤10^9) satisfying conditions from the problem statement on the second line.


