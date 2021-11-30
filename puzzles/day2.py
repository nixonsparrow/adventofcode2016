from os import path


def bathroom_keypad_clicker(moves_sequences, letters=False):
    if not letters:
        keypad = ((7, 8, 9),
                  (4, 5, 6),
                  (1, 2, 3))
    else:
        keypad = ((0, 0, 'D', 0, 0),
                (0, 'A', 'B', 'C', 0),
                   (5, 6, 7, 8, 9),
                   (0, 2, 3, 4, 0),
                   (0, 0, 1, 0, 0))

    current_position = [1, 1] if not letters else [2, 0]
    code = ''

    def get_digit(position=tuple(current_position)):
        return keypad[position[0]][position[1]]

    for moves_sequence in moves_sequences:
        for move in moves_sequence:

            if not letters:   # PART 1 MOVEMENT
                if move == 'U' and current_position[0] < 2:
                    current_position[0] += 1
                elif move == 'D' and current_position[0] > 0:
                    current_position[0] -= 1
                elif move == 'L' and current_position[1] > 0:
                    current_position[1] -= 1
                elif move == 'R' and current_position[1] < 2:
                    current_position[1] += 1

            else:             # PART 2 MOVEMENT
                old_position = tuple(current_position)
                if move == 'U' and current_position[0] < 4:
                    current_position[0] += 1
                    current_position = current_position if get_digit(current_position) != 0 else list(old_position)
                elif move == 'D' and current_position[0] > 0:
                    current_position[0] -= 1
                    current_position = current_position if get_digit(current_position) != 0 else list(old_position)
                elif move == 'L' and current_position[1] > 0:
                    current_position[1] -= 1
                    current_position = current_position if get_digit(current_position) != 0 else list(old_position)
                elif move == 'R' and current_position[1] < 4:
                    current_position[1] += 1
                    current_position = current_position if get_digit(current_position) != 0 else list(old_position)

        code += str(get_digit(current_position))

    return code


def part1(input_file=''):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    return bathroom_keypad_clicker(final_input)


def part2(input_file=''):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    return bathroom_keypad_clicker(final_input, letters=True)
