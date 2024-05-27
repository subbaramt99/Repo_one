# Running via command prompt open the pytest file directory (cd C:\SUBBARAM T\Applications\Python\Exercise Files\Samurai working copy\pytest_Demo)
# type "py.test" to execute full file
# type "py.test -v -s" with results
# type can run specific file "py.test <file name> -v -s" to run specific file 'py.test test_Demo2 -v -s'
# type "py.test -k (method name) -v -s" to run specific file 'py.test -k tes2 -v -s'
# -k stands for method name execution, -s logs in out put, -v stands for more info matadata
import pytest

# we can mark <tag> teste @pytest.Mark.smoke and then run with -m 'py.test -m smoke -v -s'
@pytest.mark.smoke   # it is Anatations
def test2_FirstPrograme(test_preRequisite): # I'm passing fixture to run pre-requisite of the test
    print("hello")

# we can mark as skip testcase @pytest.mark.skip and then run with all 'py.test -v -s'
@pytest.mark.skip
def test2_FirstPrograme1():
    print("Good morning")

# we can pass the test case with execute @pytest.mark.xfail
@pytest.mark.xfail
def test2_FirstPrograme2():
    msg = "hello"
    assert msg == "Hai", "Test failed because of string mismatch"