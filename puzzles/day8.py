import re
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


def rotate(line, rotation, screen):

    row = ''.join(str(int(x)) for x in list(screen[line])) * 2
    row = row[- len(screen[line]) - rotation:-rotation]
    for i in range(len(screen[0])):
        screen[line][i] = row[i]
    return screen


def command_rotate(direction, line, rotation, screen):

    if direction == 'x':
        line = len(screen[0]) - line - 1
        screen = np.rot90(screen, k=1)

    elif not direction == 'y':
        raise ValueError('Wrong direction!')

    screen = rotate(line, rotation, screen)

    return np.rot90(screen, k=3) if direction == 'x' else screen


def command_rect(width, height, screen):
    for hei in range(height):
        for wid in range(width):
            screen[hei][wid] = 1

    return screen


def advent_commander(cmd, screen):
    if cmd.startswith('rect'):          # ie. rect 3x2
        width, height = cmd[5:].split('x')
        screen = command_rect(int(width), int(height), screen)

    elif cmd.startswith('rotate'):      # ie. rotate row y=0 by 4
        line = int(re.findall(r'=\d+', cmd)[0].replace('=', ''))
        rotation = int(re.findall(r' \d+', cmd)[0])
        direction = 'x' if ' x=' in cmd else 'y'
        screen = command_rotate(direction, line, rotation, screen)

    return screen


def count_lights(screen):
    return int(np.sum(screen))


def part1(input_file, screen_width=50, screen_height=6):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))

    screen = np.zeros((screen_height, screen_width))
    for command in final_input:
        screen = advent_commander(command, screen)
    return count_lights(screen)


def part2(input_file, screen_width=50, screen_height=6):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))

    screen = np.zeros((screen_height, screen_width))
    print(screen_visualisation(screen))
    for command in final_input:
        screen = advent_commander(command, screen)
        print(screen_visualisation(screen))

    return screen_visualisation(screen)


if __name__ == '__main__':
    part2('/../inputs/day8_test.txt', 7, 3)
