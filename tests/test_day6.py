from ..puzzles import day6


class TestDay6:

    def test_part1(self):
        assert day6.part1('inputs/day6_1_test.txt') == 'easter'

    def test_part2(self):
        assert day6.part2('inputs/day6_final.txt') == 'evakwaga'
