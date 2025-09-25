import pytest
@pytest.mark.functional
def test_login():
    print('executing login test')
@pytest.mark.regression
def test_user_reg():
    print('executing user registration')
@pytest.mark.functional
def test_compose_mail():
    print('executing mail test')
@pytest.mark.skip
def test_skip():
    print('skipping test')