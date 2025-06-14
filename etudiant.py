class Etudiant():
    def __init__(self, nom, prenom, age, email):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = email

    def __str__(self):
        return f"Etudiant(nom={self.nom}, prenom={self.prenom}, age={self.age}, email={self.email})"

    def __repr__(self):
        return self.__str__()
    

    def noter(self, module, note):
        if hasattr(module, 'name') and hasattr(module, 'professeur'):
            if 0 <= note <= 20:
                setattr(module, 'note', note)
            else:
                raise ValueError("La note doit être entre 0 et 20")
        else:
            raise TypeError("L'objet doit être une instance de la classe Module")
        
    
    def get_info(self):
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'age': self.age,
            'email': self.email
        }
    


    def renvoyer(self):
        return f"Etudiant {self.prenom} {self.nom} a été renvoyé."