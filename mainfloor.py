import random
import sys
import time
from time import sleep

class Tank:
    def __init__(self, name):
        self.name=name
        self.maxph=250
        self.health=self.maxph
        self.attack=20
 
class Magiker:
    def __init__ (self, name):
        self.name=name
        self.maxhp=150
        self.health=self.maxhp
        self.attack=50

class Krigare:
    def __init__(self, name):
        self.name=name
        self.maxhp=200
        self.health=self.maxhp
        self.attack=30
    
class Jägare:
    def __init__(self, name):
        self.name=name
        self.maxhp=100
        self.health=self.maxhp
        self.attack=40
ryggsäck=[]
    
def start():
    print("Du slogs mot en stor drake men började förlora..")
    sleep(1)
    print("Du försöker fly så fort som möjligt och hittar en grotta..")
    sleep(1)
    print("Du tar dig in i grottan där du är säker men kan inte ta dig ut för där vaktar draken..")
    sleep(1)
    print("vilken klass vill du välja.. Det finns 4 klasser att välja på:tank, krigare, magiker och jägare.")
    
    character=input(">")
    character=character.lower()

    if character == "tank":
        print("du har valt klassen tank.")
        sleep(1)
        grottöppning()
    

    if character == "krigar":
        print("du har valt klassen krigare.")
        sleep(1)
        grottöppning()

    if character == "magiker":
        print("du har valt klassen magiker.")
        sleep(1)
        grottöppning()

    if character == "jägare":
        print("du har valt klassen jägare.")
        sleep(1)
        grottöppning()

def grottöppning():
    print("du står nu i grottöppningen, det är kvavt och du ser inte så mycket..")
    sleep(1)
    print("du går lite längre in och ser ljus, när du kollar närmare ser du 3 dörrar..")
    sleep(1)
    print("en dörr rakt framför dig, en träddörr, till vänster har ser du en gulddörr och till höger om dig har du en dörr med en dödskalle hängandes över..")
    sleep(1)
    print("du blir väldigt försiktig med tanke på att det kan bo fler monster här eller något annat mystiskt, men du behöver ta dig ut..")
    sleep(1)
    print("hur gör du? vilken dörr väljer du?")
    sleep(1)
    print("vänster höger eller rakt fram.")
    
    förstadörr=input(">")
    förstadörr=förstadörr.lower()
    
    if förstadörr == "vänster":
        print("du står nu och kikar in i gulddörren, du ser ett tomt rum och en till gulddörr framför dig..")
        sleep(1)
        print("du går in och kikar in i nästa rum..")
        sleep(1)
        guldkorridor()
    
    if förstadörr == "höger":
        bosskoridor()

    
    if förstadörr == "framåt":
        print("när du väl kikar in i rummet så upptäcker du monster..")
        sleep(1)
        print("du kommer inte kunna fly eftersom att ett monster redan hoppat på dig..")
        sleep(1)
        print("gör dig redo för strid..")
    

def bosskoridor():
    print("du har nu gått igenom dörren med en dödskalle över sig..")
    sleep(1)
    print("du ser massor av skelett delar överallt från döda personer..")
    sleep(1)
    print("du blir genast försiktig och kollar runt för att se om det finns någon fiende i rummet..")
    sleep(1)
    print("du ser bara massa bokhyllor med blod på från de döda och en stor port längre in i rummet..")
    sleep(1)
    print("bakom en död kropp vid en bokhylla så ser det ut att ligga en karta av något slag..")
    sleep(1)
    print("när du kollar närmare på den stora svarta porten så ser du tydliga mönster av drakar och andra monster och andra saker som du inte kan identifiera..")
    sleep(1)
    print("du misstänker att bakom den dörren finns något riktigt farligt..")
    sleep(1)
    print("vågar du gå igenom den stora porten?")

    bossdörr=input(">")
    bossdörr=bossdörr.lower()

    if bossdörr == "ja":
        bossrum()
    if bossdörr == "nej":
        print("du står kvar i korridoren, vill du inte göra något annat?")

    gåtillgrottöppning=input(">")
    gåtillgrottöppning=gåtillgrottöppning.lower()
    
    if gåtillgrottöppning == "ja":
            grottöppning()
    if gåtillgrottöppning == "nej":
        bosskoridor()

def bossrum():
    print("du har nu öppnat den stora tunga porten..")
    sleep(1)
    print("du ser dig omkring, det är en stor sal med bord och stolar lite överallt, dammigt och en stor tron längst in i rummet..")
    sleep(1)
    print("Du ser inte om någon sitter på tronen eftersom att det är så mörkt längre in. det lyser knappt där du står redan..")
    sleep(1)
    print("du ser återigen skelett delar som ligger på stolar och bord.Du märker även att inget av möblerna är trasiga..")
    sleep(1)
    print("kan det vara en magiker som gjort detta?")

def guldrum():
    print("du är nu i guldrummet..")
    sleep(1)
    print("rummet är upplyst och du ser en guldkista mitt i rummet..")
    sleep(1)
    print("du känner dig säker när du går in..")
    sleep(1)
    print("rummet är mycket dammigt och det ser ut som om rummet har varit övergivet väldigt länge..")
    sleep(1)
    print("vill du gå fram till guldkistan?")
        
def guldkorridor():
    print("du står nu i vad som ser ut och vara en guldig korridor..")
    sleep(1)
    print("när du ser dig omkring så ser du massa bokhyllor fullt med böcker och rummet är även dammigt..")
    sleep(1)
    print("rummet är även någorlunda upplyst..")
    sleep(1)
    print("längre in i rummet ser du en till guldig dörr..")
    sleep(1)
    print("bakom dig har du dörren du kom ifrån..")
    sleep(1)
    print("vill du gå igenom dörren framför dig?")

    gåiniguldrum=input(">")
    gåiniguldrum=gåiniguldrum.lower()

    if gåiniguldrum =="ja":
        guldrum()
    if gåiniguldrum == "nej":
        print("du står kvar i guldkorridoren, säker på att du inte vil göra något?")
        sleep(1)
        print("vill du gå tillbaka till grottöppningen?")
        gåtillgrottöppning=input(">")
        gåtillgrottöppning=gåtillgrottöppning.lower()
        if gåtillgrottöppning == "ja":
            grottöppning()
        if gåtillgrottöppning == "nej":
            print("du står nu kvar i guldkorridoren..")

    guldkista=input(">")
    guldkista=guldkista.lower()

    if guldkista == "ja":
        print("du står nu framför guldkistan.") 
        sleep(1)
        print("vill du öppna guldkistan?")
        öppnakista=input(">")
        öppnakista=öppnakista.lower()

        if guldkista == "nej":
            print("du känner att guldkistan kan vara farlig men du känner dig fortfarande säker i rummet..")

        if öppnakista == "ja":
            print("i kistan så ligger det några guldmynt och ett vapen.")
            sleep(1)
            print("vill du ta upp vapnet och guldmynten?")
            kistaitems=input(">")
            kistaitems=kistaitems.lower()
            if kistaitems == "ja":
                print("du tar upp svärdet och mynten..")
                ryggsäck.append("svärd")
                ryggsäck.append("guldmynt")
                
            if kistaitems == "nej":
                print("du låter föremålen ligga kvar.")

        if öppnakista == "nej":
            print("du känner att guldkistan kan vara farlig men du känner dig fortfarande säker i rummet..")
    
    print("vill du gå ut ur rummet?")

    gåut=input(">")
    gåut=gåut.lower()

    if gåut == "ja":
        guldkorridor()
    if gåut == "nej":
        print("du står kvar och stirrar på en stängd guldkista..")
        sleep(1)
        print("säker på att du inte vill gå ut ur rummet?")


start()










