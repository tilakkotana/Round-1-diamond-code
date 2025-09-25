import pytest
def test_validate_title():
    expected_title='Google.com'
    actual_title='Gmail.com'
    # if expected_title==actual_title:
    #     print("test case passed")
    # else:
    #     print('test case failed')
    assert expected_title==actual_title , "not same"

    assert 'Gmails' in actual_title , "not present"


    assert False,'Failed forcefully'
