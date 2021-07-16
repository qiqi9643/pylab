import pygame
import sys

pygame.init()

class Car(pygame.sprite.Sprite):
    def __init__(self, filename, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(filename)
        
        self.rect=self.image.get_rect()
        self.rect.bottomright=initial_position
        print(self.rect.bottom)
        
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("20210606練習")
screen.fill([255,255,255])
fi='mycar.jpg'
b=Car(fi,[600,300])
screen.blit(b.image,b.rect)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    