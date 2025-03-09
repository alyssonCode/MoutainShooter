#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_ORANGE, MENU_OPTION, C_YELLOW, C_WHITE, WIN_WIDTH


class Menu:
    def __init__(self, window):
        # Inicializa a classe Menu com a janela do jogo (window)
        self.window = window

        # Carrega a imagem de fundo do menu (MenuBg.png) para o atributo surf
        self.surf = pygame.image.load('./asset/MenuBg.png')  # importar a imagem
        # Obtém o retângulo da superfície (imagem), com a posição de topo e esquerda definidas para 0
        self.rect = self.surf.get_rect(left=0, top=0)  # Define a posição da imagem no topo esquerdo da tela

    def run(self, menu_option=None):

        pygame.mixer_music.load('./asset/Menu.mp3')  # importar a música
        pygame.mixer_music.play(-1)  # tocar a música o -1 é para ela ficar em loop

        while True:

            # Desenha a imagem carregada na janela do jogo, usando a posição definida por rect
            self.window.blit(source=self.surf, dest=self.rect) # a ordem aqui é muito importe, se inverter não aparece o texto

            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70)) # Escreve o títuto do jogo
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120)) # Escreve o títuto do jogo

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Atualiza a tela para refletir as mudanças
            pygame.display.flip()

        # Verifica todos os eventos da janela
            for event in pygame.event.get():  # A variável event vai pegar todos os eventos com "pygame.event.get()"
                if event.type == pygame.QUIT:
                    # Como quero pegar um evento específico,
                    # setei para pegar apenas o fechamento de janela
                    # com a variável "QUIT" presente no pygame
                    pygame.quit()  # Quando o "QUIT" ocorrer é para dar o comando "pygame.quit()", fechar janela
                    quit()  # Deve ainda, sair do pygame, como o "quit()"

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

