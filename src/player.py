class Player:

    # Método construtor da classe
    def __init__(self):
        self.money = 0

    # Método para adicionar dinheiro ao jogador
    def earn_money(self, amount):
        self.money += amount
