#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        # player = EntityFactory.get_entity('Player1')
        # player.score = player_score[0]
        # self.entity_list.append(player)
        # if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
        #     player = EntityFactory.get_entity('Player2')
        #     player.score = player_score[1]
        #     self.entity_list.append(player)
        # pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        # pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # 100ms

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
