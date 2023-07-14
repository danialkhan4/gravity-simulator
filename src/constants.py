import math
import pygame

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
AQUA = pygame.Color('aqua')

G = 6.674 * math.pow(10, -11)  # Gravitational constant
AU = 1.496 * math.pow(10, 11)  # 1 AU in meters

width, height = 1280, 720

earth_mass = 5.972 * math.pow(10, 24)  # kg
sun_mass = 1.989 * math.pow(10, 30)  # kg
