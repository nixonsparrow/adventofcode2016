def bunny_jumper(bunny_path, full_course=True):
    # ------------------------------ starting variables
    directions = ['N', 'E', 'S', 'W']
    direction = directions[0]
    position = [0, 0]
    positions_already_visited = []

    for segment in bunny_path:
        steps = int(segment[1:])

        # ------------------------------ turn
        if 'R' in segment:
            try:
                direction = directions[directions.index(direction) + 1]
            except IndexError:
                direction = directions[0]
        elif 'L' in segment:
            try:
                direction = directions[directions.index(direction) - 1]
            except IndexError:
                direction = directions[-1]

        # ------------------------------ move
        # PART 1

        for step in range(steps):
            current_position = tuple(position)

            if not full_course:
                if current_position not in positions_already_visited:
                    positions_already_visited.append(current_position)
                else:
                    break

            if direction == 'N':
                position[0] += 1
            elif direction == 'S':
                position[0] -= 1
            elif direction == 'E':
                position[1] += 1
            elif direction == 'W':
                position[1] -= 1

    # ------------------------------ calculate distance
    distance = sum((abs(position[0]), abs(position[1])))
    return distance


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


### PUZZLES MAIN
# -------------------------- day 1
def day1_1(input_file=''):
    final_input = list(map(str, open(input_file).readline().replace(' ', '').split(',')))
    return bunny_jumper(final_input)


def day1_2(input_file=''):
    final_input = list(map(str, open(input_file).readline().replace(' ', '').split(',')))
    return bunny_jumper(final_input, full_course=False)


# -------------------------- day 2
def day2_1(input_file=''):
    final_input = list(map(str, open(input_file).read().split('\n')))
    return bathroom_keypad_clicker(final_input)


def day2_2(input_file=''):
    final_input = list(map(str, open(input_file).read().split('\n')))
    return bathroom_keypad_clicker(final_input, letters=True)


# -------------------------- day 3


if __name__ == '__main__':
    print(day2_2('inputs/day2_final.txt'))

