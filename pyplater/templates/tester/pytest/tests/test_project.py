import pytest

@pytest.fixture
def setup_and_teardown():
    print("Setting up")
    yield "Hello, test!"
    print("Tearing down")

def test_example(setup_and_teardown):
    print(setup_and_teardown)
    print("Running test")