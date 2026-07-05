import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from greet import greet


def test_greet_basic():
    assert greet("Ada") == "Hello, Ada!"
