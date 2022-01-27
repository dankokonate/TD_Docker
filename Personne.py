

class Personne:
    def __init__(self, nom, prenom, ssn):
        self.nom = nom
        self.prenom = prenom
        self.ssn = ssn

    def __getNom__(self):
        return self.nom

    def __getPrenom__(self):
        return self.prenom

    def __getSsn__(self):
        return self.ssn

    def hasValid(self):
        if self.ssn.is_valid():
            return True
        else:
            return False
