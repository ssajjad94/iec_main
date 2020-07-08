# -*- coding: utf-8 -*-

import printbar as pb
import decimal


pb.printbar()

s = "My name is Sajjad"
x = 99.45678

print(f"{s}")

pb.printbar()

print(f"|{s:>25}|")
print(f"|{s:<25}|")
print(f"|{s:^25}|")

pb.printbar()

print(f"|{s:.>25}|")
print(f"|{s:.<25}|")
print(f"|{s:.^25}|")

pb.printbar()

print(f"|x = {x:25.2f}|")