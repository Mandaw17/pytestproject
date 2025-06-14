from etudiant import Etudiant


class Classe():
    def __init__(self, nom, niveau):

        self.nom = nom
        self.etudiants = []
        self.niveau = niveau

    def __str__(self):
        return f"Nome: {self.nom}"
    
    def add_etudiant(self, etudiant):
        if isinstance(etudiant, Etudiant): #verifie
            self.etudiants.append(etudiant)
        else:
            raise TypeError("L'objet doit être une instance de la classe Etudiant")
        

    def set_niveau(self, niveau):
        if hasattr(niveau, 'nom') and hasattr(niveau, 'difficulte'):
            self.niveau = niveau
        else:
            raise TypeError("L'objet doit être une instance de la classe Niveau")
        
    def remove_etudiant(self, etudiant):
        if etudiant in self.etudiants:
            self.etudiants.remove(etudiant)
        else:
            raise ValueError("L'étudiant n'est pas dans la classe")


   