```python
#!/usr/bin/python3
""" FizzBuzz
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

    result_list = []
    for idx in range(1, n + 1):
        if (idx % 3) == 0 and (idx % 5) == 0:
            result_list.append("FizzBuzz")
        elif (idx % 3) == 0:
            result_list.append("Fizz")
        elif (idx % 5) == 0:
            result_list.append("Buzz")
        else:
            result_list.append(str(idx))
    print(" ".join(result_list))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    num = int(sys.argv[1])
    fizzbuzz(num)
