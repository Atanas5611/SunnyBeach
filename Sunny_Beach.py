import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((950, 550))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Load images
water_surface = pygame.image.load('Graphics/background.png').convert()
fish_surface = pygame.image.load('Graphics/fish.png')
submarine_surface = pygame.image.load('Graphics/submarine.png')

# Loading the background music
music = pygame.mixer.Sound('Graphics/sailor_waltz_with_water_effects_c64_style.ogg')



# Scale images
new_fish = pygame.transform.scale(fish_surface, (75, 75))
new_submarine = pygame.transform.scale(submarine_surface, (130, 75))

# Set initial positions and speeds
fish_rect = new_fish.get_rect(bottomleft=(600, 300))
submarine_rect = new_submarine.get_rect(bottomright=(100, 300))
fish_x_speed = 4
fish_y_speed = 4
fish_x_direction = 0
fish_y_direction = 0
submarine_x_speed = 4
submarine_y_speed = 4
submarine_x_direction = 0
submarine_y_direction = 0

# Text surfaces for displaying winner message
submarine_wins_text = test_font.render("Submarine wins, press escape to quit", False, (255, 255, 255))
fish_wins_text = test_font.render("Fish wins, press escape to quit", False, (255, 255, 255))


start_time = pygame.time.get_ticks() // 1000  # Get start time in seconds
game_active = True  # Flag to check if the game is still active

pygame.mixer.Sound.play(music)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            # Handle key presses for fish movement
            if event.key == pygame.K_a:
                fish_x_direction = -1
            elif event.key == pygame.K_d:
                fish_x_direction = 1
            elif event.key == pygame.K_w:
                fish_y_direction = -1
            elif event.key == pygame.K_s:
                fish_y_direction = 1

            # Handle key presses for submarine movement
            if event.key == pygame.K_LEFT:
                submarine_x_direction = -1
            elif event.key == pygame.K_RIGHT:
                submarine_x_direction = 1
            elif event.key == pygame.K_UP:
                submarine_y_direction = -1
            elif event.key == pygame.K_DOWN:
                submarine_y_direction = 1

        if event.type == pygame.KEYUP:
            # Handle key releases for fish movement
            if event.key == pygame.K_a or event.key == pygame.K_d:
                fish_x_direction = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                fish_y_direction = 0

            # Handle key releases for submarine movement
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                submarine_x_direction = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                submarine_y_direction = 0

    if game_active:
        # Update fish and submarine positions
        fish_rect.x += fish_x_direction * fish_x_speed
        fish_rect.y += fish_y_direction * fish_y_speed
        submarine_rect.x += submarine_x_direction * submarine_x_speed
        submarine_rect.y += submarine_y_direction * submarine_y_speed

        # Blit images onto the screen
        screen.blit(water_surface, (0, 0))
        screen.blit(new_fish, fish_rect)
        screen.blit(new_submarine, submarine_rect)

        # Collision detection
        if submarine_rect.colliderect(fish_rect):
            game_active = False
            square_rect = submarine_wins_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(submarine_wins_text, square_rect)
            music.stop()

        # Calculate and display elapsed time
        elapsed_time = pygame.time.get_ticks() // 1000 - start_time
        timer_text = test_font.render("Time: " + str(elapsed_time), True, (255, 255, 255))
        screen.blit(timer_text, (800, 20))

        if elapsed_time >= 10:
            game_active = False
            square_rect = fish_wins_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(fish_wins_text, square_rect)
            music.stop()
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
