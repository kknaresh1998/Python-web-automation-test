import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")

@pytest.fixture(scope="class")
def dataLoad():
    print("user profile data is being created")
    return (["rahul", "shetty"])



@pytest.fixture(params=["chrome", "firefox","Edge"])
def crossBrowser(request):
    return request.param
