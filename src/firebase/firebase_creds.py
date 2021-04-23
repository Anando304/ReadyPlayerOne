import pyrebase

class firebase_class:
    def __init__(self):
        # firebase stuff
        self.config = {
            "apiKey": "AIzaSyAfU6MKWJDmKR8yn7McUUeICF-B1di_00s",
            "authDomain": "a04-d50d2.firebaseapp.com",
            "databaseURL": "https://a04-d50d2-default-rtdb.firebaseio.com/",
            "projectId": "a04-d50d2",
            "storageBucket": "a04-d50d2.appspot.com",
            "messagingSenderId": "313059523252",
            "appId": "1:313059523252:web:58bbadf5a0ac2acdc3f5e1"
        }

        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        # firebase instance of user
        self.user = None
        # string containing username
        self.username = None
        self.db = self.firebase.database()

    ## @brief Getter method to retrieve DB instance
    #  @details Gets reference to database
    #  @return Returns a firebase DB object
    def get_db(self):
        return self.db

    ## @brief Setter method sign-in a user and update the user-field.
    #  @param email: string value representing email address
    #  @param password: string value representing password
    # @details Authenticates the user and creates a session.
    def sign_in(self, email, password):
        self.user = self.auth.sign_in_with_email_and_password(email, password)

    ## @brief Setter method that creates an account for the user
    #  @param email: string value representing email address
    #  @param password: string value representing password
    # @details Authenticates the user and creates a session.
    def sign_up(self, email, password):
        self.user = self.auth.create_user_with_email_and_password(email, password)

    ## @brief Getter method used for user instance.
    #  @details  Useful for signing out and identifying the user-ID(UID) of a given user.
    #  @return Returns String representing the UID of the current logged-in user. Otherwise, returns None
    def get_user_instance(self):
        return self.user

    ## @brief Getter method that retrieves the username
    #  @return Returns the username, if user field is populated ONCE user is authenticated. Otherwise, returns None
    def get_username(self):
        return self.username

    ## @brief Setter method that updates the local username
    #  @param username: string value representing username
    #  @details Updates the local_username during authentication, to use with the rest of the app
    def set_username(self, username):
        self.username = username

    ## @brief Getter method to retreive UID
    # @details Gets the Unique userID if the user is authenticated.
    # @return Returns the UID string
    def get_UID(self):
        if self.user:
            return self.auth.get_account_info(self.user['idToken'])["users"][0]['localId']
        return None


    def GetLocalHighScore(self, game):
        user_highscore = self.db.child("Users").child(self.get_username()).child(
            game).get().val()
        return user_highscore

    # Updates highscore and returns the value, otherwise just returns the highscore
    def UpdateLocalHighScore(self, game, score):
        user_highscore = max(self.GetLocalHighScore(game), score)
        self.db.child("Users").child(self.get_username()).update(
            {game: user_highscore})
        return user_highscore

    # returns the global highscore for a given game
    def GetGlobalHighScore(self, game):
        data = self.db.child("Games").child(game).get().val()

        global_highscore_user, global_highscore = "None", 0
        if data:
            data = dict(data.items())
            global_highscore_user = list(data.keys())[0]
            global_highscore = list(data.values())[0]

        return global_highscore_user, global_highscore

    # updates and returns the highscore for a given game
    def UpdateGlobalHighScore(self, game, score):
        data = self.db.child("Games").child(game).get().val()

        # if global score data exists for the specific game
        if data:
            data = dict(data.items())
            global_highscore_user = list(data.keys())[0]
            global_highscore = list(data.values())[0]

            # replace with our score if it is greater
            if global_highscore < score:
                global_highscore = score
                global_highscore_user = self.get_username()
                print("Succussfully updated highscore for", game)

            self.db.child("Games").child(game).set({global_highscore_user: global_highscore})
            return global_highscore_user, global_highscore

        # if branch doesnt exist for whatever reason, create a highscore branch for the game
        else:
            user = self.get_username()
            self.db.child("Games").child(game).set({user: score})
            print("Succussfully updated highscore for", game)
            return user, score

    def GetScoreList(self):
        data = self.db.child("Games").get().val()
        return dict(data.items())

    def GetGameList(self):
        data = self.db.child("Games").get().val()
        return list(dict(data.items()).keys())
