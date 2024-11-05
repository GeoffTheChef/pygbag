import asyncio
import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Audio setup
pygame.mixer.init()
print("Mixer initialized:", pygame.mixer.get_init())

# Sound loading (only .ogg)
def load_sound(name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, "sfx", f"{name}.ogg")
    
    print(f"Attempting to load sound from: {path}")
    print(f"File exists: {os.path.exists(path)}")
    return pygame.mixer.Sound(path)

async def main():
    background_color = (64, 128, 255)
    
    # Load sound - updated to match actual filename
    try:
        beep_sound = load_sound("file_example_OOG_2MG")
        print("Sound loaded successfully!")
    except Exception as e:
        print(f"Could not load sound: {str(e)}")
        beep_sound = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse clicked!")
                if beep_sound:
                    try:
                        beep_sound.play()
                        print("Playing sound!")
                    except Exception as e:
                        print(f"Error playing sound: {str(e)}")
        
        screen.fill(background_color)
        
        font = pygame.font.Font(None, 36)
        text = font.render("Click anywhere to play sound!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)
        
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())