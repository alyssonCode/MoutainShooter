#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame  # É necessário importar o pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # Comando para iniciar o pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Inserir uma janela para exibição

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass








