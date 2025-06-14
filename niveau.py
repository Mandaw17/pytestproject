class Niveau:
    def __init__(self, nom, difficulte, modules, classes):
        self.nom = nom
        self.difficulte = difficulte
        self.modules = modules
        self.classes = classes

    def __str__(self):
        return f"Niveau: {self.nom}, Difficulte: {self.difficulte}"

    def __repr__(self):
        return f"Niveau(nom='{self.nom}', difficulte={self.difficulte})"