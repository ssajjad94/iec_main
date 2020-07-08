# -*- coding: utf-8 -*-





class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def printname(self):
        print(self._name, self._age)
        
p1 = Person("Sajjad", 26)

print(p1._name)
print(p1._age)

# p1.printname()

class Account:
    def __init__(self, name, balance):
        self.name = name
        if balance < 0:
            raise ValueError("Cannot be less than zero")
        self.balance = balance
        
    def my_balance(self):
        print(f"Balance is {self.balance}")
        
        