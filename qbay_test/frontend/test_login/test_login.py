def test_login():

    from os import popen
    from pathlib import Path
    import subprocess

    # get expected input/output file
    current_folder = Path(__file__).parent

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_login.in.txt'))
    expected_out = open(current_folder.joinpath(
        'test_login.out.txt')).read()
    """ print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Expected out...")
    print(expected_out)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^") """

    """ capsys -- object created by pytest to 
    capture stdout and stderr """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    """ print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Actual output...")
    print(output)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^") """
    output = output.replace('\r', '')
    assert output.strip() == expected_out.strip()
    

 