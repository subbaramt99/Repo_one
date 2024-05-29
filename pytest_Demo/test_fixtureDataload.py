import pytest


@pytest.mark.usefixtures("dataLoad") # The data will loaded from conftest of dataload
class TestExample:
    def test_editProfile(self, dataLoad):
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])

# data load by parameterization from crossbrowser in conftest
@pytest.mark.usefixtures("crossbrowser")
def test_crossbrowser(crossbrowser):
    print(crossbrowser[0])
