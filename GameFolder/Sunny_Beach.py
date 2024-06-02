# Import necessary libraries
import pygame
from pygame.locals import *
from sys import exit

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 950
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Runner")

# Load images
background = pygame.image.load('Graphics/background.png').convert()
fish_surface = pygame.image.load('Graphics/fish.png').convert_alpha()
submarine_surface = pygame.image.load('Graphics/submarine.png').convert_alpha()
star_surface = pygame.image.load('Graphics/star.png').convert_alpha()

# Load font
font = pygame.font.Font('font/Pixeltype.ttf', 30)

# Load background music
pygame.mixer.music.load('Graphics/sailor_waltz_with_water_effects_c64_style.ogg')
pygame.mixer.music.play(-1)  # Loop the music

# Scale images
fish = pygame.transform.scale(fish_surface, (90, 90))  # Increase fish size
submarine = pygame.transform.scale(submarine_surface, (120, 60))
star = pygame.transform.scale(star_surface, (70, 70))

# Set initial positions and speeds
fish_rect = fish.get_rect(midleft=(600, 275))
submarine_rect = submarine.get_rect(midright=(100, 275))
star_rect = star.get_rect(center=(screen_width // 2, screen_height // 2))

# Initial speeds
fish_speed = 5
submarine_speed = 4

# Scores
fish_score = 0
submarine_score = 0

# Game state
game_active = True

# Timer
start_time = pygame.time.get_ticks() // 1000

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        # Handle key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            fish_rect.x -= fish_speed
        if keys[pygame.K_d]:
            fish_rect.x += fish_speed
        if keys[pygame.K_w]:
            fish_rect.y -= fish_speed
        if keys[pygame.K_s]:
            fish_rect.y += fish_speed

        if keys[pygame.K_LEFT]:
            submarine_rect.x -= submarine_speed
        if keys[pygame.K_RIGHT]:
            submarine_rect.x += submarine_speed
        if keys[pygame.K_UP]:
            submarine_rect.y -= submarine_speed
        if keys[pygame.K_DOWN]:
            submarine_rect.y += submarine_speed

        # Boundaries
        fish_rect.clamp_ip(screen.get_rect())
        submarine_rect.clamp_ip(screen.get_rect())

        # Check for collision with star
        if fish_rect.colliderect(star_rect):
            fish_score += 1
            fish_speed += 0.5
            star_rect.center = (screen_width * 2, screen_height * 2)  # Move star off-screen

        # Check for collision between submarine and fish
        if fish_rect.colliderect(submarine_rect):
            game_active = False

        # Draw everything
        screen.blit(background, (0, 0))
        screen.blit(fish, fish_rect)
        screen.blit(submarine, submarine_rect)
        if star_rect.x < screen_width:  # Only blit star if it's on-screen
            screen.blit(star, star_rect)

        # Display scores
        fish_score_text = font.render(f"Fish Score: {fish_score}", True, (255, 255, 255))
        submarine_score_text = font.render(f"Submarine Score: {submarine_score}", True, (255, 255, 255))
        screen.blit(fish_score_text, (20, 20))
        screen.blit(submarine_score_text, (20, 60))

        # Calculate and display elapsed time
        elapsed_time = pygame.time.get_ticks() // 1000 - start_time
        timer_text = font.render(f"Time: {elapsed_time}s", True, (255, 255, 255))
        screen.blit(timer_text, (20, 100))

        # Update display
        pygame.display.flip()

        # Check for game over
        if elapsed_time >= 10:
            game_active = False
            submarine_score += 1

    else:
        # Display winner message
        winner_text = font.render("Submarine wins, press escape to quit", True, (255, 255, 255))
        screen.blit(winner_text, (screen_width // 2 - 200, screen_height // 2))
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    clock.tick(60)









