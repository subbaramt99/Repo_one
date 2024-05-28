# fixture are used to setup tear down method for test cases - conftest file to generalize
# conftest will make generalized the for all test case
# fixture make it available in all test case.
# when we passing the fixture method name into test it will run as before/after test execute

import pytest

@pytest.fixture(scope= "class") # this fixture will be in class level now
# It will execute before test run
def test_preRequisite():
    print("I'm generalized for all test (conftest) I'll execute first")
    yield
    print("I'm generalized for all test (conftest) I'll execute at last")


@pytest.fixture()
def dataLoad():
    print("User profile data being created")
    return ["Subbaram", "Theerthagiri", "subbaramt99@gmail.com"]