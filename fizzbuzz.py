#!/usr/bin/env python
import sys


def is_multiple_of_3(n):
    pass


def is_multiple_of_5(n):
    pass


def is_fizz_buzz(n):
    """
    if n is multiple of 3 returns 'Fizz'
    if n is multiple of 5 returns 'Buzz'
    if n is multiple of 3 and 5 returns 'FizzBuzz'
    """
    fizz_buzz_string = ""
    return fizz_buzz_string


def print_usage():
    usage_string = "Usage: fizzbuzz.py n\n Check if the integer 'n' is a multple of 3, 5 or 3 and 5 prints Fizz, Buzz or FizzBuzz respectively. "
    print(usage_string)


def main():
    try:
        n = int(sys.argv[1])
        print(is_fizz_buzz(n))
    except:
        print_usage()


if __name__ == "__main__":
    main()
