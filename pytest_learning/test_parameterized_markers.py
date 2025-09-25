import pytest
def data():
    return [
        ('abc@xyz.com','123@xyz'),
        ('def@pqr.com','456@pqr')
    ]
@pytest.mark.parametrize("username,password",data())
def test_login(username,password):
    print(username+'---'+password)