from ..puzzles import day06


class TestDay6:

    def test_part1(self):
        assert day06.part1('/../inputs/day6_test.txt') == 'easter'
        assert day06.part1('/../inputs/day6_final.txt') == 'wkbvmikb'

    def test_part2(self):
        assert day06.part2('/../inputs/day6_test.txt') == 'advent'
        assert day06.part2('/../inputs/day6_final.txt') == 'evakwaga'
