#This class stores the information related to the user's buyer account
class buyer():

    def __init__(self, purchaseHistory, activeAuctions, savedSellers, recentlyViewed, watchList):
        self.purchaseHistory = [] #past purchases made from the user's buyer account
        self.activeAuctions = []  #current auctions the user is taking part in
        self.savedSellers = [] #'favorites' list of sellers for the user
        self.recentlyViewed = [] #stores the top 10 most recently viewed items
        self.watchList = [] #users can add items to their watch list to automatically recieve updates on them

#This class is responsible for storing the users account information      
class user():

    def __init__(self, username, password, accountBalance):
        self.username = ""
        self.password = ""
        self.accountBalance = 0 


