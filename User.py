__author__ = 'maxomdal'

# User Class

class User:
    ratings = {}
    username = ""
    unionCount = 0

    def __init__(self, ratings, username):
        print "Initiating User Class"
        self.ratings = ratings
        self.username = username

    def hasRating(self, restaurantID):
        if restaurantID in self.ratings.keys():
            return True
        return False

    def getRating(self, restaurantID):
        return self.ratings[restaurantID]

    def getUsername(self):
        return self.username
