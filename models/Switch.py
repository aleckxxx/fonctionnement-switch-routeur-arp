from models import BasicObject as bo
from models import CAMRecord as cr
class Switch(bo.BasicObject):
    def __init__(self,nom=None,interfaces=None):
        super().__init__()
        self.nom = nom
        self.interfaces = interfaces
        self.cam = []
    def print_cam(self):
        print("table cam de "+self.nom)
        print("\t mac \t\t\t\t interface")
        for i in range(0,len(self.cam)):
            print(self.cam[i].mac+"\t\t"+self.cam[i].interface.nom+"\n")
    def voir_si_dans_cam(self,mac):
        for i in range(0,len(self.cam)):
            if self.cam[i].mac == mac:
                return self.cam[i]
        return None
    def voir_interface_correspondant(self,mac):
        for i in range(0,len(self.interfaces)):
            lien = self.interfaces[i].lien.parent
            if lien.mac == mac:
                return self.interfaces[i]
        return None
    def send_to_all_interfaces(self,requete):
        for i in range(0,len(self.interfaces)):
            self.interfaces[i].lien.parent.receive_request(requete)
    def receive_request(self,requete):
        print(self.nom+" recoit de données from "+requete.macenvoyeur)
        envoyeur = self.voir_si_dans_cam(requete.macenvoyeur)
        if envoyeur == None:
            print("l'envoyeur n'est pas enregistré alors on l'enregistre")
            interface = self.voir_interface_correspondant(requete.macenvoyeur)
            envoyeur = cr.CAMRecord(interface,requete.macenvoyeur)
            self.cam.append(envoyeur)
            self.print_cam()
        if requete.macdestinataire == "FF:FF:FF:FF:FF:FF:FF":
            print("le destinataire est un mac de broadcast alors on envoie une requete ARP à tous les interfaces\n")
            self.send_to_all_interfaces(requete)
        if requete.macdestinataire != "FF:FF:FF:FF:FF:FF:FF":
            receveur = self.voir_si_dans_cam(requete.macdestinataire)
            receveur.interface.lien.parent.receive_request(requete)


