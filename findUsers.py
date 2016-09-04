__author__ = 'maxomdal'

# Union Algorithm

from User import *
from Restaurant import *


class UserFinder:  # Uses a list of randomly Chosen restaurants to select users to compare ratings with
    restaurantArrData = []  # restaurants to be checked to restaurant's the host has eaten at
    checkedUsers = []  # users who have already been compared

    def __init__(self, restaurantArrData):
        print "Initiating UserFinder Class"
        self.restaurantArrData = restaurantArrData

    def appendToCheckedUsers(self, checkedUser):
        print checkedUser.getUsername() + " will be added to checkedUsers"
        self.checkedUsers.append(checkedUser)

    def checkUsers(self):
        for restaurant in self.restaurantArrData:
            for user in restaurant.usersWithRatings:
                if user not in self.checkedUsers:
                    print "This new user will be checked: " + user.getUsername()
                    for restaurant2 in self.restaurantArrData:
                        if user.hasRating(restaurant2.dataID):
                            print "User " + user.getUsername() + " has reviewed " + restaurant2.dataID
                            user.unionCount += 1
                    self.appendToCheckedUsers(user)
                else:
                    print "This user, " + user.getUsername() + " has already been checked. Moving on to next user."
                    break
            print restaurant.dataID + " has been checked"

        highUnionUsers = self.checkedUsers
        return highUnionUsers

# All of this here is for the sake of testing. Provides no functionality
UserA = User({"A": 1, "B": 2, "C": 3}, "noah")
UserB = User({"A": 2, "B": 1, "C": 2}, "maxwell")
UserC = User({"A": 3, "B": 3}, "tammy")
RestaurantA = Restaurant({UserA: 1, UserB: 2, UserC: 3}, "A")
RestaurantB = Restaurant({UserA: 2, UserB: 1, UserC: 3}, "B")
RestaurantC = Restaurant({UserA: 3, UserB: 2}, "C")

finder = UserFinder([RestaurantA, RestaurantB, RestaurantC])

print finder.checkUsers()[1].unionCount
