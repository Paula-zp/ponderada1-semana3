import pytest

from src.visitor import Visitor
from src.zoo import Zoo
from src.animal import Animal
from src.enclosure import Enclosure

# Teste para verificar se a classe Visitor existe
def test_visitor_exists():
    visitor = Visitor()
    assert isinstance(visitor, Visitor), "A classe Visitor não existe."

# Teste para verificar se o método decide_to_visit existe funciona corretamente
def test_decide_to_visit():
    zoo = Zoo()
    mouse = Animal("Tata", "Mouse", zoo)
    enclosure = Enclosure(zoo)
    enclosure.add_animal(mouse)
    visitor = Visitor()
    assert visitor.decide_to_visit(zoo) == True, "A decisão de visitar o zoológico não foi feita corretamente."

# Teste para verificar se o método visit_zoo existe funciona corretamente
def test_visit_zoo():
    zoo = Zoo()
    mouse = Animal("Tata", "Mouse", zoo)
    enclosure = Enclosure(zoo)
    enclosure.add_animal(mouse)
    visitor = Visitor()
    player = Player()
    visitor.visit_zoo(zoo, player)
    assert player.money == 10, "O dinheiro do jogador não foi alterado corretamente."