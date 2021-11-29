from ..puzzles import day5


class TestDay5:

    #           IF COMMENTED OUT IT'S DUE TO LONG COMPUTING TIME  |  EXCHANGEABLE TO SKIPIF LATER
    def test_part1(self):
        assert day5.door_breaker('abc') == '18f47a30'
        assert day5.part1('cxdnnyjw') == 'f77a0e6e'
        pass

    #           IF COMMENTED OUT IT'S DUE TO LONG COMPUTING TIME  |  EXCHANGEABLE TO SKIPIF LATER
    def test_part2(self):
        assert day5.door_breaker('abc', advanced=True) == '05ace8e3'
        assert day5.part2('cxdnnyjw') == '999828ec'
        pass
