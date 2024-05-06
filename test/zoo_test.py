import pytest
from src.zoo import Zoo

# Teste para verificar se a classe Zoo existe
def test_zoo_exists():
    zoo = Zoo()
    assert isinstance(zoo, Zoo), "A classe Zoo não existe."