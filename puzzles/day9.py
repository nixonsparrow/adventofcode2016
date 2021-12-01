import re
from os import path


def txt_opener(input_file):
    the_list = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    return the_list if len(the_list) > 1 else the_list[0]


def command_executor(sequence):
    processed_sequence = sequence
    return processed_sequence


def decompressor(old_sequence):
    new_sequence = ''
    i = 0
    while i < len(old_sequence):
        if old_sequence[i] != '(':
            new_sequence += old_sequence[i]
            i += 1
        else:
            command = re.search(r'\d+x\d+', old_sequence[i:]).group()
            cmd_length, length, multiplier = len(command) + 2, int(command.split('x')[0]), int(command.split('x')[1])
            new_sequence += old_sequence[sum((i, cmd_length)): sum((i, cmd_length, length))] * multiplier
            i += cmd_length + length

    return new_sequence


def part1(input_file=''):
    final_input = txt_opener(input_file)
    decompressed_file = decompressor(final_input)
    return len(decompressed_file)


def part2(input_file=''):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    return False


if __name__ == '__main__':
    print(decompressor('A(1x5)BC'))
