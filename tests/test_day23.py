from ..puzzles import day23
import pytest

@pytest.mark.ignored
class TestDay23:

    def test_part1(self):
        assert 2 == 2
        assert day23.part1('/../inputs/day23_test.txt') == 1
        assert day23.part1('/../inputs/day23_final.txt') == 1

    def test_part2(self):
        assert 2 == 2
        assert day23.part2('/../inputs/day23_test.txt') == 1
        assert day23.part2('/../inputs/day23_final.txt') == 1
