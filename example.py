from lkfuzzy import *

food = InputVariable('food', range=[0, 10])
service = InputVariable('service', range=[0, 10])

food['good'] = TriangularFunction(5, 10, 10)
food['medium'] = TriangularFunction(0, 5, 10)
food['bad'] = TriangularFunction(0, 0, 5)

service['good'] = TriangularFunction(5, 10, 10)
service['medium'] = TriangularFunction(0, 5, 10)
service['bad'] = TriangularFunction(0, 0, 5)

rules = [
    Rule(food['good'] & service['good'], 15),
    Rule(food['bad'] & service['bad'], 0),
]

system = FuzzySystem(rules)
tip = system.compute(food=10, service=20)
print(f"Tip should be {tip}%")
