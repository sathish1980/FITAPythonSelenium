import pytest

@pytest.mark.usefixtures("before")
class Test_Secondclass():

    @pytest.mark.Sanity
    def test_firsttestcase(self):
        print("firsttestcase")

    @pytest.mark.SIT
    def test_secondtestcase(self,before1):
        print("secondtestcase")

    @pytest.mark.SIT
    def test_thirdtestcase(self):
        print("thirdtestcase")

    @pytest.mark.SIT
    def test_GetData(self,LoadData):
        #print(LoadData[0])
        #print(LoadData[1])
        #print(LoadData[2])
        print(len(LoadData))
        for eachvalue in range(0,len(LoadData)):
            print(LoadData[eachvalue])

    #@pytest.mark.SIT
    def test_GetDatawithparam(self, LoadDatawithParam):
        print(LoadDatawithParam)

    #@pytest.mark.SIT
    def test_GetDatawithparam(self, LoadDatawithtuple):
        #print(LoadDatawithtuple)
        print(LoadDatawithtuple[0])
        print(LoadDatawithtuple[1])

    @pytest.mark.SIT
    def test_GetDatawithparam(self, LoadDatawithdic):
        # print(LoadDatawithtuple)
        print(LoadDatawithdic["username"])
        print(LoadDatawithdic["password"])
        print("login is clicked")
        #print(LoadDatawithdic)



