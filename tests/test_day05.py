from ..puzzles import day05
import pytest


class TestDay5:
    pytestmark = pytest.mark.ignored

    def test_part1(self):
        assert day05.door_breaker('abc') == '18f47a30'
        assert day05.part1('cxdnnyjw') == 'f77a0e6e'

    def test_part2(self):
        assert day05.door_breaker('abc', advanced=True) == '05ace8e3'
        assert day05.part2('cxdnnyjw') == '999828ec'
