def test_falling():
    assert(1,2,3) == (3,2,1)

def hoge():
    """pytestの命名規則にあてはまらないので、テスト実行されない"""
    assert 1 == 2