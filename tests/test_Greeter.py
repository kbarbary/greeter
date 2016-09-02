"""
Unit tests for Greeter class
"""
import pytest
import os
import greeter

@pytest.fixture
def jeeves():
    jeeves = greeter.Greeter()
    yield jeeves

    # Clean up any mock data files created by the tests.
    if jeeves.outputs is not None:
        for file in jeeves.files:
            try:
                os.remove(file)
            except:
                pass

def test_greet(jeeves):
    jeeves.greet()
    assert jeeves.message == "hello world!"
