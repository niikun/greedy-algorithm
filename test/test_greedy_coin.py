import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from greedy_coin import greedy_coin

def test_greedy_coin():
    amount = 0.67
    assert greedy_coin(amount)=={'quarter': 2, 'dime': 1, 'nickel': 1, 'penny': 2}
