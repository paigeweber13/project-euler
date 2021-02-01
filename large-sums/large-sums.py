#!/usr/bin/python3

with open('numbers', 'r') as f:
    sum = 0
    for line in f:
        sum += int(line)
    print(sum)

