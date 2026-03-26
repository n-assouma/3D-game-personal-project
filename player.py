import map
from math import cos, sin, pi 
from settings import PLAYER_ROT_SPEED


class Player():
    def __init__(self, game_map: map.Map):
        self._map = game_map
        self._position = (5, 5) #initial position
        self._direction = (0, -1) #player initialy look toward top of screen
        self._camera_plane = ...

    def move(self, user_input) -> None:
        match user_input:
            case 'F':
                self._move_forward()
            case 'B':
                self._move_backward()
            case 'L':
                self._rotate_left()
            case 'R':
                self._rotate_right()

    def _move_forward(self) -> None:
        self._position = (
            self._position[0] + self._direction[0],
            self._position[1] + self._direction[1]
        )

    def _move_backward(self) -> None:
        self._position = (
            self._position[0] - self._direction[0],
            self._position[1] - self._direction[1]
        )

    def _rotate_left(self) -> None:
        self._direction = (
            self._direction[0] *  ANGLE_COS - self._direction[1] *  ANGLE_SIN,
            self._direction[0] * -ANGLE_SIN - self._direction[1] *  ANGLE_COS
        )

    def _rotate_right(self) -> None:
        self._direction = (
            self._direction[0] *  ANGLE_COS - self._direction[1] * -ANGLE_SIN,
            self._direction[0] *  ANGLE_SIN - self._direction[1] *  ANGLE_COS
        )

ANGLE = (PLAYER_ROT_SPEED * pi) / 180
ANGLE_COS = cos(ANGLE)
ANGLE_SIN = sin(ANGLE)
'''
Left rotation matrix:  | ANGLE_COS  ANGLE_SIN |
                       |-ANGLE_SIN  ANGLE_COS |

Right rotation matrix: | ANGLE_COS -ANGLE_SIN |
                       | ANGLE_SIN  ANGLE_COS | 
'''
