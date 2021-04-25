from models import BasicObject as bo
class Router(bo.BasicObject):
    def __init__(self,nom=None,gateways=None):
        super().__init__()
        self.nom = nom
        self.gateways = gateways
