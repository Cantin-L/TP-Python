class robot : 
    def __init__(self,nom , marque, modele): 
        self.nom = nom
        self.marque = marque
        self.modele = modele

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque


    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele

    
        

robot1 = robot('lancelot','apple','mk1')
robot2 = robot('Arthur','samsung','mk2')

print (robot1.nom)
print (robot2.marque)
