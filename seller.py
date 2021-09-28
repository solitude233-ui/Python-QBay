class Seller():
    """This class defines the attributes of a seller including
    the seller's inventory, customer reviews, history,
    average rating, and total number of ratings.
    """

    def __init__(self, inventory, reviews, history, rating, numRating):
        self.inventory = {}
        self.reviews = {}
        self.history = []
        self.rating = 0
        self.numRating = 0
