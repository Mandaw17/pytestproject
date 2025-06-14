import pytest
from classe import Classe
from etudiant import Etudiant

@pytest.fixture
def classe():
    return Classe("M1Miage", "Master")

# Fixture pour une instance d'Etudiant
@pytest.fixture
def etudiant():
    return Etudiant("Dupont", "Jean", 22, "")


class TestClasse:
    

    def test_add_etudiant(self, etudiant, classe):
        # Arrange
        nb_etudiants_initial = len(classe.etudiants)

        # Act
        classe.add_etudiant(etudiant)
        # Assert
        assert len(classe.etudiants) == nb_etudiants_initial + 1

    
    def test_remove_etiudiant(self, classe, etudiant):
        # Arrange
        classe.add_etudiant(etudiant)
        nb_etudiants_initial = len(classe.etudiants)

        # Act
        classe.remove_etudiant(etudiant)

        # Assert
        assert len(classe.etudiants) == nb_etudiants_initial - 1


    def test_etudiant_not_in_classe(self):
        # Arrange
        classe = Classe("M1Miage", "Master")
        etudiant = Etudiant("Dupont", "Jean", 22, "")

        # Act & Assert
        with pytest.raises(ValueError, match="L'étudiant n'est pas dans la classe"):
            classe.remove_etudiant(etudiant)