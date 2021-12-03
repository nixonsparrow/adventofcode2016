from ..puzzles import day02


class TestDay2:

    def test_part1(self):
        assert day02.part1('/../inputs/day2_test.txt') == '1985'
        assert day02.part1('/../inputs/day2_final.txt') == '98575'

    def test_part2(self):
        assert day02.part2('/../inputs/day2_test.txt') == '5DB3'
        assert day02.part2('/../inputs/day2_final.txt') == 'CD8D4'
