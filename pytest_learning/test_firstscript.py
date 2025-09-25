import pytest

# def setup_function():
#     print("opening browser")
# def teardown_function():
#     print("closing browser")
def setup_module():
    print("opening browser")
def teardown_module():
    print("closing browser")
def test_login():
    print("executing login test")
def test_user_reg():
    print('executing user registration')
