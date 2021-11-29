from ..puzzles import day1


class TestDay1:

    def test_part1(self):
        assert day1.part1('/../inputs/day1_1_test1.txt') == 5
        assert day1.part1('/../inputs/day1_1_test2.txt') == 2
        assert day1.part1('/../inputs/day1_1_test3.txt') == 12
        assert day1.part1('/../inputs/day1_final.txt') == 146

    def test_part2(self):
        assert day1.part2('/../inputs/day1_2_test1.txt') == 4
        assert day1.part2('/../inputs/day1_final.txt') == 131
