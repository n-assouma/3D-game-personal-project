#Digital differential analyzer
from map import Map

from player import Player
from settings import SCREEN_WIDTH 

class Raycaster():
    def __init__(self, map: Map, player: Player):
        self._map = map
        self._player = player
        self._distances = []

    def _cast_ray(self, screen_column_index: int) -> None:
        '''Cast on ray corresponding to a column of pixels on the screen
          at rendering time. append the distance of the player to a wall'''
        #compute the ray direction vector
        camera_offset = (2 * screen_column_index / SCREEN_WIDTH) - 1 #range from -1 to 1
        ray_dir = (
            self._player.direction[0] + self._player.camera_plane[0] * camera_offset,
            self._player.direction[1] + self._player.camera_plane[1] * camera_offset
        )
        #initalise step_x, step_y, next_x, next_y, ray_ps_x ray_posy
        ray_pos = self._player.position

        #current grid boundary coordordonate, just initialize map
        map_x, map_y = int(ray_pos[0]), int(ray_pos[1]) 

        next_x = map_x + 1 if ray_dir[0] > 0 else map_x # next horizontal boundary 
        next_y = map_y + 1 if ray_dir[1] > 0 else map_y # next vertical boundary

        #number of step to next horizontal boundary
        step_x = (next_x - ray_pos[0]) / ray_dir[0] if ray_dir[0] else float('inf')
        #number of step to next vertical boundary
        step_y = (next_y - ray_pos[1]) / ray_dir[1] if ray_dir[1] else float('inf')
        side = 0

        hit_wall = False
        while not hit_wall:
            if step_x < step_y:    
                side = 'x'
                map_x += 1 if ray_dir[0] > 0 else -1 #update grid boundary coordonate
            else:
                side = 'y'
                map_y += 1 if ray_dir[1] > 0 else -1 #update grid boundary coordonate
            
            if self._map.is_wall(map_x, map_y):
                hit_wall = True
            elif side == 'x':
                next_x += 1 if ray_dir[0] > 0 else -1
                step_x = (next_x - ray_pos[0]) / ray_dir[0]
            elif side == 'y':
                next_y += 1 if ray_dir[1] > 0 else -1
                step_y = (next_y - ray_pos[1]) / ray_dir[1]
        
        #compute distance from ray to horizontal boundary and vertical boundary
        if side == 'x':
            dist_x = step_x * ray_dir[0]
            dist_y = step_x * ray_dir[1]
        else:
            dist_x = step_y * ray_dir[0]
            dist_y = step_y * ray_dir[1]

        #compute distance
        distance = (dist_x**2 + dist_y**2) ** 0.5 
        self._distances.append(distance) 

    def cast_all_rays(self) -> list:
        self._distances = []
        for screen_pixel_column in range(SCREEN_WIDTH):
            self._cast_ray(screen_pixel_column)
        
        return self._distances
