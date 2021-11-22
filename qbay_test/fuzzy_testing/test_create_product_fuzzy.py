'''
This test module inserts generic attack payloads into each parameter in turn,
with all other parameters being set to legal values.
'''
from datetime import date

from qbay.models import create_product


def get_file():
    '''
    Reads payloads into file object named 'expected_in' and returns it
    '''
    from os import popen
    from pathlib import Path

    # get expected input/output file
    current_folder = Path(__file__).parent

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    return expected_in


def test_product_title():
    '''
    Injects payloads in 'Generic_SQLI.txt' into product title parameter
    '''
    expected_in = get_file()
    appendI = 0
    product_title = "Fuzzy Title"
    product_description = "A fuzzy description for a new product."
    price = 50
    last_date = date(2021, 5, 2)
    owner_email = "fuzzyemail@gmail.com"
    for line in expected_in:
        create_product(line, product_description,
                       price + appendI, last_date, owner_email)
        print("(Payload delivered to product title) Created product: "
              + product_title + str(appendI))
        appendI += 1


def test_product_description():
    '''
    Injects payloads in 'Generic_SQLI.txt' into product description parameter
    '''
    expected_in = get_file()
    appendI = 0
    product_title = "Fuzzy Title"
    product_description = "A fuzzy description for a new product."
    price = 50
    last_date = date(2021, 5, 2)
    owner_email = "fuzzyemail@gmail.com"
    for line in expected_in:
        create_product(product_title + str(appendI), line,
                       price + appendI, last_date, owner_email)
        print("(Payload delivered to product description) Created product: "
              + product_title + str(appendI))
        appendI += 1


def test_price():
    '''
    Injects payloads in 'Generic_SQLI.txt' into price parameter
    '''
    expected_in = get_file()
    appendI = 0
    product_title = "Fuzzy Title"
    product_description = "A fuzzy description for a new product."
    price = 50
    last_date = date(2021, 5, 2)
    owner_email = "fuzzyemail@gmail.com"
    for line in expected_in:
        create_product(product_title + str(appendI), product_description,
                       line, last_date, owner_email)
        print("(Payload delivered to price) Created product: "
              + product_title + str(appendI))
        appendI += 1


def test_date():
    '''
    Injects payloads in 'Generic_SQLI.txt' into date parameter
    '''
    expected_in = get_file()
    appendI = 0
    product_title = "Fuzzy Title"
    product_description = "A fuzzy description for a new product."
    price = 50
    last_date = date(2021, 5, 2)
    owner_email = "fuzzyemail@gmail.com"
    for line in expected_in:
        create_product(product_title + str(appendI), product_description,
                       price + appendI, line, owner_email)
        print("(Payload delivered to date) Created product: "
              + product_title + str(appendI))
        appendI += 1


def test_email():
    '''
    Injects payloads in 'Generic_SQLI.txt' into email parameter
    '''
    expected_in = get_file()
    appendI = 0
    product_title = "Fuzzy Title"
    product_description = "A fuzzy description for a new product."
    price = 50
    last_date = date(2021, 5, 2)
    owner_email = "fuzzyemail@gmail.com"
    for line in expected_in:
        create_product(product_title + str(appendI), product_description,
                       price + appendI, last_date, line)
        print("(Payload delivered to email) Created product: "
              + product_title + str(appendI))
        appendI += 1
