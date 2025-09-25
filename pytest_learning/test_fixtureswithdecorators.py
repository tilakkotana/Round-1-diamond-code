import pytest
@pytest.fixture(scope='module')
def setup():
    print("creating DB connection")
    yield
    print('closing db connection')
@pytest.fixture(scope='function')
def start():
    print("opening browser")
    yield
    print("closing browser")
# def test_login(setup,start):
#     print("executing login test")
# def test_user_reg(setup,start):
#     print('executing user registration')
@pytest.mark.usefixtures('setup','start')
def test_login():
    print("executing login test")
@pytest.mark.usefixtures('setup','start')
def test_user_reg():
    print('executing user registration')