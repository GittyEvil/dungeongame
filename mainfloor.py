import random
import sys
import time

class Tank:
    def __init__(self, name):
        self.name=name
        self.maxph=250
        self.health=self.maxph
        self.attack=20
 
class Mage:
    def __init__ (self, name):
        self.name=name
        self.maxhp=150
        self.health=self.maxhp
        self.attack=50

class Warrior:
    def __init__(self, name):
        self.name=name
        self.maxhp=200
        self.health=self.maxhp
        self.attack=30
    
class Hunter:
    def __init__(self, name):
        self.name=name
        self.maxhp=100
        self.health=self.maxhp
        self.attack=40
    
def start():
    print("Du slogs mot en stor drake men började förlora..")
    print("Du försöker fly så fort som möjligt och hittar en grotta..")
    print("Du tar dig in i grottan där du är säker men kan inte ta dig ut för där vaktar draken..")
    print("vilken klass vill du välja.. Det finns 4 klasser att välja på:tank, warrior, mage och hunter.")
    
    character=input(">")
    character=character.lower()

    if character == "tank":
        print("du har valt klassen tank.")
        grottöppning()
    

    if character == "warrior":
        print("du har valt klassen warrior.")
        grottöppning()

    if character == "mage":
        print("du har valt klassen mage.")
        grottöppning()

    if character == "hunter":
        print("du har valt klassen hunter.")
        grottöppning()

def grottöppning():
    print("du står nu i grottöppningen, det är kvavt och du ser inte så mycket..\n")
    print("du går lite längre in och ser ljus, när du kollar närmare ser du 3 dörrar..\n")
    print("en dörr rakt framför dig, en träddörr, till vänster har ser du en gulddörr och till höger om dig har du en dörr med en dödskalle hängandes över..")
    print("du blir väldigt försiktig med tanke på att det kan bo fler monster här eller något annat mystiskt, men du behöver ta dig ut..")
    print("hur gör du? vilken dörr väljer du?")
    print("vänster höger eller rakt fram.")
    
    förstadörr=input(">")
    förstadörr=förstadörr.lower()
    
    if förstadörr == "vänster":
        print("du står nu och kikar in i gulddörren, du ser ett tomt rum och en träddörr framför dig..")
        print("du går in och kikar in i nästa rum..")
        guldrum()
    
    if förstadörr == "höger":
        print("rummet är tomt och du ser en väldigt stor dörr när du kikar in, som en stor port med massa figurer och annat på..")
    
    if förstadörr == "fram":
        print("när du väl kikar in i rummet så upptäcker du monster..")
        print("du kommer inte kunna fly eftersom att ett monster redan hoppat på dig..")
        print("gör dig redo för strid..")
    
def guldrum():
    print("du är nu i guldrummet där du ser...")
    

start()










