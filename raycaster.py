'''
Comments to myself for when I resume.
CLaude pointed out the edge case when ray_dir[0] or [1] is 0 when 
it is used for division, ahould add safe guard.
Also need to implement cast all to be done with that file'''

#Digital differential analyzer
from map import Map

from player import Player
from settings import SCREEN_WIDTH 

class Raycaster():
    def __init__(self, map: Map, player: Player):
        self._map = map
        self._player = player
        self._distances = []

    def cast_ray(self, screen_column_index: int) -> None:
        '''Cast on ray corresponding to a column of pixels on the screen
          a rendering time. append the distance of the player to a wall'''
        #compute the ray direction vector
        camera_offset = (2 * screen_column_index / SCREEN_WIDTH) - 1 #range from -1 to 1
        ray_dir = (
            self._player.direction[0] + self._player.camera_plane[0] * camera_offset,
            self._player.direction[1] + self._player.camera_plane[1] * camera_offset
        )
        #initalise step_x, step_y, next_x, next_y, ray_ps_x ray_posy
        ray_pos = self._player.position

        #logic loop
        hit_wall = False
        while not hit_wall:
            next_x = int(ray_pos[0] + 1) if ray_dir[0] > 0 else int(ray_pos[0] - 1)
            next_y = int(ray_pos[1] + 1) if ray_dir[1] > 0 else int(ray_pos[1] - 1)
            step_x = (next_x - ray_pos[0]) / ray_dir[0]
            step_y = (next_y - ray_pos[1]) / ray_dir[1]

            #if ray reach vertical boundary
            if step_x < step_y:
                #update ray position
                ray_pos = (
                    ray_pos[0] + step_x * ray_dir[0],
                    ray_pos[1] + step_x * ray_dir[1]
                )
            #else (ray reach horizontal noundary)
            else:
                ray_pos = (
                    ray_pos[0] + step_y * ray_dir[0],
                    ray_pos[1] + step_y * ray_dir[1]
                )                
            #check if it is a wall (reurn it to hit wall variable directly)
            hit_wall = self._map.is_wall(int(ray_pos[0]), int(ray_pos[1]))
        #compute distance
        distance = ((ray_pos[0] - self._player.position[0])**2 + 
                    (ray_pos[1] - self._player.position[1])**2) ** 0.5 
        self._distances.append(distance)