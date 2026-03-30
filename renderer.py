import pygame
from settings import (
    SCREEN_HEIGHT,   
    FLOOR_COLOR, 
    CEILING_COLOR, 
    WALL_COLOR
)

'''Taking a distance of 1 unit in our initial 10x10 grid as a reference
to a wall height of 80%
DIstance of 1      --> 80% of screen height
Distance from wall --> ?
'''
COEFF = SCREEN_HEIGHT * 0.8
class Renderer:
    def __init__(self, screen: pygame.Surface):
        self._screen = screen

    def _draw_wall(self, screen_pixel_column: int,
                    screen_row: int, wall_size: float) -> None:
        pygame.draw.line(
            self._screen,
            WALL_COLOR,
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
            wall_size = COEFF / distance 
            wall_start_row = floor_and_ceiling_len = (SCREEN_HEIGHT - wall_size) / 2
            #call draw wall, ceiling and floor passing wall size and index of the column
            self._draw_ceiling(column, floor_and_ceiling_len)
            self._draw_wall(column, int(wall_start_row), wall_size)
            self._draw_floor(column, floor_and_ceiling_len)
    