import pytest
from src.animal import Animal
from src.zoo import Zoo
from src.enclosure import Enclosure
from src.visitor import Visitor
from src.player import Player

# Teste para verificar se o sistema completo funciona corretamente
def test_full_system():
    zoo = Zoo()
    player = Player()

    # Adicionando animais ao recinto 1
    enclosure1 = Enclosure(zoo)
    for i in range(3):
        animal = Animal(f"Animal{i}", "Coelho", zoo)
        animal.feed(5)
        enclosure1.add_animal(animal)

    # Adicionando animais ao recinto 2
    enclosure2 = Enclosure(zoo)
    for i in range(4):
        animal = Animal(f"Animal{i}", "Girafa", zoo)
        animal.feed(2)
        enclosure2.add_animal(animal)

    #Adicionando visitantes ao zoológico
    visitor = Visitor()
    for i in range(100):
        visitor.visit_zoo(zoo, player)
        zoo.increment_visit_count()

    print("Com o zológico bem cuidado, recebemos: ", zoo.visit_count, " visitantes.")

    zoo.reset_visit_count()
    
    #Mudando a condição dos recintos
    enclosure1.change_condition()
    enclosure2.change_condition()

    #Adicionando novamente visitantes ao zoológico
    visitor = Visitor()
    for i in range(100):
        visitor.visit_zoo(zoo, player)
        zoo.increment_visit_count()
    
    print("Com o zológico mais ou menos cuidado, recebemos: ", zoo.visit_count, " visitantes.")
    
    #Verificando se o jogador ganhou dinheiro
    assert player.money > 0, "O jogador não ganhou dinheiro."
