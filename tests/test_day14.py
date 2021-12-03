from ..puzzles import day14
import pytest

@pytest.mark.ignored
class TestDay14:

    def test_part1(self):
        assert 2 == 2
        assert day14.part1('/../inputs/day14_test.txt') == 1
        assert day14.part1('/../inputs/day14_final.txt') == 1

    def test_part2(self):
        assert 2 == 2
        assert day14.part2('/../inputs/day14_test.txt') == 1
        assert day14.part2('/../inputs/day14_final.txt') == 1
