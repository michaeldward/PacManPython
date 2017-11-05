import pygame

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
