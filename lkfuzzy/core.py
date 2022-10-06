from .nodes import VariableNode


class InputVariable:

    def __init__(self, name, range):
        self._name = name
        self._range = range
        self._functions = {}

    def __getitem__(self, item):
        mf = self._functions[item]
        return VariableNode(self, mf)

    def __setitem__(self, key, value):
        self._functions['key'] = value

    def is_within_range(self, crisp_value):
        return self._range[0] <= crisp_value <= self._range[1]


class Rule:

    def __init__(self, a, b):
        pass


class FuzzySystem:

    def __init__(self, rules):
        pass

    def compute(self, **inputs):
        pass
