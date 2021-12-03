from ..puzzles import day10
import pytest


class TestDay10:

    def test_part1(self):
        assert day10.part1('/../inputs/day10_test.txt', (3, 5)) == 0
        assert day10.part1('/../inputs/day10_final.txt', (61, 17)) == 2

    @pytest.mark.ignored
    def test_part2(self):
        assert day10.part2('/../inputs/day10_test.txt') == 2
        assert day10.part2('/../inputs/day10_final.txt') == 2
