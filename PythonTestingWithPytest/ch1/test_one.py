def test_passing():
    assert (1, 2, 3) == (1, 2, 3)
    print("End!")

"""
$ pytest test_one.py

# 詳細なコマンドが知りたいならば、
$ pytest -v test_one.py
"""