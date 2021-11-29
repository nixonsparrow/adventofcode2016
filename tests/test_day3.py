from ..puzzles import day3


class TestDay3:

    def test_part1(self):
        assert day3.is_triangle([5, 15, 19]) is True
        assert day3.is_triangle([5, 15, 25]) is False
        assert day3.part1('inputs/day3_final.txt') == 983

    def test_part2(self):
        assert day3.part2('inputs/day3_2_test.txt') == 6
        assert day3.part2('inputs/day3_final.txt') == 1836
