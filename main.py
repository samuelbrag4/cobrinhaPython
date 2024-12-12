# Jogo feito com Python - Jogo da Cobrinha (Snake Game)

# Biblioteca utilizada para criar o jogo
import pygame
import time
import random

# Definição da velocidade da cobra
snake_speed = 15

# Tamanho da janela
window_x = 720
window_y = 480

# Definindo cores 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Inicializando o pygame
pygame.init()

# Inicializando a janela do jogo
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# Controlador de FPS (frames por segundo)
fps = pygame.time.Clock()

# Posição padrão da cobra
snake_position = [100, 50]

# Definindo os primeiros 4 blocos do corpo da cobra
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Posição da comida da cobra
food_position = [
    random.randrange(1, (window_x//10)) * 10,
    random.randrange(1, (window_y//10)) * 10
]

fruit_spawn = True

# Direção padrão da cobra
direction = 'RIGHT'
change_to = direction

# Pontuação inicial
score = 0

# Função para exibir a pontuação na tela do jogo
def show_score(choice, color, font, size):
    
    # Criando objeto de fonte score_font
    score_font = pygame.font.SysFont(font, size)
    
    # Criação do objeto de superfície de exibição score_surface
    score_surface = score_font.render('Pontuação: ' + str(score), True, color)
    
    # Criando um objeto retangular para a superficie de texto score_surface
    score_rect = score_surface.get_rect()
    
    # Exibindo o texto 
    game_window.blit(score_surface, score_rect)