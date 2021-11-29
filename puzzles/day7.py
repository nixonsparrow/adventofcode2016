def check_word_for_abba(a_word):
    a_list = a_word if type(a_word) == list else list(a_word)
    for i in range(1, len(a_list) - 2):
        if a_list[i] == a_list[i + 1] and a_list[i - 1] == a_list[i + 2] and a_list[i] != a_list[i - 1]:
            return True
    return False


def is_ip7_address_valid_tls(address):
    words_in_brackets = []
    words_outside_brackets = []
    temp_word = []

    for char in address:
        if char not in ['[', ']']:
            temp_word.append(char)
            continue
        elif char == '[':
            words_outside_brackets.append(temp_word)
            temp_word = []
        elif char == ']':
            words_in_brackets.append(temp_word)
            temp_word = []
    words_outside_brackets.append(temp_word)

    if any([x for x in words_in_brackets if check_word_for_abba(x)]):
        return None
    return [x for x in words_outside_brackets if check_word_for_abba(x)]


def is_ip7_address_valid_ssl(address):
    pass


def part1(input_file=''):
    final_input = list(map(str, open(input_file).read().split('\n')))
    valid_addresses = [ip7address for ip7address in final_input if is_ip7_address_valid_tls(ip7address)]
    return len(valid_addresses)


def part2(input_file=''):
    final_input = list(map(str, open(input_file).read().split('\n')))
    valid_addresses = [ip7address for ip7address in final_input if is_ip7_address_valid_ssl(ip7address)]
    return 'Finish day 7, please'
