import pytest

from src.zoo import Zoo
from src.animal import Animal
from src.enclosure import Enclosure
from src.visitor import Visitor
from src.player import Player

def test_animal_exists():
    zoo = Zoo()
    mouse = Animal("Tata", "Mouse", zoo)
    assert mouse.name == "Tata", "O animal não foi criado corretamente."

def test_enclosure_exists():
    enclosure = Enclosure()
    assert isinstance(enclosure, Enclosure), "O recinto não foi criado corretamente."

def test_visitor_exists():
    visitor = Visitor()
    assert isinstance(visitor, Visitor), "A classe Visitor não existe."

def test_player_exists():
    player = Player()
    assert isinstance(player, Player), "A classe Player não existe."

def test_zoo_exists():
    zoo = Zoo()
    assert isinstance(zoo, Zoo), "A classe Zoo não existe."