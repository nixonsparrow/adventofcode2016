from ..puzzles import day20
import pytest

@pytest.mark.ignored
class TestDay20:

    def test_part1(self):
        assert 2 == 2
        assert day20.part1('/../inputs/day20_test.txt') == 1
        assert day20.part1('/../inputs/day20_final.txt') == 1

    def test_part2(self):
        assert 2 == 2
        assert day20.part2('/../inputs/day20_test.txt') == 1
        assert day20.part2('/../inputs/day20_final.txt') == 1
