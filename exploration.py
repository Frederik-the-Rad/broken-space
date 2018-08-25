print("beaming down...")
import random
"""
import markus
"""
global extradata
global playership
raw_input = input
import time
from colorama import init, Fore, Back, Style

green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW



init(convert=True)


from brokenspace import *
#basic npc fighting system
global avatarhealth
def fight(creature,storydir,inv):
    global playership
    global avatarhealth
    power = 0
    if "adamantarium armor" in inv:
        power+=20
    elif "celengil armor" in inv:
        power+=7
    elif "eximus armor" in inv:
        power+=5
    elif "prismite armor" in inv:
        power+=50
    elif "nokia 3310 armor" in inv:
        power+=70
    elif "mobedium armor" in inv:
        power+=5
    elif "iron armor" in inv:
        power+=10
    elif "copper armor" in inv:
        power+=7
    elif "gold armor" in inv:
        power+=15
    elif "atlarite armor" in inv:
        power+=70
    elif "traddium armor" in inv:
        power+=40
    elif "The OmniBlade" in inv:
        power+=100
    elif "Handheld Railgun" in inv:
        power+=75
    elif "Photon Sword" in inv:
        power+=50
    elif "Plasma Rifle" in inv:
        power+=60
    elif "Traddium sword" in inv:
        power+=50
    elif "Prismite sword" in inv:
        power+=45
    elif "iron sword" in inv:
        power+=10
    elif "copper sword" in inv:
        power+=5
    elif "the god cube" in inv:
        power += 1000
    elif "Traddium Axe" in playership.inv:
        power += 80
    elif "Prismite Axe" in playership.inv:
        power += 60
    elif "iron axe" in playership.inv:
        power += 25
    elif "copper axe" in playership.inv:
        power += 15
    elif "Traddium Spear" in playership.inv:
        power += 60
    elif "Prismite Spear" in playership.inv:
        power += 55
    elif "iron spear" in playership.inv:
        power += 20
    elif "copper spear" in playership.inv:
        power += 10
    elif "Traddium Knife" in playership.inv:
        power += 20
    elif "Prismite Knife" in playership.inv:
        power += 15
    elif "iron knife" in playership.inv:
        power += 5
    elif "copper knife" in playership.inv:
        power += 3
    elif "Uru Warhammer" in playership.inv:
        power += 200
    elif "gold Battle Axe" in playership.inv:
        power += 100
    elif "Adamantarium Scythe" in playership.inv:
        power += 125
    elif "Celengil Crossbow" in playership.inv:
        power +=60
    animalhealth = avatarhealth/2 + power/random.randint(1,10)
    animalpower = 50 + power/random.randint(1,10)
    enemycanevade = True
    s = open("creatures.txt","r").readlines()
                
    
    if creature + "\n" in s:
        print(green+"you encounter a hostile " + creature + ", it has these traits:\n\n\n" + creaturedesc(s.index(creature + "\n")))
    fighting = True
    
    
    while fighting == True:
        esc = raw_input("Do you attemp to escape?[y/n]:").lower()
        if esc == "y":
            if random.choice([1,0,1,1]) == 1:
                
                print(green + "got away safely!")
                time.sleep(1)
                break
            else:
                print(red + "Oh no you couldn't escape!")
        
        
        
        
        a = raw_input("part to attack[head/body/limbs]:")
        if a == "head":
            dodamage = random.randint(20,30) + power
            miss = random.choice([True,False,False,False])
            if miss == False:
                animalhealth -= dodamage
                print("you did " + str(dodamage + power) + " damage")
            else:
                print("you missed!")
                time.sleep(0.5)
                
        elif a == "body":
            dodamage = random.randint(15,20) + power
            miss = random.choice([True,False,False,False])
            if miss == False:
                animalhealth -= dodamage
                print("you did " + str(dodamage + power) + " damage")
            else:
                print("you missed!")
                time.sleep(0.5) 
            
                
                
        elif a == "limbs":
           dodamage = random.randint(10,15) + power
           miss = random.choice([True,False,False,False])
           if miss == False:
               animalhealth -= dodamage
               print("you did " + str(dodamage + power) + " damage")
           else:
               print("you missed!")
               time.sleep(0.5)
        else:
            print("you decided to sit there and let the animal attack you, because you didn't select the part of the animal to attack")
            time.sleep(0.5)
            
        if animalhealth <= 0:
            print(green + "you win!")
            
            with open(storydir,'a') as s:
                s.write('defeated animal\n')
            fighting = False
            time.sleep(2)
        if avatarhealth <= 0:
            print(red + "You died! Luckily you are cloned back on your ship...")
            with open(storydir,'a') as s:
                s.write('defeated by animal\n')
            time.sleep(2)
            inexplorer = False
            fighting = False
        time.sleep(1)
        dealdamage = random.randint(20,30) + animalpower/3
        
        
        print(red + "you dealt " + str(dealdamage) + " damage.")
        avatarhealth -= dealdamage
        time.sleep(1)

def explorergame(starmap,playership,storydir,allspecies):
    global avatarhealth
    avatarhealth = 200
    
        
    if "adamantarium armor" in playership.inv:
        avatarhealth+=120
    elif "celengil armor" in playership.inv:
        avatarhealth+=45
    elif "eximus armor" in playership.inv:
        avatarhealth+=30
    elif "prismite armor" in playership.inv:
        avatarhealth+=300
    elif "nokia 3310 armor" in playership.inv:
        avatarhealth+=600
    elif "mobedium armor" in playership.inv:
        avatarhealth+=30
    elif "iron armor" in playership.inv:
        avatarhealth+=60
    elif "copper armor" in playership.inv:
        avatarhealth+=45
    elif "gold armor" in playership.inv:
        avatarhealth+=15
    elif "atlarite armor" in playership.inv:
        avatarhealth-=30
    elif "traddium armor" in playership.inv:
        avatarhealth+=210
    
    
    
        
    with open(storydir,'r') as f:
       lines = f.readlines()
       story = str(lines)
                         
    
        
    pos = [0,0] 
    if starmap["size"] != 6:
        inexplorer = True
        while inexplorer==True:
               if avatarhealth <= 0:
                   break
                   inexplorer = False
               print("you have " + str(avatarhealth) + " health")
               #print(pos)
               
               num1 = starmap['seed'] + 1
               num2 = starmap['seed'] + 2
               num3 = starmap['seed'] + 3
               random.seed(starmap["seed"])
               
               
               def planetevent(playership,avatarhealth):
                   def town(playership,avatarhealth):
                       print(green + "\n\nYou encounter a civilization!")
                       if raw_input("do you explore it? [y/n]") == "y":
                           print(green + "\n\nyou decide to explore it")
                           time.sleep(2)
                           print("The town is " + random.choice(["small","large","very large","mid sized"]) + ". With " + random.choice(["Lots of housing","Lots of businesses",]) + ".\nThe town is " + random.choice(["Primitive","Very advanced"]) + ", technologically speaking.")
                           act = raw_input("Do you raid it[1], or Do you continue exploring[2]?")
                           if act == "1":
                               print("You attempt to raid it")
                               if avatarhealth < 100:
                                   print("You are too weak, and are stopped, and killed by the law enforcement")
                                   time.sleep(1)
                                   avatarhealth = 0
                                   inexplorer = False
                               else:
                                   print("You successfully raid the town. Taking some of it's riches")
                                   playership.money += random.randint(100,200)
                           if act == "2":
                               print("You keep exploring the town, not really finding much, a few solicitors attempt to sell you things, but you shoo them away, their items being\nworthless. After a while, you leave the town")
                                   

                       else:
                           print(red + "\n\nyou decide not to")
                           time.sleep(2)
                   def dungeon(playership):
                        print(green + "\n\nYou find a dungeon!\n\n")
                        if raw_input("do you explore it? [y/n]") == "y":
                            indungeon = True 
                            room = random.choice(["Corridor","Long corridor","small chamber","large chamber","exit"])
                            while indungeon == True:
                                
                                print(green + "\n\n\n\nYou are currently in a " + room)

                                if room == "Corridor":
                                    print(Fore.LIGHTCYAN_EX + "\n\nYou enter a normal sized corridor, going off in multiple directions.")
                                if room == "Long corridor":
                                    print(Fore.LIGHTCYAN_EX + "\n\nYou enter a very long corridor, going off in multiple directions")
                                if room == "small chamber":
                                    print(Fore.LIGHTCYAN_EX + "\n\nYou enter a smallish room, nothing special about it.")
                                if room == "large chamber":
                                    print(Fore.LIGHTCYAN_EX + "\n\nyou enter a very large room, nothing really stands out.")
                                
                                r = raw_input("Do you go north, south, east or west? or leave:")
                                if r == "leave":
                                    print("\n\n\n\n")
                                    break
                                    
                                if r == "north":
                                    if random.choice([True,False]) == True:
                                        print(Fore.LIGHTCYAN_EX + "\n\nYou explore around")
                                        room = random.choice(["Corridor","Long corridor","small chamber","large chamber"])
                                        time.sleep(1)
                                    else:
                                        print(red + "You cant go that direction\n")
                                        time.sleep(1)
                                        
                                if r == "east":
                                    if random.choice([True,False]) == True:
                                        print(Fore.LIGHTCYAN_EX + "\n\nYou explore around")
                                        room = random.choice(["Corridor","Long corridor","small chamber","large chamber"])
                                        time.sleep(1)
                                    else:
                                        print(red + "You cant go that direction\n")
                                        time.sleep(1)
                                if r == "west":
                                    if random.choice([True,False]) == True:
                                        print(Fore.LIGHTCYAN_EX + "\n\nYou explore around")
                                        room = random.choice(["Corridor","Long corridor","small chamber","large chamber"])
                                        time.sleep(1)
                                    else:
                                        print(red + "You cant go that direction\n")
                                        time.sleep(1)
                                if r == "south":
                                    if random.choice([True,False]) == True:
                                        print(Fore.LIGHTCYAN_EX + "\n\nYou explore around")
                                        room = random.choice(["Corridor","Long corridor","small chamber","large chamber"])
                                        time.sleep(1)
                                    else:
                                        print(red + "You cant go that direction\n")
                                        time.sleep(1)
                                
                                if random.choice(["Treasure","Monster","None","None","None","None","None"]) == "Treasure":
                                    print(yellow + "You find some treasure!")
                                    playership.inv.append(random.choice(["Uru","gold","iron","copper","silicon","prismite","Eximus","Atlarite","Adamantarium","Traddium","Celengil","Mobedium"]))
                                if random.choice(["Treasure","Monster","None","None","None","None","None"]) == "Monster":
                                    print(red+"You encounter a monster")
                                    fight(creature,storydir,playership.inv)
                        else:
                            print(Fore.LIGHTCYAN_EX+"You decide to ignore it.")
                            time.sleep(1)
    
                   def crashed_ship(playership):
                       
                            
                       print(Fore.GREEN +"you find a crashed ship half buried in the ground\n, do you want to:\n[1]:loot it\n2:leave it")
                       selector = raw_input("selector:")
                       if selector == "1":
                            print(Fore.GREEN + "you walk towards the ship")
                            random.seed(pos[0] + pos[1] + random.randint(1,999))
                            canloot = random.randint(1,5)
                            #print(canloot)
                            if canloot >= 4:
                                print(Fore.YELLOW + "you found some money and ores")
                                addition = random.randint(100,200)
                                playership.money += addition
                                if len(playership.inv) < playership.cargosize:
                                    oresel = random.choice(open("ores.txt","r").readlines())
                                    playership.inv.append(oresel.replace("\n",""))
                                    print(Fore.YELLOW + "you found " + oresel.replace("\n",""))
                                
                                else:
                                    print(Fore.RED + "but where unable to take the ores to your ship due to full inventory")
                                print(Fore.GREEN + "you also found " + str(addition) + " currency points")
                            else:
                                print(Fore.RED + "but there was nothing of importance there")
                                
                   def shop(playership):
                        
                        print(Fore.GREEN + "you find a small shop, do you want to\n----------\n[1]:check it out\n----------\n[2]:leave it\n----------\n")
                        selector = raw_input("selector:")
                        if selector == "1":
                            print(Fore.GREEN +'You walk over to the shop.')
                            b = raw_input('You can get:\n----------\ncrew\n----------\nweapons\n----------\nhyperdrive\n----------\nrepair\n')
                            if b == 'crew':
                               print(Fore.YELLOW +"spending 100 currency points, are you okay with this?")
                                                                   
                               if playership.money >= 100 and raw_input("y/n") == "y":
                                   if len(playership.crew) <= playership.crewamount:
                                       
                                       if random.choice([True,False]) == True:
                                           curspecies = random.choice(["aver","human","averx","cat","Algonian"])
                                       else:
                                           curspecies = random.choice(allspecies)
                                       name = str(random.choice(characternames) + '(' + random.choice(curspecies).replace('\n','') + ')')
                                       crewgen = {'name':name,'health':100,'profession':random.choice(['engineer','pilot','gunner','to be useless']),'room':''}
                                       playership.addcustomcrewmember(crewgen)
                                       print(Fore.YELLOW +'added ' + name + ' to crew.')
                                       playership.money -= 100
                                       with open(storydir,'a') as s:
                                           s.write('recruited ' + crewgen['name'] +'\n')

                                   else:
                                       print(Fore.RED +'you can\'hold any more crew!')
                                   
                               else:
                                    print(Fore.RED +"you need at least 100 currency points to buy crew")
                            if b == "hyperdrive":
                               if playership.money >= 600:
                                  playership.flightdist += 2
                                  print("your ship can now fly further.")
                                  playership.money -= 600
                               else:
                                   print(Fore.RED +"you have no money, how will you pay the mechanic! you need at least 600")
                            if b == "repair":
                                if playership.money >= 100:
                                    playership.health = playership.maxhealth
                                    playership.money -= 100
                                else:
                                    print(Fore.RED +"you have no money, how will you pay the mechanic! you need at least 100")
                            if b == "weapons":
                               if playership.money >= 175:
                                    playership.firepower += 20
                                    playership.money -= 175
                               else:
                                    print(Fore.RED +"you have no money, how will you pay the mechanic! you need at least 175") 
                            if b == "ship":
                                imgs = []
                                shipgen.make_cruiser(imgs)
                                #print(imgs)
                                testshipimg = random.choice(imgs)
                                testshipstats = [
                                    playership.name,
                                    random.randint(100,playership.health + 200),
                                    5,
                                    random.randint(3,playership.crewamount + 3),
                                    random.randint(30,playership.firepower + 20),
                                    50,
                                    20,
                                    random.randint(3,playership.cargosize + 3),
                                    playership.inv,
                                    playership.crew,
                                    playership.money,
                                    playership.fleet,
                                    playership.colonies,
                                    playership.colonies, #the more colonies the more fleet you can have
                                    playership.maxhealth,
                                    playership.allies,
                                    random.randint(12,playership.flightdist + 5),
                                    playership.kills,
                                    playership.mined,
                                    playership.role]
                                testship = ship(testshipstats,testshipimg)
                                testship.displayship('      ')
                                print(Fore.YELLOW +"price = 1000")
                                dobuy = raw_input("buy? y/n:")
                                if dobuy == "y":

                                    if playership.money >= 1000:
                                        playershipstats = testshipstats
                                       
                                        playership = ship(testshipstats,testshipimg)
                                        playershipimg = testshipimg
                                        playership.money = playership.money - 1000
                                        print(Fore.GREEN +'you now have a new ship')
                                        
                                    else:
                                        print(Fore.YELLOW +'you need 1000 currency points to buy this ship')

                        if selector == "2":
                            print(Fore.GREEN +"You decide you don't want to buy anything right now.")
                            time.sleep(1.5)
                  
                   exec(random.choice(["shop(playership)","crashed_ship(playership)","dungeon(playership)","town(playership,avatarhealth)","pass","pass","pass","pass","pass","pass","pass","pass","pass","pass","pass","pass","pass","pass","pass"]))
               random.seed(pos[0] + pos[1])
               
               
               
               buildings =  starmap['structures']
               ore = random.choice(starmap["ores"])
               ore = ore.replace("\n","")
               try:
                   creature = random.choice(starmap['creatures'])
                   creature = creature.replace("\n","")
               except:
                   pass
               random.seed(random.randint(1,99999999)) 
               if starmap['creatures'] != []:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   description = "you arive at a " + starmap["weather"] + " area, there is a " + creature + " walking around. and there is a deposit of " + ore
                   print(Fore.GREEN + description)
                   random.seed(random.randint(1,99999999)) 
                   print(Fore.GREEN +"there is " + random.choice(["moderate","some","average","extreme","barely any"]) + " amount of flora here")
                   if random.choice([True,False,False]) == True:
                       random.seed(random.randint(1,99999999)) 
                       print(Fore.LIGHTCYAN_EX +"You can" + random.choice([" faintly"," hazily"," feebly"," firmly"," clearly",""," loudly"," softly"," gently"," vaguely"]) + " hear the sound of a " + random.choice(["animal rustling through some grass","bird singing","predatorial animal stalking something","bird flying","water flowing","leaves rustling","small rocks falling","bugs chirping"]))
                   print(Fore.LIGHTCYAN_EX + "you're gps says your coordinates are " + str(pos[0]) + "," + str(pos[1]))
                   if random.choice([True,False,False,False,False]) == True:
                       fight(creature,storydir,playership.inv)
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
               else:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   description = "you arive at a " + starmap["weather"] + " area. and there is a deposit of " + ore
                   random.seed(random.randint(1,99999999)) 
                   print(Fore.GREEN +description)
                   random.seed(random.randint(1,99999999)) 
                   print(Fore.GREEN +"there is " + random.choice(["moderate","some","average","extreme","barely any"]) + " amount of flora here")
                   print(Fore.LIGHTCYAN_EX +"you're gps says your coordinates are " + str(pos[0]) + "," + str(pos[1]))
               for radbuilds in range(len(buildings)):
                   if buildings[radbuilds]["pos"] == pos:
                       #print(buildings[radbuilds]["pos"])
                       #print(pos)
                       print(Fore.GREEN +"you see a " + buildings[radbuilds]["name"] + " here")

               
                       
               planetevent(playership,avatarhealth)
               if avatarhealth <= 0:
                   break
                   inexplorer = False
               cmd = raw_input("you:")
               
               if "help" in cmd:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   print(Fore.GREEN +"\n\n\n----------\nheal: heals your avatar\n----------\ninv:displays inventory\n----------\nmine:mines the ores currently here\n----------\nleave:returns to ship\n----------\ncapture:captures any creature and adds it to inventory\n----------\ngo north/south/east/west:walks in that direction\n----------\nenter:enters the nearest building, if any\n----------\nbuild:builds a building with:name||frame material||interior material||exterior material\n\n\n")
                   time.sleep(5)
               elif "capture" in cmd:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   if len(playership.inv) < playership.cargosize:
                       playership.inv.append(creature)
                       print(Fore.RED +"captured " + creature)
                   else:
                       print(Fore.RED +"inventory full dude")
               elif "mine" in cmd:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   if len(playership.inv) < playership.cargosize:
                       playership.inv.append(ore)
                       print(Fore.YELLOW +"mined " + ore)
                   else:
                       print(Fore.RED +"inventory full dude")
               elif "inv" in cmd:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   print(Fore.GREEN +str(playership.inv))
               elif "leave" in cmd:
                   
                   inexplorer = False
               
               if "enter" in cmd:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   #name = raw_input("name of building")
                   for radbuilds in range(len(buildings)):
                       if buildings[radbuilds]["pos"] == pos:
                           if buildings[radbuilds]["extradata"]["type"] == "house":
                               print(Fore.GREEN +"you enter the house")
                               print(Fore.GREEN +"these people live here:")
                               print(Fore.GREEN +buildings[radbuilds]["extradata"]["items"])
                      
                           elif buildings[radbuilds]["extradata"]["type"] == "shop":
                               print(Fore.GREEN +"you enter the shop")
                               print(Fore.GREEN +"these items are sold")
                               for it in range(len(buildings[radbuilds]["extradata"]["items"])):
                                   print(buildings[radbuilds]["extradata"]["items"][it]['item'])
                                   print(str(buildings[radbuilds]["extradata"]["items"][it]["price"]))
                               print(Fore.GREEN +"enter the name of the item to purchase or press enter to leave")
                               selection = raw_input("you:")
                               for it in range(len(buildings[radbuilds]["extradata"]["items"])):
                                   if selection == buildings[radbuilds]["extradata"]["items"][it]["item"]:
                                       if playership.money >= buildings[radbuilds]["extradata"]["items"][it]["price"]:
                                           playership.inv.append(buildings[radbuilds]["extradata"]["items"][it]["item"])
                                           playership.money -= buildings[radbuilds]["extradata"]["items"][it]["price"]
                            
                           else:
                               print(Fore.GREEN +"you enter the building, um, there's nothing to do here. You walk out.") 
               if "north" in cmd:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   pos[1] = pos[1] + 1
                   
               elif "south" in cmd:
                    if avatarhealth <= 0:
                       break
                       inexplorer = False
                    pos[1] = pos[1] - 1
                   
               elif "west" in cmd:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   pos[0] = pos[0] - 1
                   
               elif "east" in cmd:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   pos[0] = pos[0] + 1

               elif "heal" in cmd:
                   if "health pack" in playership.inv:
                       avatarhealth = 200
                       playership.inv.remove("health pack")
                   else:
                       print(red + "You need a health pack item to do this!")
                       time.sleep(1)
               elif "build" in cmd:
                   if avatarhealth <= 0:
                       break
                       inexplorer = False
                   def askmaterials():
                       run = True
                       while run == True:
                           name = raw_input("name of structure?(type leave to leave)")
                           if "leave" in name:
                               run = False
                               break
                           mat1 = raw_input("frame material?:")
                           mat2 = raw_input("interior material?:")
                           mat3 = raw_input("exterior material?:")
                           def selecttype():
                               global extradata
                               typeof = raw_input("what type of building is this? shop/house/other")
                               if typeof == "shop":
                                   items = []
                                   amountofsells = raw_input("how many items can be sold here?:")
                                   for sells in range(int(amountofsells)):
                                       item = raw_input("item name:") 
                                       price = raw_input("price:")
                                       items.append({"item":item,"price":int(price)})
                                   extradata = {"type":"shop","items":items}
                               elif typeof == "house":
                                   members = []
                                   maxamounts = int(raw_input("how many people can live here? 1-10 preferred(if it is lower than 1 the game will crash)"))
                                   for people in range(maxamounts):
                                       members.append(random.choice(characternames))
                                       
                                   extradata = {"type":"house","items":members}
                               elif typeof == "other":
                                   newtype = raw_input("what is this other type?:")
                                   print(Fore.GREEN +"erm ok...")
                                   extradata = {"type":newtype,"items":[]}
                               else:
                                   print(Fore.RED +"I am afraid that type doesn't exist")
                                   selecttype()
                           selecttype()    
                           print("building structure:")
                           time.sleep(3)
                           if mat1 in playership.inv:
                               playership.inv.remove(mat1)
                               if mat2 in playership.inv:
                                   playership.inv.remove(mat2)
                                   if mat3 in playership.inv:
                                       playership.inv.remove(mat3)
                                       global extradata
                                       buildings.append({"pos":[pos[0],pos[1]],"name":name,"materials":{"in":mat2,"out":mat3,"mid":mat1},"extradata":extradata})
                                       print(Fore.GREEN +"ok done! a " + name + " has been built!")
                                       run = False
                           
                               
                               
                                   
                                   else:
                                       print(Fore.GREEN +"the exterior material is not in your inventory")
                                       askmaterials()
                               else:
                                   print(Fore.GREEN +"the interior material is not in your inventory")
                                   askmaterials()
                           else:
                               print(Fore.GREEN +"the frame material is not in your inventory")
                               askmaterials()
                   askmaterials()
                   
               else:
                   print("You " + str(cmd))
                   time.sleep(1)
                   
                  
             
                
    else:
        print(Fore.RED +"you cannot explore a gas giant silly, no mortal being can survive it")

  

               
if __name__ == "__main__":
    from brokenspace import *
    species = "human"
    playershipstats = [
        "test",
        300,
        5,
        8,
        30,
        50,
        20,
        8,
        ['rocks','antimatter',"rocks","rocks","prismite armor","Railgun"],
        [
        {'profession': 'engineer', 'health': 100, 'name': 'Harper(' + species + ')','room':'corridor'},
        {'profession': 'captain', 'health': 100, 'name': 'P.R.I.S.M(robot)','room':'bridge'},
        {'profession': 'gunner', 'health': 100, 'name': 'Levi(' + species + ')','room':'corridor'}],
        100,
        0,
        0,
        0, #the more colonies the more fleet you can have,
        300,
        [],
        12,
        0,
        0,
        'a vagabond hired to do dirty work for your government.',10]
    playershipimg = [
    {"       ____,----._                                 "},
    {"   ,--'| _|\" o;.  `.____        ____  ,,=====._   "},
    {" .=|.':| U| ;:;:  .- \,,`-.===='}.,'\//       \"`   "},
    {"(]=|;: |o |  ,.  (  :;)::(     ):;::>}X==========- "},
    {" `=| :;|  | ,: o  `-_/``,-`====.}___/\\       _,   "},
    {"  `--.|__|_ .:  _,' \"""              ``=====''     "},
    {"       ~  ~`----'                                  "},
    ]    
    playership = ship(playershipstats,playershipimg)
    explorergame({'treasures': 'brittle shovel', 'creatures': ['Ojoi', 'Poee', 'Avfouoraea', 'Exooo', 'Ceiuxou', 'Xga'], 'structures': [], 'name': 'Learre', 'seed': 585772, 'colonies': ['Zkouar colony'], 'quest': {'item': 'Qulaorium\n', 'type': 'mine', 'text': 'ok good, please find Qulaorium\n ore on this planet'}, 'size': 4, 'spacestation': False, 'weather': 'Mesa', 'notes': 'you land on a large planet. it has scarce flora and some fauna. it has a freezing enviroment, several ore deposits of Anlaraceasium, Qulaorium, Veanlaasium, Mabeesesasium, Mobedium, Leresoinium, Eximus, Alarebeorium, Areddiium, Diarbeinium, and no habitability(at least for you).', 'fauna': 'some', 'foliage': 'scarce', 'ores': ['Anlaraceasium\n', 'Qulaorium\n', 'Veanlaasium\n', 'Mabeesesasium\n', 'Mobedium\n', 'Leresoinium\n', 'Eximus\n', 'Alarebeorium\n', 'Areddiium\n', 'Diarbeinium\n'], 'ishabitable': False},playership,"c:/broken space/save1/story.txt",open("creatures.txt","r").read())
                                


                                       
