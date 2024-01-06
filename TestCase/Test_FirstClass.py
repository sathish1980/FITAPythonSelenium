import pytest


class Test_Firstclass():

    @pytest.mark.Sanity
    @pytest.mark.order(3)
    @pytest.mark.dependency()
    def test_firsttestcase(self):
        print("firsttestcase")

    @pytest.mark.Sanity
    @pytest.mark.order(1)
    @pytest.mark.dependency(depends=["test_firsttestcase"])
    def test_secondtestcase(self):
        print("secondtestcase")

    @pytest.mark.Sanity
    @pytest.mark.order(2)
    def test_thirdtestcase(self):
        print("thirdtestcase")

