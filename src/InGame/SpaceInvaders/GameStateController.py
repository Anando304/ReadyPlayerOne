## @file GameStateController.py
# @author David Yao
# @brief Controller module for Space Invaders
# @date April 13, 2021
import sys
sys.path.insert(0, './')

from InGame.SpaceInvaders.SpaceInvaders import startGame
from InGame.Pause.pauseScreen import pauseScreen
from InGame.Instruction.instructionScreen import instructionScreen

# GameStateController Controller Class
# Constructor contains firebase instance & db to retrieve/update scores
# Constructor also contains runningState flag for play/exit boolean statuses
class GameStateController:
    def __init__(self, firebase_instance, db):
        self.firebase_instance = firebase_instance
        self.db = db
        self.runningState = True

    #Display gameplay screen
    def display_GameScreen(self):
        state = startGame(self.UpdateLocalHighScore, self.UpdateGlobalHighScore, self.runningState)

        if state == "pause":
            self.runningState = True
            self.display_PauseScreen()
        
        else:
            self.runningState = False
        
        return

    #Display pause screen
    def display_PauseScreen(self):
        state = pauseScreen()

        if state == "resume":
            self.runningState = True
            self.display_GameScreen()

        elif state == "instruction":
            self.display_InstructionScreen()

        elif state == "quit":
            self.runningState = False
            return

    # Display instruction screen
    def display_InstructionScreen(self):
        state = instructionScreen("spaceinvader")
        if state == "back":
            self.display_PauseScreen()
            return

    # Return the local highscore of the user
    def GetLocalHighScore(self):
        user_highscore = self.firebase_instance.GetLocalHighScore("SpaceInvader")
        return user_highscore

    # Update(if possible) & return the local highscore of the user
    def UpdateLocalHighScore(self, score):
        user_highscore = self.firebase_instance.UpdateLocalHighScore("SpaceInvader", score)
        return user_highscore

    # Update(if possible) & return the global highscore of the game
    def UpdateGlobalHighScore(self, score):
        user, score = self.firebase_instance.UpdateGlobalHighScore("SpaceInvader",score)
        return user, score