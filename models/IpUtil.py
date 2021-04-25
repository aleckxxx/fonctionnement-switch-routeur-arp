from models import IpV4SansClasse
class IpUtil:
    def count_un(self,ip=''):
        div = ip.split('.')
        number = 0
        for i in range(0,4):
            test = 0
            binary = str(bin(int(div[i])))
            for a in range(0,8):
                if binary[a+2] == '0':
                    test = 1
                    break
                number = number + 1
            if test == 1:
                break
        return number
    def voir_si_meme_reseau(self,ip,ipreceveur,masque):
        nombrebit = self.count_un(masque)
        self.utilip = IpV4SansClasse.IpV4SansClasse(ip,nombrebit)
        self.utilipreceveur = IpV4SansClasse.IpV4SansClasse(ipreceveur,nombrebit)
        if self.utilip.get_adresse_reseau() == self.utilipreceveur.get_adresse_reseau():
            return True
        return False