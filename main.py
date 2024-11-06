import pygame
import sys

# ... your existing code ...

def handle_fullscreen():
    if sys.platform == "emscripten":
        current_mode = pygame.display.get_mode()
        if current_mode[2] & pygame.FULLSCREEN:
            pygame.display.set_mode((WIDTH, HEIGHT))
        else:
            pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

# Change to bright purple
BACKGROUND_COLOR = (128, 0, 128)  # Purple
# or even brighter
BACKGROUND_COLOR = (255, 0, 255)  # Magenta

# In your game loop:
for event in pygame.event.get():
    if event.type == pygame.USEREVENT and hasattr(event, 'fullscreen'):
        handle_fullscreen()
    screen.fill(BACKGROUND_COLOR) 