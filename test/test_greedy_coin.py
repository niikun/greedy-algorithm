import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from greedy_coin import greedy_coin

def test_greedy_coin():

    assert greedy_coin(0.99) == {'quarter': 3, 'dime': 2, 'penny': 4}
    assert greedy_coin(0.00) == {}
    assert greedy_coin(-0.5) == {}
    assert greedy_coin(0.30) == {'quarter': 1, 'nickel': 1}

# if __name__ == "__main__":
#     pytest.main()
