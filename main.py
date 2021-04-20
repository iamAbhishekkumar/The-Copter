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


def render_text(text, x, y,font_size):
    DISPLAY_TEXT = pygame.font.SysFont(
        'comicsans', font_size).render(str(text), True, colors.RED)
    padding = 15
    WIN.blit(DISPLAY_TEXT, (x - DISPLAY_TEXT.get_width() // 2, y))


BG_movement = 0


def drawBG():
    global BG_movement
    WIN.blit(BACKGROUND_IMAGE, (BG_movement, 0))
    WIN.blit(BACKGROUND_IMAGE, (BG_movement + WIDTH, 0))
    BG_movement -= BACKGROUND_SPEED
    if BG_movement == -WIDTH:
        BG_movement = 0


def draw_window(ghosts, copter, score):
    drawBG()
    render_text(score, WIDTH - 40, 15,35)
    copter.draw(WIN)
    for ghost in ghosts:
        ghost.draw(WIN)
    pygame.display.update()


def game_over(ghosts, copter, score):
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    render_text("Game Over", center_x, center_y,60)
    pygame.display.update()
    pygame.time.delay(2000)
    
    # draw_window(ghosts, copter, score)
    # render_text("Your score : "+str(score), center_x, center_y)
    # pygame.time.delay(1000)
    # # draw_window(ghosts, copter, score)
    # COUNTDOWN = 5
    # while COUNTDOWN >= 0:
    #     render_text(f"Restart in {COUNTDOWN}", center_x, center_x)
    #     pygame.time.delay(1000)
    #     # draw_window(ghosts, copter, score)
    #     COUNTDOWN -= 1


def start():
    pygame.time.delay(15000)
    clock = pygame.time.Clock()
    run = True
    ghosts = []
    copter = Copter()
    score = 0
    pygame.time.set_timer(SPAWN_EVENT, SPAWN_TIME)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == SPAWN_EVENT:
                ghosts.append(Ghost())

        for ghost in ghosts:
            ghost.move()
            if ghost.rect.x < 0 - GHOST_WIDTH:
                ghosts.remove(ghost)
                score += 1
            if copter.collision(ghost):
                ghosts.remove(ghost)
                game_over(ghosts, copter, score)
                # start()
                run = False

        if copter.collison_with_boundary():
            game_over(ghosts, copter, score)
            # start()
            run = False

        keys_pressed = pygame.key.get_pressed()
        copter.update(keys_pressed)

        draw_window(ghosts, copter, score)


def main():
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    pygame.display.update()

    menu = pygame_menu.Menu(MENU_WIDTH, MENU_HEIGHT,
                            'Welcome', theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input('Name :', default='Your Name')
    menu.add.button('Play', start)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(WIN)


if __name__ == '__main__':
    start()
