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
            self.handle_input()
            # update game state
            game_output = self.update()
            # draw screen
            self.draw(game_output)

        self.exit()

    '''
    Issue, only move the player once even though a key is still pressed down.
    SHould go back to claude chat to see event.get_pressed function
    '''
    def handle_input(self) -> None:
        for event in pygame.event.get():
        #mathc the input to  the player movement
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP):
                    self._player.move('F')

                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    self._player.move('L')

                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    self._player.move('R')

                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    self._player.move('B')

            elif event.type == pygame.QUIT:
                self._running = False


    def update(self) -> list:
        #update game state
        #call raycaster
        return self._raycaster.cast_all_rays()
        

    def draw(self, update_output: list) -> None:
        #call renderer
        self._renderer.draw(update_output)

    def exit(self) -> None:
        pygame.quit()
        sys.exit()
