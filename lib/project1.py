from multiprocessing import Process, Manager
import os
from matplotlib import pyplot as plt
import sys
from prime1 import isPrime_0 as N
from prime2 import isPrime_1 as S


class PrimeNumbers:
    def __init__(self):
        self.time_dict = {}

    def naive_implementation(self, end):

        N(end, self.time_dict)


    def sieve_of_eratosthenes(self, end):
        return S(end, self.time_dict)

    @staticmethod
    def both_at_the_same_time(end):
        time_dict = Manager().dict()
        P1 = Process(target=N, args=(end, time_dict))
        P2 = Process(target=S, args=(end, time_dict))
        P1.start()
        # print('naive', P1.pid)
        P2.start()
        # print('sieve', P2.pid)
        P1.join()
        P2.join()
        efficiency = (time_dict['sieve']/time_dict['naive']) * 100
        print(f'The efficiency of the second algorithm is {round(efficiency, 3)}% over first algorithm')


if __name__ == '__main__':
    # print(" ____________________________________________________________________________________________________________________\n"
    #       "|Please note that this script was created in a Windows 10 machine.Running this in a different OS may lead to errors.|\n"
    #       " ____________________________________________________________________________________________________________________\n")
    # Algorithms: Finding number of prime numbers from 1 to the number taken as input\n"
    # "___________________________________________________________________________________________________________\n"
    # "Algorithm 1: Naive implementation\n\n"
    # "- If the integer is less than equal to 1, it returns False.\n"
    # "- If the number is equal to 2, it will return True. If the number is greater than 2 and divisible by 2,\n"
    # "- then it will return False. Now, we have checked all the even numbers.\n"
    # "- Now, look for the odd numbers. If the given number is divisible by any of the numbers\n"
    # "- from 3 to the square root of the number skipping all the even numbers,\n"
    # "- the function will return False Else it will return True\n"
    # "___________________________________________________________________________________________________________\n"
    # "Algorithm 2: Sieve of Eratosthenes\n\n"
    # "- Create a boolean array prime[0..n] and initialize all entries it as true.\n"
    # "- Updates all multiples of a number as false\n"
    # "- A value in prime[i] will finally be false if i is Not a prime, else true.\n"
    # "_____________________________________________________________________________________________________________")

    p = PrimeNumbers()
    # print(os.getpid())
    while True:
        try:
            # end = int(input("Starting number: 1 \nEnter an ending number: "))
            # print("Starting number: 1 \nEnter an ending number: ")
            end = int(''.join(sys.argv[1:2]))
        except ValueError:
            print("Enter only a number for the range \n"
                  "Enter 'project1 h' to read Readme file")
            exit()

        else:
            break


    n = ''.join(sys.argv[2:])


    if n == 'n':
        p.naive_implementation(end)
    elif n == 's':
        p.sieve_of_eratosthenes(end)
    elif n == 'b':
        p.both_at_the_same_time(end)
    else:
        print("Please enter a correct option \n"
              "Enter 'project1 h' to read Readme file")
