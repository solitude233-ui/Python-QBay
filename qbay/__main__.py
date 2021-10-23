from qbay import *
from qbay.models import *
from qbay.cli import login_page, register_page, update_profile_page
from qbay.cli import create_product_page, update_product_page


def main():
    """
    This is the main screen of our frontend.
    It repeatedly prompts the user to enter a selection which leads to 
    different pages that performs certain tasks until the user enters x. """
    selection = input(
        "Welcome. Please type 1 to login, type 2 to register, "
        "type 3 to update your profile and"
        " type 4 to go to your home page."
        " Press x anytime to logout: ")
    selection = selection.strip()

    while selection != "x":
        if selection == '1':
            login_page()
        elif selection == '2':
            register_page()
        elif selection == "3":
            # update_profile_page()
            pass
        elif selection == "4":
            product_selection = input("Press 1 to create a product and "
                                      "press 2 to update an existing product.")
            if product_selection == "1":
                create_product_page()
            elif product_selection == "2":
                update_product_page()
            else:
                print("Invalid selection.")
        else:
            print("Invalid selection")
        selection = input(
            "Welcome. Please type 1 to login, type 2 to register, "
            "type 3 to update your profile and"
            " type 4 to go to your home page."
            " Press x anytime to logout: ")
        selection = selection.strip()


if __name__ == '__main__':
    main()
