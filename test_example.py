"""
First function is say_hello/hello name
"""
from example import say_hello

def test_should_say_hello_to_dave():
    assert say_hello("Dave") == "Hello, Dave"

def test_should_say_hello_to_jimmy():
    assert say_hello("Jimmy") == "Hello, Jimmy"

"""
Second function is the generate_message/welcome name
"""
from example import generate_message

def test_generate_message():
    assert generate_message("Dave") == "Welcome, Dave"
    assert generate_message("Jim") == "Welcome, Jim"
