import random 

class Visitor:

    # Método construtor da classe
    def __init__(self):
        pass
    
    # Método para decidir se o visitante irá visitar o zoológico
    def decide_to_visit(self, zoo):
        happy_animals = [animal for animal in zoo.animals if animal.happiness > 5]
        well_cared_enclosures = [enclosure for enclosure in zoo.enclosures if enclosure.condition == "well_cared"]

        # Condições para decidir se o visitante irá visitar o zoológico
        if len(happy_animals) > len(zoo.animals) / 2 and len(well_cared_enclosures) > len(zoo.enclosures) / 2:
            return random.random() < 0.9
        elif len(happy_animals) > len(zoo.animals) / 2 or len(well_cared_enclosures) > len(zoo.enclosures) / 2:
            return random.random() < 0.5
        else:
            return random.random() < 0.2

    # Método para visitar o zoológico
    def visit_zoo(self, zoo, player):
        if self.decide_to_visit(zoo):
            player.earn_money(10)