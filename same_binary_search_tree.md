Same bsts
An array of integers is siad to represent the Binary Search Tree (bst) obtained by inserting each integer in the array , from left to right , into the bst.
Write a program that takes in two arrays of integers and determines whether these arrays represent the
same bst.
A bst is Binary Tree that consists only of bst nodes. A node is said to be a valid bst node if and only if it
satisfies the bst property : its value is strictly greater thant the values of every node to its left ; its value is less than or equal
to the values of every node to its right ; and its children nodes are either valid bst nodes themselves
or None /null

input format:

The input consists of multiple test cases so the first line of the input is the number of test cases.
The first line of each test case contains comma-separated values which indicate the first array.
The second line of each test case contains another comma-separated integer value representing the second array.
Output format:
Return true if the tow arrays represent the same Bst or false otherwise.
Constraints:
1<= array1.size <=2000
1<= array2.size <=2000

Sample input:
1
10,15,8,12,94,81,5,2,11
10,8,5,15,2,12,11,94,81
Output:
true
