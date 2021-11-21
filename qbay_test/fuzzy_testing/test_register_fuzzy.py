'''
This test module injects generic attack payloads into each parameter in turn,
with all other parameters being set to legal values. 
'''

from qbay.models import register


def get_file():
    '''
    reads payloads into file object named 'expected_in' and returns 
    '''
    from os import popen
    from pathlib import Path

    # get expected input/output file
    current_folder = Path(__file__).parent

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    return expected_in


def test_username():   
    '''
    Injects payloads in 'Generic_SQLI.txt' into username parameter
    ''' 
    expected_in = get_file()
    appendI = 0
    user_name = "fuzzyTestUsername"
    email_local = "fuzzyTestUsername"
    email_domain = "@email.com"
    user_password = "validPassword!Username"
    for line in expected_in:
        register(line, email_local + str(appendI) + email_domain, 
                 user_password + str(appendI), user_balance=100)
        print("(Payload delivered to username) Registered: " 
              + user_name + str(appendI))
        appendI += 1


def test_email():
    '''
    Injects payloads in 'Generic_SQLI.txt' into email parameter
    '''
    expected_in = get_file()
    appendI = 0
    user_name = "fuzzyTestEmail"
    email_local = "fuzzyTestEmail"
    email_domain = "@email.com"
    user_password = "validPassword!Email"
    for line in expected_in:
        register(user_name + str(appendI), line, 
                 user_password + str(appendI), user_balance=100)
        print("(Payload delivered to email) Registered: " 
              + user_name + str(appendI))
        appendI += 1


def test_password():
    '''
    Injects payloads in 'Generic_SQLI.txt' into email parameter
    '''
    expected_in = get_file()
    appendI = 0
    user_name = "fuzzyTestPassword"
    email_local = "fuzzyTestPassword"
    email_domain = "@email.com"
    user_password = "validPassword!Password"
    for line in expected_in:   
        register(user_name + str(appendI), email_local 
                 + str(appendI) + email_domain, line, user_balance=100)
        print("(Payload delivered to password) Registered: " 
              + user_name + str(appendI))
        appendI += 1
        

def test_userbalance():
    '''
    Injects payloads in 'Generic_SQLI.txt' into user balance parameter
    '''
    expected_in = get_file()
    appendI = 0
    user_name = "fuzzyTestBalance"
    email_local = "fuzzyTestBalance"
    email_domain = "@email.com"
    user_password = "validPassword!Balance"
    for line in expected_in:
        register(user_name + str(appendI), email_local + str(appendI) 
                 + email_domain, user_password + str(appendI), line)
        print("(Payload delivered to user_balance) Registered: " 
              + user_name + str(appendI))
        appendI += 1