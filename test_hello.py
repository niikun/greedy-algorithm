from hello import hello


def test_hello():
    name = "niikun"
    assert hello(name) == "hello niikun !"
