#This class stores the information related to the user's buyer account
class Buyer():

    def __init__(self, purchaseHistory, activeAuctions, savedSellers,
                 recentlyViewed, watchList):
        purchaseHistory = [] #past purchases made
        activeAuctions = []  #current auctions the user is taking part in
        savedSellers = [] #'favorites' list of sellers for the user
        recentlyViewed = [] #stores the top 10 most recently viewed items
        watchList = [] #users can add items to their watch list


#This class is responsible for storing the users account information    
class User():

    def __init__(self, username, password, accountBalance):
    	username = ""
    	password = ""
    	accountBalance = 0 
