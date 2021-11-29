from ..puzzles import day7


class TestDay7:

    def test_part1(self):
        assert day7.check_word_for_abba('aaaa') is False
        assert day7.check_word_for_abba('abba') is True
        assert day7.check_word_for_abba(list('jabbak')) is True
        assert day7.part1('inputs/day7_1_test.txt') == 2
        assert day7.part1('inputs/day7_final.txt') == 105

    def test_part2(self):
        assert day7.part2('inputs/day7_2_test.txt') == 3
