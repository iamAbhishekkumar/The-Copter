try:
    import pygame
    from configs import *
    import colors
    from events import *
except ImportError:
    print("Fulfil requirements")

COPTER_SPRITE = [pygame.transform.scale(pygame.image.load('Assets/copter/copter1.png'), (COPTER_WIDTH, COPTER_HEIGHT)),
                 pygame.transform.scale(pygame.image.load(
                     'Assets/copter/copter2.png'), (COPTER_WIDTH, COPTER_HEIGHT)),
                 pygame.transform.scale(pygame.image.load(
                     'Assets/copter/copter3.png'), (COPTER_WIDTH, COPTER_HEIGHT)),
                 pygame.transform.scale(pygame.image.load(
                     'Assets/copter/copter4.png'), (COPTER_WIDTH, COPTER_HEIGHT)),
                 pygame.transform.scale(pygame.image.load(
                     'Assets/copter/copter5.png'), (COPTER_WIDTH, COPTER_HEIGHT)),
                 pygame.transform.scale(pygame.image.load(
                     'Assets/copter/copter6.png'), (COPTER_WIDTH, COPTER_HEIGHT)),
                 pygame.transform.scale(pygame.image.load(
                     'Assets/copter/copter7.png'), (COPTER_WIDTH, COPTER_HEIGHT)),
                 pygame.transform.scale(pygame.image.load('Assets/copter/copter8.png'), (COPTER_WIDTH, COPTER_HEIGHT))]


class Copter():
    def __init__(self):
        self.hitbox_width = 110
        self.hitbox_height = 54
        self.COPTER_ANIMATION_COUNT = 0
        self.rect = pygame.Rect(
            100, HEIGHT // 2, self.hitbox_width, self.hitbox_height)

    def draw(self, WIN):
        if self.COPTER_ANIMATION_COUNT > 7:
            self.COPTER_ANIMATION_COUNT = 0
        WIN.blit(COPTER_SPRITE[self.COPTER_ANIMATION_COUNT],
                 (self.rect.x - 20, self.rect.y))
        self.COPTER_ANIMATION_COUNT += 1

    def move_up(self):
        self.rect.y -= DROP_VEL

    def move_down(self):
        self.rect.y += DROP_VEL

    def update(self, keyspressed):
        if keyspressed[pygame.K_SPACE]:
            self.move_up()
        else:
            self.move_down()

    def collision(self, ghost):
        if self.rect.colliderect(ghost):
            return True
        return False

    def collison_with_boundary(self):
        if self.rect.y < 0 or self.rect.y + self.hitbox_height > HEIGHT:
            return True
        return False

    def draw_static_copter(self, WIN):
        WIN.blit(COPTER_SPRITE[0],
                 (self.rect.x - 20, self.rect.y))
