from ..puzzles import day5
import pytest


class TestDay5:

    @pytest.mark.longrun
    def test_part1(self):
        assert day5.door_breaker('abc') == '18f47a30'
        assert day5.part1('cxdnnyjw') == 'f77a0e6e'

    @pytest.mark.longrun
    def test_part2(self):
        assert day5.door_breaker('abc', advanced=True) == '05ace8e3'
        assert day5.part2('cxdnnyjw') == '999828ec'
