#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        fibonacci_list = []
    elif length == 1:
        fibonacci_list = [0]
    else:
        fibonacci_list = [0, 1]
        for i in range(length - 2):
            num = fibonacci_list[i] + fibonacci_list[i + 1]
            fibonacci_list.append(num)
    print(fibonacci_list)
