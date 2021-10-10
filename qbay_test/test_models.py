from qbay.models import register, login, create_product, update_user_profile
import random


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
    correct_date = "2021-10-05"
    correct_email = "abc@gmail.com"
    # Test incorrect alphanumeric title
    test_title_1 = "wrong, title"
    print(create_product(test_title_1, correct_description,
                         correct_price, correct_date, correct_email))
    print("--------------------------------------------------------")
    # Test incorrect title with space prefix
    test_title_2 = " wrongtitle"
    print(create_product(test_title_2, correct_description,
                         correct_price, correct_date, correct_email))
    print("--------------------------------------------------------")
    # Test incorrect title with space suffix
    test_title_3 = "wrongtitle "
    print(create_product(test_title_3, correct_description,
                         correct_price, correct_date, correct_email))
    print("--------------------------------------------------------")
    # Test incorrect title longer than 80 characters (81)
    test_title_4 = ""
    k = 0
    while k <= 80:
        test_title_4 += "a"
        k += 1
    print(create_product(test_title_4, correct_description,
                         correct_price, correct_date, correct_email))
    print("--------------------------------------------------------")

    # Test description less than 20 characters (19)
    test_des_1 = ""
    i = 1
    while i < 20:
        test_des_1 += "a"
        i += 1
    print(create_product(correct_title, test_des_1,
                         correct_price, correct_date, correct_email))
    print("--------------------------------------------------------")
    # Test description more than 2000 characters (2001)
    test_des_2 = ""
    j = 1
    while j < 2002:
        test_des_2 += "a"
        j += 1
    print(create_product(correct_title, test_des_2,
                         correct_price, correct_date, correct_email))
    print("--------------------------------------------------------")
    # Test when description is shorter than title
    test_des_3 = "smartwatc"
    print(create_product(correct_title, test_des_3,
                         correct_price, correct_date, correct_email))
    print("--------------------------------------------------------")
    # Test correct description length, should return nothing
    print(create_product(correct_title, correct_description,
                         correct_price, correct_date, correct_email))
    print("--------------------------------------------------------")

    # Test price out of range (< 10)
    test_price_1 = 9
    print(create_product(correct_title, correct_description,
                         test_price_1, correct_date, correct_email))
    print("--------------------------------------------------------")
    # Test price out of range (> 10000)
    test_price_2 = 10001
    print(create_product(correct_title, correct_description,
                         test_price_2, correct_date, correct_email))
    print("--------------------------------------------------------")

    # Test last modified date (wrong year before 2021)
    test_date_1 = "2020-01-03"
    print(create_product(correct_title, correct_description,
                         correct_price, test_date_1, correct_email))
    print("--------------------------------------------------------")
    # Test last modified date (wrong year after 2025)
    test_date_2 = "2025-01-03"
    print(create_product(correct_title, correct_description,
                         correct_price, test_date_2, correct_email))
    print("--------------------------------------------------------")
    # Test last modified date (wrong month in year 2025)
    test_date_3 = "2025-02-01"
    print(create_product(correct_title, correct_description,
                         correct_price, test_date_3, correct_email))
    print("--------------------------------------------------------")
    # Test last modified date (wrong day in year 2025 and month 01)
    test_date_4 = "2025-01-03"
    print(create_product(correct_title, correct_description,
                         correct_price, test_date_4, correct_email))
    print("--------------------------------------------------------")

    # Test empty email
    test_email = ""
    print(create_product(correct_title, correct_description,
                         correct_price, correct_date, test_email))
    print("--------------------------------------------------------")

    # Check if owner exists in the database given email
    test_email_2 = "nonexistedemail@gmail.com"
    print(create_product(correct_title, correct_description,
                         correct_price, correct_date, test_email_2))
    print("--------------------------------------------------------")

    # Check if the product being created has the same title under the same user
    sample_username = "useruser"
    sample_password = "password"
    # Create a user in the database
    new_user = register(sample_username, correct_email, sample_password)
    # Create a product under the user
    print(create_product(correct_title, correct_description,
                         correct_price, correct_date, correct_email))
    print("--------------------------------------------------------")
    # Attempts to create the same product title under the same user again
    print(create_product(correct_title, correct_description,
                         correct_price, correct_date, correct_email))


def test_update_user_profile():
    # Correct variables to test
    user_email = "John.Smith@gmail.com"
    user_name = "John"
    shipping_address = "220 Yonge Street"
    postal_code = "M5B 2H1"
    value_to_update = None

    print("--- Testing Begins: update_user_profile() ---")

    # Testing invalid user name inputs
    # Test incorrect value: user name is empty
    test1_user_name = ""
    print("Testing an empty user name: ")
    assert update_user_profile(user_email, test1_user_name, shipping_address,
                               postal_code, value_to_update) is False

    # Test incorrect value: user name has special character
    test2_user_name = "Jo!hn"
    print("Testing a user name with special character: ")
    assert update_user_profile(user_email, test2_user_name, shipping_address,
                               postal_code, value_to_update) is False

    # Test incorrect value: user name has space as prefix
    test3_user_name = " John"
    print("Testing a user name with a space: ")
    assert update_user_profile(user_email, test3_user_name, shipping_address,
                               postal_code, value_to_update) is False

    # Test incorrect value: user name is too short
    test4_user_name = "J"
    print("Testing a user name too short: ")
    assert update_user_profile(user_email, test4_user_name, shipping_address,
                               postal_code, value_to_update) is False

    # Test incorrect value: user name is too long
    test5_user_name = "John Smith John Smith John Smith"
    print("Testing a user name too long: ")
    assert update_user_profile(user_email, test5_user_name, shipping_address,
                               postal_code, value_to_update) is False

    # Testing invalid shipping address inputs
    # Test incorrect value: shipping address is empty
    test1_shipping_address = ""
    print("Testing an empty shipping address: ")
    assert update_user_profile(user_email, user_name, test1_shipping_address,
                               postal_code, value_to_update) is False

    # Test incorrect value: shipping address has special characters
    test2_shipping_address = "220 Yo!nge Street"
    print("Testing a shipping address with special characters: ")
    assert update_user_profile(user_email, user_name, test2_shipping_address,
                               postal_code, value_to_update) is False

    # Testing invalid postal code inputs
    # Test incorrect value: invalid postal code
    test1_postal_code = "M5B 2!1"
    print("Testing an invalid postal code: ")
    assert update_user_profile(user_email, user_name, shipping_address,
                               test1_postal_code, value_to_update) is False

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
