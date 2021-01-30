import pytest

from app import greets


@pytest.mark.parametrize("got,want",[
    ("world", "hello, world"),
    ("hatsumi", "hello, hatsumi")
])
def test_greet(got, want):
    assert greets.greet(got) == want