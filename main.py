try:
    import pygame
    import os
    from configs import *
    import colors
    from ghost import Ghost
    from events import *
    from copter import Copter, COPTER_SPRITE
    import pygame_menu
except ImportError:
    print("Please ....fulfil requirements")

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Copter")

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load('Assets/bg.png'), (WIDTH, HEIGHT))


def render_text(text, x, y, font_size):
    DISPLAY_TEXT = pygame.font.SysFont(
        'comicsans', font_size).render(str(text), True, colors.RED)
    padding = 15
    WIN.blit(DISPLAY_TEXT, (x - DISPLAY_TEXT.get_width() // 2, y))
    pygame.display.update()


def draw_static_screen(copter):
    WIN.blit(BACKGROUND_IMAGE, (BG_movement, 0))
    WIN.blit(BACKGROUND_IMAGE, (BG_movement + WIDTH, 0))
    copter.draw_static_copter(WIN)


BG_movement = 0
COUNTER = 0


def spawner():
    global COUNTER
    if COUNTER >= 100:
        COUNTER = 0
        pygame.event.post(pygame.event.Event(SPAWN_EVENT))
    else:
        COUNTER += 1


def drawBG():
    global BG_movement
    WIN.blit(BACKGROUND_IMAGE, (BG_movement, 0))
    WIN.blit(BACKGROUND_IMAGE, (BG_movement + WIDTH, 0))
    BG_movement -= BACKGROUND_SPEED
    if BG_movement == -WIDTH:
        BG_movement = 0


def draw_window(ghosts, copter, score):
    drawBG()
    SCORE = pygame.font.SysFont(
        'comicsans', 35).render(str(score), True, colors.RED)
    WIN.blit(SCORE, (WIDTH - 40 - SCORE.get_width() // 2, 15))
    copter.draw(WIN)
    for ghost in ghosts:
        ghost.draw(WIN)
    pygame.display.update()


def game_over(copter, score):
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    render_text("Game Over", center_x, center_y, 60)
    draw_static_screen(copter)
    pygame.time.delay(1000)
    pygame.display.update()

    render_text("Your score : "+str(score), center_x, center_y, 60)
    draw_static_screen(copter)
    pygame.time.delay(1000)
    pygame.display.update()

    COUNTDOWN = 5
    while COUNTDOWN >= 0:
        render_text(f"Restart in {COUNTDOWN}", center_x, center_x, 60)
        draw_static_screen(copter)
        pygame.time.delay(1000)
        pygame.display.update()
        COUNTDOWN -= 1


def main():
    clock = pygame.time.Clock()
    run = True
    ghosts = []
    copter = Copter()
    score = 0
    start = False
    draw_static_screen(copter)
    render_text("Press Space to Start", WIDTH // 2, HEIGHT // 2, 60)
    pygame.display.update()
    while run:
        clock.tick(55)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True

            if event.type == SPAWN_EVENT:
                ghosts.append(Ghost())

        if start:
            for ghost in ghosts:
                ghost.move()
                if ghost.rect.x < 0 - GHOST_WIDTH:
                    ghosts.remove(ghost)
                    score += 1
                if copter.collision(ghost):
                    ghosts.clear()
                    game_over(copter, score)
                    run = False

            if copter.collison_with_boundary():
                ghosts.clear()
                game_over(copter, score)
                run = False

            keys_pressed = pygame.key.get_pressed()
            copter.update(keys_pressed)

            draw_window(ghosts, copter, score)
            spawner()
    main()


if __name__ == '__main__':
    main()
