import pytest
from src.enclosure import Enclosure
from src.zoo import Zoo
from src.animal import Animal

# Teste para verificar se a classe Enclosure existe
def test_enclosure_exists():
    zoo = Zoo()
    enclosure = Enclosure(zoo)
    assert isinstance(enclosure, Enclosure), "O recinto não foi criado corretamente."

# Teste para verificar se o método condition existe e funciona corretamente
def test_enclosure_condition():
    zoo = Zoo()
    enclosure = Enclosure(zoo)
    assert enclosure.condition == "well_cared", "A condição do recinto não foi criada corretamente."

# Teste para verificar se o método change_condition existe e funciona corretamente
def test_enclosure_change_condition():
    zoo = Zoo()
    enclosure = Enclosure(zoo)
    enclosure.change_condition("poorly_cared")
    assert enclosure.condition == "poorly_cared", "A condição do recinto não foi alterada corretamente."

# Teste para verificar se o método add_animal existe e funciona corretamente
def test_enclosure_add_animal():
    zoo = Zoo()
    enclosure = Enclosure(zoo)
    mouse = Animal("Tata", "Mouse", zoo)
    enclosure.add_animal(mouse)
    assert enclosure.animals == [mouse], "O animal não foi adicionado corretamente ao recinto."