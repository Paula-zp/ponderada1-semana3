class Zoo:

    # Método construtor da classe
    def __init__(self):
        self.animals = []
        self.enclosures = []
        self.visit_count = 0

    # Método para contar a quantidade de visitas ao zoológico
    def increment_visit_count(self): 
        self.visit_count += 1

    #Método para zerar a quantidade de visitas ao zoológico
    def reset_visit_count(self):
        self.visit_count = 0