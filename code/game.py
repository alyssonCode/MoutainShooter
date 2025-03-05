#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame  # É necessário importar o pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # Comando para iniciar o pygame
        self.window = pygame.display.set_mode(size=(600, 480))  # Inserir uma janela para exibição

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



            # # Verifica todos os eventos da janela
            # for event in pygame.event.get():  # A variável event vai pegar todos os eventos com "pygame.event.get()"
            #     if event.type == pygame.QUIT:
            #         # Como quero pegar um evento específico,
            #         # setei para pegar apenas o fechamento de janela
            #         # com a variável "QUIT" presente no pygame
            #         pygame.quit()  # Quando o "QUIT" ocorrer é para dar o comando "pygame.quit()", fechar janela
            #         quit()  # Deve ainda, sair do pygame, como o "quit()"





