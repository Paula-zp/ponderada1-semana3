import pytest
from src.player import Player

# Teste para verificar se a classe Player existe
def test_player_exists():
    player = Player()
    assert isinstance(player, Player), "A classe Player não existe."

def test_player_money():
    player = Player()
    assert player.money == 0, "O dinheiro do jogador não foi criado corretamente."

def test_earn_money():
    player = Player()
    player.earn_money(10)
    assert player.money == 10, "O dinheiro do jogador não foi alterado corretamente."