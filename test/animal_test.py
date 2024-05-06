import pytest

from src.animal import Animal
from src.zoo import Zoo

# Teste para verificar se a classe Animal existe
def test_animal_exists():
    zoo = Zoo()
    mouse = Animal("Tata", "Mouse", zoo)
    assert mouse.name == "Tata", "O animal não foi criado corretamente."

def test_feed_animal():
    mouse = Animal("Tata", "Mouse", 0)
    mouse.feed(1)
    assert mouse.happiness == 2, "A alimentação não foi feita corretamente."