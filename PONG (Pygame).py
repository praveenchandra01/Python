import pygame
import sys
import random


def ball_animation():

    global ball_speedx, ball_speedy, player_score, opponent_score, init_Time

    ball.x += ball_speedx
    ball.y += ball_speedy

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speedy *= -1

    if ball.left <= 0:
        player_score += 1
        init_Time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        opponent_score += 1
        init_Time = pygame.time.get_ticks()
        # print("1.",init_Time)

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speedx *= -1


def player_animation():

    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():

    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        # if opponent.centery > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_start():

    global ball_speedx, ball_speedy, init_Time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)
    # print("2.",current_time)
    # print("3.",current_time-init_Time)

    if current_time - init_Time < 700:
        number_three = text_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 4, screen_height/2 + 20))

    if 700 < current_time - init_Time < 1400:
        number_two = text_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width/2 - 4, screen_height/2 + 20))

    if 1400 < current_time - init_Time < 2100:
        number_one = text_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width/2 - 5, screen_height/2 + 20))

    if current_time - init_Time < 2100:
        ball_speedx, ball_speedy = 0, 0
    else:
        ball_speedy = 8 #* random.choice((1, -1))
        ball_speedx = 8 * random.choice((1, -1))

        init_Time = None


if __name__ == '__main__':

    # General setup
    pygame.init()
    clock = pygame.time.Clock()

    # Main Window
    screen_width = 1050
    screen_height = 550
    # screen = pygame.display.set_mode((screen_width, screen_height))
    screen = pygame.display.set_mode(
        (screen_width, screen_height), pygame.NOFRAME)
    # pygame.display.set_caption("Collide")
    # i = pygame.image.load('1.ico')
    # pygame.display.set_icon(i)

    # Colors
    light_grey = (220, 220, 220)
    op_color = "#f55142"
    plyr_color = "#4293f5"
    ball_color = "#f5b642"
    bg_color = pygame.Color('#26354a')

    # Game Rectangles
    ball = pygame.Rect(screen_width / 2 - 10, screen_height / 2 - 10, 30, 30)
    player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 130)
    opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 130)

    # Game varibles
    ball_speedx = 9
    ball_speedy = 9
    player_speed = 0
    opponent_speed = 9

    # Text varibles
    player_score = 0
    opponent_score = 0
    text_font = pygame.font.Font('freesansbold.ttf', 22)
    over_font = pygame.font.Font('freesansbold.ttf', 16)

    # Score time
    init_Time = True

    while True:

        # Handling inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # Player movement
            if event.type == pygame.KEYDOWN:  # Key press
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:  # Key release
                    player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7

        ball_animation()
        player_animation()
        opponent_ai()

        # Visuals
        screen.fill(bg_color)
        pygame.draw.rect(screen, plyr_color, player)
        pygame.draw.rect(screen, op_color, opponent)
        pygame.draw.aaline(screen, light_grey, (screen_width / 2,
                                                0), (screen_width / 2, screen_height))
        pygame.draw.ellipse(screen, ball_color, ball,)

        if init_Time:
            ball_start()

        player_text = text_font.render(f"{player_score}", False, light_grey)
        screen.blit(player_text, (535, 244))
        opponent_text = text_font.render(
            f"{opponent_score}", False, light_grey)
        screen.blit(opponent_text, (505, 244))

        if player_score == 5:
            txt = text_font.render("You   Win!", False, light_grey)
            screen.blit(txt, (480, 50))
            restart = over_font.render(
                "Press Enter    to start new game", False, light_grey)
            screen.blit(restart, (425, 500))
            pygame.display.flip()
            wait = True
            while wait:
                # clock.tick(70)
                for event in pygame.event.get():
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            wait = False
            player_score = 0
            opponent_score = 0

        if opponent_score == 5:
            txt = text_font.render("You   Loose!", False, light_grey)
            screen.blit(txt, (480, 50))
            restart = over_font.render(
                "Press Enter    to start new game", False, light_grey)
            screen.blit(restart, (425, 500))
            pygame.display.flip()
            # pygame.time.wait(3000)
            wait = True
            while wait:
                # clock.tick(70)
                for event in pygame.event.get():
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            wait = False
            opponent_score = 0
            player_score = 0

        # Updating the screen
        pygame.display.flip()
        clock.tick(70)  # fps =60
