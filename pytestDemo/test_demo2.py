import pytest

@pytest.mark.smoke
@pytest.mark.skip
def testAssertionMethod():
    assert "hello" == "hi"

@pytest.mark.xfail
def testSecondAssertionMethodCreditCard():
    a = 4
    b = 6
    assert a+2 == 6