import pytest
from models.score import Score


@pytest.fixture
def bad():
    return Score("Bad", 0)


@pytest.fixture
def good():
    return Score("Good", 9999)


def test_score_to_dict(good):
    assert good.to_dict() == {"name": 'Good', "score": 9999}


def test_score_lt(good, bad):
    assert bad < good
    assert not bad > good
