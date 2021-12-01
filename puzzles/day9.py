from os import path


def txt_opener(input_file):
    return list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))


def decompressor(file):
    dec_file = file
    return dec_file


def part1(input_file=''):
    final_input = txt_opener(input_file)
    decompressed_file = decompressor(final_input)
    return len(decompressed_file)


def part2(input_file=''):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    return False


if __name__ == '__main__':
    print([input for input in txt_opener('/../inputs/day9_test.txt')])
