import pygame
import constants
import math
from particle import Particle
import default_objects
import exoplanets

# Game setup
pygame.init()

screen = pygame.display.set_mode((constants.width, constants.height))

pygame.display.set_caption('Particle Simulator')

clock = pygame.time.Clock()
font = pygame.font.SysFont('dejavusans', 11)

particles = []

particles.append(default_objects.get_sun())
particles.append(default_objects.get_earth())

planets = exoplanets.load_exoplanet_data()

# Define scaling factors
scale_factor = constants.width / (8 * constants.AU)  # Scaling sim space

# Mouse functions
drag_start = [0, 0]
drag_end = [0, 0]
clicking = False
dragging = False
running = True

# Text input
selected_planet = planets[0]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                drag_start = [pos[0], pos[1]]
                clicking = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False
                dragging = False
                pos = pygame.mouse.get_pos()

                velocity = [drag_start[0] - pos[0], drag_start[1] - pos[1]]
                if velocity[0] > 50: velocity[0] = 50
                if velocity[1] > 50: velocity[1] = 50

                velocity[0] = velocity[0] * 2_000
                velocity[1] = velocity[1] * 2_000

                scaled_pos = [(pos[0] - constants.width / 2) / scale_factor,
                              (pos[1] - constants.height / 2) / scale_factor]

                name, mass = selected_planet
                particles.append(Particle(name, scaled_pos, velocity, mass * constants.earth_mass))
                    
        elif event.type == pygame.MOUSEMOTION:
            if clicking:
                dragging = True
            else:
                dragging = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_1]:
                selected_planet = planets[0]
                print("Selecting earth")
                
            for key_code in range(pygame.K_1, pygame.K_9 + 1):
                if keys[key_code]:
                    key = chr(key_code).upper()
                    key = int(key) - 1
                    selected_planet = planets[key]
                    print("Selecting ", key, selected_planet)
                    
    screen.fill(constants.BLACK)
    if dragging:
        pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, constants.WHITE, drag_start, pos, width=1)

    dt = 80_000
    for particle in particles:
        particle.update(particles, dt)

    # Draw particles
    for particle in particles:

        # Map simulation coordinates to screen coordinates
        screen_x = int(particle.pos[0] * scale_factor + constants.width / 2)
        screen_y = int(particle.pos[1] * scale_factor + constants.height / 2)
        pygame.draw.circle(screen, constants.WHITE, [screen_x, screen_y], particle.display_size)

        # Text label
        text = font.render(particle.name, True, constants.WHITE)
        text_rect = text.get_rect()
        text_rect.center = [screen_x, screen_y + 15]
        screen.blit(text, text_rect)


    pos = 0
    for planet in planets:
        name, _ = planet
        selected_name, _ = selected_planet

        colour = constants.AQUA if name == selected_name else constants.WHITE
        name_text = '[' + str(pos + 1) + '] ' + name
        text_input = font.render(name_text, True, colour)
        text_input_rect = text_input.get_rect()
        text_input_rect.topleft = [pos * 60, constants.height - 15]
        screen.blit(text_input, text_input_rect)
        pos = pos + 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
