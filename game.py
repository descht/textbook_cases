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

RAIN_COLOUR = GREY

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.init()


pygame.display.set_caption('Textbook Mysteries')
game_icon = pygame.image.load('magnifying_glass.png')
pygame.display.set_icon(game_icon)

# pygame.mixer.music.load("{}/NoirJazz_MH_V2_010219.mp3".format(music_folder))
# pygame.mixer.music.set_volume(0.8)
# pygame.mixer.music.play(-1)


channel1 = pygame.mixer.Channel(1)
game_sound = pygame.mixer.Sound("{}/rain_sound.ogg".format(sounds_folder))
channel1.play(game_sound, loops=-1)

MAIN_FONT = "8-bit pusab.ttf"
red_light = pygame.image.load("red_siren.png")
blue_light = pygame.image.load("blue_siren.png")

logo = pygame.image.load("sc_logo_white_v3.png")
logo_scaled = pygame.transform.rotozoom(logo, 0, 0.25)
k = 0

clock = pygame.time.Clock()
done = False

raindrops = []
x_speed = 5
y_speed = 50

for i in range(200):
    x = random.randrange(0, round(SCREEN_WIDTH + (SCREEN_HEIGHT * x_speed)/y_speed))
    y = random.randrange(-10, SCREEN_HEIGHT + 10)
    raindrops.append([[x, y], y_speed])

pause_screen = PauseScreen(screen, 160)

game_phase = 1
paused = False
intro_phase = 0
buffer = ""
response = ""

while not done and player.is_alive:
    timer = pygame.time.get_ticks() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if paused:
                pause_screen.update_cursor(event.key)
            elif game_phase == 0:
                game_phase = 1
            elif game_phase > 0:
                if intro_phase < 2:
                    intro_phase += 1
                elif event.key == pygame.K_ESCAPE:
                    if not paused:
                        paused = True
                elif not paused:
                    if event.key not in (pygame.K_KP_ENTER, pygame.K_RETURN):
                        buffer = update_buffer(buffer, event)
                    else:
                        action = clean_input(buffer)
                        response = check_action(action, player)
                        buffer = ""
                # print(input_text)

    screen.fill(BLACK)

    for i in range(len(raindrops)):
        pygame.draw.line(screen, RAIN_COLOUR, raindrops[i][0], (raindrops[i][0][0] - x_speed/5, raindrops[i][0][1] + raindrops[i][1]/5))
        if not paused:
            raindrops[i][0][0] -= x_speed
            raindrops[i][0][1] += raindrops[i][1]

        if raindrops[i][0][1] > (SCREEN_HEIGHT + 10):
            y = random.randrange(-50, -10)
            x = random.randrange(0, round(SCREEN_WIDTH + (SCREEN_HEIGHT * x_speed)/y_speed))
            new_speed = random.randrange(y_speed - 5, y_speed + 5)
            raindrops[i][0][0] = x
            raindrops[i][0][1] = y
            raindrops[i][1] = new_speed

    if -2 < game_phase < 1:
        if timer < 18:
            temp_print_to_screen(logo_scaled, None, 24, WHITE, screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80), True, 4, 8, 2)
            temp_print_to_screen("SLUG CITY", MAIN_FONT, 24, WHITE, screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), True, 4, 8, 2)
            temp_print_to_screen("PRESENTS", MAIN_FONT, 12, WHITE, screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40), True, 4, 8, 2)
            temp_print_to_screen("TEXTBOOK MYSTERIES", MAIN_FONT, 36, WHITE, screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), True, 12, 18, 4)
        else:
            print_to_screen("TEXTBOOK MYSTERIES", MAIN_FONT, 36, WHITE, screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), True)
            print_to_screen("Press any key to start", MAIN_FONT, 12, WHITE, screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40), True)
            game_phase = 0
    # elif game_phase == -2:
    #     print_to_screen("PAUSED", MAIN_FONT, 24, WHITE, screen, (SCREEN_WIDTH/2, 30), True)
    #     print_to_screen("Pause options", MAIN_FONT, 12, WHITE, screen, (SCREEN_WIDTH/2, 60), True)
    # elif game_phase == -3:
    #     print_to_screen("NOTEBOOK", MAIN_FONT, 24, WHITE, screen, (SCREEN_WIDTH/2, 30), True)
    #     print_to_screen("Notebook text goes here", MAIN_FONT, 12, WHITE, screen, (10, 60), False)
    elif game_phase == 1:
        if intro_phase == 0:
            print_to_screen(room_text["intro_text"]["first_line"], MAIN_FONT, 12, WHITE, screen, (10, 10), False)
            print_to_screen("< Press ANY KEY to continue >", MAIN_FONT, 16, GREEN, screen, (10, SCREEN_HEIGHT - 25), False)
        elif intro_phase == 1:
            print_to_screen(room_text["intro_text"]["second_line"], MAIN_FONT, 12, WHITE, screen, (10, 10), False)
            print_to_screen("< Press ANY KEY to continue >", MAIN_FONT, 16, GREEN, screen, (10, SCREEN_HEIGHT - 25), False)
        else:
            print_to_screen(player.currentroom.intro_desc, MAIN_FONT, 12, WHITE, screen, (10, 10), False)
            print_to_screen("> " + buffer, MAIN_FONT, 16, GREEN, screen, (10, SCREEN_HEIGHT - 25), False)
            if response:
                print_to_screen(response, MAIN_FONT, 12, GREEN, screen, (10, SCREEN_HEIGHT - 400), False)

    if paused:
        pause_screen.display()


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
