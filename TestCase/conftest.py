import pytest


@pytest.fixture(scope="class")
def before():
    print("beforeeach test case")
    yield
    print("after each test case")

@pytest.fixture()
def before1():
    print("before1 each test case")
    yield
    print("after1 each test case")

@pytest.fixture()
def LoadData():
    return ["sathish","kumar","R"]

@pytest.fixture(params={"sathish","kumar","R","K"})
def LoadDatawithParam(request):
    return request.param

@pytest.fixture(params=[("sathish","kumar"),("raja","H")])
def LoadDatawithtuple(request):
    return request.param

@pytest.fixture(params=[{"username" : "sathish","password" : "kumar"},{"username" : "raja","password": "H"}])
def LoadDatawithdic(request):
    return request.param
