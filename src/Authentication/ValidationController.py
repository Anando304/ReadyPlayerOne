##  @file ValidationController.py
#  @author Anando Zaman
#  @brief Controller module for authentication
#  @date March 18, 2021

import sys
sys.path.insert(0, './')

# import firebase credentials and text reader input
from firebase.firebase_creds import firebase_class
from Authentication.LoginScreen import loginScreen
from Authentication.RegisterScreen import registerScreen
from Authentication.StartScreen import button_choice
from MainMenu.MainMenuController import MainMenuController

class ValidationController:
    def __init__(self):
        '''FIREBASE DB'''
        self.firebase_instance = firebase_class()
        self.db = self.firebase_instance.get_db()

    def display_StartScreen(self):
        button = button_choice()
        if button == "Login":
            # transition to login screen
            self.display_LoginScreen()

        elif button == "Register":
            # transition to register screen and pass the register method!
            # because of the nature of pygame, we can't really return without ending the program :(
            self.display_RegisterScreen()

    def display_RegisterScreen(self):
        isSuccuss = registerScreen(self.register)
        if isSuccuss:
            self.sendUserToMainMenu()

        # if return back, then redirect to start-screen once again
        self.display_StartScreen()

    def display_LoginScreen(self):
        isSuccuss = loginScreen(self.login)
        if isSuccuss:
            self.sendUserToMainMenu()
            return

        # if return back, then redirect to start-screen once again
        self.display_StartScreen()

    def sendUserToMainMenu(self):
        main_menu_controller = MainMenuController(self.firebase_instance, self.db)

        # transition control to main menu controller to display GameSelectionScreen
        main_menu_controller.display_GameSelectionScreen()

        # if return back, then redirect to start-screen once again
        self.display_StartScreen()

    # Used for login authentication
    def login(self, email, password):
        try:
            # register if new email
            self.firebase_instance.sign_in(email, password)
            # create username
            self.firebase_instance.set_username(email[:email.find('@')])
            print(self.db.get().val())

            # return True if succussfully authenticated
            return True

        except Exception as e:
            # print(e)
            print("Login failed")
            # Otherwise, return False
            return False

    # Used for Registeration of new account
    def register(self, email, password):
        try:
            # register if new email
            self.firebase_instance.sign_up(email, password)
            # create username
            self.firebase_instance.set_username(email[:email.find('@')])
            # create default score for games
            self.db.child("Users").child(self.firebase_instance.get_username()).update({"FlappyBird": 0})
            self.db.child("Users").child(self.firebase_instance.get_username()).update({"BasketballShootOut": 0})
            self.db.child("Users").child(self.firebase_instance.get_username()).update({"SpaceInvader": 0})
            self.db.child("Users").child(self.firebase_instance.get_username()).update({"Dodge": 0})
            self.db.child("Users").child(self.firebase_instance.get_username()).update({"FruitNinja": 0})
            print(self.db.get().val())

            # return True so that validation controller can transfer over to game screen
            return True


        except:
            print("Signup failed")
            return False


