import pytest

from pytest_Demo.Baseclass import Baseclass


@pytest.mark.usefixtures("dataLoad") # The data will loaded from conftest of dataload
class TestExample(Baseclass):
    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])

# data load by parameterization from crossbrowser in conftest
@pytest.mark.usefixtures("crossbrowser")
def test_crossbrowser(crossbrowser):
    print(crossbrowser[0])

@pytest.mark.usefixtures("dataLoad")
class testExample2(Baseclass):
    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        print (dataLoad[1])
