# All pytest file should start with "test_" or ends with "_test"
# All pytest method should start with "test"
import pytest

# Running via command prompt open the pytest file directory (cd C:\SUBBARAM T\Applications\Python\Exercise Files\Samurai working copy\pytest_Demo)
# type "py.test" to execute full file
# type "py.test -v -s" with results

class TestExample:

    #@pytest.mark.smoke  # we can mark the test run it accordingly using mark anatation
    def test_FirstPrograme(test_preRequisite): # I'm passing fixture to run pre-requisite of the test
        print("hello")
    ##@pytest.mark.smoke
    def test_FirstPrograme1(test_preRequisite):
        print("Good morning")
    #@pytest.mark.smoke
    def test_FirstPrograme2(test_preRequisite):
        msg = "hello"
        assert msg == "Hai"