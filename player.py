import map
from math import cos, sin, tan, sqrt, trunc, pi 
from settings import FOV, FPS, PLAYER_SPEED, PLAYER_ROT_SPEED

ANGLE = (PLAYER_ROT_SPEED * pi) / 180
ANGLE_COS = cos(ANGLE)
ANGLE_SIN = sin(ANGLE)
'''
Left rotation matrix:  | ANGLE_COS  ANGLE_SIN |
                       |-ANGLE_SIN  ANGLE_COS |

Right rotation matrix: | ANGLE_COS -ANGLE_SIN |
                       | ANGLE_SIN  ANGLE_COS | 
'''
STEP_SIZE = PLAYER_SPEED / FPS #SPEED per frame


class Player():
    def __init__(self, game_map: map.Map):
        self._map = game_map
        self._position = (5, 5) #initial position
        self._direction = (0, -1) #player initialy look toward top of screen
        CAMERA_PLAN_LENGHT = tan((FOV * pi)/360) # basically tan (FOV in rad / 2)
        self._camera_plane = (CAMERA_PLAN_LENGHT, 0) 

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
        new_x_pos = self._position[0] + self._direction[0] * STEP_SIZE
        new_y_pos = self._position[1] + self._direction[1] * STEP_SIZE

        if not self._map.is_wall(trunc(new_x_pos), trunc(new_y_pos)):
            self._position = (
                new_x_pos,
                new_y_pos,
            )

    def _move_backward(self) -> None:
        new_x_pos = self._position[0] - self._direction[0] * STEP_SIZE
        new_y_pos = self._position[1] - self._direction[1] * STEP_SIZE
        if not self._map.is_wall(trunc(new_x_pos), trunc(new_y_pos)):
            self._position = (
                new_x_pos,
                new_y_pos,
            )

    def _rotate_left(self) -> None:
        self._direction = (
            self._direction[0] *  ANGLE_COS - self._direction[1] *  ANGLE_SIN,
            self._direction[0] * -ANGLE_SIN - self._direction[1] *  ANGLE_COS
        )
        self._update_camera_plan()

    def _rotate_right(self) -> None:
        self._direction = (
            self._direction[0] *  ANGLE_COS - self._direction[1] * -ANGLE_SIN,
            self._direction[0] *  ANGLE_SIN - self._direction[1] *  ANGLE_COS
        )
        self._update_camera_plan()
    
    def _update_camera_plan(self):
        #FOrcing the dot product of the direction vector and camera plan to be 0
        #Also maintaining camera plan module constant and equal to camera lenght
        pass