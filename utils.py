import json


def load_descriptions_file(file_name):
    with open(file_name, "r") as f:
        contents = json.load(f)
    return contents


def load_room_text(contents, room_name, text_type):
    return contents["room_text"][room_name][text_type]