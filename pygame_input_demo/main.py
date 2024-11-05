import asyncio
import pygame

pygame.init()
pygame.display.set_mode((320, 240))
clock = pygame.time.Clock()

async def main():
    count = 60
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        print(f"{count}: Hello from Pygame")
        pygame.display.update()
        await asyncio.sleep(0)

        if not count:
            running = False
            break
        
        count -= 1
        clock.tick(60)
    
    pygame.quit()

asyncio.run(main()) 