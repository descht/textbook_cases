import json
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (120, 120, 120)

font_folder = "fonts"
music_folder = "music"
sounds_folder = "sounds"


def load_descriptions_file(file_name):
    with open(file_name, "r") as f:
        contents = json.load(f)
    return contents


def load_room_text(contents, room_name, text_type):
    return contents["room_text"][room_name][text_type]


def print_to_screen(text, font, size, colour, screen, screen_pos, is_faded, fade_in_start, fade_out_start, fade_time):
    font_type = pygame.font.Font("{}/{}".format(font_folder, font), size)
    text_surface = font_type.render(text, True, colour)
    text_rect = text_surface.get_rect(center=screen_pos)

    if is_faded:
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
    else:
        screen.blit(text_surface, text_rect)

    return 0



