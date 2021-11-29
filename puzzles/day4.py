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
    alphabet = string.ascii_lowercase * 2       # double whole alphabet to avoid Index Errors
    caesar_key = int(code_with_id.split('-')[-1]) % 26
    encrypted_password = code_with_id.split('-')[:-1]

    password = ''
    for word in encrypted_password:
        password += ' ' if encrypted_password.index(word) != 0 else ''
        for char in word:
            password += (alphabet[alphabet.index(char) + caesar_key])
    return password


def part1(input_file=''):
    all_rooms = list(map(str, open(input_file).read().split('\n')))
    id_total_sum = sum([get_room_value(ax) for ax in all_rooms if is_room_real(ax)])
    return id_total_sum


def part2(input_file=''):
    all_codes = list(map(str, open(input_file).read().split('\n')))
    for code in all_codes:
        password = caesar_decrypter(code[:-7])
        if 'north' in password and 'pole' in password:
            return int(code.split('-')[-1][:3])

    return None
