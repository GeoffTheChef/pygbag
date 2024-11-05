import asyncio
import pygame
import sys

async def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    # Add a background color to make it visible
    background_color = (64, 128, 255)  # Light blue
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill with background color
        screen.fill(background_color)
        
        # Add some text to show it's working
        font = pygame.font.Font(None, 36)
        text = font.render("Game is running!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)
        
        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(60)

asyncio.run(main()) 