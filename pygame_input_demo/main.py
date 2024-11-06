import sys
import pygame
import asyncio
import random

# Get viewport size if running in browser
if sys.platform == 'emscripten':
    import platform
    def get_window_size():
        # Get current window dimensions
        return (platform.window.innerWidth, platform.window.innerHeight)
else:
    # Default fallback sizes for desktop
    def get_window_size():
        return (1920, 1080)

# Constants
FPS = 60
BACKGROUND_COLOR = (64, 128, 255)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 72

async def main():
    pygame.init()
    
    # Get initial window size
    WINDOW_WIDTH, WINDOW_HEIGHT = get_window_size()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    
    # Current background color
    current_bg = BACKGROUND_COLOR
    
    running = True
    while running:
        # Update window size each frame when in browser
        if sys.platform == 'emscripten':
            WINDOW_WIDTH, WINDOW_HEIGHT = get_window_size()
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse clicked!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                current_bg = (random.randint(0, 255), 
                            random.randint(0, 255), 
                            random.randint(0, 255))
        
        screen.fill(current_bg)
        font = pygame.font.Font(None, FONT_SIZE)
        text = font.render("TESTING MANY MANY MANY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(text, text_rect)
        
        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)
    
    pygame.quit()

if __name__ == '__main__':
    asyncio.run(main())