"""The main game, hopefully."""

from player import *
import time
import subprocess as sp
from utils import *
import pygame
import random

room_text = load_descriptions_file('room_description.json')

player = Player()

now = time.strftime("%Y%m%d%H%M%S")

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
RAIN_COLOUR = GREY

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.init()


pygame.display.set_caption('Textbook Mysteries')
game_icon = pygame.image.load('magnifying_glass.png')
pygame.display.set_icon(game_icon)

pygame.mixer.music.load("{}/NoirJazz_MH_V2_010219.mp3".format(music_folder))
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)


channel1 = pygame.mixer.Channel(1)
game_sound = pygame.mixer.Sound("{}/rain_sound.ogg".format(sounds_folder))
channel1.play(game_sound, loops=-1)

MAIN_FONT = "8-bit pusab.ttf"

clock = pygame.time.Clock()
done = False

raindrops = []
x_speed = 5
y_speed = 50

for i in range(200):
    x = random.randrange(0, round(SCREEN_WIDTH + (SCREEN_HEIGHT * x_speed)/y_speed))
    y = random.randrange(-10, SCREEN_HEIGHT + 10)
    raindrops.append([[x, y], y_speed])

timer = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    screen.fill(BLACK)

    for i in range(len(raindrops)):
        pygame.draw.line(screen, RAIN_COLOUR, raindrops[i][0], (raindrops[i][0][0] - x_speed/5, raindrops[i][0][1] + raindrops[i][1]/5))

        raindrops[i][0][0] -= x_speed
        raindrops[i][0][1] += raindrops[i][1]

        if raindrops[i][0][1] > (SCREEN_HEIGHT + 10):
            y = random.randrange(-50, -10)
            x = random.randrange(0, round(SCREEN_WIDTH + (SCREEN_HEIGHT * x_speed)/y_speed))
            new_speed = random.randrange(y_speed - 5, y_speed + 5)
            raindrops[i][0][0] = x
            raindrops[i][0][1] = y
            raindrops[i][1] = new_speed

    print_to_screen("SLUG CITY", MAIN_FONT, 24, WHITE, screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 20), True, 4, 8, 2)
    print_to_screen("PRESENTS", MAIN_FONT, 12, WHITE, screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20), True, 4, 8, 2)
    print_to_screen("TEXTBOOK MYSTERIES", MAIN_FONT, 36, WHITE, screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), True, 12, 18, 4)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

# with open("TextbookMysteriesUserTest{}.log".format(now), "w+") as f:
#     sp.call('clear', shell=True)
#
#     print(Fore.WHITE + room_text["intro_text"]["first_line"])
#     input(Fore.GREEN + "< Press ANY KEY to continue >")
#
#     print(Fore.WHITE + room_text["intro_text"]["second_line"])
#     input(Fore.GREEN + "< Press ANY KEY to continue >")
#
#     print(Fore.WHITE + "\n{}\n".format(player.currentroom.intro_desc))
#
#     while player.is_alive and not player.victory:
#         action = input(Fore.GREEN + "> ")
#         f.writelines("> {}\n".format(action))
#         action = clean_input(action)
#         response = check_action(action, player)
#         print(Fore.WHITE + "\n{}".format(response))
#         f.writelines("{}\n".format(response))
