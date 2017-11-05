import pygame
from random import randint

class Food(pygame.sprite.Sprite):
    big = False
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        if randint(1, 50) is 49:
            self.big = True
            self.image = pygame.image.load("img/bigFood.jpg")
        else:
            self.image = pygame.image.load("img/food.jpg")
        self.rect = self.image.get_rect()
        self.eaten = False
        self.rect.top = y
        self.rect.left = x
    def reset(self):
        self.eaten = False