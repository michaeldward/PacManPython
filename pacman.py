import sys, pygame
from random import randint
pygame.init()

width = 640
height = 480
class Barrier(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

class PacMan(pygame.sprite.Sprite):
    moveDirect = 0 #1 for LEFT, 2 for RIGHT, 3 for UP, 4 for DOWN
    nextDirect = 0 #0 means unassigned
    mouthOpen = False
    xPos = 0
    yPos = 0
    mouthCounter = 0
    image = pygame.image.load("img/PacManLeftOpen.png")
    rect = image.get_rect()
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.moveDirect = direction
        if self.moveDirect is 1:
            self.image = pygame.image.load("img/PacManLeftOpen.png")
        elif self.moveDirect is 2:
            self.image = pygame.image.load("img/PacManRightOpen.png")
        elif self.moveDirect is 3:
            self.image = pygame.image.load("img/PacManUpOpen.png")
        elif self.moveDirect is 4:
            self.image = pygame.image.load("img/PacmanDownOpen.png")
        screen = pygame.display.get_surface()
        #self.area = self.image.get_rect()
        xPos = x
        yPos = y
        self.rect.top = y
        self.rect.left = x
        #screen.blit(self, self.rect)
    def changeDirection(self, direction, Barriers):
        if(self.canMove(direction, Barriers)):
            self.moveDirect = direction
        else:
            self.nextDirect = direction
    def openClose(self):
        if self.mouthCounter is 4:
            self.mouthCounter = 0
            if self.mouthOpen is False:
                self.mouthOpen = True
                if self.moveDirect is 1:
                    self.image = pygame.image.load("img/PacManLeftOpen.png")
                elif self.moveDirect is 2:
                    self.image = pygame.image.load("img/PacManRightOpen.png")
                elif self.moveDirect is 3:
                    self.image = pygame.image.load("img/PacManUpOpen.png")
                elif self.moveDirect is 4:
                    self.image = pygame.image.load("img/PacManDownOpen.png")
            else:
                self.mouthOpen = False
                if self.moveDirect is 1:
                    self.image = pygame.image.load("img/PacManLeftClosed.png")
                elif self.moveDirect is 2:
                    self.image = pygame.image.load("img/PacManRightClosed.png")
                elif self.moveDirect is 3:
                    self.image = pygame.image.load("img/PacManUpClosed.png")
                elif self.moveDirect is 4:
                    self.image = pygame.image.load("img/PacManDownClosed.png")
        else:
            self.mouthCounter += 1
    def canMove(self, direction, Barriers):
        for barrier in Barriers:
            if direction is 1:
                if self.rect.left <= barrier.rect.right and self.rect.left >= barrier.rect.left and self.rect.bottom > barrier.rect.top and self.rect.top < barrier.rect.bottom:
                    return False
            if direction is 2:
                if self.rect.right >= barrier.rect.left and self.rect.right <= barrier.rect.right and self.rect.bottom > barrier.rect.top and self.rect.top < barrier.rect.bottom:
                    return False
            if direction is 3:
                if self.rect.top <= barrier.rect.bottom and self.rect.top >= barrier.rect.top and self.rect.left < barrier.rect.right and self.rect.right > barrier.rect.left:
                    return False
            if direction is 4:
                if self.rect.bottom >= barrier.rect.top and self.rect.bottom <= barrier.rect.bottom and self.rect.left < barrier.rect.right and self.rect.right > barrier.rect.left:
                    return False
        return True
    def update(self, Barriers):
        for x in range(0, 4):
            if self.nextDirect is not 0:
                self.changeDirection(self.nextDirect, Barriers)
                if self.nextDirect is self.moveDirect:
                    self.nextDirect = 0
            if self.canMove(self.moveDirect, Barriers):
                if self.moveDirect is 1:
                    if self.rect.left > 0:
                        self.rect.move_ip([-1, 0])
                elif self.moveDirect is 2:
                    if self.rect.right < width:
                        self.rect.move_ip([1, 0])
                elif self.moveDirect is 3:
                    if self.rect.top > 0:
                        self.rect.move_ip([0, -1])
                elif self.moveDirect is 4:
                    if self.rect.bottom < height:
                        self.rect.move_ip([0, 1])
        #self.image.get_rect().bottom = self.yPos
        #self.image.get_rect().right = self.xPos
        #print self.moveDirect
        #print self.rect
        #print self.rect.topleft
        #print self.rect.bottomleft
        #print self.rect.topright
        #print self.rect.bottomright
        self.openClose()
        screen.blit(self.image, self.rect)
class MissPacMan(pygame.sprite.Sprite):
    moveDirect = 0 #1 for LEFT, 2 for RIGHT, 3 for UP, 4 for DOWN
    nextDirect = 0 #0 means unassigned
    mouthOpen = False
    xPos = 0
    yPos = 0
    mouthCounter = 0
    image = pygame.image.load("img/MissPacManLeftOpen.png")
    rect = image.get_rect()
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.moveDirect = direction
        if self.moveDirect is 1:
            self.image = pygame.image.load("img/MissPacManLeftOpen.png")
        elif self.moveDirect is 2:
            self.image = pygame.image.load("img/MissPacManRightOpen.png")
        elif self.moveDirect is 3:
            self.image = pygame.image.load("img/MissPacManUpOpen.png")
        elif self.moveDirect is 4:
            self.image = pygame.image.load("img/MissPacmanDownOpen.png")
        screen = pygame.display.get_surface()
        #self.area = self.image.get_rect()
        xPos = x
        yPos = y
        self.rect.top = y
        self.rect.left = x
        #screen.blit(self, self.rect)
    def changeDirection(self, direction, Barriers):
        if(self.canMove(direction, Barriers)):
            self.moveDirect = direction
        else:
            self.nextDirect = direction
    def openClose(self):
        if self.mouthCounter is 4:
            self.mouthCounter = 0
            if self.mouthOpen is False:
                self.mouthOpen = True
                if self.moveDirect is 1:
                    self.image = pygame.image.load("img/MissPacManLeftOpen.png")
                elif self.moveDirect is 2:
                    self.image = pygame.image.load("img/MissPacManRightOpen.png")
                elif self.moveDirect is 3:
                    self.image = pygame.image.load("img/MissPacManUpOpen.png")
                elif self.moveDirect is 4:
                    self.image = pygame.image.load("img/MissPacManDownOpen.png")
            else:
                self.mouthOpen = False
                if self.moveDirect is 1:
                    self.image = pygame.image.load("img/MissPacManLeftClosed.png")
                elif self.moveDirect is 2:
                    self.image = pygame.image.load("img/MissPacManRightClosed.png")
                elif self.moveDirect is 3:
                    self.image = pygame.image.load("img/MissPacManUpClosed.png")
                elif self.moveDirect is 4:
                    self.image = pygame.image.load("img/MissPacManDownClosed.png")
        else:
            self.mouthCounter += 1
    def canMove(self, direction, Barriers):
        for barrier in Barriers:
            if direction is 1:
                if self.rect.left <= barrier.rect.right and self.rect.left >= barrier.rect.left and self.rect.bottom > barrier.rect.top and self.rect.top < barrier.rect.bottom:
                    return False
            if direction is 2:
                if self.rect.right >= barrier.rect.left and self.rect.right <= barrier.rect.right and self.rect.bottom > barrier.rect.top and self.rect.top < barrier.rect.bottom:
                    return False
            if direction is 3:
                if self.rect.top <= barrier.rect.bottom and self.rect.top >= barrier.rect.top and self.rect.left < barrier.rect.right and self.rect.right > barrier.rect.left:
                    return False
            if direction is 4:
                if self.rect.bottom >= barrier.rect.top and self.rect.bottom <= barrier.rect.bottom and self.rect.left < barrier.rect.right and self.rect.right > barrier.rect.left:
                    return False
        return True
    def update(self, Barriers):
        for x in range(0, 5):
            if self.nextDirect is not 0:
                self.changeDirection(self.nextDirect, Barriers)
                if self.nextDirect is self.moveDirect:
                    self.nextDirect = 0
            if self.canMove(self.moveDirect, Barriers):
                if self.moveDirect is 1:
                    if self.rect.left > 0:
                        self.rect.move_ip([-1, 0])
                elif self.moveDirect is 2:
                    if self.rect.right < width:
                        self.rect.move_ip([1, 0])
                elif self.moveDirect is 3:
                    if self.rect.top > 0:
                        self.rect.move_ip([0, -1])
                elif self.moveDirect is 4:
                    if self.rect.bottom < height:
                        self.rect.move_ip([0, 1])
        #self.image.get_rect().bottom = self.yPos
        #self.image.get_rect().right = self.xPos
        #print self.moveDirect
        #print self.rect
        #print self.rect.topleft
        #print self.rect.bottomleft
        #print self.rect.topright
        #print self.rect.bottomright
        self.openClose()
        screen.blit(self.image, self.rect)
class Blinky(pygame.sprite.Sprite):
    movement = [0, -1]
    speed = 5
    inPath = False
    moving = True
    freeze = False
    freezeTimer = 0
    timer = 0
    stage = 0
    whiteBlue = 0
    white = True
    image = pygame.image.load("img/blinky.png")
    rect = image.get_rect()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.rect.top = 215
        #self.rect.left = 249
        self.rect.top = 215
        self.rect.left = 249
    def reset(self):
        self.rect.top = 215
        self.rect.left = 249
        self.inPath = False
        self.moving = True
        self.freeze = False
        self.freezeTimer = 0
        #self.speed += 1
        self.stage = 0
        self.movement = [0, -1]
        self.image = pygame.image.load("img/blinky.png")
    def move(self):
        if self.freeze:
            if self.freezeTimer is 0:
                self.freeze = False
                self.image = pygame.image.load("img/blinky.png")
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
                    if self.rect.left < 5:
                            self.movement = [0, -1]
                            self.rect.left = 5
                    if self.rect.right > width - 5:
                        self.movement = [0, 1]
                        self.rect.right = width - 5
                    if self.rect.top < 5:
                        self.movement = [1, 0]
                        self.rect.top = 5
                    if self.rect.bottom > height - 5:
                        self.movement = [-1, 0]
                        self.rect.bottom = height - 5
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
                        self.stage = 5
                        self.movement = [-1, 0]
            elif self.stage is 5:
                for x in range(0, self.speed):
                    if self.rect.left > 116:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 6
                        self.movement = [0, -1]
            elif self.stage is 6:
                for x in range(0, self.speed):
                    if self.rect.top > 116:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 7
                        self.movement = [1, 0]
            elif self.stage is 7:
                for x in range(0, self.speed):
                    if self.rect.right < 312:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 8
                        self.movement = [0, -1]
            elif self.stage is 8:
                for x in range(0, self.speed):
                    if self.rect.top > 79:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 9
                        self.movement = [1, 0]
            elif self.stage is 9:
                for x in range(0, self.speed):
                    if self.rect.right < 561:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 10
                        self.movement = [0, 1]
            elif self.stage is 10:
                for x in range(0, self.speed):
                    if self.rect.bottom < 401:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 11
                        self.movement = [1, 0]
            elif self.stage is 11:
                for x in range(0, self.speed):
                    if self.rect.right < 598:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 12
                        self.movement = [0, -1]
            elif self.stage is 12:
                for x in range(0, self.speed):
                    if self.rect.top > 42:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 13
                        self.movement = [-1, 0]
            elif self.stage is 13:
                for x in range(0, self.speed):
                    if self.rect.left > 42:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 14
                        self.movement = [0, 1]
            elif self.stage is 14:
                for x in range(0, self.speed):
                    if self.rect.top < 47:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 15
                        self.movement = [-1, 0]
            elif self.stage is 15:
                for x in range(0, self.speed):
                    if self.rect.left > 5:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.inPath = True
                        self.movement = [0, -1]
        elif self.timer is 0:
            self.moving = True
        else:
            self.timer -= 1
class Pinky(pygame.sprite.Sprite):
    movement = [0, -1]
    speed = 4
    inPath = False
    moving = False
    freeze = False
    freezeTimer = 0
    timer = 400
    stage = 0
    whiteBlue = 0
    white = True
    image = pygame.image.load("img/pinky.png")
    rect = image.get_rect()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect.top = 215
        self.rect.left = 286
    def reset(self):
        self.rect.top = 215
        self.rect.left = 286
        self.inPath = False
        self.moving = False
        self.freeze = False
        self.freezeTimer = 0
        self.image = pygame.image.load("img/pinky.png")
        self.timer = 400
        self.stage = 0
        self.movement = [0, -1]
    def move(self):
        if self.freeze:
            if self.freezeTimer is 0:
                self.image = pygame.image.load("img/pinky.png")
                self.freeze = False
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
                    if self.rect.left < 42:
                        self.movement = [0, 1]
                        self.rect.left = 42
                    if self.rect.right > width - 42:
                        self.movement = [0, -1]
                        self.rect.right = width - 42
                    if self.rect.top < 42:
                        self.movement = [-1, 0]
                        self.rect.top = 42
                    if self.rect.bottom > height - 42:
                        self.movement = [1, 0]
                        self.rect.bottom = height - 42
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
                        self.stage = 5
                        self.movement = [-1, 0]
            elif self.stage is 5:
                for x in range(0, self.speed):
                    if self.rect.left > 116:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 6
                        self.movement = [0, -1]
            elif self.stage is 6:
                for x in range(0, self.speed):
                    if self.rect.top > 116:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 7
                        self.movement = [1, 0]
            elif self.stage is 7:
                for x in range(0, self.speed):
                    if self.rect.right < 312:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 8
                        self.movement = [0, -1]
            elif self.stage is 8:
                for x in range(0, self.speed):
                    if self.rect.top > 79:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 9
                        self.movement = [1, 0]
            elif self.stage is 9:
                for x in range(0, self.speed):
                    if self.rect.right < 561:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 10
                        self.movement = [0, 1]
            elif self.stage is 10:
                for x in range(0, self.speed):
                    if self.rect.bottom < 401:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 11
                        self.movement = [1, 0]
            elif self.stage is 11:
                for x in range(0, self.speed):
                    if self.rect.right < 598:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.inPath = True
                        self.movement = [0, -1]
        elif self.timer is 0:
            self.moving = True
            self.rect.top = 215
            self.rect.left = 249
        else:
            self.timer -= 1
class Inky(pygame.sprite.Sprite):
    movement = [0, -1]
    speed = 3
    inPath = False
    moving = False
    freeze = False
    freezeTimer = 0
    timer = 800
    stage = 0
    whiteBlue = 0
    white = True
    image = pygame.image.load("img/inky.png")
    rect = image.get_rect()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect.top = 252
        self.rect.left = 286
    def reset(self):
        self.rect.top = 252
        self.rect.left = 286
        self.inPath = False
        self.moving = False
        self.freeze = False
        self.freezeTimer = 0
        self.image = pygame.image.load("img/inky.png")
        self.timer = 800
        self.stage = 0
        self.movement = [0, -1]
    def move(self):
        if self.freeze:
            if self.freezeTimer is 0:
                self.freeze = False
                self.image = pygame.image.load("img/inky.png")
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
                    if self.rect.left < 79:
                        self.movement = [0, -1]
                        self.rect.left = 79
                    if self.rect.right > width - 79:
                        self.movement = [0, 1]
                        self.rect.right = width - 79
                    if self.rect.top < 79:
                        self.movement = [1, 0]
                        self.rect.top = 79
                    if self.rect.bottom > height - 79:
                        self.movement = [-1, 0]
                        self.rect.bottom = height - 79
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
                        self.stage = 5
                        self.movement = [-1, 0]
            elif self.stage is 5:
                for x in range(0, self.speed):
                    if self.rect.left > 116:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 6
                        self.movement = [0, -1]
            elif self.stage is 6:
                for x in range(0, self.speed):
                    if self.rect.top > 116:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 7
                        self.movement = [1, 0]
            elif self.stage is 7:
                for x in range(0, self.speed):
                    if self.rect.right < 312:
                        self.rect = self.rect.move(self.movement)
                    else:
                        self.stage = 8
                        self.movement = [0, -1]
            elif self.stage is 8:
                for x in range(0, self.speed):
                    if self.rect.top > 79:
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
        
    
blinkyspeed = [5, 0]
tie2speed = [7, 0]
tieadvancedspeed = [10, 0]
black = 0,0,0
blue = 0, 0, 250
red = 250, 0, 0
green = 0, 250, 0

Barriers = []
barrier1 = Barrier(white, 0, 0, width, 5)
Barriers.append(barrier1)
barrier2 = Barrier(white, 0, 0, 5, height)
Barriers.append(barrier2)
barrier3 = Barrier(white, width - 5, 0, 5, height)
Barriers.append(barrier3)
barrier4 = Barrier(white, 0, height - 5, width, 5)
Barriers.append(barrier4)
barrier5 = Barrier(white, 37, 37, width - 74, 5)
Barriers.append(barrier5)
barrier6 = Barrier(white, width - 42, 37, 5, height - 74)
Barriers.append(barrier6)
barrier7 = Barrier(white, 37, height - 42, width - 74, 5)
Barriers.append(barrier7)
barrier8 = Barrier(white, 37, 37, 5, 10)
Barriers.append(barrier8)
barrier8a = Barrier(white, 37, 79, 5, height - 116)
Barriers.append(barrier8a)
barrier9 = Barrier(white, 74, 74, width - 148, 5)
Barriers.append(barrier9)
barrier10 = Barrier(white, 74, 74, 5, height - 148)
Barriers.append(barrier10)
barrier11 = Barrier(white, 74, height - 79, width - 148, 5)
Barriers.append(barrier11)
barrier12 = Barrier(white, width - 79, 74, 5, 295)
Barriers.append(barrier12)
barrier13 = Barrier(white, 111, 111, 169, 5)
Barriers.append(barrier13)
barrier13a = Barrier(white, 312, 111, 217, 5)
Barriers.append(barrier13a)
barrier14 = Barrier(white, 111, 111, 5, height - 222)
Barriers.append(barrier14)
barrier15 = Barrier(white, 111, height - 116, width - 222, 5)
Barriers.append(barrier15)
barrier16 = Barrier(white, width - 116, 111, 5, height - 222)
Barriers.append(barrier16)
barrier17 = Barrier(white, 148, 148, width - 296, 5)
Barriers.append(barrier17)
barrier18 = Barrier(white, 148, 148, 5, height - 296)
Barriers.append(barrier18)
barrier19 = Barrier(white, 148, height - 153, 158, 5)
Barriers.append(barrier19)
barrier19a = Barrier(white, 338, height - 153, 154, 5)
Barriers.append(barrier19a)
barrier20 = Barrier(white, width - 153, 148, 5, height - 296)
Barriers.append(barrier20)
barrier21 = Barrier(white, 185, 185, 64, 5)
Barriers.append(barrier21)
barrier22 = Barrier(white, 281, 185, 174, 5)
Barriers.append(barrier22)
barrier23 = Barrier(white, 185, 185, 5, height - 370)
Barriers.append(barrier23)
barrier24 = Barrier(white, 185, height - 190, width - 370, 5)
Barriers.append(barrier24)
barrier25 = Barrier(white, width - 190, 185, 5, height - 370)
Barriers.append(barrier25)
barrier26 = Barrier(white, 320, 185, 5, height - 370)
Barriers.append(barrier25)

Foods = []
for num1 in range(0, 17):
    for num2 in range(0, 13):
        if (num1 <= 7):
            a = 5 + 37 * num1
        else:
            a = 11 + 37 * num1
        if (num2 <= 5):
            b = 5 + 37 * num2
        else:
            b = 4 + 37 * num2
        Foods.append(Food(a, b))


screen = pygame.display.set_mode([width, height+32])
lightsaber = pygame.image.load("img/PacManRightOpen.png")
pygame.display.set_icon(lightsaber)
pygame.display.set_caption('Pac Man')
#pygame.mouse.set_visible(0)
pygame.key.set_repeat(10, 10)
twoPlayer = False
playerSelect = True
clock = pygame.time.Clock()
myfont = pygame.font.SysFont("monospace", 30)
while playerSelect:
    clock.tick(30)
    screen.fill(black)
    selectlabel = myfont.render("Select one or two player: ", True, (250, 250, 250), (0, 0, 0))
    selectrect = selectlabel.get_rect()
    selectrect.top = 100
    selectrect.left = 75
    onePlayerImage = pygame.image.load("img/onePlayer.png")
    onePlayerImageRect = onePlayerImage.get_rect()
    onePlayerImageRect.top = 180
    onePlayerImageRect.left = 85
    twoPlayerImage = pygame.image.load("img/twoPlayer.jpg")
    twoPlayerImageRect = twoPlayerImage.get_rect()
    twoPlayerImageRect.top = 180
    twoPlayerImageRect.left = 360
    onePlayerLabel = myfont.render("Press a", True, (250, 250, 250), (0, 0, 0))
    onePlayerLabelRect = onePlayerLabel.get_rect()
    onePlayerLabelRect.top = 400
    onePlayerLabelRect.left = 85
    twoPlayerLabel = myfont.render("Press b", True, (250, 250, 250), (0, 0, 0))
    twoPlayerLabelRect = twoPlayerLabel.get_rect()
    twoPlayerLabelRect.top = 400
    twoPlayerLabelRect.left = 360
    screen.blit(onePlayerImage, onePlayerImageRect)
    screen.blit(twoPlayerImage, twoPlayerImageRect)
    screen.blit(onePlayerLabel, onePlayerLabelRect)
    screen.blit(twoPlayerLabel, twoPlayerLabelRect)
    screen.blit(selectlabel, selectrect)
    pygame.display.flip()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_a]:
                playerSelect = False
                twoPlayer = False
            if keys_pressed[pygame.K_b]:
                playerSelect = False
                twoPlayer = True
#CODE FOR ONE OR TWO PLAYER SELECT HERE
player1 = PacMan(5, 5, 4)
if twoPlayer is True:
    player2 = MissPacMan(5, 37, 1)

background = pygame.Surface(screen.get_size())
background = background.convert()

blinky = Blinky()
pinky = Pinky()
inky = Inky()
clyde = Clyde()
tie = pygame.image.load("img/MissPacManDownClosed.png")
tierect = tie.get_rect()
tie2 = pygame.image.load("img/PacManDownOpen.png")
tie2rect = tie2.get_rect()
tieadvanced = pygame.image.load("img/PacManUpOpen.png")
tieadvancedrect = tieadvanced.get_rect()

tierect.bottom = 120
tierect.right = 100
tieadvancedrect.bottom = 240
tieadvancedrect.right = 100

tie2rect.bottom = 360
tie2rect.right = 100


x = 50
y = 50

level = 1
collide1 = False
collide2 = False
collide3 = False
collide4 = False
levelFinish = False
done = False
lives = 3

livesThree = pygame.image.load("img/PacManRightClosed.png")
livesTwo = pygame.image.load("img/PacManRightClosed.png")
livesOne = pygame.image.load("img/PacManRightClosed.png")
livesThreeRect = livesThree.get_rect()
livesTwoRect = livesTwo.get_rect()
livesOneRect = livesOne.get_rect()
livesOneRect.top = height
livesOneRect.left = 0
livesTwoRect.top = height
livesTwoRect.left = 42
livesThreeRect.top = height
livesThreeRect.left = 84

def gameOver():
    screen.fill(black)
    pygame.draw.line(screen, white, [0, height], [width, height], 1)
    labelcaption = "Level: " + `level`
    label = myfont.render(labelcaption, True, (250, 250, 250), (0, 0, 0))
    labelrect = label.get_rect()
    labelrect.top = height + 3
    labelrect.left = 200
    screen.blit(label, labelrect)
    gameOver = myfont.render("Game over!", True, (250, 250, 250), (0, 0, 0))
    gameOverRect = gameOver.get_rect()
    gameOverRect.left = 200
    gameOverRect.top = 200
    screen.blit(gameOver, gameOverRect)
    pygame.display.flip()

while True:
    if not done:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_DOWN]:
                player1.changeDirection(4, Barriers)
            if keys_pressed[pygame.K_UP]:
                player1.changeDirection(3, Barriers)
            if keys_pressed[pygame.K_LEFT]:
                player1.changeDirection(1, Barriers)
            if keys_pressed[pygame.K_RIGHT]:
                player1.changeDirection(2, Barriers)
            if twoPlayer is True:
                if keys_pressed[pygame.K_w]:
                    player2.changeDirection(3, Barriers)
                if keys_pressed[pygame.K_a]:
                    player2.changeDirection(1, Barriers)
                if keys_pressed[pygame.K_s]:
                    player2.changeDirection(4, Barriers)
                if keys_pressed[pygame.K_d]:
                    player2.changeDirection(2, Barriers)
        for item in Foods:
            if item.rect.colliderect(player1.rect):
                if item.eaten is False:
                    if item.big is True:
                        if blinky.moving is True:
                            blinky.freeze = True
                            blinky.freezeTimer = randint(200, 400)
                        if inky.moving is True:
                            inky.freeze = True
                            inky.freezeTimer = randint(200, 400)
                        if pinky.moving is True:
                            pinky.freeze = True
                            pinky.freezeTimer = randint(200, 400)
                        if clyde.moving is True:
                            clyde.freeze = True
                            clyde.freezeTimer = randint(200, 400)
                item.eaten = True
            if twoPlayer is True:
                if item.rect.colliderect(player2.rect):
                    if item.eaten is False:
                        if item.big is True:
                            if blinky.moving is True:
                                blinky.freeze = True
                                blinky.freezeTimer = randint(200, 400)
                            if inky.moving is True:
                                inky.freeze = True
                                inky.freezeTimer = randint(200, 400)
                            if pinky.moving is True:
                                pinky.freeze = True
                                pinky.freezeTimer = randint(200, 400)
                            if clyde.moving is True:
                                clyde.freeze = True
                                clyde.freezeTimer = randint(200, 400)
                    item.eaten = True
        if twoPlayer is False:
            if not blinky.rect.colliderect(player1.rect):
                collide1 = False
                blinky.move()
            else:
                if blinky.freeze is True:
                    blinky.reset()
                    blinky.timer = 100
                else:
                    collide1 = True
                    done = True
            if not pinky.rect.colliderect(player1.rect):
                collide2 = False
                pinky.move()
            else:
                if pinky.freeze is True:
                    pinky.reset()
                    pinky.timer = 100
                else:
                    collide2 = True
                    done = True
            if not inky.rect.colliderect(player1.rect):
                collide3 = False
                inky.move()
            else:
                if inky.freeze is True:
                    inky.reset()
                    inky.timer = 100
                else:
                    collide3 = True
                    done = True
            if not clyde.rect.colliderect(player1.rect):
                collide3 = False
                clyde.move()
            else:
                if clyde.freeze is True:
                    clyde.reset()
                    clyde.timer = 100
                else:
                    collide3 = True
                    done = True
        else:
            if blinky.rect.colliderect(player1.rect) or blinky.rect.colliderect(player2.rect):
                if blinky.freeze is True:
                    blinky.reset()
                    blinky.timer = 100
                else:
                    collide1 = True
                    done = True
            else:
                collide1 = False
                blinky.move()
            if pinky.rect.colliderect(player1.rect) or pinky.rect.colliderect(player2.rect):
                if pinky.freeze is True:
                    pinky.reset()
                    pinky.timer = 100
                else:
                    collide2 = True
                    done = True
            else:
                collide2 = False
                pinky.move()
            if inky.rect.colliderect(player1.rect) or inky.rect.colliderect(player2.rect):
                if inky.freeze is True:
                    inky.reset()
                    inky.timer = 100
                else:
                    collide3 = True
                    done = True
            else:
                collide3 = False
                inky.move()
            if clyde.rect.colliderect(player1.rect) or clyde.rect.colliderect(player2.rect):
                if clyde.freeze is True:
                    clyde.reset()
                    clyde.timer = 100
                else:
                    collide3 = True
                    done = True
            else:
                collide3 = False
                clyde.move()
        screen.fill(black)
        levelFinish = True
        for item in Foods:
            if not item.eaten:
                levelFinish = False
                screen.blit(item.image, item.rect)
        if levelFinish is True:
            for item in Foods:
                item.eaten = False
            blinky.reset()
            pinky.reset()
            inky.reset()
            clyde.reset()
            player1.rect.top = 5
            player1.rect.left = 5
            if twoPlayer:
                player2.rect.top = 37
                player2.rect.left = 37
            level += 1
            levelFinish = False
            blinky.speed += 1
            pinky.speed += 1
            inky.speed += 1
            clyde.speed += 1
        pygame.draw.line(screen, white, [0, height], [width, height], 1)
        
        labelcaption = "Level: " + `level`
        label = myfont.render(labelcaption, True, (250, 250, 250), (0, 0, 0))
        labelrect = label.get_rect()
        labelrect.top = height + 3
        labelrect.left = 200
        screen.blit(label, labelrect)
        screen.blit(blinky.image, blinky.rect)
        screen.blit(pinky.image, pinky.rect)
        screen.blit(inky.image, inky.rect)
        screen.blit(clyde.image, clyde.rect)

        for barrier in Barriers:
            screen.blit(barrier.image, barrier.rect)
        player1.update(Barriers)
        if twoPlayer is True:
            player2.update(Barriers)
        if lives is 3:
            screen.blit(livesThree, livesThreeRect)
        if lives >= 2:
            screen.blit(livesTwo, livesTwoRect)
        if lives >= 1:
            screen.blit(livesOne, livesOneRect)
        pygame.display.flip()
    else:
        if lives is not 0:
            lives -= 1
            done = False
            player1.rect.top = 5
            player1.rect.left = 5
            if twoPlayer:
                player2.rect.top = 37
                player2.rect.left = 5
            blinky.reset()
            pinky.reset()
            inky.reset()
            clyde.reset()
        else:
            gameOver()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

