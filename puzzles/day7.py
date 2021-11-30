from os import path


def check_sequence_for_abba(sequence):
    a_list = sequence if type(sequence) == list else list(sequence)     # initially sequence can be either a string or a list
    for i in range(1, len(a_list) - 2):
        if a_list[i] == a_list[i + 1] and a_list[i - 1] == a_list[i + 2] and a_list[i] != a_list[i - 1]:
            return True
    return False


def search_sequence_for_aba(sequence, letters=None):         # letters come as a trio ie. 'aba'
    a_list = sequence if type(sequence) == list else list(sequence)     # initially sequence can be either a string or a list
    possible_abas = []

    if letters:
        if len(letters) != 3 or letters[0] == letters[1]:
            return False
        else:
            if letters in ''.join(a_list):
                return True
        return False

    for i in range(1, len(a_list) - 1):
        if a_list[i - 1] == a_list[i + 1] and a_list[i] != a_list[i - 1]:
            try:
                possible_abas.append(''.join(a_list[i - 1: i + 2]))
            except IndexError:
                possible_abas.append(''.join(a_list[i - 1:]))

    return possible_abas


def is_ip7_address_valid(address, protocol='tls'):
    if protocol not in ['tls', 'ssl']:
        raise AttributeError('Protocol needs to be set: TLS/SSL')

    sequences_inside_brackets = []
    sequences_outside_brackets = []
    temp_word = []

    for char in address:
        if char not in ['[', ']']:
            temp_word.append(char)
            continue
        elif char == '[':
            sequences_outside_brackets.append(temp_word)
            temp_word = []
        elif char == ']':
            sequences_inside_brackets.append(temp_word)
            temp_word = []
    sequences_outside_brackets.append(temp_word)        # append also last sequence

    if protocol == 'tls':
        if any([seq for seq in sequences_inside_brackets if check_sequence_for_abba(seq)]):
            return []
        return [seq for seq in sequences_outside_brackets if check_sequence_for_abba(seq)]

    elif protocol == 'ssl':
        for seq_outside in sequences_outside_brackets:
            possible_abas = search_sequence_for_aba(seq_outside)
            for aba in possible_abas:
                bab = ''.join([aba[1], aba[0], aba[1]])
                for seq_inside in sequences_inside_brackets:
                    if search_sequence_for_aba(seq_inside, letters=bab):
                        return True

    return False


def part1(input_file=''):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    valid_addresses = [ip7address for ip7address in final_input if is_ip7_address_valid(ip7address)]
    return len(valid_addresses)


def part2(input_file=''):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).read().split('\n')))
    valid_addresses = [ip7address for ip7address in final_input if is_ip7_address_valid(ip7address, protocol='ssl')]
    return len(valid_addresses)


if __name__ == '__main__':
    # part2('/../inputs/day7_2_test.txt')
    print(search_sequence_for_aba('aba'))
    print(search_sequence_for_aba('ababa'))
    print(search_sequence_for_aba('zbasa'))
    print(is_ip7_address_valid('aba[aaa]asaaa', protocol='ssl'))
