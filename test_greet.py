from greet import greet


def test_greet_includes_name():
    assert greet("Joyce") == "Hello, Joyce!"
