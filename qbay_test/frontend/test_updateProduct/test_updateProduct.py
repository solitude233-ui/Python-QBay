from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
expected_in = open(current_folder.joinpath(
    'test_updateProduct.in'))
expected_out = open(current_folder.joinpath(
    'test_updateProduct.out')).read()

print(expected_out)


def test_updateProduct():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    output = output.replace('\r', '')
    assert output == expected_out
