import pytest
from tests.dockerfile_Generation import assert_Dockerfile_Generation, list_test

@pytest.mark.parametrize("Test_Number", list_test('Database'))
def test_FrontEnd(Test_Number):
    assert_Dockerfile_Generation('FrontEnd', Test_Number)