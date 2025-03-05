import pygame # É necessário importar o pygame

pygame.init() # Comando para iniciar o pygame

window = pygame.display.set_mode(size=(600, 480)) # Inserir uma janela para exibição
print('Set End') # print que vai aparecer no terminal, para termos controle do que está ocorrendo

print('Loop Start') # print que vai aparecer no terminal, para termos controle do que está ocorrendo

while True:
    # Verifica todos os eventos da janela

    for event in pygame.event.get(): # A variável event vai pegar todos os eventos com "pygame.event.get()"
        if event.type == pygame.QUIT:
            # Como quero pegar um evento específico,
            # setei para pegar apenas o fechamento de janela
            # com a variável "QUIT" presente no pygame
            print('Quitting...') # print teste
            pygame.quit() # Quando o "QUIT" ocorrer é para dar o comando "pygame.quit()", fechar janela
            quit() # Deve ainda, sair do pygame, como o "quit()"




