
if __name__ == '__main__':
    for day in range(10, 26):
        with open(f'test_day{day}.py', 'w+') as the_day:
            the_day.write(f'from ..puzzles import day{day}\n'
                          f'import pytest\n'
                          f'\n@pytest.mark.ignored\n'
                          f'class TestDay{day}:\n\n'
                          f'{" "*4}def test_part1(self):\n{" "*8}assert 2 == 2\n'
                          f"{' '*8}assert day{day}.part1('/../inputs/day{day}_test.txt') == 1\n"
                          f"{' '*8}assert day{day}.part1('/../inputs/day{day}_final.txt') == 1\n\n"
                          f'{" "*4}def test_part2(self):\n{" "*8}assert 2 == 2\n'
                          f"{' '*8}assert day{day}.part2('/../inputs/day{day}_test.txt') == 1\n"
                          f"{' '*8}assert day{day}.part2('/../inputs/day{day}_final.txt') == 1\n")
