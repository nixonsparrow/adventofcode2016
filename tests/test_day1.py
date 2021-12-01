from ..puzzles import day1


class TestDay1:
    def test_bunny_jumper(self):
        assert day1.bunny_jumper(['L4']) == 4
        assert day1.bunny_jumper(['L4'], full_course=False) == 4
        assert day1.bunny_jumper(['R4', 'L5', 'L1', 'L3']) == 5
        assert day1.bunny_jumper(['L4', 'L4', 'L2', 'L6']) == 4
        assert day1.bunny_jumper(['L4', 'L4', 'L2', 'L6'], full_course=False) == 2

    def test_ultimate_bunny_jumper(self):
        assert day1.bunny_jumper([f'L{x}' for x in range(999)]) == 999
        assert day1.bunny_jumper([f'{"R" if x%2==0 else "L"}{x}' for x in range(999)]) == 498501

    def test_part1(self):
        assert day1.part1('/../inputs/day1_1_test1.txt') == 5
        assert day1.part1('/../inputs/day1_1_test2.txt') == 2
        assert day1.part1('/../inputs/day1_1_test3.txt') == 12
        assert day1.part1('/../inputs/day1_final.txt') == 146

    def test_part2(self):
        assert day1.part2('/../inputs/day1_2_test1.txt') == 4
        assert day1.part2('/../inputs/day1_final.txt') == 131
