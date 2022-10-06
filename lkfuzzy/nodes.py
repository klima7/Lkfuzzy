from abc import ABC, abstractmethod

from lkfuzzy.exceptions import *


class Node(ABC):

    @abstractmethod
    def evaluate(self, inputs):
        pass

    def __and__(self, other):
        return AndNode(self, other)

    def __or__(self, other):
        return OrNode(self, other)


class OrNode(Node):

    def __init__(self, left, right):
        self._left = left
        self._right = right

    def evaluate(self, inputs):
        left_result = self._left.evaluate(inputs)
        right_result = self._right.evaluate(inputs)
        return max(left_result, right_result)


class AndNode(Node):

    def __init__(self, left, right):
        self._left = left
        self._right = right

    def evaluate(self, inputs):
        left_result = self._left.evaluate(inputs)
        right_result = self._right.evaluate(inputs)
        return min(left_result, right_result)


class VariableNode(Node):

    def __init__(self, var, mf):
        self._var = var
        self._mf = mf

    def evaluate(self, inputs):
        crisp_value = self._get_crisp_value(inputs)
        fuzzy_value = self._mf.fuzzify(crisp_value)
        return fuzzy_value

    def _get_crisp_value(self, inputs):
        if self._var.name not in inputs.keys():
            raise InputVariableNotPassedException

        crisp_value = inputs[self._var.name]

        if not self._var.is_within_range(crisp_value):
            raise InputVariableOutOfRangeException

        return crisp_value
