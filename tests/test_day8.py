import pytest
import numpy as np
from ..puzzles import day8


class TestDay8:
    def test_screen_visualisation(self):
        assert '\n.#\n#.\n' == day8.screen_visualisation([[0, 1], [1, 0]])
        assert '\n##\n##\n' == day8.screen_visualisation([[1, 1], [1, 1]])
        assert '\n..\n.\n' == day8.screen_visualisation([[0, 0], [0]])

        assert '\n' + f'{"."*50}\n'*6 == day8.screen_visualisation(np.zeros((6, 50)))

        with pytest.raises(ValueError):
            day8.screen_visualisation([[0, 0], [0, 2]])

        with pytest.raises(ValueError):
            day8.screen_visualisation([[0, 0], [0, 'x']])

    def test_count_lights(self):
        day8.count_lights([[0, 1, 0, 0, 1, 0, 1]])

    def test_cmd_rectangle(self):
        assert day8.command_rect(2, 2, [[0, 0, 0], [0, 0, 0]]) == [[1, 1, 0], [1, 1, 0]]
        assert day8.command_rect(1, 1, [[0, 0, 0], [0, 0, 0]]) == [[1, 0, 0], [0, 0, 0]]

    def test_cmd_rotate(self):
        assert day8.rotate(0, 2, [[0, 1, 0, 0, 1, 0, 1]]) == [['0', '1', '0', '1', '0', '0', '1']]
        assert day8.command_rotate('y', 0, 2, [[0, 1, 0, 0, 1, 0, 1]]) == [['0', '1', '0', '1', '0', '0', '1']]

    def test_part1(self):
        assert day8.part1('/../inputs/day8_test.txt', 7, 3) is 6
        assert day8.part1('/../inputs/day8_final.txt') is 106

    def test_part2(self):
        assert day8.part2('/../inputs/day8_final.txt') == '''
.##..####.#....####.#.....##..#...#####..##...###.
#..#.#....#....#....#....#..#.#...##....#..#.#....
#....###..#....###..#....#..#..#.#.###..#....#....
#....#....#....#....#....#..#...#..#....#.....##..
#..#.#....#....#....#....#..#...#..#....#..#....#.
.##..#....####.####.####..##....#..#.....##..###..
'''
