import pytest
import numpy as np
from ..puzzles import day08


class TestDay8:
    def test_screen_visualisation(self):
        assert '\n.#\n#.\n' == day08.screen_visualisation([[0, 1], [1, 0]])
        assert '\n##\n##\n' == day08.screen_visualisation([[1, 1], [1, 1]])
        assert '\n..\n.\n' == day08.screen_visualisation([[0, 0], [0]])

        assert '\n' + f'{"."*50}\n' * 6 == day08.screen_visualisation(np.zeros((6, 50)))

        with pytest.raises(ValueError):
            day08.screen_visualisation([[0, 0], [0, 2]])

        with pytest.raises(ValueError):
            day08.screen_visualisation([[0, 0], [0, 'x']])

    @pytest.mark.parametrize(('lights', 'counted'), [([[0, 1, 0, 0, 1, 0, 1]], 3),
                             ([[0, 0], [0, 0]], 0), ([[[1, 0] for x in range(50)]], 50)])
    def test_count_lights(self, lights, counted):
        assert day08.count_lights(lights) == counted

    def test_cmd_rectangle(self):
        assert day08.command_rect(2, 2, [[0, 0, 0], [0, 0, 0]]) == [[1, 1, 0], [1, 1, 0]]
        assert day08.command_rect(1, 1, [[0, 0, 0], [0, 0, 0]]) == [[1, 0, 0], [0, 0, 0]]

    def test_cmd_rotate(self):
        assert day08.rotate(0, 2, [[0, 1, 0, 0, 1, 0, 1]]) == [['0', '1', '0', '1', '0', '0', '1']]
        assert day08.command_rotate('y', 0, 2, [[0, 1, 0, 0, 1, 0, 1]]) == [['0', '1', '0', '1', '0', '0', '1']]

    def test_part1(self):
        assert day08.part1('/../inputs/day8_test.txt', 7, 3) is 6
        assert day08.part1('/../inputs/day8_final.txt') is 106

    def test_part2(self):
        assert day08.part2('/../inputs/day8_final.txt') == '''
.##..####.#....####.#.....##..#...#####..##...###.
#..#.#....#....#....#....#..#.#...##....#..#.#....
#....###..#....###..#....#..#..#.#.###..#....#....
#....#....#....#....#....#..#...#..#....#.....##..
#..#.#....#....#....#....#..#...#..#....#..#....#.
.##..#....####.####.####..##....#..#.....##..###..
'''
