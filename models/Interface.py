class Interface:
    def add_lien(self,lien):
        self.lien = lien
        if(lien!=None):
            lien.lien = self
    def __init__(self,nom=None,parent=None,lien=None):
        self.parent = parent
        self.nom = nom
        self.add_lien(lien)
