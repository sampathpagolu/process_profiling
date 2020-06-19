*******************************************************************************
#           Advanced Operating Systems Design, CS5352 - Project 1             #
#                   Author: Lakshmi Sampath Somanath Pagolu                   #
#                         Email ID: lpagolu@ttu.edu                           #
********************************************************************************
Please note that this script was created in a Windows 10 machine.
Running this on a different OS may lead to errors.
--------------------------------------------------------------------------------
command line arguments
--------------------------------------------------------------------------------
*RUN THIS PROGRAM ON A WINDOWS 10 MACHINE and check the required libraries below*
*RUN THIS IN COMMAND PROMPT*
 ______________________________________________________________________________
|                                                                              |
| 1. p1_pagolu h - "To display Readme file"                                    |
| 2. p1_pagolu positive_number algorithm_option - "To run the algorithms"      |
|______________________________________________________________________________|
option 1 [positive Number]:
The algorithms find the number of prime numbers in the range of 1 to the user's
choice
option 1 is users choice: ending number in the range

option 2 [algorithm_option]:
  1. n - naive implementation
  2. s - sieve of Eratosthenes
  3. b - both at the same time

examples:
  1. p1_pagolu 1000 n
     Calculates number of prime numbers in the range(1,1000) using naive 
     implementation and saves the graph in pictures folder
  2. p1_pagolu 1000 b
     Calculates number of prime numbers using both algorithmsin the range(1,1000) by
     taking advantage of multiprocessing and saves both graphs in pictures folder
  3. p1_pagolu h
     Displays the Readme file on screen
--------------------------------------------------------------------------------
Required python version: 3.8.1
required python libraries:
  1. OS
  2. psutil
  3. matplotlib
  4. multiprocessing
--------------------------------------------------------------------------------
 Algorithms: Finding number of prime numbers from 1 to the number taken as input
--------------------------------------------------------------------------------
Algorithm 1: Naive implementation
  - If the integer is less than equal to 1, it returns False.
  - If the number is equal to 2, it will return True. If the number is greater
      than 2 and divisible by 2,
  - then it will return False. Now, we have checked all the even numbers.
  - Now, look for the odd numbers. If the given number is divisible by any of
      the numbers
  - from 3 to the square root of the number skipping all the even numbers,
  - the function will return False Else it will return True
--------------------------------------------------------------------------------
Algorithm 2: Sieve of Eratosthenes
  - Create a boolean array prime[0..n] and initialize all entries it as true.
  - Updates all multiples of a number as false\n"
  - A value in prime[i] will finally be false if i is Not a prime, else true.
--------------------------------------------------------------------------------
Design:
 _________________     ___________________
|   prime1.py     |   |   prime2.py       |
|    Naive        |   |    Sieve of       |
| implementation  |   |  Eratosthenes     |
|   Algorithm 1   |   |  Algorithm 2      |
|_________________|   |___________________|
            \               /
       	_____\_____________/____
       |project1.py             |
       |import prime1           |
       |import prime2           |
       |________________________|
From the command line user can choose which algorithm to run.
Running algorithms separately just calls the isPrime function in the respective
file. But running both at the same time is a challenge. To achieve this python
library multiprocessing is used. In that Process class is used to create
separate process for each algorithm. Multi threading can also be used but due to
GIL in python, multi threading was avoided.
Comparison of the algorithms is printed when both of the algorithms are run at
the same time i.e. when 'b' is chosen. The efficiency comes different each time
as multiprocessing is being used.
________________________________________________________________________________
