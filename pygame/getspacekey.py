import pygame, sys

def get_input_space():
    space = pygame.key.get_pressed()[pygame.K_SPACE]
    return space

pygame.init()    
while True:    
    if get_input_space():
            print('I got space key')
            sys.exit(1)
            