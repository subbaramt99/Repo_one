# Fixture will help to run pre-requisite and post requisite of the test case

import pytest

# It will execute 1st and yield will execute at last
#@pytest.fixture()
# It will execute before test run
#def test_preRequisite():
#    print("I'll execute first")
#    yield
#    print("I'll execute at last")

def test_fixtureDemo(test_preRequisite):  # need to pass the fixture method
    print("I'll execute steps in fixture demo method")

@pytest.mark.usefixtures("test_preRequisite")
class TestExample:
    def test_fixtureDemo1(self): # need to pass the fixture method
        print("I'll execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self): # need to pass the fixture method
        print("I'll execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self): # need to pass the fixture method
        print("I'll execute steps in fixtureDemo3 method")
