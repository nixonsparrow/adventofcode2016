import numpy as np


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


def is_triangle(triangle):
    x, y, z = int(triangle[0]), int(triangle[1]), int(triangle[2])
    if x < (y+z) and y < (x+z) and z < (x+y):
        return True
    return False


def get_room_value(room):
    return int(room.split('-')[-1][:3])


def is_room_real(room):
    import string
    encrypted_name = ''.join(room.split('-')[:-1])

    # visualisation of checksum: {'a': 5, 'b': 3, 'c': 1, ...}
    checksum = {x: encrypted_name.count(x) for x in room[-6:-1]}

    # check if there are more frequent letters than mentioned in checksum
    for char in string.ascii_lowercase:
        if encrypted_name.count(char) > checksum[list(checksum.keys())[-1]] \
                and char not in checksum.keys():
            return False
    # print('HERE!', checksum, list(checksum.keys())[-1])

    # check if total is in descending order
    sequence = [checksum[x] for x in checksum]
    if not all(earlier >= later for earlier, later in zip(sequence, sequence[1:])):
        return False

    # check if there are same totals -> if so, check alphabetical order
    while len(sequence) > 1:
        total_to_compare = sequence[0]
        tied_characters = [char for char in checksum if checksum[char] == total_to_compare]
        if ''.join(tied_characters) not in ''.join(checksum):
            return False
        if all(previous_char < next_char for previous_char, next_char in zip(tied_characters, tied_characters[1:])):
            for i in range(len(tied_characters)):
                del sequence[0]
        else:
            return False

    return True


def caesar_decrypter(code_with_id):
    import string
    alphabet = string.ascii_lowercase * 2
    caesar_key = int(code_with_id.split('-')[-1]) % 26
    encrypted_password = code_with_id.split('-')[:-1]

    password = ''
    for word in encrypted_password:
        if encrypted_password.index(word) != 0:
            password += ' '
        for char in word:
            password += (alphabet[alphabet.index(char) + caesar_key])
    return password


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
def day3_1(input_file=''):
    all_sets = np.loadtxt(input_file)

    return sum([1 for tri in all_sets if is_triangle(tri)])


def day3_2(input_file=''):
    all_sets = np.loadtxt(input_file)

    def find_triangles(np_array):
        np_array.sort(axis=-1)
        return sum(np.sum(np_array[:, :2], axis=-1) > np_array[:, 2])

    return find_triangles(all_sets.T.reshape(-1, 3))


def day4_1(input_file=''):
    all_rooms = list(map(str, open(input_file).read().split('\n')))
    id_total_sum = sum([get_room_value(ax) for ax in all_rooms if is_room_real(ax)])
    return id_total_sum


def day4_2(input_file=''):
    all_codes = list(map(str, open(input_file).read().split('\n')))
    for code in all_codes:
        password = caesar_decrypter(code[:-7])
        if 'north' in password and 'pole' in password:
            return int(code.split('-')[-1][:3])

    return None


if __name__ == '__main__':
    print(caesar_decrypter('qzmt-zixmtkozy-ivhz-343'))
    print(day4_2('inputs/day4_final.txt'))
