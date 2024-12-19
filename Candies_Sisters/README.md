# Candies and Two Sisters
There are two sisters Alice and Betty. You have n
 candies. You want to distribute these n
 candies between two sisters in such a way that:

- Alice will get a (a>0) candies;
- Betty will get b (b>0) candies;
- each sister will get some integer number of candies;
- Alice will get a greater amount of candies than Betty (i.e. a>b);
- all the candies will be given to one of two sisters (i.e. a+b=n).
Your task is to calculate the number of ways to distribute exactly n
 candies between sisters in a way described above. Candies are indistinguishable.

Formally, find the number of ways to represent n as the sum of n=a+b, where a and b are positive integers and a>b.
You have to answer t independent test cases.

Input: The first line of the input contains one integer t (1≤t≤10^4) — the number of test cases. Then t test cases follow.
The only line of a test case contains one integer n (1≤n≤2x10^9) — the number of candies you have.

Output: For each test case, print the answer — the number of ways to distribute exactly n candies between two sisters in a way described in the problem statement. If there is no way to satisfy all the conditions, print 0.