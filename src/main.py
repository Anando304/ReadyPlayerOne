##  @file main.py
#  @author Anando Zaman
#  @brief Main module for execution
#  @date March 21, 2021

import sys
import os
import platform

# change directory
sys.path.insert(0, './')
os.chdir(os.getcwd() + "/Authentication")
cwd = os.getcwd()

# display driver setup if on Linux
if platform.system() == "Linux":
    try:
        os.environ["DISPLAY"]
    except:
        os.environ["SDL_VIDEODRIVER"] = "dummy"

# import Controller
from Authentication.ValidationController import ValidationController

# Execute controller to begin program
Controller = ValidationController()
Controller.display_StartScreen()