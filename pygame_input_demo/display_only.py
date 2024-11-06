import sys
import pygame
import asyncio

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (64, 128, 255)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36

async def main():
    # Initialize only the display module
    pygame.display.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BACKGROUND_COLOR)
        font = pygame.font.Font(None, FONT_SIZE)
        text = font.render("Look at all these exclamation points!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)
    
    pygame.quit()

if __name__ == '__main__':
    asyncio.run(main())