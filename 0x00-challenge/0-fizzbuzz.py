#!/usr/bin/python3
""" FizzBuzz5
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """

    if n < 1:
        return

    modulo_list = [
        (3, "Fizz"),
        (5, "Buzz")
    ]

    tmp_result = []

    for i in range(1, 101):
        print_string = ""
        for mod in modulo_list:
            if i % mod[0] == 0:
                print_string += mod[1]
        if print_string == "":
            tmp_result.append(str(i))
        else:
            tmp_result.append(print_string)

    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
