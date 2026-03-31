import map
from math import cos, sin, tan, trunc, pi 
from settings import FOV, FPS, PLAYER_SPEED, PLAYER_ROT_SPEED

ANGLE = (PLAYER_ROT_SPEED * pi) / 180
ANGLE_COS = cos(ANGLE)
ANGLE_SIN = sin(ANGLE)
'''
Left rotation matrix:  | ANGLE_COS  ANGLE_SIN |
                       |-ANGLE_SIN  ANGLE_COS |

Right rotation matrix: | ANGLE_COS -ANGLE_SIN |
                       | ANGLE_SIN  ANGLE_COS | 
by uing a signed angle, we can easy switch from right to left matrix
rotate(ANGLE) //Right matrix
rotate(-ANGLE) //LEFT matrix
'''
STEP_SIZE = PLAYER_SPEED / FPS #SPEED per frame
CAMERA_PLAN_LENGHT = tan((FOV * pi)/360) # basically tan (FOV in rad / 2)

class Player():
    def __init__(self, game_map: map.Map):
        self._map = game_map
        self._position = (5, 5) #initial position
        self._direction = (0, -1) #player initialy look toward top of screen
        self._camera_plane = (CAMERA_PLAN_LENGHT, 0) 

    @property
    def position(self):
        return self._position
    
    @property
    def direction(self):
        return self._direction
    
    @property
    def camera_plane(self):
        return self._camera_plane

    def move(self, user_input: str) -> None:
        match user_input:
            case 'F':
                self._move_forward()
            case 'B':
                self._move_backward()
            case 'L':
                self._rotate_FOV(user_input)
            case 'R':
                self._rotate_FOV(user_input)

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

    #rotate direction vector and camera plan at the same time
    def _rotate_FOV(self, direction) -> None:
        match direction:
            case 'R':
                self._direction    =  (
                    self._direction[0] *  ANGLE_COS + self._direction[1] * -ANGLE_SIN,
                    self._direction[0] *  ANGLE_SIN + self._direction[1] *  ANGLE_COS
                )
                self._camera_plane =  (
                    self._camera_plane[0] *  ANGLE_COS + self._camera_plane[1] * -ANGLE_SIN,
                    self._camera_plane[0] *  ANGLE_SIN + self._camera_plane[1] *  ANGLE_COS
                )
            case 'L':
                self._direction = (
                    self._direction[0] *  ANGLE_COS + self._direction[1] *  ANGLE_SIN,
                    self._direction[0] * -ANGLE_SIN + self._direction[1] *  ANGLE_COS
                )
                self._camera_plane =  (
                    self._camera_plane[0] *  ANGLE_COS + self._camera_plane[1] *  ANGLE_SIN,
                    self._camera_plane[0] * -ANGLE_SIN + self._camera_plane[1] *  ANGLE_COS
                )
