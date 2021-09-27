class Transaction:
    """This class supports a few commonly used transaction functions like
    buying, selling and rating between the buyer and the seller.
    """

    def buy(buyer, seller, inventory, item):
        """Completes the buy transaction between buyer and seller.

        Verifies if the buyer has enough balance left to complete the
        purchase and if yes then deduct the buyer balance and increase
        the seller balance and leave the item information within
        the buyer and seller's purchase/sell history.

        """
        if buyer.balance >= item.price:
            buyer.balance -= item.price
            buyer.history.append(item)
            seller.balance += item.price
            seller.history.append(item)
            del seller.inventory[item.id]

    def sell(seller, productID, itemDescription):
        """Performs the sell transaction by the seller.

        Whenever the seller wants to sell an item, this function update the
        seller inventory with the item Id and the description of the item.
        """
        seller.inventory[productID] = itemDescription

    def rate(person1, person2, review, score, product):
        """Supports the rating system.

        Whenever person #2 rates person #1 with an optional review, this
        function appends the review to the person #1's review history and
        updates the total number of ratings and average ratings of person #1.
        """
        person1.reviews[person2] = [score, review]
        person1.rating = (person1.rating * person1.numRating + score) / (
            person1.numRating + 1
        )
        person1.numRating += 1
        product.append[review]
