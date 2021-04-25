from models import RequeteARP as rARP
class GateWay:
    def __init__(self,ip=None,mac=None,router=None,interface=None):
        self.ip = ip
        self.mac = mac
        self.router = router
        self.interface = interface
    def send_data(self,destinataire,mac):
        print("renvoi de l'adresse du "+self.router.nom)
        requete = rARP.RequeteARP(self.ip,destinataire,self.mac,mac)
        self.interface.lien.parent.receive_request(requete)
    def receive_request(self,requete):
        if requete.ipdestinataire == self.ip:
            if requete.macdestinataire == "FF:FF:FF:FF:FF:FF:FF":
                self.send_data(requete.ipenvoyeur,requete.macenvoyeur)