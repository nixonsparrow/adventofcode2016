from os import path


def clear_signal_from_noise(signal_list, modified_repetition_code=False):
    old_array = [x for x in signal_list]
    new_array = []
    for x in range(len(old_array[0])):  # create array rotated by 90 - easier to search for letter
        new_array.append([word[x] for word in old_array])

    if modified_repetition_code:        # get least common letter for each index
        return ''.join([min(char_list, key=char_list.count) for char_list in new_array])
    else:                               # get most common letter for each index
        return ''.join([max(char_list, key=char_list.count) for char_list in new_array])


def part1(input_file=''):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    return clear_signal_from_noise(final_input)


def part2(input_file=''):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    return clear_signal_from_noise(final_input, modified_repetition_code=True)
