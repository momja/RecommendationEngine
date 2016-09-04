__author__ = 'maxomdal'

# Restaurant Class

class Restaurant:
    ratings = []  # dictionary of User:int
    usersWithRatings = []  # holds User class object
    dataID = ""

    def __init__(self, ratings, dataID):
        print "Initiating Restaurant Class"
        self.ratings = ratings
        self.usersWithRatings = ratings.keys()
        self.dataID = dataID

    def checkForUser(self, userID):
        if userID in self.usersWithRatings:
            return True
        else:
            return False

    def getUserRating(self, user):
        return self.ratings[user]
