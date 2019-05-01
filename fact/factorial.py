#!/usr/bin/env python3

x = int(input("Enter a number: "))
f = 1
for i in range(1, x):
    f = f * i
print(x, '! = ', f)

