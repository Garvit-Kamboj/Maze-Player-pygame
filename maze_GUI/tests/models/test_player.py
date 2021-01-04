import pytest
from models.player import Player

@pytest.fixture
def player():
    return Player('Garvit')

def test_name(player):
    """010A checks and confirms the name of player"""
    assert player.name == 'Garvit'

def test_backpack(player):
    """010B checks the player backpack where items are stored"""
    assert player.backpack == []