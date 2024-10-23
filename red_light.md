Red light
In a crowded city, a network of traffic cameras is installed on all crosses and capture the image of the cars that
pass the red lights. The law enforcement department requires a software system to process all the captured
numbers, and issue a ticket for all the cars that violate the law. An image processing module has already preprocessed the video recordings and generated a file contianing the recorded car numbers. You are requested to write the ticketing module . The problem is that the image processing module is not perfect, and some car numbers are wrong.

A true car number should meet all of the following requirements:

It is 8 characters long.
The two leftmost characters are identical digits between 1 to 9, which indicate in which city the car number is issued.
The following two characters are two digits between 1 to 9.
The following character is a capital English letter.
The three rightmost characters are also digits between 1 to 9.

Input format:
The input consists of multiple test cases so the first line of the input is the number of test cases.
The first line of each test case contains the number of captured car numbers (n) that are reported by the image processing module
In each of the next n lines , there are exactly 8 numerical or English alphabetical characters, showing one inferred car number.

Output format:
You should report the car numbers that have violated the law, one in each line, in the same order that they appear in the input. If the same car number has voilated the law multiple times, all of the violation cases should be reported . The wrong car numbers, which do not meet one or more of the above requirements,
should not be listed in the Output

Sample Output:
1
5
8835R551
4352S132
2241X223
55123456
9914t521

Sample Output:

8835R551
2241X223
