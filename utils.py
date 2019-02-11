import json
import pygame
import string

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (120, 120, 120)
GREEN = (50, 205, 50)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "

font_folder = "fonts"
music_folder = "music"
sounds_folder = "sounds"


def load_descriptions_file(file_name):
    with open(file_name, "r") as f:
        contents = json.load(f)
    return contents


def load_room_text(contents, room_name, text_type):
    return contents["room_text"][room_name][text_type]


def render_text(text, font, size, colour, screen_pos, centered):
    font_type = pygame.font.Font("{}/{}".format(font_folder, font), size)
    text_surface = font_type.render(text, True, colour)

    if centered:
        text_rect = text_surface.get_rect(center=screen_pos)
    else:
        text_rect = text_surface.get_rect(topleft=screen_pos)

    return text_rect, text_surface


def temp_print_to_screen(text, font, size, colour, screen, screen_pos, centered, fade_in_start, fade_out_start, fade_time):
    text_rect, text_surface = render_text(text, font, size, colour, screen_pos, centered)

    fade_surf = pygame.Surface((text_rect.width, text_rect.height))

    timer = pygame.time.get_ticks() / 1000
    if fade_in_start < timer < fade_in_start + fade_time:
        alpha = 1 - (fade_in_start + fade_time - timer)/fade_time
    elif fade_in_start + fade_time <= timer <= fade_out_start:
        alpha = 1
    elif fade_out_start < timer < fade_out_start + fade_time:
        alpha = (fade_out_start + fade_time - timer)/fade_time
    else:
        alpha = 0

    fade_surf.set_alpha(255 * alpha)
    fade_surf.blit(text_surface, (0, 0))
    screen.blit(fade_surf, text_rect)

    return 0


def print_to_screen(text, font, size, colour, screen, screen_pos, centered):
    lines = text.split("\n")
    formatted_lines = []
    font_type = pygame.font.Font("{}/{}".format(font_folder, font), size)
    for line in lines:
        words = line.split(" ")
        formatted_line = ""
        for word in words:
            test_line = formatted_line + word + " "
            if font_type.size(test_line)[0] < SCREEN_WIDTH - 20:
                formatted_line = test_line
            else:
                formatted_lines.append(formatted_line)
                formatted_line = word + " "
        formatted_lines.append(formatted_line)
        formatted_lines.append(" ")

    for line in range(len(formatted_lines)):
        text_rect, text_surface = render_text(formatted_lines[line], font, size, colour, (screen_pos[0], screen_pos[1]+(line*size)+(15*line)), centered)

        screen.blit(text_surface, text_rect)

    return 0


def update_buffer(buffer, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            if buffer:
                buffer = buffer[:-1]
        elif event.unicode in ACCEPTED:
            buffer += event.unicode

    return buffer


