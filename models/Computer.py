from models import BasicObject as bo
from models import RequeteARP as rARP
from models import ARPRecord
from models import IpUtil
class Computer(bo.BasicObject):
    def __init__(self,nom,ip,mac,masque):
        super().__init__()
        self.nom = nom
        self.ip = ip
        self.mac = mac
        self.interface = None
        self.masque = masque
        self.tablearp = []
    def print_table_arp(self):
        print("table arp de "+self.nom+" \n")
        print("\t ip \t\t mac \n")
        for i in range(0,len(self.tablearp)):
            text = str(self.tablearp[i].ip)+"\t"+str(self.tablearp[i].mac+"\n")
            print(text)
    def voir_si_dans_table(self,destinataire):
        for i in range(0,len(self.tablearp)):
            if self.tablearp[i].ip == destinataire:
                return self.tablearp[i].mac
        return "FF:FF:FF:FF:FF:FF:FF"
    def send_data(self,destinataire):
        print(self.nom + " envoi de données vers " + destinataire)
        util = IpUtil.IpUtil()
        if util.voir_si_meme_reseau(self.ip,destinataire,self.masque):
            self.print_table_arp()
            mac = self.voir_si_dans_table(destinataire)
            requete = rARP.RequeteARP(self.ip,destinataire,self.mac,mac)
            self.interface.lien.parent.receive_request(requete)
        else:
            print("L'adresse d'envoi ne se trouve pas sur le même  reseau,on l'envoie au routeur")
            self.send_data(util.utilip.get_dernier_adresse())

    def receive_request(self,requete):
        if requete.ipdestinataire == self.ip:
            print(self.nom + " recoit des données from" + requete.ipenvoyeur)
            mac = self.voir_si_dans_table(requete.ipenvoyeur)
            if mac == "FF:FF:FF:FF:FF:FF:FF":
                print("l'adresse ip de l'envoyeur n'est pas enregistré donc "+self.nom+" on enregistre")
                mac = requete.macenvoyeur
                self.tablearp.append(ARPRecord.ARPRecord(requete.ipenvoyeur,mac))
            self.print_table_arp()
            if requete.macdestinataire == "FF:FF:FF:FF:FF:FF:FF":
                self.send_data(requete.ipenvoyeur)
