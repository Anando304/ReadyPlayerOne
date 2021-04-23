##  @file MainMenuController.py
#  @author Anando Zaman
#  @brief Controller module for game selection
#  @date March 18, 2021

import sys
sys.path.insert(0, './')

from MainMenu.GameSelectionScreen import GameSelectionScreen
from MainMenu.HighScoreScreen import HighScoreScreen
from InGame.basketballShootOut.GameStateController import GameStateController as BasketBall_controller
from InGame.Dodge.GameStateController import GameStateController as Dodge_controller
from InGame.FruitNinja.GameStateController import GameStateController as Fruit_controller
from InGame.FlappyBird.GameStateController import GameStateController as FlappyBird_controller
from InGame.SpaceInvaders.GameStateController import GameStateController as SpaceInvaders_controller

# MainMenu Controller Class
# Constructor contains firebase instance & db to retrieve/update scores
# Constructor also contains an instance of each of the other game controllers in order to retrieve info
class MainMenuController:
    def __init__(self,firebase_instance,db):
        '''FIREBASE DB'''
        self.firebase_instance = firebase_instance
        self.db = db
        self.basketball_controller = BasketBall_controller(self.firebase_instance,self.db)
        # TODO Fill out other game controllers here!
        self.dodge_controller = Dodge_controller(self.firebase_instance, self.db)
        self.Fruit_controller = Fruit_controller(self.firebase_instance, self.db)
        self.FlappyBird_controller = FlappyBird_controller(self.firebase_instance, self.db)
        self.SpaceInvaders_controller = SpaceInvaders_controller(self.firebase_instance, self.db)
        self.game5_controller = None


    def display_GameSelectionScreen(self):
        selection = GameSelectionScreen()

        # go back to main startup screen
        if selection == "back_button":
            return

        # go back to highscore screen
        elif selection == "score_button":
            self.display_HighscoreScreen()

        # otherwise, if valid game name returned
        elif selection:
            self.StartGame(selection)

        # otherwise return to startup screen if nothing!
        return

    def display_HighscoreScreen(self):
        selection = HighScoreScreen(self.GetGameList,self.GetScoreList)

        # if exited highscore screen and returned back to mainmenu
        if selection == "back_button":
            self.display_GameSelectionScreen()

        # otherwise exit if something else
        return

    # Retrieve scoreList of games from DB
    def GetScoreList(self):
        return self.firebase_instance.GetScoreList()

    # Retrieve GameList of games from DB
    def GetGameList(self):
        return self.firebase_instance.GetGameList()

    # Retrieve GlobalHighScore for a game
    def GetGlobalHighScore(self, game):
        return self.firebase_instance.GetGlobalHighScore(game)

    # Retrieve GlobalHighScore for a game
    def FindScoreTable(self):
        return self.firebase_instance.GetScoreList()

    # Execute a game using the respective game controller
    def StartGame(self, game):

        if game == "BasketballShootOut":
            self.basketball_controller.display_GameScreen()

        elif game == "Dodge":
            self.dodge_controller.display_GameScreen()

        elif game == "fruitninja":
            self.Fruit_controller.display_GameScreen()
        elif game == "FlappyBird":
            self.FlappyBird_controller.display_GameScreen()

        elif game == "SpaceInvaders":
            self.SpaceInvaders_controller.display_GameScreen()

        elif game == "game5":
            pass

        # if returned from a game, display GameSelectionScreen
        self.display_GameSelectionScreen()
        return



