'''
This test module inserts generic attack payloads into each parameter in turn,
with all other parameters being set to legal values.
'''
from datetime import date

from qbay.models import place_order


def get_file():
    """
    Reads payloads into file object named 'expected_in' and returns it
    """
    from os import popen
    from pathlib import Path

    # get expected input/output file
    current_folder = Path(__file__).parent

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    return expected_in


def test_buyer_email():
    """
    Injects payloads in 'Generic_SQLI.txt' into buyer email parameter
    """
    expected_in = get_file()
    buyer_email = "buyer100@gmail.com"
    seller_email = "seller100@gmail.com"
    product_title = "Fuzzy Title"
    appendI = 0
    for line in expected_in:
        place_order(line, seller_email, product_title + str(appendI))
        print(" (Payload delivered to buyer email) Order placed for product: "
              + product_title + str(appendI))
        appendI += 1


def test_seller_email():
    """
    Injects payloads in 'Generic_SQLI.txt' into buyer email parameter
    """
    expected_in = get_file()
    buyer_email = "buyer100@gmail.com"
    seller_email = "seller100@gmail.com"
    product_title = "Fuzzy Title"
    appendI = 0
    for line in expected_in:
        place_order(buyer_email, line, product_title + str(appendI))
        print(" (Payload delivered to seller email) Order placed for product: "
              + product_title + str(appendI))
        appendI += 1


def test_product_title():
    """
    Injects payloads in 'Generic_SQLI.txt' into buyer email parameter
    """
    expected_in = get_file()
    buyer_email = "buyer100@gmail.com"
    seller_email = "seller100@gmail.com"
    product_title = "Fuzzy Title"
    appendI = 0
    for line in expected_in:
        place_order(buyer_email, seller_email, line)
        print(" (Payload delivered to buyer email) Order placed for product: "
              + product_title + str(appendI))
        appendI += 1
