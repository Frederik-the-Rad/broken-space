# coding: utf-8
import random
engines = [


]

def generatehull():
    beg = ["[","[=","{=","||","|=|","]:=]]"]
    mid = ["+=+","|+|","[=]","{=]","{||}","[::]","[<]"]
    end = ["]","=]","=}","||","|=|","=>","->>","]>>>"]
    return random.choice(beg) + random.choice(mid) + random.choice(end)
def generateengine():
    thrusters = [
        '#',
        '>=',
        '}=+',
        '}=|=|',
        '}[]=|',
        '}[+]==|',
        ']=[]==>',
        '>=|+|=<>',
        '}>=||=]',
        '>:-',
        ">#[]>",
        ]
    enginebodies = [
         '===',
         '<=>',
         '+-+',
         '|==|',
         '<||>',
         '|[+]|',
         '[=+=]',
         '{+++}',
         '<===>',
         "<[===]>",
         "|<>|",
         
         ]
    enginecaps = [
         '=>>',
         '|}>',
         '==>',
         '-}',
         '=>',
         '=}',
         '+>',
         '+}',
         '+]',
         '=]',
         '||]',
         "[]>>>",
         "|3",
         ]
    engine = random.choice(thrusters) + random.choice(enginebodies) + random.choice(enginecaps)
    return engine
    
def generateweapon():
    backs = [
        '+',
        '|=',
        '<+=',
        '<=',
        '|=<',
        ]
    bodies = [
        '----',
        '------',
        '========',
        '<=======>',
        '===---',
        '[|====---',
        ]
    endcaps = [
        '*',
        'o',
        '+',
        '0',
        ]

    weapon = random.choice(backs) + random.choice(bodies) + random.choice(endcaps)
    return weapon

def generatecockpit():
    seats = [
        '|<>|',
        '|{}|',
        '{<>}',
        '|0|', 
        ]
    middle = [
        '===',
        '====',
        '<====',
        '<=====',
        ]
    nosecones = [
        '>',
        '}',
        '>>>',
        ]
        
    cockpit = random.choice(seats) + random.choice(middle) + random.choice(nosecones)
    return cockpit

def makeship(shipspritelist):
    weapontype = generateweapon()
    enginetype = generateengine()
    shiptype = random.randint(1,3)
    if shiptype == 1:
        ship = [
            enginetype,
            ' ' + str(weapontype),
            '    ' + generatecockpit(),
            ' ' + str(weapontype),
            enginetype,
            ]
        if ship != "":
           shipspritelist.append(ship)
        else:
            return ship
    elif shiptype == 2:
        ship = [
            weapontype,
            ' ' + str(enginetype),
            '    ' + generatecockpit(),
            ' ' + str(enginetype),
            weapontype,
            ]
        if ship != "":
           shipspritelist.append(ship)
        else:
            return ship
    elif shiptype == 2:
        ship = [
            weapontype,
            ' ' + str(enginetype) + weapontype,
            '        ' + generatecockpit(),
            ' ' + str(enginetype) + weapontype,
            weapontype,
            ]
        if ship != "":
           shipspritelist.append(ship)
        else:
            return ship
def make_cruiser(shipspritelist):
    weapontype = generateweapon()
    enginetype = generateengine()
    cockpittype = generatecockpit()
    h1 = generatehull()
    h2 = generatehull()
    h3 = generatehull()
    shiptype = random.randint(1,8)
    if shiptype == 1 or shiptype == 2:
        ship = [
        enginetype + h1 + h1 + h1 + h2 + weapontype,
        ' ' + enginetype + "|----------|" + h3 + h3 + cockpittype,
        ' ' + h1 + h1 +    "|          |" + h3 + h2 + cockpittype,
        ' ' + enginetype + "|----------|" + h3 + h3 + cockpittype,
        enginetype + h1 + h1 + h1 + h2 + weapontype,
        ]
        
        if ship != "":
           shipspritelist.append(ship)
        else:
            return ship
    elif shiptype == 3 or shiptype == 4:
        ship = [
        enginetype + h1 + h1 + h1 + h2 + weapontype,
        ' ' + enginetype + "|-------------\\" + h3 + h3 + cockpittype,
        ' ' + h1 + h1 +    "|             |" + h3 + h2 + cockpittype + weapontype,
        ' ' + enginetype + "|-------------/" + h3 + h3 + cockpittype,
        enginetype + h1 + h1 + h1 + h2 + weapontype,
        ]
        
        if ship != "":
           shipspritelist.append(ship)
        else:
            return ship
    elif shiptype == 5 or shiptype == 6:
        ship = [
        enginetype + h1 + h1 + h1 + h2 + weapontype,
        ' ' + h1 + h2 + "/------------|" + h3 + h3 + cockpittype +weapontype,
        ' ' + h1 + h1 +    "|            |" + h3 + h2 + cockpittype,
        ' ' + h1 + h2 + "\\------------|" + h3 + h3 + cockpittype + weapontype,
        enginetype + h1 + h1 + h1 + h2 + weapontype,
        ]
        if ship != "":
           shipspritelist.append(ship)
        else:
            return ship
    elif shiptype == 7 or shiptype == 8:
        ship = [
        enginetype + h3 + h3 + h3 + h2 + h2 + h1 + weapontype,
        enginetype + h3 + h3 + h3 + h2 + h2 + h1 + weapontype,
        '  ' + h2 + h2 + "/----------------------------------|" + h2 + h2 + h3 + cockpittype,
        '  ' + h3 + h1 + "|                                  |" + h2 + h2 + h3 + h3 + h3 + cockpittype,
        '  ' + h3 + h1 + "|                                  |" + h2 + h2 + h3 + h3 + h3 + cockpittype,
        '  ' + h2 + h2 + "\\----------------------------------|" + h2 + h2 + h3 + cockpittype,
        enginetype + h3 + h3 + h3 + h2 + h2 + h1 + weapontype,
        enginetype + h3 + h3 + h3 + h2 + h2 + h1 + weapontype,
    
        

            ]
        if ship != "":
           shipspritelist.append(ship)
        else:
            return ship
if __name__ == "__main__":
    while True:
        lists = []
        make_cruiser(lists)
        for x in range(len(lists)):
            for y in range(len(lists[x])):
                print(str(lists[x][y]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
            
           

        print("\n\n\n")
        lists = []
        makeship(lists)
        for x in range(len(lists)):
            for y in range(len(lists[x])):
                print(str(lists[x][y]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
            
           

        print("\n\n\n")
        input("")

	
