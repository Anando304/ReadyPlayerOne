##  @file GameStateController.py
#  @author Qiushi xu
#  @brief Controller module for GamePlay of Basketball shootout
#  @date April 12, 2021

import sys
sys.path.insert(0, './')
from InGame.FruitNinja.FruitNinja import startGame
from InGame.Pause.pauseScreen import pauseScreen
from InGame.Instruction.instructionScreen import instructionScreen


# GameStateController Controller Class
# Constructor contains firebase instance & db to retrieve/update scores
# Constructor also contains runningState flag for play/exit boolean statuses
class GameStateController:
    def __init__(self,firebase_instance,db):
        '''FIREBASE DB'''
        self.firebase_instance = firebase_instance
        self.db = db
        self.runningState = True

    # Transition to the gameplay screen
    def display_GameScreen(self):
        # Pass the Score updating functions so that we can call these functions from within game screen once it ends
        state = startGame(self.UpdateLocalHighScore, self.UpdateGlobalHighScore, self.runningState)

        # show pause screen
        if state == "pause":
            self.runningState = True
            self.display_PauseScreen()

        # Otherwise, quit the game and return to MainMenuController
        else:
            self.runningState = False
        return

    # Transition to the pause screen
    def display_PauseScreen(self):
        state = pauseScreen()
        # if "resume" status found from pauseScreen, transition back to the game
        if state == "resume":
            self.display_GameScreen()

        elif state == "instruction":
            self.display_InstructionScreen()

        # Otherwise, return to game selection screen
        elif state == "quit":
            self.runningState = False
            return

    # Transition to the Instruction screen
    def display_InstructionScreen(self):
        state = instructionScreen("FruitNinja")
        if state == "back":
            self.display_PauseScreen()
            return

    # Return the local highscore of the user
    def GetLocalHighScore(self):
        user_highscore = self.firebase_instance.GetLocalHighScore("FruitNinja")
        return user_highscore

    # Update(if possible) & return the local highscore of the user
    def UpdateLocalHighScore(self, score):
        user_highscore = self.firebase_instance.UpdateLocalHighScore("FruitNinja", score)
        return user_highscore

    # Update(if possible) & return the global highscore of the game
    def UpdateGlobalHighScore(self, score):
        user, score = self.firebase_instance.UpdateGlobalHighScore("FruitNinja",score)
        return user, score


