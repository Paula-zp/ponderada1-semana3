import pytest

from src.animal import Animal
from src.zoo import Zoo

# Teste para verificar se a classe Animal existe
def test_animal_exists():
    zoo = Zoo()
    mouse = Animal("Tata", "Mouse", zoo)
    assert mouse.name == "Tata", "O animal não foi criado corretamente."
    assert mouse.species == "Mouse", "A espécie não foi identificada corretamente."

# Teste para verificar se o método feed existe e funciona corretamente
def test_feed_animal():
    zoo = Zoo()
    mouse = Animal("Tata", "Mouse", zoo)
    mouse.feed(2)
    assert mouse.happiness == 10, "A alimentação não foi feita corretamente."