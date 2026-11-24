import pygame
import random
import math
pygame.init()

boundary = 800, 600
boarder = 15
screen = pygame.display.set_mode(boundary)


class alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.topleft = (self.x, self.y)
    def Alien_Move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.topleft = (self.x, self.y)

        if Alien >= boundary or Alien <= boarder:
            self.move(0, 10)
            self.dx *= -1
    self.move(random.randint(-9, 9), random.randint(-9, 9))


