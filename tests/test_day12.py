from ..puzzles import day12
import pytest

@pytest.mark.ignored
class TestDay12:

    def test_part1(self):
        assert 2 == 2
        assert day12.part1('/../inputs/day12_test.txt') == 1
        assert day12.part1('/../inputs/day12_final.txt') == 1

    def test_part2(self):
        assert 2 == 2
        assert day12.part2('/../inputs/day12_test.txt') == 1
        assert day12.part2('/../inputs/day12_final.txt') == 1
