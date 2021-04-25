class IpV4SansClasse:
    part1 = 0
    part2 = 0
    part3 = 0
    part4 = 0
    masque = 0
    def __init__(self,stringip=None,masque=0):
        if stringip != None:
            div = stringip.split('.')
            self.part1 = int(div[0])
            self.part2 = int(div[1])
            self.part3 = int(div[2])
            self.part4 = int(div[3])
        self.masque = masque
    def get_adresse(self):
        return str(self.part1) + "." + str(self.part2) + "." + str(self.part3) + "." + str(self.part4) + "/"+str(self.masque)
    def get_tab(self):
        rep =[self.part1,self.part2,self.part3,self.part4]
        return rep
    def get_id(self):
        return int(self.masque/8)
    def get_reste(self):
        return 8*(1+self.get_id())-self.masque
    def get_masque(self):
        id = self.get_id()
        reste = self.get_reste()
        tab = self.get_tab()
        rep = ''
        for i in range(0,4):
            if i < id:
                rep += '255.'
            if i == id:
                binaire = '0b'
                for a in range(0,8):
                    if a < 8-reste:
                        binaire+= '1'
                    else:
                        binaire+= '0'
                rep += str(eval(binaire))+'.'
            if i > id:
                rep+= '0.'
        return rep[0:len(rep)-1]
    def get_adresse_reseau(self):
        id = self.get_id()
        reste = self.get_reste()
        tab = self.get_tab()
        rep = ''
        for i in range(0, 4):
            if i < id:
                rep += str(tab[i])+'.'
            if i == id:
                binaire = '0b'
                strbinaire = str(bin(tab[i]))
                for a in range(0, 8):
                    if a < 8 - reste:
                        binaire += strbinaire[a+2:a+3]
                    else:
                        binaire += '0'
                rep += str(eval(binaire)) + '.'
            if i > id:
                rep += '0.'
        return rep[0:len(rep) - 1]
    def get_adresse_diffusion(self):
        id = self.get_id()
        reste = self.get_reste()
        tab = self.get_tab()
        rep = ''
        for i in range(0, 4):
            if i < id:
                rep += str(tab[i]) + '.'
            if i == id:
                binaire = '0b'
                strbinaire = str(bin(tab[i]))
                for a in range(0, 8):
                    if a < 8 - reste:
                        binaire += strbinaire[a + 2:a + 3]
                    else:
                        binaire += '1'
                rep += str(eval(binaire)) + '.'
            if i > id:
                rep += '255.'
        return rep[0:len(rep) - 1]
    def get_nombre_adresse_disponible(self):
        return pow(2,32-self.masque) - 2
    def get_premier_adresse(self):
        adressereseau = self.get_adresse_reseau()
        split = adressereseau.split('.')
        newbit = int(split[3])+1
        return str(split[0])+'.'+str(split[1])+'.'+str(split[2])+'.'+str(newbit)
    def get_dernier_adresse(self):
        adressediffusion = self.get_adresse_diffusion()
        split = adressediffusion.split('.')
        newbit = int(split[3])-1
        return str(split[0])+'.'+str(split[1])+'.'+str(split[2])+'.'+str(newbit)
