import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hello import hello



def test_hello():
    name = "niikun"
    assert hello(name) == "hello niikun !"
