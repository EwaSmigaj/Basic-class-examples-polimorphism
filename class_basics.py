
import math
from abc import abstractmethod


class SquareFunc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_roots(self):
        if self.a == 0 and self.b == 0:
            if self.c == 0:
                return math.inf, math.inf
            else:
                return float("nan"), float("nan")
        if self.a != 0:
            delta = self.b**2 - 4*self.a*self.c
            if delta < 0:
                return float("nan"), float("nan")
            if delta == 0:
                return (-self.b)/2*self.a
            if delta > 0:
                return (-self.b - math.sqrt(delta))/2*self.a, (-self.b + math.sqrt(delta))/2*self.a

    def display_func(self):
        print(f"{self.a}x^2+{self.b}x+{self.c}")
        print("root(s): ", self.find_roots())


class ComplexNumb:
    def __init__(self, r, i):
        self.i = i
        self.r = r

    def __add__(self, other):
        return self.r + other.r, self.i + other.i

    def __sub__(self, other):
        return self.r - other.r, self.i - other.i

    def __mul__(self, other):
        return self.r*other.r - self.i*other.i, self.r*other.i - self.i*other.r

    def module(self):
        return math.sqrt(self.i**2 + self.r**2)


class Animal:
    def __init__(self, name, av_life_exp, av_weight):
        self.name = name
        self.av_life_exp = av_life_exp
        self.av_weigh = av_weight

    @abstractmethod
    def group_name(self):
        pass

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species_name()}")
        print(f"Average life expectancy: {self.av_life_exp}")
        print(f"Average weight: {self.av_weigh}")

    def say_hi(self):
        print(f"{self.name} say's hi!")


class Mammal(Animal):
    def __init__(self, name, av_life_exp, av_weight, is_marsupial):
        super().__init__(name, av_life_exp, av_weight)
        self.is_marsupial = is_marsupial

    def group_name(self):
        return "Mammal"

    def print_info(self):
        super().print_info()
        if self.is_marsupial is True:
            print("Specification: Marsupial")


class Bird(Animal):
    def __init__(self, name, av_life_exp, av_weight, wingspan):
        super().__init__(name, av_life_exp, av_weight)
        self.wingspan = wingspan

    def group_name(self):
        return "Bird"

    def print_info(self):
        super().print_info()
        print(f"Wingspan: {self.wingspan}")








