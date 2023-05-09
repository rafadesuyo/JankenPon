import pygame
import random
from pygame import mixer


# init
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("bg.png")
pygame.init()
pygame.display.set_caption("Janken pon!")



# Sound loading
bgm = pygame.mixer.Sound("BGM.wav")
fight = pygame.mixer.Sound("fight.wav")
select = pygame.mixer.Sound("click.wav")
win = pygame.mixer.Sound("win.wav")
lose = pygame.mixer.Sound("lose.wav")
draw = pygame.mixer.Sound("draw.wav")
rsound = pygame.mixer.Sound("go_back.wav")

# set volume sound
fight.set_volume(0.3)
select.set_volume(0.3)
win.set_volume(0.3)
lose.set_volume(0.3)
draw.set_volume(0.3)
rsound.set_volume(0.3)
bgm.set_volume(0.4)


# importing images
rock_image = pygame.image.load("ROCK.png")
paper_image = pygame.image.load("Paper.png")
scissor_image = pygame.image.load("scissor.png")
vs_image = pygame.image.load("VS.png")
draw_image = pygame.image.load("DRAW.png")
win_image = pygame.image.load("WIN.png")
lose_image = pygame.image.load("LOSE....png")
again_image = pygame.image.load("again.png")
aura_image = pygame.image.load("win_aura.png")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

cards_image = [rock_image, paper_image, scissor_image]


# scrolling bg
scrolling = pygame.image.load("loopingbg.png")
selection = pygame.image.load("Selection.png")

# ai image and card ID
bg_card = pygame.image.load("back.png")
cards = [0, 1, 2]  # ai cards,if 0 rock,1 paper and 2 scissor.
cards_random = random.choice(cards) # ai card id output


# mouse
mouse_x = str(pygame.mouse.get_pos()[0])
mouse_y = str(pygame.mouse.get_pos()[1])


class Card:
    def __init__(self, x, y, x_change, y_change):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change


rock = Card(20, 170, 0, 0)
paper = Card(300, 170, 0, 0)
scissor = Card(570, 170, 0, 0)
ai = Card(800, 170, 0, 0)

# bugfixes-code improvement 5/8/2023
def draw_sprite(image, x, y):
    screen.blit(image, (x, y))


def draw_again(x, y):
    screen.blit(again_image, (x, y))


def draw_lose(x, y):
    screen.blit(lose_image, (x, y))


def draw_win(x, y):
    screen.blit(win_image, (x, y))


def draw_ai(x, y):
    screen.blit(bg_card, (x, y))


def draw_draw(x, y):
    screen.blit(draw_image, (x, y))


def draw_paper(x, y):
    screen.blit(paper_image, (x, y))


def draw_scissor(x, y):
    screen.blit(scissor_image, (x, y))


def draw_vs(x, y):
    screen.blit(vs_image, (x, y))


def restart():  # Resets the cards to the menu position
    rsound.play()
    rock.x_change = 0
    rock.x = 20
    rock.y = 170

    paper.x_change = 0
    paper.x = 300
    paper.y = 170

    scissor.x_change = 0
    scissor.x = 570
    scissor.y = 170

    ai.x_change = 0
    ai.x = 800
    ai.y = 170


def fight_sound():
    fight.play()


def click_sound():
    select.play()


def win_sound():
    win.play()


def lose_sound():
    lose.play()


def draw_sound():
    draw.play()


# Player card ID
card_id = 0

# states
menu = True
rock_choose = False
paper_choose = False
scissor_choose = False
running = True
sound_played = False

pygame.mixer.music.load("bgm.wav")
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # close game
            pygame.quit()
            exit()



    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(scrolling, (0, 0))
    mouse = pygame.mouse.get_pos()

    if menu:  # if on menu, choose a card.
        sound_played = False
        draw_sprite(rock_image, rock.x, rock.y) # displays the rock image
        draw_paper(paper.x, paper.y)  # scissor location
        draw_scissor(scissor.x, scissor.y)  # paper location
        cards_random = random.choice(cards)

        if mouse[0] in range(20, 240):  # if in rock click range
            screen.blit(selection, (-237, 42))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                    menu = False
                    rock_choose = True
                    fight_sound()
                    select.play()

        if mouse[0] in range(300, 500):  # if in paper click range
            screen.blit(selection, (43, 42))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                    menu = False
                    paper_choose = True
                    fight_sound()
                    select.play()

        if mouse[0] in range(580, 780):  # if in scissor click range
            screen.blit(selection, (313, 42))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                    menu = False
                    scissor_choose = True
                    fight_sound()
                    select.play()

    if rock_choose:
        card_id = 0  # Player rock id = 0

        if rock.x < 100:
            rock.x_change = 5  # move rock to the middle
            rock.x += rock.x_change
            draw_sprite(rock_image, rock.x, rock.y)

            paper.x_change = 35 # move paper away
            paper.x += paper.x_change
            draw_paper(paper.x, paper.y)

            scissor.x_change = 35  # move paper away
            scissor.x += scissor.x_change
            draw_scissor(scissor.x, scissor.y)

        if rock.x == 100:
            draw_sprite(rock_image, 100, rock.y)
            if ai.x > 500:
                ai.x_change = -10
                ai.x += ai.x_change
                draw_ai(ai.x, ai.y)

            if ai.x == 500:
                draw_ai(500, ai.y)
                draw_vs(350, 250)
                ai.x = 499

            if ai.x == 499:
                if cards_random == 0: # if ai choice is rock[0] DRAW.
                    draw_sprite(rock_image, 500, ai.y)
                    draw_vs(350, 250)
                    draw_draw(200, 20)
                    draw_again(330, 500)
                    if not sound_played:
                        draw_sound()
                        sound_played = True
                    if mouse[0] in range(330, 500):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                                restart()
                                menu = True
                                rock_choose = False
                if cards_random == 1:  # if ai  choice is paper[1] LOSE
                    draw_paper(500, ai.y)
                    draw_vs(350, 250)
                    draw_lose(200, 20)
                    draw_again(330, 500)
                    draw_sprite(aura_image, 446, 116)  # win pos
                    if not sound_played:
                        lose_sound()
                        sound_played = True
                    if mouse[0] in range(330, 500):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                                restart()
                                menu = True
                                rock_choose = False
                if cards_random == 2:  # if ai choice is scissor[2] WIN
                    draw_scissor(500, ai.y)
                    draw_vs(350, 250)
                    draw_win(250, 20)
                    draw_again(330, 500)
                    draw_sprite(aura_image, 46, 116)
                    if not sound_played:
                        win_sound()
                        sound_played = True
                    if mouse[0] in range(330, 500):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                                restart()
                                menu = True
                                rock_choose = False

    if paper_choose:
        card_id = 1  # Player rock id = 0

        if paper.x > 100:
            paper.x_change = -5  # move paper to the middle
            paper.x += paper.x_change
            draw_paper(paper.x, paper.y)

            rock.x_change = 45  # move rock away
            rock.x += paper.x_change
            draw_sprite(rock_image, rock.x, rock.y)

            scissor.x_change = 35  # move paper away
            scissor.x += scissor.x_change
            draw_scissor(scissor.x, scissor.y)

        if paper.x == 100:
            draw_paper(100, paper.y)
            if ai.x > 500:
                ai.x_change = -10
                ai.x += ai.x_change
                draw_ai(ai.x, ai.y)

            if ai.x == 500:
                draw_ai(500, ai.y)
                draw_vs(350, 250)
                ai.x = 499

            if ai.x == 499:
                if cards_random == 0:  # if ai choice is rock[0] WIN
                    draw_sprite(rock_image, 500, ai.y)
                    draw_vs(350, 250)
                    draw_win(200, 20)
                    draw_again(330, 500)
                    draw_sprite(aura_image, 46, 116)
                    if not sound_played:
                        win_sound()
                        sound_played = True
                    if mouse[0] in range(330, 500):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                                restart()
                                menu = True
                                paper_choose = False
                if cards_random == 1:  # if ai  choice is paper[1] DRAW
                    draw_paper(500, ai.y)
                    draw_vs(350, 250)
                    draw_draw(200, 20)
                    draw_again(330, 500)
                    if not sound_played:
                        draw_sound()
                        sound_played = True
                    if mouse[0] in range(330, 500):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                                restart()
                                menu = True
                                paper_choose = False
                if cards_random == 2:  # if ai choice is scissor[2] Lose
                    draw_scissor(500, ai.y)
                    draw_vs(350, 250)
                    draw_lose(250, 20)
                    draw_again(330, 500)
                    draw_sprite(aura_image, 446, 116)  # win pos
                    if not sound_played:
                        lose_sound()
                        sound_played = True
                    if mouse[0] in range(330, 500):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                                restart()
                                menu = True
                                paper_choose = False

    if scissor_choose:
        card_id = 2  # Player scissor id = 2

        if scissor.x > 100:
            scissor.x_change = - 10  # move paper to the middle
            scissor.x += scissor.x_change
            draw_scissor(scissor.x, scissor.y)

            rock.x_change = 45  # move rock away
            rock.x += paper.x_change
            draw_sprite(rock_image, rock.x, rock.y)

            paper.x_change = 35  # move paper away
            paper.x += paper.x_change
            draw_paper(paper.x, paper.y)

        if scissor.x == 100:
            draw_scissor(100, scissor.y)
            if ai.x > 500:
                ai.x_change = -10
                ai.x += ai.x_change
                draw_ai(ai.x, ai.y)

            if ai.x == 500:
                draw_ai(500, ai.y)
                draw_vs(350, 250)
                ai.x = 499

            if ai.x == 499:
                if cards_random == 0:  # if ai choice is rock[0] LOSE
                    draw_sprite(rock_image, 500, ai.y)
                    draw_vs(350, 250)
                    draw_lose(200, 20)
                    draw_again(330, 500)
                    draw_sprite(aura_image, 446, 116)
                    if not sound_played:
                        lose_sound()
                        sound_played = True
                    if mouse[0] in range(330, 500):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                                restart()
                                menu = True
                                scissor_choose = False
                if cards_random == 1:  # if ai  choice is paper[1] Win
                    draw_paper(500, ai.y)
                    draw_vs(350, 250)
                    draw_win(200, 20)
                    draw_again(330, 500)
                    draw_sprite(aura_image, 46, 116)
                    if not sound_played:
                        win_sound()
                        sound_played = True
                    if mouse[0] in range(330, 500):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                                restart()
                                menu = True
                                scissor_choose = False
                if cards_random == 2:  # if ai choice is scissor[2] DRAW
                    draw_scissor(500, ai.y)
                    draw_vs(350, 250)
                    draw_draw(250, 20)
                    draw_again(330, 500)
                    if not sound_played:
                        draw_sound()
                        sound_played = True
                    if mouse[0] in range(330, 500):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:  # if player chooses card,ai chooses 1.
                                restart()
                                menu = True
                                scissor_choose = False

    pygame.display.update()
