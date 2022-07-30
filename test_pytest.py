import pytest
from unittest import mock
from helloworld import HelloWorld


class TestHelloWorld:
    def test_print_hello(self):
        hello_world = HelloWorld()
        hello_world.print_hello = mock.Mock(side_effect="mock print_hello")
        hello_world.print_hello(2)

    def test_print(self):
        print("this is a test_print func")


if __name__ == "__main__":
    pytest.main(["-s", "-v"])
