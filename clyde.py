import pygame

class Clyde(pygame.sprite.Sprite):
    movement = [0, -1]
    speed = 2
    inPath = False
    moving = False
    freeze = False
    freezeTimer = 0
    timer = 1200
    stage = 0
    whiteBlue = 0
    white = True
    image = pygame.image.load("img/clyde.png")
    rect = image.get_rect()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect.top = 252
        self.rect.left = 323
        self.movement = [0, -1]
    def reset(self):
        self.rect.top = 252
        self.rect.left = 323
        self.inPath = False
        self.moving = False
        self.freeze = False
        self.freezeTimer = 0
        self.image = pygame.image.load("img/clyde.png")
        self.timer = 1200
        self.stage = 0
        self.movement = [0, -1]
    def move(self):
        if self.freeze:
            if self.freezeTimer is 0:
                self.freeze = False
                self.image = pygame.image.load("img/clyde.png")
            else:
                self.freezeTimer -= 1
                if self.whiteBlue is 0:
                    self.whiteBlue = 10
                    if self.white is True:
                        self.image = pygame.image.load("img/blueGhost.png")
                        self.white = False
                    else:
                        self.image = pygame.image.load("img/whiteGhost.png")
                        self.white = True
                else:
                    self.whiteBlue -= 1
        elif self.moving:
            if self.inPath:
                for x in range(0, self.speed):
                    if self.rect.left < 116:
                        self.movement = [0, 1]
                        self.rect.left = 116
                    if self.rect.right > width - 116:
                        self.movement = [0, -1]
                        self.rect.right = width - 116
                    if self.rect.top < 116:
                        self.movement = [-1, 0]
                        self.rect.top = 116
                    if self.rect.bottom > height - 116:
                        self.movement = [1, 0]
                        self.rect.bottom = height - 116
                    self.rect = self.rect.move(self.movement)
            elif self.stage is 0:
                for x in range(0, self.speed):
                    if self.rect.top > 153:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 1
                        self.movement = [1, 0]
            elif self.stage is 1:
                for x in range(0, self.speed):
                    if self.rect.right < 487:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 2
                        self.movement = [0, 1]
            elif self.stage is 2:
                for x in range(0, self.speed):
                    if self.rect.bottom < 327:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 3
                        self.movement = [-1, 0]
            elif self.stage is 3:
                for x in range(0, self.speed):
                    if self.rect.left > 305:
                       self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 4
                        self.movement = [0, 1]
            elif self.stage is 4:
                for x in range(0, self.speed):
                    if self.rect.bottom < 364:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.inPath = True
                        self.movement = [1, 0]
        elif self.timer is 0:
            self.moving = True
            self.rect.top = 215
            self.rect.left = 249
        else:
            self.timer -= 1
white = 250, 250, 250