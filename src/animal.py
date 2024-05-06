class Animal:
    #Construtor da classe Animal
    def __init__(self, name, species, zoo):
        self.name = name
        self.species = species
        self.happiness = 6
        self.zoo = zoo
        zoo.animals.append(self)

    #Método para alimentar os animais
    def feed(self, food_amount):
        self.happiness += 2 * food_amount
        if self.happiness > 10:
            self.happiness = 10
