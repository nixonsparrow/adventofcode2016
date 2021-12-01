import re
from os import path


def txt_opener(input_file):
    the_list = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    return the_list if len(the_list) > 1 else the_list[0]


def decompressor(old_sequence, count_max=False):
    new_sequence = '' if not count_max else [1 for _ in old_sequence]
    algorithm_sum = 0
    i = 0
    while i < len(old_sequence):
        if old_sequence[i] != '(':
            if not count_max:
                new_sequence += old_sequence[i]
            else:
                algorithm_sum += new_sequence[i]
            i += 1
        else:
            command = re.search(r'\d+x\d+', old_sequence[i:]).group()
            cmd_length, length, multiplier = len(command) + 2, int(command.split('x')[0]), int(command.split('x')[1])

            if not count_max:
                new_sequence += old_sequence[sum((i, cmd_length)): sum((i, cmd_length, length))] * multiplier
                i += cmd_length + length
            else:
                for char in range(sum([i, cmd_length]), sum([i, cmd_length, length])):
                    new_sequence[char] *= multiplier
                i += cmd_length

    return new_sequence if not count_max else algorithm_sum


def part1(input_file=''):
    final_input = txt_opener(input_file)
    decompressed_file = decompressor(final_input)
    return len(decompressed_file)


def part2(input_file=''):
    final_input = txt_opener(input_file)
    result = decompressor(final_input, count_max=True)
    return result


if __name__ == '__main__':
    print(decompressor('X(8x2)(3x3)ABCY', count_max=True))
