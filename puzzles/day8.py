from os import path
import numpy as np


def screen_visualisation(screen):
    visualisation = '\n'

    for row in screen:
        for number in row:
            if number == 1:
                visualisation += '#'
            elif number == 0:
                visualisation += '.'
            else:
                raise ValueError
        visualisation += '\n'
    return visualisation


def part1(input_file, screen_width=50, screen_height=6):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))

    # screen = [[0 for col in range(screen_width)] for row in range(screen_height)]  # clean Python approach
    screen = np.zeros((screen_height, screen_width))
    # print(screen)
    # print(screen_visualisation(screen))
    for command in final_input:
        print(command)
    return None


def part2(input_file):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    return None


if __name__ == '__main__':
    part1('/../inputs/day8_test.txt')
