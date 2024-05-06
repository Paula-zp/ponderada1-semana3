class Enclosure:
    # Método construtor da classe
    def __init__(self, zoo):
        self.animals = []
        self.condition = "well_cared"
        zoo.enclosures.append(self)

    # Método para adicionar um animal ao recinto
    def add_animal(self, animal):
        if not self.animals or animal.species == self.animals[0].species:
            self.animals.append(animal)
        else:
            raise ValueError("Todos os animais de um recinto devem ser da mesma espécie")

    # Método para alterar a condição do recinto
    def change_condition(self):
        if self.condition == "well_cared":
            new_condition = "poorly_cared"
        else:
            new_condition = "well_cared"
        self.condition = new_condition
