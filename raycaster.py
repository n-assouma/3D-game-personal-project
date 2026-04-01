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

        '''
        map_x, map_y — current grid cell (integers)
        step_x, step_y — +1 or -1 per axis
        dist_x, dist_y — distance along the ray to the next vertical/horizontal boundary
        delta_x, delta_y — the fixed increment to add each step (1 / ray_dir)
        '''
        map_x, map_y = int(ray_pos[0]), int (ray_pos[1])

        step_x = 1 if ray_dir[0] > 0 else -1
        step_y = 1 if ray_dir[1] > 0 else -1

        next_x = map_x + 1 if step_x > 0 else map_x
        dist_x = (next_x - ray_pos[0]) / ray_dir[0] if ray_dir[0] != 0 else float('inf')

        next_y = map_y + 1 if step_y > 0 else map_y
        dist_y = (next_y - ray_pos[1]) / ray_dir[1] if ray_dir[1] != 0 else float('inf')

        delta_x = 1 / ray_dir[0] if ray_dir[0] != 0 else float('inf')
        delta_y = 1 / ray_dir[1] if ray_dir[1] != 0 else float('inf')

        hit_wall = False
        while not hit_wall:
            '''
            Compare dist_x vs dist_y to decide which boundary to step to
            Advance map_x or map_y by step_x or step_y
            Add delta_x or delta_y to dist_x or dist_y
            Check is_wall(map_x, map_y)
            '''
            if dist_x < dist_y:
                map_x += step_x 
                dist_x += delta_x
                side = 'x'
            else:
                map_y += step_y
                dist_y += delta_y
                side = 'y'
                
            hit_wall = self._map.is_wall(map_x, map_y)

        #compute distance
        if side == 'x':
            distance = dist_x - delta_x
        elif side == 'y':
            distance = dist_y - delta_y

        self._distances.append(distance) 

    def cast_all_rays(self) -> list:
        self._distances = []
        for screen_pixel_column in range(SCREEN_WIDTH):
            self._cast_ray(screen_pixel_column)
        
        return self._distances
