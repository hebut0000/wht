import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,33),(4,44)])
def test_multiplicationn_11(num,output):
    print("传入参数是")
    assert num * 11 == output