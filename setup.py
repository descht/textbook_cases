import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["player", "time", "pygame", "utils", "objects", "rooms", "items"], "excludes": [], "include_files": ["room_description.json", "magnifying_glass.png", "fonts/8-bit pusab.ttf", "music/NoirJazz_MH_V2_010219.mp3", "sounds/rain_sound.ogg"]}

base=None
if sys.platform == "win32":
	# base = "Win32GUI"
	pass

setup( name = "Textbook Mysteries",
	version = "0.1",
	description = "My game",
	options = {"build.exe": build_exe_options},
	executables = [Executable("game.py", base=base)])
