from ..puzzles import day2


class TestDay2:

    def test_part1(self):
        assert day2.part1('inputs/day2_test.txt') == '1985'
        assert day2.part1('inputs/day2_final.txt') == '98575'

    def test_part2(self):
        assert day2.part2('inputs/day2_test.txt') == '5DB3'
        assert day2.part2('inputs/day2_final.txt') == 'CD8D4'
