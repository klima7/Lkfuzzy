from .nodes import VariableNode


class InputVariable:

    def __init__(self, name, range):
        self.name = name
        self.range = range
        self._mfs = {}

    def __getitem__(self, item):
        mf = self._mfs[item]
        return VariableNode(self, mf)

    def __setitem__(self, key, value):
        self._mfs[key] = value

    def is_within_range(self, crisp_value):
        return self.range[0] <= crisp_value <= self.range[1]


class Rule:

    def __init__(self, premise, output):
        self.premise = premise
        self.output = output

    def evaluate(self, inputs):
        return self.premise.evaluate(inputs)


class FuzzySystem:

    def __init__(self, rules):
        self.rules = rules

    def compute(self, **inputs):
        numerator = 0
        denominator = 0

        for rule in self.rules:
            weight = rule.evaluate(inputs)
            numerator += weight * rule.output
            denominator += weight

        return numerator / denominator
