"""Test the Task data type."""

from collections import namedtuple
import pytest

"""
namedtupleを使うと、名前でアクセスできるようになる
"""
Task = namedtuple("Task", ["summary", "owner", "done", "id"])

"""
__new__.defaults__を使うと、未指定時のデフォルト値を予め指定できる
"""
Task.__new__.__defaults__ == (None, None, False, None)

def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


@pytest.mark.run_these_please
def test_member_access():
    """Check .firld functionality of namedtuple."""
    t = Task("buy milk", "brian")
    assert t.summary == "buy milk"
    assert t.owner == "brian"
    assert (t.done, t.id) == (False, None)