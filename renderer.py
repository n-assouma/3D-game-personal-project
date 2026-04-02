import pygame
import sys
from settings import (
    SCREEN_HEIGHT,   
    FLOOR_COLOR, 
    CEILING_COLOR, 
    WALL_COLOR,
    MAX_DISTANCE_FOR_SHADING
)

'''Taking a distance of 1 unit in our initial 10x10 grid as a reference
to a wall height of 50%
DIstance of 1      --> 50% of screen height
Distance from wall --> ?
'''
COEFF = SCREEN_HEIGHT * 0.5
class Renderer:
    def __init__(self, screen: pygame.Surface):
        self._screen = screen

    def _shader(self, distance: float) -> tuple:
        shade = max(0, 1 - distance/MAX_DISTANCE_FOR_SHADING)
        shaded_wall_color = (
            int(WALL_COLOR[0] * shade), 
            int(WALL_COLOR[1] * shade), 
            int(WALL_COLOR[2] * shade)
        ) 
        return shaded_wall_color
    
    def _draw_wall(self, screen_pixel_column: int,
                    screen_row: int, wall_size: float,
                    distance: float) -> None:
        pygame.draw.line(
            self._screen,
            self._shader(distance), #color of the wall and shadow
            (screen_pixel_column, screen_row),
            (screen_pixel_column, screen_row + int(wall_size) + 1),
            width=1
        )

    def _draw_ceiling(self, screen_pixel_column: int, ceiling_len: float) -> None:
        pygame.draw.line(
            self._screen,
            CEILING_COLOR,
            (screen_pixel_column, 0),
            (screen_pixel_column, ceiling_len),
            width=1
        )

    def _draw_floor(self, screen_pixel_column: int, floor_len: float) -> None:
        pygame.draw.line(
            self._screen,
            FLOOR_COLOR,
            (screen_pixel_column, SCREEN_HEIGHT - 1),
            (screen_pixel_column, SCREEN_HEIGHT - int(floor_len)),
            width=1
        )

        
        #we have an issue with the use of hte loop and the argument of functions called
    def draw(self, distances_to_wall: list) -> None:
        #clean the screen with white
        self._screen.fill((255, 255, 255))

        #for each cloumn of pixel
        for column, distance in enumerate(distances_to_wall):
            #compute wall size and floor and ceiling size
            try:
                size = COEFF / distance 
            except ZeroDivisionError:
                print('Error: Player spawn on wall. Change player initial spawning position')
                pygame.quit()
                sys.exit(1)
            wall_size = size if size < SCREEN_HEIGHT else SCREEN_HEIGHT
            wall_start_row = floor_and_ceiling_len = (SCREEN_HEIGHT - wall_size) / 2
            #call draw wall, ceiling and floor passing wall size and index of the column
            self._draw_ceiling(column, floor_and_ceiling_len)
            self._draw_wall(column, int(wall_start_row), wall_size, distance)
            self._draw_floor(column, floor_and_ceiling_len)
    