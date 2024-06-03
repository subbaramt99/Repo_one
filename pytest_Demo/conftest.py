# fixture are used to setup tear down method for test cases - conftest file to generalize
# conftest will make generalized the for all test case
# fixture make it available in all test case.
# when we passing the fixture method name into test it will run as before/after test execute
# Datadriven and paramertization can be done with return statement in tuple formate.
# when we define fixture scope to class alone, it will run before class will initiated and at the end

import pytest

@pytest.fixture(scope= "class") # this fixture will be in class level now
# It will execute before test run
def test_preRequisite():
    print("I'm generalized for all test (conftest) I'll execute first")
    yield
    print("I'm generalized for all test (conftest) I'll execute at last")


@pytest.fixture() # Loading the data by using fixtures
def dataLoad():
    print("User profile data being created")
    return ["Subbaram", "Theerthagiri", "subbaramt99@gmail.com"]

@pytest.fixture(params=[("chrome", "subbaram"), ("firefox", "theerthagiri"), ("edge", "puvila")]) # parameterizing the data
def crossbrowser(request): # passing the data into crossbrowser "request" is key word to use get parameterized data.
    return request.param # returning the data which is passing by fixtures