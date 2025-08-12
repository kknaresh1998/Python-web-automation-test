import pytest
@pytest.mark.usefixtures("setup")
class TestExamples:
    def test_FixtureDemo1(self):
        print("I will execute 1")

    def test_FixtureDemo2(self):
        print("I will execute 2")

    def test_FixtureDemo3(self):
        print("I will execute 3")
        
    def test_FixtureDemo4(self):
        print("I will execute 4")


