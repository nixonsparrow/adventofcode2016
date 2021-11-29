def door_breaker(door_id, advanced=False):
    import hashlib

    password = [x for x in '_' * 8]     # ['_', '_', '_', '_', '_', '_', '_', '_']
    i = 0
    while '_' in password:
        next_code = ''.join([door_id, str(i)])
        next_hash = hashlib.md5(next_code.encode())
        if next_hash.hexdigest().startswith('00000'):
            if advanced:
                _hash = next_hash.hexdigest()
                if _hash[5].isdigit() and -1 < int(_hash[5]) < 8:
                    _index = int(_hash[5])
                    if password[_index] == '_':
                        password[_index] = _hash[6]
            else:
                password[password.index('_')] = next_hash.hexdigest()[5]
        i += 1

    return ''.join(password)


def part1(code=''):
    return door_breaker(code)


def part2(code=''):
    return door_breaker(code, advanced=True)
