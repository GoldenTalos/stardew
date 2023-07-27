import pygame
from settings import *


class Overlay:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player

        self.tools_surf = {tool:surface for tool in player.tool}
        self.seeds_surf = {}
