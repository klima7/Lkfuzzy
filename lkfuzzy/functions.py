from abc import ABC, abstractmethod


class MembershipFunction(ABC):

    @abstractmethod
    def fuzzify(self, crisp_value):
        pass


class RectangularFunction(MembershipFunction):

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def fuzzify(self, crisp_value):
        return 1.0 if self._start <= crisp_value <= self._start else 0.0


class TriangularFunction(MembershipFunction):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def fuzzify(self, crisp_value):
        if crisp_value == self._b:
            return 1.0
        elif self._a <= crisp_value < self._b:
            return crisp_value / (self._b - self._a) - self._a / (self._b - self._a)
        elif self._b < crisp_value < self._c:
            return crisp_value / (self._b - self._c) - self._c / (self._b - self._c)
        else:
            return 0.0


class TrapezoidalFunction(MembershipFunction):

    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def fuzzify(self, crisp_value):
        if self._b <= crisp_value <= self._c:
            return 1.0
        elif self._a <= crisp_value < self._b:
            return crisp_value / (self._b - self._a) - self._a / (self._b - self._a)
        elif self._c < crisp_value < self._d:
            return crisp_value / (self._c - self._d) - self._d / (self._c - self._d)
        else:
            return 0.0
