try:
    import pygame
    from configs import *
    import random
    import colors
    from events import *
except ImportError:
    print("Please ....fulfil requirements")


GHOST_SPRITE = pygame.transform.scale(pygame.image.load(
    'Assets/ghost.png'), (GHOST_WIDTH, GHOST_HEIGHT))


class Ghost():
    def __init__(self):
        self.hitbox_width = 76
        self.hitbox_height = 70
        self.GHOST_ANIMATION_COUNT = 0
        self.rect = pygame.Rect(WIDTH, random.randint(
            GHOST_HEIGHT, HEIGHT-GHOST_HEIGHT), self.hitbox_width, self.hitbox_height)

    def draw(self, WIN):
        WIN.blit(GHOST_SPRITE, (self.rect.x - 20, self.rect.y - 30))
        

    def move(self):
        self.rect.x -= GHOST_SPEED
