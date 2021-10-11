from qbay.models import register, login, create_product, updateProduct, product
from datetime import date


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u0', 'test0@test.com', '123456') is True
    assert register('u0', 'test1@test.com', '123456') is True
    assert register('u1', 'test0@test.com', '123456') is False


def test_updateProduct():
    # create a user to have the email for the product below
    register("u002", "someone@exmaple.com", "123456")
    
    # create a valid product to be used for some test cases, eg title collision
    create_product("Smartphone", "The best smartphone money can buy", 999.99,
                   date(2022, 4, 15), "someone@example.com")
    ID = 30
    newID = 30
    title = "Title"
    description = "A description longer than title, for a great product"
    price = 35.50
    ownerEmail = "someone@example.com"
    create_product(title, description, price, date(2022, 4, 15),
                   "someone@example.com")
    ID = product.query.filter_by(ownerEmail=ownerEmail, title=title).first().ID
    # All params valid

    # Title not valid - too long
    title += "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    title += "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    # Title not valid - not alphanum
    title = "not alphanumeric!"
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    # Title not valid - space as prefix
    title = " space as prefix"
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    # Title not valid - space as suffix
    title = "space as suffix "
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    # Title not valid, already exists
    title = "Smartphone"
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    # description not valid - To short <20 chars
    description = "<20chars"
    title = "A Valid Title"
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    # description not valid - Shorter than title
    title = "A shorter title"
    description = "Short description here"
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    # description not valid - too long
    for i in range(60):
        description += "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    # Price not valid - too low
    description = "A Valid description"
    price = 5.0
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    # Price not valid - too high
    price = 20000.0
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    # Price not valid - lower than current price
    price = 25.0
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False
    price = 40.0

    # newID not valid, already exists
    newID = product.query.filter_by(title="Smartphone").first().ID
    assert updateProduct(ID, newID, title, description, price,
                         ownerEmail) is False


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test, so we already have u0,
      u1 in database)
    '''

    user = login('test0@test.com', 123456)
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', 1234567)
    assert user is None


def test_create_product():
    """
    Testing the create_product function.
    In this function, different test cases will be created to test out all the
    constraints under title, description, price, date and email address.
    """
    # Create a list of correct variables
    correct_title = "smartwatch"
    correct_description = "A small smartphonelike device worn on wrist."
    correct_price = 50
    correct_date = date(2020, 10, 5)
    correct_email = "abc@gmail.com"
    # Test incorrect alphanumeric title
    test_title_1 = "wrong, title"
    product_1 = create_product(test_title_1, correct_description,
                               correct_price, correct_date, correct_email)
    assert product_1 is None
    # Test incorrect title with space prefix
    test_title_2 = " wrongtitle"
    product_2 = create_product(test_title_2, correct_description,
                               correct_price, correct_date, correct_email)
    assert product_2 is None
    # Test incorrect title with space suffix
    test_title_3 = "wrongtitle "
    product_3 = create_product(test_title_3, correct_description,
                               correct_price, correct_date, correct_email)
    assert product_3 is None
    # Test incorrect title longer than 80 characters (81)
    test_title_4 = ""
    k = 0
    while k <= 80:
        test_title_4 += "a"
        k += 1
    product_4 = create_product(test_title_4, correct_description,
                               correct_price, correct_date, correct_email)
    assert product_4 is None

    # Test description less than 20 characters (19)
    test_des_1 = ""
    i = 1
    while i < 20:
        test_des_1 += "a"
        i += 1
    product_5 = create_product(correct_title, test_des_1,
                               correct_price, correct_date, correct_email)
    assert product_5 is None
    # Test description more than 2000 characters (2001)
    test_des_2 = ""
    j = 1
    while j < 2002:
        test_des_2 += "a"
        j += 1
    product_6 = create_product(correct_title, test_des_2,
                               correct_price, correct_date, correct_email)
    assert product_6 is None
    # Test when description is shorter than title
    test_des_3 = "smartwatc"
    product_7 = create_product(correct_title, test_des_3,
                               correct_price, correct_date, correct_email)
    assert product_7 is None
    # Test correct description length, should return nothing
    product_8 = create_product(correct_title, correct_description,
                               correct_price, correct_date, correct_email)
    assert product_8 is None

    # Test price out of range (< 10)
    test_price_1 = 9
    product_10 = create_product(correct_title, correct_description,
                                test_price_1, correct_date, correct_email)
    assert product_10 is None
    # Test price out of range (> 10000)
    test_price_2 = 10001
    product_11 = create_product(correct_title, correct_description,
                                test_price_2, correct_date, correct_email)
    assert product_11 is None

    # Test last modified date (wrong year before 2021)
    test_date_1 = date(2020, 1, 3)
    product_12 = create_product(correct_title, correct_description,
                                correct_price, test_date_1, correct_email)
    assert product_12 is None
    # Test last modified date (wrong year after 2025)
    test_date_2 = date(2025, 1, 3)
    product_13 = create_product(correct_title, correct_description,
                                correct_price, test_date_2, correct_email)
    assert product_13 is None
    # Test last modified date (wrong month in year 2025)
    test_date_3 = date(2025, 2, 1)
    product_14 = create_product(correct_title, correct_description,
                                correct_price, test_date_3, correct_email)
    assert product_14 is None
    # Test last modified date (wrong day in year 2025 and month 01)
    test_date_4 = date(2025, 1, 3)
    product_15 = create_product(correct_title, correct_description,
                                correct_price, test_date_4, correct_email)
    assert product_15 is None

    # Test empty email
    test_email = ""
    product_16 = create_product(correct_title, correct_description,
                                correct_price, correct_date, test_email)
    assert product_16 is None
    # Check if owner exists in the database given email
    test_email_2 = "nonexistedemail@gmail.com"
    product_17 = create_product(correct_title, correct_description,
                                correct_price, correct_date, test_email_2)
    assert product_17 is None

    # Check if the product being created has the same title under the same user
    # sample_username = "useruser"
    # sample_password = "password"
    # Create a user in the database
    # new_user = register(sample_username, correct_email, sample_password)
    # Create a product under the user
    create_product(correct_title, correct_description,
                   correct_price, correct_date, correct_email)
    # Attempts to create the same product title under the same user again
    product_18 = create_product(correct_title, correct_description,
                                correct_price, correct_date, correct_email)
    assert product_18 is None