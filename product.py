class Product:
    '''The product class is an abstraction for all products. Each product has a
     price, an ID, reviews, and total review score.'''

    def __init__(self, price, id, reviews):
        self.ID = id
        self.price = price
        self.reviews = reviews
        self.reviewScore = 0
        self.calcReviewScore(self)

    def calcReviewScore(self):
        score = 0.0
        for i in self.reviews:
            score += i
        score /= len(self.reviews)
        self.reviewScore = score
    '''Various get and set methods below, along with methods to manipulate the
     review list'''

    def getPrice(self):
        return self.price

    def getReviews(self):
        return self.reviews

    def getID(self):
        return self.ID

    def addReview(self, review):
        self.review.append(review)

    def deleteReview(self, review):
        self.review.remove(review)

    def setPrice(self, price):
        self.price = price

    def getReviewScore(self):
        return self.reviewScore
