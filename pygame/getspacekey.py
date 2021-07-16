import pygame, sys

def get_input_space():
    space = pygame.key.get_pressed()[pygame.K_SPACE]
    return space

pygame.init()

print('start')
display_surface = pygame.display.set_mode((10, 10))
while not get_input_space():
    pygame.event.get()
    pygame.display.update()
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        break
    # print('going')
print('The End')        
    
            