from ..puzzles import day9
import pytest


class TestDay9:
    @pytest.mark.parametrize(('sequence', 'length'),
        zip([input for input in day9.txt_opener('/../inputs/day9_1_test.txt', '\n')],
        (6, 7, 9, 11, 6, 18)))
    def test_examples(self, sequence, length):
        assert len(day9.decompressor(sequence)) == length

    def test_decompressor(self):
        assert day9.decompressor('PyTest') == 'PyTest'
        assert day9.decompressor('A_(1x1)Test') == 'A_Test'
        assert day9.decompressor('A_(2x2)Te(2x2)st') == 'A_TeTestst'
        assert day9.decompressor('A_(4x2)Test') == 'A_TestTest'

    def test_part1(self):
        assert day9.part1('/../inputs/day9_final.txt') == 112830

    @pytest.mark.parametrize(('filename', 'result'), [('/../inputs/day9_final.txt', 10931789799),
        ('/../inputs/day9_2_test1.txt', 9), ('/../inputs/day9_2_test2.txt', 20),
        ('/../inputs/day9_2_test3.txt', 241920), ('/../inputs/day9_2_test4.txt', 445)])
    def test_part2(self, filename, result):
        assert day9.part2(filename) == result
