from map import Map
from player import Player
from raycaster import Raycaster
from renderer import Renderer
from settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
import sys


class Game():
    def __init__(self):
        #instantiate all component class
        self._map = Map()
        self._player = Player(self._map)
        self._raycaster = Raycaster(self._map, self._player)
        #initialise all modules
        pygame.init()
        #initialise the screen
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('3D map using raycasting')
        #initialise renderer
        self._renderer = Renderer(pygame.display.get_surface())
        #initialise clock
        self._clock = pygame.time.Clock()
        self._running = True

    def run(self) -> None:
        #handle game loop
        while self._running:
            #set fps limit
            self._clock.tick(FPS)
            #handle_input
            self._handle_input()
            # update game state
            game_output = self._update()
            # draw screen
            self._draw(game_output)
            print(self._clock.get_fps())
            pygame.display.flip()

        self.exit()
    '''
    Issue, only move the player once even though a key is still pressed down.
    SHould go back to claude chat to see event.get_pressed function
    '''
    def _handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

        key_pressed = pygame.key.get_pressed()
        #pressed key is ...match movement
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            self._player.move('F')
        elif key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            self._player.move('B')
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            self._player.move('R')
        elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            self._player.move('L')

    def _update(self) -> list:
        #update game state
        #call raycaster
        return self._raycaster.cast_all_rays()
        

    def _draw(self, update_output: list) -> None:
        #call renderer
        self._renderer.draw(update_output)

    def exit(self) -> None:
        pygame.quit()
        sys.exit()
