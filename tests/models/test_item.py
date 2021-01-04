import pytest
from models.item import Item

@pytest.fixture
def item():
    return Item('Salmon', 'Fish')

def test_name(item):
    """Checks and confirms the value of name in init"""
    assert item.name == 'Salmon'

def test_family(item):
    """Checks and confirms the value of family in init"""
    assert item.family == 'Fish'

