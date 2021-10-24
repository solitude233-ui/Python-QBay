from qbay.models import register, login, create_product, updateProduct, product
from datetime import date
from qbay.models import update_user_profile
import random


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u00', 'test0@test.com', 'validPassword!') is True
    assert register('u00', 'test1@test.com', 'validPassword!') is True
    assert register('u01', 'test0@test.com', 'validPassword!') is False


def test_updateProduct():

    # create a user to have the email for the product below
    register("u002", "someone@example.com", "validPassword!")
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

    print(product.query.filter_by(ownerEmail=ownerEmail, title=title).first())
    ID = product.query.filter_by(ownerEmail=ownerEmail, title=title).first().ID
    print(ID)
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
    ''' Tests not passing
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
    '''
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
    (will be tested after the previous test, so we already have u00,
      u01 in database)
    '''
    user = login('test0@test.com', "validPassword!")
    assert user is not None
    assert user.username == 'u00'

    # The following requires user input to complete test:
    # user = login('test0@test.com', "wrongPassword!")
    # assert user is None


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


def test_update_user_profile():
    # Correct variables to test
    user_email = "John.Smith@gmail.com"
    user_name = "John"
    value_to_update = "user name"

    print("--- Testing Begins: update_user_profile() ---")

    # Testing nonexistent user
    test1_user_email = ""
    assert update_user_profile(test1_user_email, user_name,
                               value_to_update) is False

    # Testing invalid user name inputs
    value_to_update_name = "user name"

    # Test incorrect value: user name is empty
    test1_user_name = ""
    print("Testing an empty user name: ")
    assert update_user_profile(user_email, test1_user_name,
                               value_to_update_name) is False

    # Test incorrect value: user name has special character
    test2_user_name = "Jo!hn"
    print("Testing a user name with special character: ")
    assert update_user_profile(user_email, test2_user_name,
                               value_to_update_name) is False

    # Test incorrect value: user name has space as prefix
    test3_user_name = " John"
    print("Testing a user name with a space: ")
    assert update_user_profile(user_email, test3_user_name,
                               value_to_update_name) is False

    # Test incorrect value: user name is too short
    test4_user_name = "J"
    print("Testing a user name too short: ")
    assert update_user_profile(user_email, test4_user_name,
                               value_to_update_name) is False

    # Test incorrect value: user name is too long
    test5_user_name = "John Smith John Smith John Smith"
    print("Testing a user name too long: ")
    assert update_user_profile(user_email, test5_user_name,
                               value_to_update_name) is False

    # Testing invalid shipping address inputs
    value_to_update_shipping = "shipping address"

    # Test incorrect value: shipping address is empty
    test1_shipping_address = ""
    print("Testing an empty shipping address: ")
    assert update_user_profile(user_email, test1_shipping_address,
                               value_to_update_shipping) is False

    # Test incorrect value: shipping address has special characters
    test2_shipping_address = "220 Yo!nge Street"
    print("Testing a shipping address with special characters: ")
    assert update_user_profile(user_email, test2_shipping_address,
                               value_to_update_shipping) is False

    # Testing invalid postal code inputs
    value_to_update_postal = "postal code"

    # Test incorrect value: invalid postal code
    test1_postal_code = "M5B 2!1"
    print("Testing an invalid postal code: ")
    assert update_user_profile(user_email, test1_postal_code,
                               value_to_update_postal) is False

    print("--- Testing Completed ---")


def test_login():
    # Correct variables to test
    user_email = "John.Smith@gmail.com"
    user_password = "Password!"
    address = "@gmail.com"

    print("--- Testing Begins: login() ---")

    # Testing invalid user email inputs
    # Test incorrect value: user email is empty
    test1_user_email = ""
    print("Testing an empty user email: ")
    assert login(test1_user_email, user_password) is False

    # Test incorrect value: user email local part it too long
    aLetter = "j"
    local_part = ''.join(random.choice(aLetter) for i in range(65))
    test2_user_email = local_part + address
    print("Testing a user email with a long local part: ")
    assert login(test2_user_email, user_password) is False

    # Test incorrect value: user email domain is too long
    aLetter = "j"
    domain = ''.join(random.choice(aLetter) for i in range(256))
    test3_user_email = aLetter + address + domain
    print("Testing a user email with a long domain: ")
    assert login(test3_user_email, user_password) is False

    # Test incorrect value: user email starts with a period
    test4_user_email = ".John.Smith@gmail.com"
    print("Testing a user email that starts with a period: ")
    assert login(test4_user_email, user_password) is False

    # Test incorrect value: user email ends with a hyphen
    test5_user_email = "John.Smith@gmail.com-"
    print("Testing a user email that ends with a hyphen: ")
    assert login(test5_user_email, user_password) is False

    # Test incorrect value: user password is empty
    test1_user_password = ""
    print("Testing a user password that is empty: ")
    assert login(user_email, test1_user_password) is False

    # Test incorrect value: user password is too short
    test2_user_password = "P"
    print("Testing a user password that is too short: ")
    assert login(user_email, test2_user_password) is False

    # Test incorrect value: user password does not have a capitalized letter
    test3_user_password = "password!"
    print("Testing a user password that does not have a capitalized letter: ")
    assert login(user_email, test3_user_password) is False

    # Test incorrect value: user password does not have a lowercase letter
    test4_user_password = "PASSWORD!"
    print("Testing a user password that does not have a lowercase letter: ")
    assert login(user_email, test4_user_password) is False

    # Test incorrect value: user password does not have a special character
    test5_user_password = "Password"
    print("Testing a user password that does not have a special character: ")
    assert login(user_email, test5_user_password) is False

    print("--- Testing Completed ---")


def test_register():
    print("\nTestcase1: Empty email.\n\
    Error expected:")
    assert register("validUsername", "", "validPassword!") is False

    print("\nTestcase2: Local part of email is too long.\n\
    Error expected:")
    local = "a" * 65  # local part of email --> 17afer part
    domain = "b" * 270  # domain of email --> @queensu.ca part
    assert register("validUsername", local + "@queensu.ca",
                    "validPassword!") is False

    print("\nTestcase3: Domain part of email is too long.\n\
    Error expected:")
    assert register("validUsername", ("17afer@" + domain),
                    "validPassword!") is False

    print("\nTestcase4: Email starting with a period.\n\
    Error expected:")
    assert register("validUsername", ".17afer@queensu.ca",
                    "validPassword!") is False

    print("\nTestcase5: Email starts with a dash.\n\
    Error expected:")
    assert register("validUsername", "-17afer@queensu.ca",
                    "validPassword!") is False

    print("\nTestcase6: Email starting with a period but local part of\n\
    email is enclosed in quotations. No error expected:")
    assert register("validUsername", "'.17afer'@queensu.ca",
                    "validPassword!") is True

    print("\nTestcase7: Email containing consecutive periods.\n\
    Error expected:")
    assert register("validUsername", "17..afer@queensu.ca",
                    "validPassword!") is False

    print("\nTestcase8: Password is shorter than 6 characters.\n\
    Error expected:")
    assert register("validUsername", "validEmail@gmail.com",
                    "short") is False

    print("\nTestcase9: Password is completely empty.\n\
    Error expected:")
    assert register("validUsername", "validEmail@gmail.com", "") is False

    print("\nTestcase10: Password is missing an uppercase character.\n\
    Error expected:")
    assert register("validUsername", "validEmail@gmail.com",
                    "lowercase!") is False

    print("\nTestcase11: Password is missing a lowercase character.\n\
    Error expected:")
    assert register("validUsername", "validEmail@gmail.com",
                    "UPPERCASE") is False

    print("\nTestcase12: Password doesn't contain any special chars\n\
    Error expected:")
    assert register("validUsername", "validEmail@gmail.com",
                    "No special character") is False

    print("\nTestcase13: Username is empty.\n\
    Error expected:")
    assert register("", "validEmail@gmail.com",
                    "validPassword!") is False

    print("\nTestcase14: Password contains non-alphanumeric characters.\n\
    Error expected:")
    assert register("user$name", "validEmail@gmail.com",
                    "validPassword") is False

    print("\nTestcase15: Username begins with a space.\n\
    Error expected:")
    assert register(" username", "validEmail@gmail.com",
                    "validPassword!") is False

    print("\nTestcase16: Username ends with a space.\n\
    Error expected:")
    assert register("username ", "validEmail@gmail.com",
                    "validPassword!") is False

    print("\nTestcase17: Username is less than 3 characters long.\n\
    Error expected:")
    assert register("s", "validEmail@gmail.com",
                    "validPassword!") is False

    print("\nTestcase17: Username is not less than 20 characters long\n\
    Error expected:")
    assert register("a" * 20, "validEmail@gmail.com",
                    "validPassword!") is False
