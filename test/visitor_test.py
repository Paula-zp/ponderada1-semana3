import pytest

from src.visitor import Visitor
from src.zoo import Zoo
from src.animal import Animal
from src.enclosure import Enclosure
from src.player import Player

# Teste para verificar se a classe Visitor existe
def test_visitor_exists():
    visitor = Visitor()
    assert isinstance(visitor, Visitor), "A classe Visitor não existe."

# Teste para verificar se o método decide_to_visit existe e funciona corretamente
def test_decide_to_visit():
    zoo = Zoo()
    enclosure = Enclosure(zoo)
    for i in range(6):
        animal = Animal(f"Animal{i}", "Mouse", zoo)
        animal.feed(5)
        enclosure.add_animal(animal)
    visitor = Visitor()

    # Executa decide_to_visit 1000 vezes e conta quantas vezes retorna True
    results = [visitor.decide_to_visit(zoo) for _ in range(1000)]
    true_results = results.count(True)

    # Verifica se a frequência de True está correta, como utilizamos Random, nem sempre dá certo, é aproximadamente
    assert 0.85 < true_results / 1000 < 0.95, "A probabilidade não está sendo aplicada corretamente."

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

# Teste para verificar se as visitas são contadas corretamente
def test_visit_count():
    zoo = Zoo()

    # Testa o método increment_visit_count
    for i in range(5):
        zoo.increment_visit_count()
    assert zoo.visit_count == 5, "O contador de visitas não foi incrementado corretamente."

    # Testa o método reset_visit_count
    zoo.reset_visit_count()
    assert zoo.visit_count == 0, "O contador de visitas não foi zerado corretamente."