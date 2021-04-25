from models import Computer
from models import Interface
from models import Router
from models import Switch
from models import GateWay
pc1 = Computer.Computer("pc1","192.168.1.1","AA:AA:AA:AA:AA:AA:AA:AA","255.255.255.0")
pc2 = Computer.Computer("pc2","192.168.1.2","BB:BB:BB:BB:BB:BB:BB:BB","255.255.255.0")
pc3 = Computer.Computer("pc3","192.168.2.1","CC:CC:CC:CC:CC:CC:CC:CC","255.255.255.0")
switch1 = Switch.Switch("Switch 1")
switch2 = Switch.Switch("Switch 2")
interfacepc1 = Interface.Interface("E0",pc1)
interfacepc2 = Interface.Interface("E0",pc2)
interface1switch1 = Interface.Interface("E0",switch1,interfacepc1)
interface2switch1 = Interface.Interface("E1",switch1,interfacepc2)
interfacepc3 = Interface.Interface("E0",pc3)
interface1switch2 = Interface.Interface("E0",switch2,interfacepc3)
router = Router.Router("router")
routegateway1 = GateWay.GateWay("192.168.1.254","DD:DD:DD:DD:DD:DD:DD:DD",router)
routegateway2 = GateWay.GateWay("192.168.2.254","EE:EE:EE:EE:EE:EE:EE:EE",router)
interface3switch1 = Interface.Interface("E2",switch1)
interfaceroutegateway1 = Interface.Interface("E0",routegateway1,interface3switch1)
interface2switch2 = Interface.Interface("E1",switch2)
interfaceroutegateway2 = Interface.Interface("E1",routegateway2,interface2switch2)
switch1.interfaces = [interface1switch1,interface2switch1,interface3switch1]
switch2.interfaces = [interface1switch2,interface2switch2]
pc1.interface = interfacepc1
pc2.interface = interfacepc2
pc3.interface = interfacepc3
routegateway1.interface = interfaceroutegateway1
routegateway2.interface = interfaceroutegateway2
router.gateways = [routegateway1,routegateway2]
print("envoi de fichier de PC1 à PC2(meme reseau)\n")
pc1.send_data("192.168.1.2")
print("\n\n\nenvoi de fichier de PC3 à PC1(reseau different)\n")
pc3.send_data("192.168.1.1")