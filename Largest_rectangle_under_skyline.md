Largest Rectangle under skyline
Write a program that takes in an array of positive integers representing the heights of adjacent buildings and
returns the area of the largest rectangle that can be created by any number of adjacent buildings, including just one building. Note that all buildings have the same width of 1 unit.
or example , given buildings =[2,1,2], the area of the largest rectange that can be created is 3, using all three buildings . Since the minimum height of the three buildings is 1, you can create a rectangle that has a height of 1 and width of 3 (the number of buildings). You could also create rectangles of area 2 by using only the first building or the last building, but these clearly wouldn't be the largest rectangels, Similarly, you coluld create rectangels of area 2 by using the first and second building or the second and third building.
To clarify, the width of a created rectangle is the number of buildings used to create the rectangle, and its height is the height of the samllest building used to crate it.
Note that if no rectangle can be created, your program should return 0.
input format:
The input consists of multiple test cases so the first line of the inut is the number of test cases.
The first line of each test case contains comma-separated values representing the heights of addjacent.
Output format:
returns the area of the largest rectangle that can be created by any number of adjacent buildings, including just one building if no rectangles can be created, your program should return 0

Sample input:
1
1,3,3,2,4,1,5,3,2

Sample output:

9
