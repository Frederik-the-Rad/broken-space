print("""Powered By Quantum Engine:
````````````````````````````````````````````````````````````````````````````````
``````````````````````````````-/++/-``````````.---.`````````````````````````````
`````````````````````````````+s:--:+s+.````:+so+/+s+````````````````````````````
````````````````````````````-y:`````.-``.+s+:.````-y/```````````````````````````
````````````````````````````/y-```````-os/.```````.y+```````````````````````````
````````````````````````````:y:`````.+s/.`````````-y:```````````````````````````
````````````````````````````-yo:///+sy++///::--.```.````````````````````````````
```````````````````````-/+ssooy+:/ss:----::://+osso+/-.`````````````````````````
````````````````````.+so:-```.so-so.``````````````.-/+so/-``````````````````````
````````````````````ss.```````:yy/````:++/````os.``````./so-````````````````````
````````````````````ss.```````/yy-```.yyyy/```.ss.````````os````````````````````
````````````````````.+s+:.```/y:+s-```:++/`````.s+```````-so````````````````````
``````````````````````.:+:``:y/``+s-````````````:y:```:+so:`````````````````````
```````````````````````````.so````+y:````````````os```::.```````````````````````
```````````````````````````+y.`````:y+```````````:y:````````````````````````````
```````````````````````````so```````-ss-``````````y+````````````````````````````
``````````````````````````.y/`````````/y+.````````so````````````````````````````
```````````````````````````so.```.:+o``.+s+.`````.y+````````````````````````````
```````````````````````````.osooos+:.````./so/--:os.````````````````````````````
``````````````````````````````..````````````-:+++:``````````````````````````````
````````````````````````````````````````````````````````````````````````````````
""")
import random
import time
import sys
import threading
from threading import Thread

import os
import datalib
global currentsave
def startmenu():
    print("""
    |------------------------------------------------------------------------------------------------------------------------------------------------------|
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                             1:--start---------                                                                         | 
    |                                                             2:--credits-------                                                                         | 
    |                                                             3:--quit----------                                                                         | 
    |                                                             4:--manage saves--                                                                         | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |                                                                                                                                                      | 
    |------------------------------------------------------------------------------------------------------------------------------------------------------|
    """)
    def getsave():
        global currentsave
        currentsave = input("Save slot to open 1/2/3:")
        if currentsave == "1" or currentsave == "2" or currentsave == "3":
            savedir = os.path.join('c:/broken space/save' + currentsave + '/','save.data')
        else:
            print("please enter 1/2/3")
            time.sleep(1)
            getsave()
    def credit():
        print("""

Scripting: Caleb Morgan
Sprites: Caleb Morgan
Story: Caleb Morgan
Game Engine:: Caleb Morgan
Python 3.4:Guido van Rossum (https://www.python.org/)
Py2exe:jretz, mhammond, theller  (https://sourceforge.net/projects/py2exe/ , http://www.py2exe.org/)




""")
        input("")
        startmenu()
    
    def managesaves():
        global currentsave
        currentsave = input("Save slot to delete 1/2/3:")
        if currentsave == "1" or currentsave == "2" or currentsave == "3":
            try:
                os.remove(os.path.join('c:/broken space/save' + currentsave + '/','save.data'))
            except:
                print("Save error #A1")    
            try:
                os.remove(os.path.join('c:/broken space/save' + currentsave + '/','story.txt'))
            except:
                print("Save error #A2")    
            try:
                os.remove(os.path.join('c:/broken space/save' + currentsave + '/','backup/save.data'))
                
            except:
                print("Save error #A3")
                time.sleep(1)
            startmenu()
        else:
            print("please enter 1/2/3")
            time.sleep(1)
            managesaves()
    s = input("1/2/3/4:")
    if s == "1":
        getsave()
    elif s == "2":
        credit()
    elif s == "3":
        sys.exit()
    elif s == "4":
        managesaves()
    else:
        startmenu()
#the names of the crew
    
startmenu()
earthcreatures = ["humans","cat","dog","bear","lion","wolf","tiger","starling","cardinal","duck","chicken","leopard","snow leopard","peacock","cow","horse","bull","bison","pony","donkey","turtle","rat","mouse","hamster","gerbil","sheep","pig","goat"]
characternames = ['Noah','Emma','Ethan','Mason','Sophia','Isabella','Oliver','Mia','Aiden','Charlotte','Elijah','Jame','Benjamin','Abigail','Logan','Emily','Jacob','Madison','Jackson','Ella','Lily','Carter','Avery','Daniel','Evelyn','Sofia','William','Alexander','Riley','Owen','Chloe','Jack','Scarlett','Gabriel','Ellie','Matthew','Elizabeth','Henry','Aubrey','Sebastian','Layla','Grace','Jayden','Zoey','Nathan','Mila','Grayson','Ryan','Hannah','Isaac','Victoria','Caleb','Eli','Lucy','Jesse','Petra','Axel','Lucas','Olivia']
#sol
sol = [
{"structures":[],'colonies':['human colony'],"seed":99999999995,'size':3,'name':'Earth','quest':{'type':'finditem','text':'please recover us a mars rover.' ,'item':'mars rover'},'ishabitable':1,'treasures':['nokia 3310'],'weather':'earth like','foliage':'extreme','fauna':'extreme','notes':'you land on humanity\'s home world. it is crawling with species of every type, from plants to animals. also, it is still filled with cities,','spacestation':True,"ores":["gold","copper","iron","silicon","prismite"],"creatures":earthcreatures},
{"structures":[],'colonies':['human colony'],"seed":99999999994,'size':1,'name':'Pluto','ishabitable':2,'treasures':"the banhammer",'weather':'freezing cold','foliage':'no','fauna':'no','notes':'well, it is pluto!','spacestation':True,"ores":["gold","copper","iron","silicon","prismite"],"creatures":[]},
{"structures":[],'colonies':['human colony'],"seed":99999999993,'size':2,'name':'Mars','ishabitable':2,'treasures':'mars rover','weather':'mars like','foliage':'no','fauna':'no','notes':'well, it is mars!','spacestation':True,"ores":["gold","copper","iron","silicon","prismite"],"creatures":["martians"]},
{"structures":[],'colonies':['human colony'],"seed":99999999992,'size':3,'name':'Venus','ishabitable':2,'treasures':'Venus Gases','weather':'venus like','foliage':'no','fauna':'no','notes':'well, it is venus!','spacestation':True,"ores":["gold","copper","iron","silicon","prismite"],"creatures":[]},
{"structures":[],'colonies':['human colony'],"seed":99999999991,'size':2,'name':'Mercury','ishabitable':2,'treasures':'Mercury rock','weather':'blazing hot','foliage':'no','fauna':'no','notes':'well, it is Mercury!','spacestation':True,"ores":["gold","copper","iron","silicon","prismite"],"creatures":[]},
{"structures":[],'colonies':['human colony'],"seed":99999999990,'size':4,'name':'Neptune','ishabitable':2,'treasures':'Neptune Gases','weather':'neptune like','foliage':'extreme','fauna':'extreme','notes':'well, it is Neptune!','spacestation':True,"ores":["gold","copper","iron","silicon","prismite"],"creatures":[]},
{"structures":[],'colonies':['human colony'],"seed":99999999989,'size':5,'name':'Saturn','ishabitable':2,'treasures':'Saturn Gases','weather':'neptune like','foliage':'no','fauna':'no','notes':'well, it is Saturn!','spacestation':True,"ores":["gold","copper","iron","silicon","prismite"],"creatures":[]},
{"structures":[],'colonies':['human colony'],"seed":99999999988,'size':5,'name':'Uranus','ishabitable':2,'treasures':'<dad joke here>','weather':'uranus like','foliage':'no','fauna':'no','notes':'well, it is Uranus!','spacestation':True,"ores":["gold","copper","iron","silicon","prismite"],"creatures":[]},
{"structures":[],'colonies':['human colony'],"seed":99999999987,'size':6,'name':'Jupiter','ishabitable':2,'treasures':'Jupiter Gases','weather':'jupiter like','foliage':'extreme','fauna':'extreme','notes':'well, it is jupiter!','spacestation':True,"ores":["gold","copper","iron","silicon","prismite"],"creatures":[]}]
galeus = [
{"structures":[],'colonies':['cat colony'],"seed":99999999986,'size':4 ,'name': 'qesnoth','ishabitable':1,'treasures':'the god cube','quest': {'type': 'finditem', 'text': 'We ask that you find the statue of noah the cat on Makara.', 'item': 'statue of noah the cat'},'weather':'earth like','foliage':'extreme','fauna':'extreme','notes':'this is the cat homeworld','spacestation':True,"ores":["gold","copper","iron","silicon","prismite"],"creatures":["cats"]},
{"structures":[],'colonies':['cat colony'],"seed":99999999985,'size':2,'name':'safrolla','ishabitable':1,'treasures':'statue of noah the cat','quest': {'type': 'finditem', 'text': 'We need the the god cube found and returned to us. please, don\'t ask any questions.', 'item': 'the god cube'},'weather':'tropical','foliage':'extreme','fauna':'extreme','notes':'this tropical, jungle planet is full of animals that the carnivorous cats eat.','spacestation':True,'ores':["gold"],'creatures':['dragon','Vrerablade','Murhazar','Erureer']},]
usleatho = [
{"structures":[],'creatures': ['algonian'], "seed":99999999984,'ores': ['iron', 'copper'], 'size': 3, 'spacestation': True, 'name': 'viania', 'ishabitable': False, 'fauna': 'none', 'weather': 'baren', 'colonies': ['algonian colony'], 'foliage': 'none', 'treasures': 'pirate crusher','quest': {'type': 'finditem', 'text': 'We want you to find the pirate crusher.. now.', 'item': 'pirate crusher'}, 'notes': 'you land on the algonian homeworld, it is not habitable for any creature but the algonians.'},
{"structures":[],'creatures': ['algonian'], "seed":99999999983,'ores': ['iron', 'copper','Eximus'], 'size': 5, 'spacestation': True,'name': 'smuxoter', 'ishabitable': False, 'fauna': 'none', 'weather': 'baren', 'colonies': ['algonian colony'], 'foliage': 'none', 'treasures': 'Algonian mining laser','quest': {'type': 'finditem', 'text': 'We want you to find the Algonian mining laser.. for it is long since lost.', 'item': 'Algonian mining laser'}, 'notes': 'you land on the algonian homeworld, it is not habitable for any creature but the algonians.'}]
exluagtos = [
{"structures":[],'name': 'juethea', "seed":99999999981,'ishabitable': True, 'fauna': 'extreme', 'foliage': 'extreme', 'size': 4, 'treasures': 'Rare metals.', 'creatures': ['dragon','Zouz\'oq','Wrowib','Stremupt','Kmipryx','Eaglok'], 'quest': {'type': 'finditem', 'text': 'We ask that you find the Rare metals on this planet.', 'item': 'Rare metals'}, 'spacestation': False, 'ores': ['copper', 'gold'], 'weather': 'hot', 'colonies': ['dragon colony'], 'notes': 'you land on the dragon homeworld, it has many mountain ranges(where the dragons live since they are like dwarves), just don\'t try to steal their precious metals and gems.'}]
Algira = [
{"structures":[],'name': 'Brayonus', "seed":99999999980,'ishabitable': True, 'fauna': 'none', 'foliage': 'none', 'size': 4, 'treasures': 'universe seed', 'creatures': [], 'quest': {}, 'spacestation': False, 'ores': ['Uru', 'iron','steel','celestite'], 'weather': 'celestial homeworld', 'colonies': [], 'notes': 'you land on strange world, it is a entirely metallic artificial planet, no plant or animal life at all, just a cold, metal ball, floating in space.'}]
Dakara = [
{"structures":[],'name': 'Vittelius', "seed":99999999996,'ishabitable': True, 'fauna': 'extreme', 'foliage': 'extreme', 'size': 5, 'treasures': 'admin core', 'creatures': [], 'quest': {}, 'spacestation': True, 'ores': ['Uru', 'iron','steel','prismite','gold','copper','silicon'], 'weather': 'Savanna', 'colonies': ["human colony"], 'notes': 'Arguably the weirdest, most interesting planet in the universe. Everything eventually makes it\'s way here. The grass is cyan, the trees come in every color, the sky is magenta, and lots of weird stuff happens here, as everyone eventually comes here.'}]

items = []
global creatures
creatures = [
"cat",
"martians",
"humans",
]

raw_input = input
    #custom creature
def addcreature(creature):
    #sample: "test_creature":{"sentient":{False}
    creatures.append(creature)
    #player ship
class ship():
    def __init__(self,stats,sprite):
        #stats
        self.name = stats[0]
        self.health = stats[1]
        self.evade = stats[2]
        self.crewamount = stats[3]
        self.firepower = stats[4]
        self.speed = stats[5]
        self.armor = stats[6]
        self.cargosize = stats[7]
        self.inv = stats[8]
        self.sprite = sprite
        self.crew = stats[9]
        self.money = stats[10]
        self.fleet = stats[11]
        self.colonies = stats[12]
        self.maxfleetmembers = stats[13]
        self.maxhealth = stats[14]
        self.allies = stats[15]
        self.flightdist = stats[16]
        self.kills = stats[17]
        self.mined = stats[18]
        self.role = stats[19]
        self.reputation = stats[20]
    #generates the players crew
    def generatecrew(self):
        for x in range(self.crewamount):
            name = random.choice(characternames)
            crewmember = {'name':name,'health':100,'profession':random.choice(['engineer','pilot','gunner','to be useless']),'room':random.choice(['bridge','corridor','gun room','hangar','lounge'])}
            self.crew.append(crewmember)
    #displays ship info
    def displayship(self,indent):
        print(str(indent) + self.name)
        for x in range(len(self.sprite)):            
            print(str(indent) + str(self.sprite[x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
        self.updatecrew()
        #displays hud
        print('||health:' + str(self.health) + ' | | evade:' + str(self.evade) + '||')
        print('||crew:' + str(self.crewamount) + ' | | firepower:' + str(self.firepower) + '||')       
        print('||speed:' + str(self.speed) + ' | | armor:' + str(self.armor) + '||')
        print('||cargosize:' + str(self.cargosize) + ' | | money:' + str(self.money) + '||')
        print('||inv:' + str(self.inv) + ' | | fleet member:' + str(self.fleet) + '||')
        print('||colonies created:' + str(self.colonies) + ' | | max fleet members:' + str(self.maxfleetmembers) + '||')
        print("||allies:" + str(self.allies) + ' | | flight distance:' + str(self.flightdist) + " parsecs||")
        try:
            comquests = datalib.load(savedir)['cquests']
        
            print('\nquests done:' + str(comquests))
        except:
            pass
        print("role:" + self.role)
        rep = ""
        if self.reputation == 0:
            rep = "bad"
        elif self.reputation >= 5 and self.reputation <= 9:
            rep = "average"
        elif self.reputation >= 10 and self.reputation <= 19:
            rep = "decent"
        elif self.reputation >= 20 and self.reputation <= 29:
            rep = "good person"
        elif self.reputation >= 30:
            rep = "hero"
        elif self.reputation <= -5 and self.reputation >= -9:
            rep = "pretty bad"
        elif self.reputation <= -10 and self.reputation >= -19:
            rep = "despicable"
        elif self.reputation <= -20:
            rep = "villain" 
        print("reputation:" + rep)
        print('\ncrewmembers:\n')
        i = 0
        for x in range(len(self.crew)):            
                try:
                    print(' name:' + self.crew[i]['name'])
                except:
                    pass
                try:
                    print(' health:' + str(self.crew[i]['health']))
                except:
                    pass
                try:
                    print(' profession:' + self.crew[i]['profession'])
                except:
                    pass
                try:
                    print(' location on ship:' + self.crew[i]['room'])
                except:
                    pass
                try:
                    print(' \n')
                except:
                    pass
                i += 1           
    #custom crew
    def addcustomcrewmember(self,stats):
        self.crew.append(stats)
    #adds an item to the playership's inventory
    def additem(self,itemtoadd):
        self.inv.append(itemtoadd)
    #removes an item to the playership's inventory    
    def delitem(self,itemtorem):
        self.inv.remove(itemtorem)
    #returns the playership's inventory as a value
    def returninv(self):
        return self.inv
    #returns the playership's crew as a value
    def returncrewdata(self):        
        return self.crew
    #depletes a crewmember's health
    def depletehealth(self,crewmembername,amountodeplete):
            for x in range(len(self.crew)):
            #try:
                if self.crew[x]['name'] == crewmembername:
                    self.crew[x]['health'] -= amountodeplete
    #updates the crew, 
    def updatecrew(self):
         for x in range(len(self.crew)):
             if self.crew[x]['health'] <= 0:
                 self.crew.pop(x)
             self.crew[x]['room'] = random.choice(['bridge','corridor','gun room','hangar','lounge'])    
#random item generator
class items():
    def __init__(self,maxitems):
        self.max = maxitems
        #note there are 3 adjective types not 1
        self.determiners = ['big',"small","huge","tiny"] 
        self.quantities = ['a few','a lot of','several','many']
        self.qualities = ['ancient','metal','stone','brittle','glowing','pulsating','strange','smelly','round','blocky','heavy','evil','broken','useless']
        #it's obvious what this is
        self.nouns = ['statue','artifact','gem','object','thing']
        #what is the material made of?
        self.substances = ['metal','stone','wood']
        #tool type?
        self.tools = ['sword','pickaxe','axe','shovel','saw','bow','knife']
        #material(used in recipe not substance) type
        self.materials = ['machine part','wheel']
        self.items = []
    #makes those items
    def generate(self,type,data):
        if data != 'null':
            toolparts = data['toolparts']
            materials = data['materials']
            substance = data['substance']
        if data == 'null':
            toolparts = self.tools
            materials = self.materials
            substance = self.substances
        if type == 'generic':
            for x in range(self.max):                
                adjtype = random.randint(1,3)
                if adjtype == 1:
                    item = str(random.choice(self.determiners) + ' ' + random.choice(self.nouns))
                    self.items.append(item)
                if adjtype == 2:
                    item = str(random.choice(self.qualities) + ' ' + random.choice(self.nouns))
                    self.items.append(item)
                if adjtype == 3:
                    amount = random.randint(1,2)
                    if amount == 1:
                        item = str(random.choice(self.quantities) + ' ' + random.choice(self.nouns)) + 's'
                        self.items.append(item)
                    elif amount == 2:
                        item = str(random.choice(self.quantities) + ' ' + random.choice(self.qualities) + ' ' + random.choice(self.nouns)) + 's'
                        self.items.append(item)
        if type == 'tool':
            for x in range(self.max):
                adjtype = random.randint(1,3)
                if adjtype == 1:
                    item = str(random.choice(self.determiners) + ' ' + random.choice(toolparts))
                    self.items.append(item)
                if adjtype == 2:
                    item = str(random.choice(self.qualities) + ' ' + random.choice(toolparts))
                    self.items.append(item)
                if adjtype == 3:
                    amount = random.randint(1,2)
                    if amount == 1:
                        item = str(random.choice(self.quantities) + ' ' + random.choice(toolparts)) + 's'
                        self.items.append(item)
                    elif amount == 2:
                        item = str(random.choice(self.quantities) + ' ' + random.choice(self.qualities) + ' ' + random.choice(toolparts)) + 's'
                        self.items.append(item)
        if type == 'material':
            for x in range(self.max):
                item = str(random.choice(substance) + ' ' + random.choice(materials))
                self.items.append(item)    
    #in case you want to add unique items manually
    def customitems(self,item):
        if len(item) > 0:
            for x in range(0,len(item) ):
                self.items.append(str(item[x]))
        if len(item) == 0:
            self.items.append(str(item[0]))
    def returnitems(self):
        return self.items
#first half of a black hole name
blackhole1 = ['OJ','APM','NGC','MRK','Messier','PKS','SGI']
#generates a name
def namegen():    
    planets = open("names.txt",'r').readlines()
    return random.choice(planets).replace("\n","")
#gets width/heigh of the terminal
def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0]) * 2
(columns, rows) = getTerminalSize()
#planet
def oredesc(orenumber):
    if orenumber < 357:
        orenumber = 357
    random.seed(orenumber)
    oretype  =  ["crystal","stone","metal","polymer"]
    descriptions = ["strange","radioactive","magnetic","extremely conductive","poor conductor","prismatic","transparent","toxic","pulsating","flamable","flame retardant"]
    colors = ["red","green","blue","yellow","purple","violet","pink","fuchsia","magenta","cyan","teal","black","grey","white","dark grey","yellow","tan","brown","orange"]
    strenghts = ["brittle","strong","fragile","dense","sparse","flimsy","hard","flexible","moldable","porous","spongy"]
    s1 = random.choice(oretype)
    s2 = random.choice(descriptions)
    s3 = random.choice(colors)
    s4 = random.choice(strenghts)
    return str("this ore is a " + random.choice(oretype) + ". it is a " + s2 + " " + s1 + ". It's color is " + s3 + ". it is also " + s4)
def creaturedesc(number):    
    random.seed(number)
    ctype  =  ["avian","reptile","fish","mammal","insect"]
    descriptions = ["strange","aggressive","docile","mentally volatile","weak","extremely strong","low intelligence","extremely intelligent","addorable","ugly"]
    colors = ["red","green","blue","yellow","purple","violet","pink","fuchsia","magenta","cyan","teal","black","grey","white","dark grey","yellow","tan","brown","orange"]
    attributes = ["flying","big","small","fast","slow","blood sucking","carnivorous","herbivorous","omnivorous","virtually immortal"]
    s1 = random.choice(ctype)
    s2 = random.choice(descriptions)
    s3 = random.choice(colors)
    s4 = random.choice(attributes)
    return str("this creature is a " + s1 + ". it is a " + s2 + " " + s1 + ". It's color is " + s3 + ". it is also " + s4)
class Planet():
    def __init__(self,size,name):
        if size != '':
            self.size = size
        else:
            #size of planet
            self.size = random.choice(['tiny','small','earth sized','large','giant','gas giant'])
        self.name = name
        self.ishabitable = random.choice([1,5])
        self.treasures = ""
        self.ores = []        
        #ores on planet
        ores = open("ores.txt",'r').readlines()
        for x in range(10):
            self.ores.append(random.choice(ores))
        #enviroment type and fauna and flora
        self.weather = random.choice(
        ["Frozen wasteland","Radioactive","Lightless","Sky Islands","Tundra","Forest","Savanna","Taiga","Chaparral","Rainforest","Grasslands","Desert","Alpine","Arctic","Desert Scrub","Deciduous Forest","Tundra Alpine","Mountain range","Grassland","Temperate deciduous forest","Temperate grasslands, savannas, and shrublands","Temperate forest","Temperate forest","Woodland","Mangrove swamp","Bog","Mesa","Ravine","Ocean","Arctic","Cave","Volcano"])

        self.fauna = random.choice(['no','scarce','some','average','extreme'])
        self.foliage = random.choice(['no','scarce','some','average','extreme'])
        self.inhabitants = []
        if self.fauna != "no":
            for x in range(100):
                self.inhabitants.append(random.choice(creatures))
        #does it have a space station orbiting it?
        self.hasspacestation = random.choice([True,False])
        if self.size == 1:
            size = 'tiny'
        if self.size == 2:
            size = 'small'
        if self.size == 3:
            size = 'earth sized'
        if self.size == 4:
            size = 'large'
        if self.size == 5:
            size = 'giant'
        if self.size == 6:
            size = 'gas giant'        
        if self.ishabitable > 1:
            habitability = 'no'
        if self.ishabitable == 1:
            habitability = 'full'            
        #generates the description.
        if habitability == 'no':
            self.notes = 'you land on a ' + size + ' planet. it has ' + self.foliage + ' flora and ' + self.fauna + ' fauna. it has a ' + self.weather + ' enviroment, several ore deposits of ' + ', '.join(self.ores).replace('\n','') + ', and no habitability(at least for you).'        
        elif self.name == 'Earth':
            self.hasspacestation = True
            self.notes = 'you land on a earth sized planet. it has extreme flora and extreme fauna. it has an earth-like enviroment, several ore deposits of ' + ', '.join(self.ores).replace('\n','') + ',and has full habitability. also, what the heck is earth doing in this universe!'
        elif habitability == 'full':
            self.notes = 'you land on a ' + size + ' planet. it has ' + self.foliage + ' flora and ' + self.fauna + ' fauna. it has a ' + self.weather + ' enviroment, several ore deposits of ' + ', '.join(self.ores).replace('\n','') + ',and has ' + habitability + ' habitability.'        
        if self.ishabitable > 1:
            self.habitable = False
        if self.ishabitable == 1:
            self.habitable = True
        if self.name == '':
            self.name = namegen()
            #makes 29 artifacts
        self.planetitems = items(100)
        self.planetitems.generate(random.choice(['generic','material','tool']),'null')
        #4 unique artifacts.
        self.planetitems.customitems([
            "statue of noah the cat",
            "hyperdrive","pirate crusher",
            "the god cube",
            "nokia 3310",
            "adamantarium armor",
            "celengil armor",
            "eximus armor",
            "prismite armor",
            "nokia 3310 armor",
            "mobedium armor",
            "iron armor",
            "copper armor",
            "gold armor",
            "atlarite armor",
            "traddium armor",
            "The OmniBlade",
            "Handheld Railgun",
            "Photon Sword",
            "Plasma Rifle",
            "Traddium sword",
            "Prismite sword",
            "iron sword",
            "copper sword",
            "Traddium Axe",
            "Prismite Axe",
            "iron axe",
            "copper axe",
            "Traddium Spear",
            "Prismite Spear",
            "iron spear",
            "copper spear",
            "Traddium Knife",
            "Prismite Knife",
            "iron knife",
            "copper knife",
            "Uru Warhammer",
            "gold Battle Axe",
            "Adamantarium Scythe",
            "Celengil Crossbow",
            
            
            
            ])
        hasitem = random.randint(1,5)
        if hasitem >= 3:
            self.treasures = ""
        if hasitem == 1 or hasitem == 2:
            self.treasures = random.choice(self.planetitems.returnitems())
        #has any colonies?
        self.colonies = []
        self.seed = random.randint(1,999999)
        self.hasalien = random.randint(1,5)
        self.structures = []
        if self.hasalien >= 3:
            self.colonies = []
        if self.hasalien == 1 or self.hasalien == 2:
            self.colonies.append(str(random.choice(creatures) + " colony"))
        #boring old find ore/artifact quest generator.
        if self.treasures != "":
            self.questtype = random.choice(["finditem","mine"])
        else:
            self.questtype = "mine"    
        if self.questtype == "finditem":
            self.questitem = self.treasures
            self.questtext = "ok good, please find the " + self.questitem + " on this planet"            
        if self.questtype == "mine":
            self.questitem = random.choice(self.ores)
            self.questtext = "ok good, please find " + self.questitem + " ore on this planet"        
    #returns the planet info
    def returnplanetinfo(self):
        questdata = {"type":self.questtype,"item":self.questitem,"text":self.questtext}
        stats = {"structures":self.structures,"seed":self.seed,"quest":questdata,"colonies":self.colonies,"creatures":self.inhabitants,'size':self.size,"ores":self.ores,'name':self.name,'ishabitable':self.habitable,'treasures':self.treasures,'weather':self.weather,'foliage':self.foliage,'fauna':self.fauna,'notes':self.notes,'spacestation':self.hasspacestation}
        return stats
#star
class Star():
    def __init__(self,planets,forcedstats):
        #forced stats by programmer
        self.forcedstats = forcedstats
        if self.forcedstats == []:        
            self.color = random.choice(['red','yellow','orange','white','blue']) 
            self.planetamount = random.randint(1,6)
            self.binary = 0
            self.size = random.choice([1,2,3,4,5]) #1 is dwarf, 2 is small, 3 is average, 4 is large, 5 is giant[only white and blue stars],6 being black hole
            if self.size >= 4:
                self.binary = random.choice([1,35])                
            isblackhole = random.randint(1,35)
            if isblackhole == 1:
                self.size = 6
            if isblackhole >= 2:
                pass        
        self.name = namegen()
        try:
            if self.binary == 1:
                self.name = 'binary ' + self.name
                self.color = 'star 1:' + self.color + ', star 2:' + random.choice(['red','yellow','orange','white','blue'])
                self.size = 'star 1:' + str(self.size) + ', star 2:' + str(self.size - 2)
            else:
                pass
        except:
            pass
        self.planets = []
        for x in range(self.planetamount):
            planet = Planet(random.randint(1,6),'') #1 being dwarf(pluto sized), 2 being small(mars sized), 3 being average(earth sized),4 being large(neptune sized), 5 being giant(saturn sized), 6 being gas giant(jupiter sized)
            planetstats = planet.returnplanetinfo() 
            self.planets.append(planetstats)        
        if self.forcedstats != []:
            self.color = self.forcedstats['color']
            self.planetamount = self.forcedstats['planetamount']
            self.size = self.forcedstats['size']
        if self.size == 5:
            self.color = random.choice(['white','blue'])        
        if self.size == 6:
            self.color = ['none(absorbs light)']
            self.planets = []
            for x in range(self.planetamount):
                planet = Planet(random.randint(1,6),'') #1 being dwarf(pluto sized), 2 being small(mars sized), 3 being average(earth sized),4 being large(neptune sized), 5 being giant(saturn sized), 6 being gas giant(jupiter sized)
                planetstats = planet.returnplanetinfo() 
                self.planets.append(planetstats)
            blackhole2 = ' ' + str(random.randint(100,300))
            self.name = str(random.choice(blackhole1) + str(blackhole2))
    def returnstarinfo(self):
        stats = {'name':self.name,'color':self.color,'size':self.size,'planets':self.planets}
        return stats
