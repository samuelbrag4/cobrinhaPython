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