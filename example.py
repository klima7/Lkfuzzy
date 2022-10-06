from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np

from lkfuzzy import *


def main():
    food = InputVariable('food', range=[0, 10])
    service = InputVariable('service', range=[0, 10])

    food['bad'] = TriangularFunction(0, 0, 5)
    food['medium'] = TriangularFunction(0, 5, 10)
    food['good'] = TriangularFunction(5, 10, 10)

    service['bad'] = TriangularFunction(0, 0, 5)
    service['medium'] = TriangularFunction(0, 5, 10)
    service['good'] = TriangularFunction(5, 10, 10)

    rules = [
        Rule(food['bad'] & service['bad'], 0),
        Rule(food['good'] & service['good'], 20),
        Rule(food['medium'], 10),
        Rule(food['bad'] & service['good'], 10),
        Rule(food['good'] & service['bad'], 5),
    ]

    system = FuzzySystem(rules)

    test_on_examples(system)
    draw_heatmap(system)


def test_on_examples(system):
    Example = namedtuple('example', 'food service')

    examples = [
        Example(10, 10),
        Example(4, 4),
        Example(0, 0),
        Example(10, 0),
        Example(0, 10),
        Example(2, 6),
        Example(6, 2),
    ]

    for example in examples:
        tip = system.compute(food=example.food, service=example.service)
        print(f'food: {example.food:2}/10, service: {example.service:2}/10 -> tip: {tip:.1f}%')


def draw_heatmap(system):
    resolution = 20
    food_values = np.linspace(0, 10, resolution)
    service_values = np.linspace(0, 10, resolution)

    food_grid, service_grid = np.meshgrid(food_values, service_values)
    tip_grid = np.zeros_like(food_grid)
    for food_index in range(resolution):
        for service_index in range(resolution):
            food_value = food_values[food_index]
            service_value = service_values[service_index]
            tip_grid[food_index, service_index] = system.compute(food=food_value, service=service_value)

    fig, ax = plt.subplots()
    cp = ax.contourf(service_grid, food_grid, tip_grid, 200)

    ax.set_xlabel('Service quality')
    ax.set_ylabel('Food quality')
    ax.set_title('Tip values')
    ax.grid()
    fig.colorbar(cp, label='Tip in percents')
    fig.show()


if __name__ == '__main__':
    main()
