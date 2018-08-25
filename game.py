 
helpmes = """
If you ever need help, then type help.
Note:
    a <> around a word is an argument,
    e.g.: <star name>, that means, just type out the name of a
    Star. If a command is just one word without the <>, there are no arguments
            

    If it is two words but no <> then consider it one word
    e.g.: ship stats
    Also, a [y/n] is a yes/no, but in a quest you get a
    [y/n/c] so what is the 'c', well, it stands for
    Continue quest.	

List of commands for star map:
    Cheat: if you are a developer you know how it works,
    
    <Star name>: if the star is within the range of "parsecs" your ship 	can travel in then in flies to the star
    How to know if your ship can reach a star:
            Each column or row = 1 parsec however 6 columns + 6 rows does not equal 12 parsecs, it equals 6. Get the idea?
    
    Describe:describes an ore or creature.
    Stats:displays stats

    Crew:displays crew
    
    Train: retrains a crewmember

    Exploreship: explore your ship, similarely to exploring a planet
    
    Fire: after typing this, enter a crewmember's name and he/she will be removed from your ship.

    Destroy item: after typing this, enter a name of an item in your cargo hold,
    It will jettison the item from your cargo hold

    Map: shows the map

    Regenerate: If you have the right item, this allows you to "create" a new universe

    Exec: If  you have the right item, this allows you to modify the game's code, within the game.

    Repair: If you have a health pack, this allows you to use it to repair your ship
    
All star commands:
After flying to a star, you still need commands

    <planetname>: jumps to a planet

    Leave: returns to star map

    Destroy: destroys a planet, if you have the item to do so,

    Create: creates a planet, if you have the item to do so,

All planet commands:
    Leave: leaves the planet

    Capture: captures the alien colony on the planet (if any)

    Colonize: colonizes the planet

    Quest: well, it's a quest!

    Mine: mines for all ores on planet.

    Spacestation: flies to space station.


All Spacestation commands:



Crew: recruits a crewmember

Fleet: adds a ship to your fleet

Upgrade: lists upgrades

Shiplook: makes your ship look like the contents of a .txt file in the c:/broken space/ folder

Trade: trade ores for currency points

Leave: leaves space station

Shipyard: opens the shipyard menu, for buying new ships




Useful tips:
    If you come across a sketchy event like: "a pirate looking ship is offering you a weapon", and you get three choices: 1: check it out, 2: leave it, 3: destroy and loot it

    The first one has a potential to be a trap, whereas leaving it would be safer if your ship's health is low.

    If you are low on money, try mining ores on a planet, and then sell it at a Spacestation

    If you are low on health, find a Spacestation, and then go to the upgrades tab, and repair it, (note: it costs 100 currency points early game, the more you progress the more expensive it is)
    
    Also, avoid as many fights as possible early game, as your ship will slowly have it's health eaten away, and you will eventually be destroyed, meaning you lose all that gold you collected.

    One last thing, if you choose the human species DO NOT go to sol early game, as this will trigger the boss fight, and you WILL be destroyed.

    



"""


import time
from colorama import init, Fore, Back, Style
import threading
from threading import Thread
import socket
init(convert=True)
red = Fore.RED + Back.LIGHTBLACK_EX
yellow = Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX
green = Fore.GREEN + Back.LIGHTBLACK_EX
blue = Fore.BLUE + Back.LIGHTBLACK_EX
lightblue = Fore.LIGHTCYAN_EX      + Back.LIGHTBLACK_EX

if __name__ == "__main__":
     

    time.sleep(1)
    print(lightblue + 
"__________                __                     _________                          \n"+
red+"\______   \_______  ____ |  | __ ____   ____    /   _____/__________    ____  ____  \n"+
yellow+" |    |  _/\_  __ \/  _ \|  |/ // __ \ /    \   \_____  \\____ \__  \ _/ ___\/ __ \ \n"+
green+" |    |   \ |  | \(  <_> )    <\  ___/|   |  \  /        \  |_> > __ \\  \__\  ___/ \n"+
blue+" |______  / |__|   \____/|__|_ \\___  >___|  / /_______  /   __(____  /\___  >___  >\n"+
lightblue+"        \/                    \/    \/     \/          \/|__|       \/     \/    \/ \n")
    print(red + "Ver Alpha 0.1" + lightblue)

    time.sleep(0.5)
print(Style.BRIGHT)
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")
import sys
global playership
import os

try:
    import clipboard
except:
    pass

import random
import platform
import subprocess
import shipgen
import cmd



from shutil import copy
from brokenspace import *
import platform
import datalib
from math import *
#list of pirate ships
pirateships = []
#generate pirate ships
for ps in range(100):
    shipgen.makeship(pirateships)
for psc in range(50):
    shipgen.make_cruiser(pirateships)
#list of ship/item sprites, a \\ instead of \ is to prevent errors
sprites = [
    #the scavenger, a startrek enterprise inspired ship
[
 "      /=======\\",
 "      \HHHHHHH/",
 "        \||/",
 "}\==============_=_/ ____.---'---`---.____",
 "}\============\_ \    \----._________.----/",
 "              \ \   /  /    `-_-'",
 "          __,--`.`-'..'-_",
 "         /____==========||",
 "              `--.____,-'",
 

    ],
    #the goliath, a more combat based version of the scavenger
[
  "    /===========\\",
  "    \HHHHHHHHHHH/",
  "        \||/",
  "         ||                  _____..---========+*+==========---.._____",
  "________/||\__________ __,-='=====____  =================== _____=====`=",
  "(._____________________I__) - _-=_/    `---------=+=--------'",
  "    /      /__...---===='---+---_'",
  "   '------'---.___ -  _ =   _.-'    *    *    *   *",
  "                  `--------'",

    ],


    #Algonian flagship, looks 10x smaller than it actually is.
[
"          /--\\",
"     ;; /++++++\\ ;;",
"  ;; []++++++++++[] ;;",
" [=[]+\"----------\"+[]=]",
" [=||++||[====]||++||=]",
" [=||++||[=@@=]||++||=]",
" [=||++||[====]||++||=]",
" [=]   ||======||   [=]",
" [=]   |+]====[+|   [=]",
" [=]   [==|==|==]   [=]",
" [==]   \=|++|=/   [==]",
" [==]	   	[==]\n",
],

    #Aeternum flagship
[
"\n[]/-----\\===\\",
"[]  |----\\_________________================\\",
"   /--==---====/-------------]",
"  |/--===---|-\___          |==|=============================\\",
"   [''```'{#]===+\\][==\\",
"   [''```'{#]===+/][==/",
"  |\-----|-/---          |==|=============================/",
"   \--===---====\-------------]",
"[]  |--==--|-----------------================/",
"[]\-----/===/\n",
],
#human flagship
[
"              A   A   A",
"             | | | | | |",
"           __| |_| |_| |___nnnnnn_____----____-===-----",
"   _    __/--| |-| |-|_|---~~~-------~~~---\==/~~\.",
"O=|-|OOOOO--<=X===X===X=>-| | |-----| | |>  HHK   |    ",
"   ~    ~~\--| |-| |-|~|---___-------___---/==\__/'    ",
"             | | | | | |                           ",
"             | | | | | |",
"              V   V   V                                            O-",


],

#cat flahsip, small but vicious, like a cat!
[   
"|==|\\",
"|==|\\\\",
"}====[-----|=|H))---o___________",
"}====[+==,-------#@#-----------'",
"}====[|----------#@#-----------/",
'}====[|____//////""~~~~~~~~/s~/',
    ],



#dragon flagship
[
"                           |-----------|",
"           i               |===========|                       ",
"           |               |,---------.|                      __--~\\__--.",
"    #---,'###`-_   `n     |`---------'|    `n    `n     ,--~~  __-/~~--'_____.",
"       |~~~~~~~~~|---~---/=|___________|=\\---~-----~-----| .--~~  |  .__|     |",
"     -[|.--_. ===|#####|-| |@@@@|+-+@@@| |]=###|/-++++-[| ||||___+_.  | `===='-.",
"     -[|'==~'    |#####|-| |@@@@|+-+@@@| |]=###|\\-++++-[| ||||~~~+~'  | ,====.-'",
"       |_________|---u---\\=|~~~~~~~~~~~|=/---u-----u-----| '--__  |  '~~|     |",
"        \\       /=-   `   |,---------.|      `     `    `--__  ~~-\\__--.~~~~~'",
"----=:===\\     /          |`---------'|                      ~~--_/~~--'",
"      --<:\\___/--         |===========|",
"                           |-----------|",
"                           |===========|",
    ],
]


itemlist = {
        #a statue of my pet cat
"noah":[
"                         _"
"                       |_\\"
"                       |_|"
"                       |_|"
"  |\                   |_|"
" /, ~\                /_/"
"X     `-.....-------./_/"
" ~-. ~  ~||||||||||    |"
"    \    |||||||||/    |"
"     \  /||||||||\   /"
"     | /\ ~~~~~   \ |"
"     |_|_\        ||_|"
"     |_|\_\       ||_)"
"    (_/ (_/      ((_/ "
"=======noah=the=cat===",],
    #this does not look like a hyperdrive, or does it?
"hyperdrive":[
"|--------------------",
"|---------------oo---",
"|--NCZ701------oooo--",
"|---------------oo---",
"|--------------------",],



    #the banhammer

"banhammer":[
"[\         /===\         /]",
"[=\        |===|        /=]",
"[==\       |===|       /==]",
"[----------|BAN|----------]",
"[----------|===|----------]",
"[----------|===|----------]",
"[==/       |===|       \==]",
"[=/        |===|        \=]",
"[/         |===|         \]",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
"           |===|           ",
    ],
    #pirate crusher.
"pirate":[
"              _________",
"            /'        /|",
"           /         / |_",
"          /         /  //|",
"         /_________/  ////|",
"        |   _ _    | 8o////|",
"        | /'// )_  |   8///|",
"        |/ // // ) |   8o///|",
"        / // // //,|  /  8//|",
"       / // // /// | /   8//|",
"      / // // ///__|/    8//|",
"     /.(_)// /// |       8///|",
"    (_)' `(_)//| |       8////|___________",
"   (_) /_\ (_)'| |        8///////////////",
"   (_) \"/ (_)'|_|         8/////////////",
"    (_)._.(_) d' Hb         8oooooooopb'",
"      `(_)'  d'  H`b",
"            d'   `b`b",
"           d'     H `b",
"          d'      `b `b",
"         d'           `b",
"        d'             `b",],

    #the god cube.
"cmd":[
"   0-------0",
"  /|/ o \ /|",
" / |\ o //\|",
"0--|----0oo|",
"| / o \-|\//",
"| o o o | /",
"| \ o / |/",
"0-------0",],

    #a generic statue for the "statue" and "artifact" item type
"statue":[
"  o  ",
" --- ",
"| = |",
"| = |",
" === ",
" | | ",
"=+ +=",
"-----",],

    #a lame attempt at a jewel shape
"gem":[
"  /--\\",
" /---\\",
" |----|",
" |----|",
" \\---|",
"  \\--/",

    ],

"universeseed":[

"```````````````````````````-//-``````````.-.``````````````````````````",
"``````````````````````````+s::+s+.````:+so+s+`````````````````````````",
"`````````````````````````/y-`````-os/.`````.y+````````````````````````",
"`````````````````````````:y:```.+s/.```````-y:````````````````````````",
"`````````````````````````-yo:/+sy++///::--.`.`````````````````````````",
"````````````````````-/+ssooy+ss:----::://+oo+/-.``````````````````````",
"``````````````````.+so:-```.soo.````````````.-/+so/-``````````````````",
"`````````````````ss.```````:y````:++/````os`````./so-`````````````````",
"`````````````````.+s+:.```/y:-```:++/`````.```````-so`````````````````",
"```````````````````.:+:``:y/`s-````````````:```:+so:``````````````````",
"````````````````````````.so``+y:```````````s```::.````````````````````",
"````````````````````````+y.```:y+``````````y:`````````````````````````",
"````````````````````````so`````-ss-````````y+`````````````````````````",
"````````````````````````so.``:+o``.+s+.````y+`````````````````````````",
"````````````````````````.osoo+:.````./so/--s.`````````````````````````",
"```````````````````````````..```````````-..:``````````````````````````",

    ],


"healthpack":[
"/--------|--------\\",
"|        |        |",
"|        |        |",
"|        |        |",
"|        |        |",
"|        |        |",
"=========H=========",
"|        |        |",
"|        |        |",
"|        |        |",
"|        |        |",
"|        |        |",
"\\-------|--------/",
    ],
    #a ridiculous jumble of symbols for the "thing" item, in making this I pretty much smacked my head on the keyboard.
"thing":
[
"6788[686.563].8[]67.4]b.h][[ rgh]",
"htrjhtrnb./;5u.5;]un.;35]u.",
"3nu3;u][u/][u35;[u;5bn 5u",
"356uy7/356;nu[]56pun7]56p",
"3n573p5735[n7[35.o73.p5[67pn3[",
"b2bn474p7=-.4n-6p7=p.b=4vp6=57p=",

    ],
    #"does this look like a sword or a knife?
"sword":[
"   /\\",
"   ||",
"   ||",
"   ||",
"   ||",
"   ||",
"   ||",
"   ||",
"   ||",
"   ||",
"   ||",
"/--++--\\",
"   ||  ",
"   ||  ",
],

    #it's a pickaxe. What more needs to be said?
"pickaxe":[
"/--------\\",
"    ||",
"    ||",
"    ||",
"    ||",
"    ||",
"    ||",
"    ||",
"    ||",


    ],

    #a lumberjack axe thingy
"axe":[
"   /'-./\\_",
"   :    ||,>",
"    \.-'||",
"        ||",
"        ||",
"        || ",
"        || ",
"        || ",
"        || ",
"        || ",
"        || ",
"        || ",
"        || ",
"        \\/ ",




    ],
"saw":[
"",
"     /=============\\",
"[===[===============\\",
"     vvvvvvvvvvvvvvvv",
"",
    ],
"bow":[
"  []\\",
"  |  \\",
"  |   \\",
"  |    \\",
"  |     \\",
"  |      \\",
">>|-------]--->",
"  |      /",
"  |     /",
"  |    /",
"  |   /",
"  |  /",
"  []/",
    ],

"knife":[
"   /\\",
"   ||",
"   ||",
"   ||",
"   ||",
" /-++-\\",
"   ||  ",
"   ||  ",
],


#a shovel, a ugly shovel
"shovel":[
" /======\\",
" |  ||  |",
" |  ||  |",
" \\ ||  /",
"  \\|| /",
"    ||",
"    ||",
"    ||",
"    ||",
"    ||",
"    ||",


    ],



    #Is a pcb a good option for the machine part or should I do a gear?
"machine":[
"                 .--------------."
"               ___|  _  _  _  _  |____________________________",
"              /   |  || || || ||_|___             _      _   /;",
"             /.--------------.      /|___       +(_)    (/) //",
"            / |  _  _  _  _  |     / ___ \      _  OUT     //",
"           /  |  || || || || |____/ ___ \(\)  -(_)        //",
"          /   |  || || || || |    | /  \(\)   _          //",
"         /    |______________|____|/   (\)  -(_)        //",
"        / _                                 _  BAT _   //",
"       / (\) MJP                          +(_) 9v (=) //",
"      /______________________________________________//",
"      `----------------------------------------------' ",


    ],

    #A wheel. A plain Wheel.
"wheel":[
"                           /\\                          \\",
"                          /''\\                          \\",
"                         /''''\\____________________      \\",
"                        /'''''/////////////////////\\      \\",
"                       /'''''////\\   \\////////////''\\      \\",
"                      /'''''////''\\   \\//////////''''\\      \\",
"                     /'''''////\\'''\\   \\   /'''/\\'''''\\      \\",
"                    /'''''//////\\'''\\   \\ /'''///\\'''''\\      \\",
"                   /'.---.////// \\'''\\   /'''//// \\'''''\\      \\",
"  _ _ _ _ _ _     /'/ _  \\\\////   \\___\\_/'''////   \\'''''\\      \\",
" '-_-_-_-_-. \\   /'/ / \\  \\\\//   /\\     \\''//// \\   \\'''''\\      \\",
"            \\\\`---------\\  \\\\------\\____ \\////___\\---\\'''''\\      \\--.",
"             \\`---------/  //------|______________|---\\'''''\\______\\--`",
"              `=======_/  //=======//////\\   \\////====/'''''////////=='",
"                \\'''\\____//  \\   \\//////''\\   \\//    /'''''////////",
"                 \\'''| |||    \\   /'''/\\'''\\   \\    /'''''////////|",
"                  \\''| |||     \\ /'''///\\'''\\   \\  /'''''////////||",
"                   \\'| |||      /'''//// \\'''\\   \\/'''''////////|||",
"                    \\| |||\\    /'''////   \\'''\\  /'''''//////// |||",
"                     | |||'\\  /'''////_____\\___\\/'''''////////| |||",
"                     | |||''\\ \\''////           \\''''//////// | |||",
"                     | |||'''\\ \\////             \\''////////  | |||",
"                     | |||''''\\___________________\\////////   | |||",
"                     | |||''''////////////////////////////    | |||",
"                     | |||\\''////////////////////////////     | |||",
"           | ||| \\////////////////////////////      | |||",
"                 ____| |||_                               ____| |||_",
"                 `.  '.||| `.                             `.  '.||| `.",
"                   `.________`.                             `.________`.",




    ]
}





#define directories for files
global difficulty
savedir = os.path.join('c:/broken space/save' + currentsave,'save.data')
savebackdir = os.path.join('c:/broken space/save' + currentsave + '/save backup','save.data')

storydir = os.path.join('c:/broken space/save' + currentsave + '/' ,'story.txt')

if not os.path.exists('c:/broken space/'):
    
    os.makedirs('c:/broken space/')
    
    os.makedirs('c:/broken space/ships')
    os.makedirs('c:/broken space/save1')
    os.makedirs('c:/broken space/save2')
    os.makedirs('c:/broken space/save3')
    os.makedirs('c:/broken space/save1/save backup/')
    os.makedirs('c:/broken space/save2/save backup/')
    os.makedirs('c:/broken space/save3/save backup/')

    
    
    h = open('c:/broken space/save1/save backup/save.data','w')
    h1 = open('c:/broken space/save2/save backup/save.data','w')
    s1 = open('c:/broken space/save1/story.txt','w')
    s2 = open('c:/broken space/save2/story.txt','w')
    s3 = open('c:/broken space/save3/story.txt','w')
    s1.close()
    s2.close()
    s3.close()
    
    
     




    
  #gets the screen size in columns and rows.
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

        ### Use get(key[, default]) instead of a try/catch
        #try:
        #    cr = (env['LINES'], env['COLUMNS'])
        #except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0]) * 2
(columns, rows) = getTerminalSize()
#loads the alien species'
with open('creatures.txt','r') as f:
    allspecies = f.readlines()
    print("loading creatures 0%\n")
for x in range(50000):
    addcreature(str(allspecies[x]).replace('\n',''))
print("loading creatures 50%\n")
for x in range(50001,100000):
    addcreature(str(allspecies[x]).replace('\n',''))
print("loading creatures 100%\n")

try:
    import console
except ImportError:
    pass

save = []

try:
    raw_input = input
except:
    pass





import math

import string

random.seed(0)

# calculate a random number where:  a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

# Make a matrix (we could use NumPy to speed this up)
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
def sigmoid(x):
    return math.tanh(x)

# derivative of our sigmoid function, in terms of the output (i.e. y)
def dsigmoid(y):
    return 1.0 - y**2

class NN:
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.ni = ni + 1 # +1 for bias node
        self.nh = nh
        self.no = no

        # activations for nodes
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no
        
        # create weights
        self.wi = makeMatrix(self.ni, self.nh)
        self.wo = makeMatrix(self.nh, self.no)
        # set them to random vaules
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)

        # last change in weights for momentum   
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)

    def update(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.ni-1):
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]

        # hidden activations
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoid(sum)

        # output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)

        return self.ao[:]


    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k]-self.ao[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error

        # update output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M*self.co[j][k]
                self.co[j][k] = change
                #print N*change, M*self.co[j][k]

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k]-self.ao[k])**2
        return error


    def test(self, patterns):
        for p in patterns:
            print(p[0], '->', self.update(p[0]))

    def weights(self):
        print('Input weights:')
        for i in range(self.ni):
            print(self.wi[i])
        print()
        print('Output weights:')
        for j in range(self.nh):
            print(self.wo[j])

    def train(self, patterns, iterations=10000, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 100 == 0:
                #print('error %-.5f' % error)
                pass


def demo():
    # Teach network XOR function
    pat = [
        [[0,0], [0]],
        [[0,1], [1]],
        [[1,0], [1]],
        [[1,1], [0]]
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(2, 2, 1)
    # train it with some patterns
    n.train(pat)
    # test it
    n.test(pat)


#basic npc fighting system
def fight():
    
    
    global playership
    enemyhealth = enemyhealthdef
    enemycanevade = True
    weaponhealth = 50
    fighting = True
    howrepaired = 0
    ship = random.choice(pirateships)
    for x in range(len(ship)):
        print(red + str(ship[x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
        esc = raw_input("Do you attemp to escape?[y/n]:").lower()
        
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        if esc == "y":
            if random.choice([1,0,1]) == 1:
                
                print(green + "got away safely!")
                time.sleep(1)
                break
            else:
                print(red + "Oh no you couldn't escape!")
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)

def rebelfight():
    
    
    global playership
    enemyhealth = enemyhealthdef
    enemycanevade = True
    weaponhealth = 50
    fighting = True
    howrepaired = 0
    ships = []
    shipgen.make_cruiser(ships)
    
    ship = random.choice(ships)
    for x in range(len(ship)):
        print(red + str(ship[x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
        esc = raw_input("Do you attemp to escape?[y/n]:").lower()
        
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        if esc == "y":
            if random.choice([1,0,1]) == 1:
                
                print(green + "got away safely!")
                time.sleep(1)
                break
            else:
                print(red + "Oh no you couldn't escape!")
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)



#final boss fight stage 1       
def finalfightl1():
    global playership
    enemyhealth = 9000 + int(bosshealthdef * 5)
    
    enemycanevade = True
    weaponhealth = 200
    fighting = True
    howrepaired = 0
    for x in range(11):
        print(lightblue + str(sprites[2][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
      
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)    
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)
        
#final boss fight stage 2
def finalfightl2():
    global playership
    enemyhealth = 2000  + int(bosshealthdef * 5)
    print("Health:" + str(enemyhealth))
    enemycanevade = True
    weaponhealth = 200
    fighting = True
    howrepaired = 0
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
      
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)    
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)


#final boss fight stage 3
def finalfightl3():
    global playership
    enemyhealth = 1000  + int(bosshealthdef * 5)
    print("Health:" + str(enemyhealth))
    enemycanevade = True
    weaponhealth = 200
    fighting = True
    howrepaired = 0
    
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
      
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)    
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)
def humanboss():
    global playership
    enemyhealth = 10000  + int(bosshealthdef * 5)
    print("Health:" + str(enemyhealth))
    enemycanevade = True
    weaponhealth = 200
    fighting = True
    howrepaired = 0
    for x in range(len(sprites[4])):
        print(yellow + str(sprites[4][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
      
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)    
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)
def aeternumfight():
    global playership
    enemyhealth = 70000  + int(bosshealthdef * 5)
    print("Health:" + str(enemyhealth))
    enemycanevade = True
    weaponhealth = 200
    fighting = True
    howrepaired = 0
    for x in range(len(sprites[4])):
        print(yellow + str(sprites[3][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
      
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)    
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)
def humanfight():
    global playership
    enemyhealth = 7000  + int(bosshealthdef * 5)
    print("Health:" + str(enemyhealth))
    enemycanevade = True
    weaponhealth = 200
    fighting = True
    howrepaired = 0
    for x in range(len(sprites[4])):
        print(yellow + str(sprites[4][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
      
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)    
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)    
def catfight():
    global playership
    enemyhealth = 16000  + int(bosshealthdef * 5)
    print("Health:" + str(enemyhealth))
    enemycanevade = True
    weaponhealth = 200
    fighting = True
    howrepaired = 0
    for x in range(len(sprites[5])):
        print(lightblue + str(sprites[5][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
      
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)    
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)


        
def dragonfight():
    global playership
    enemyhealth = 10000  + int(bosshealthdef * 5)
    print("Health:" + str(enemyhealth))
    enemycanevade = True
    weaponhealth = 200
    fighting = True
    howrepaired = 0
    for x in range(len(sprites[6])):
        print(red + str(sprites[6][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
      
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)    
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)

def Algonianfight():
    global playership
    enemyhealth = 16000  + int(bosshealthdef * 5)
    print("Health:" + str(enemyhealth))
    enemycanevade = True
    weaponhealth = 200
    fighting = True
    howrepaired = 0
    for x in range(len(sprites[6])):
        print(red + str(sprites[6][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
    pat = [
        [[0,0,1], [1,0,0]],
        [[0,1,0], [0,0,1]],
        [[1,0,0], [0,1,0]],
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 5, 3)
    # train it with some patterns
    
    weightsdir = os.path.join('c:/broken space/save' + currentsave + "/",'weights.data')
    try:
        with open(weightsdir,"r") as f:
            weight = eval(f.read())
            
            n.wi = weight[0]
            
            n.wo = weight[1]
            print("enemy ai neural net loaded")
    except:
        n.train(pat)
    while fighting == True:
      
        saveweights = [n.wi,n.wo]
        weightsdir = os.path.join('c:/broken space/save' + currentsave,'weights.data')
        with open(weightsdir,"w") as f:
            f.write(str(saveweights))
            f.close()
       
        
        
        if "the god cube" in playership.inv:
            print(green + "the the god cube graciosly adds 50 firepower to your ship\nand 50 health\/")
            playership.firepower += 50
            playership.health += 50
        
        
        a = raw_input("room to attack[weapons/bridge/hull]:")
        if "weapon" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.10,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
                
            
                
        elif "bridge" in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.50,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if doesmiss == False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,20)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
                
          
                
                
        elif "hull"  in a:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
            
            dodamage = random.randint(int(playership.firepower/2),int(playership.firepower)) * random.choice([1,1.40,1.20])
            for x in range(playership.fleet):
                dodamage += 40
            doesmiss = random.choice([True,False,False,False,False])
            if  doesmiss== False:
                enemyhealth -= int(dodamage)
                print(green + "you did " + str(int(dodamage)) + " damage.")
            else:
                print(red + "The enemy dodged the attack!")
            asteroid = random.randint(1,10)
            if asteroid == 5:
                print(green + "a passing asteroid hit the enemy ship, taking out half of it's health")
                enemyhealth -= enemyhealth/2
                time.sleep(2)
            if asteroid == 2:
                print(red + "a passing asteroid hit your ship, taking out half of it's health")
                playership.health -= playership.health/2
                time.sleep(2)
        else:
            pat = [
                [[playership.firepower,playership.health,1], [1,enemyhealthdef,0]]
            ]

            # train it with some patterns
            n.train(pat)
            damagemults = n.update([0,0,1])
            damagemult = damagemults[0] + damagemults[1] + damagemults[2]
        if enemyhealth <= 0:
            print(green + "you win!")
            playership.kills += 1
            with open(storydir,'a') as s:
                s.write('defeated enemy\n')
            fighting = False
            moneyincrease = random.randint(50,75)
            print(yellow + "you earned " + str(moneyincrease))
            playership.money += moneyincrease
            time.sleep(2)
        if playership.health <= 0:
            print(red + "game over!")
            with open(storydir,'a') as s:
                s.write('defeated by enemy\n')
            time.sleep(2)
            fighting = False
            if difficulty == "survival":
                os.remove(savedir)
                os.remove(storydir)
                sys.exit()
            elif difficulty == "easy":
                print(red + "You died")
                time.sleep(5)
                sys.exit()
        howrepaired += 2
        if howrepaired >= 10:
            weaponhealth = 50
            enemycanevade = True
            enemyhealth += 30
        time.sleep(1)
        dealdamage = random.randint(20,40 + int(enemyhealthdef/5))
        
        if weaponhealth >= 1:
            dealdamage += int(random.randint(1,30) * damagemult + enemyhealth/4)
        dealdamage = abs(dealdamage)    
        print(red + "you dealt " + str(dealdamage) + " damage.")
        playership.health -= dealdamage
        time.sleep(1)

        
#random popup event with choices
def randomevent(eventid):
    random.seed(time.time)
    
                
    global playership
    def abandonedresearchfacility():
        with open(storydir,'a') as s:
            s.write('discovered abandoned research facility\n')
            
        print(green + "do you want to, \n----------\n[1]:leave\n----------\n[2]:check it out\n")
        selector = raw_input("selector:")
        if selector == "1":
            print(green + "you leave it")
            time.sleep(1)
        if selector == "2":
            issafe = random.randint(1,10)
            if issafe >= 6:
                print(green + "The facility was entirely abanonded, but you did find something!\n")
                item = random.choice(["God splitter nuke","anti teleport generator","mobedium armor","gold","iron","prismite","traddium","planet seed"])
                time.sleep(1.5)
            elif issafe <= 5:
                print(red + "Well... seems like you found out why the facility was abandoned. And it broke your ship. \n\n\n your ship has lost half of it's health.\n")
                playership.health -= playership.health/2
                time.sleep(1.5)
                
    def pirateship():
        with open(storydir,'a') as s:
            s.write('discovered pirate\n')
        print(red + "A pirate ship is flying around in space, unaware of your existance.\n")
        print(lightblue + "do you want to, \n----------\n[1]:leave\n----------\n[2]:fight it\n")
        selector = raw_input("selector:")
        if selector == "1":
            dofight = random.randint(1,15)
            print(dofight)
            if dofight <= 10:
                print(red + "In your haste to escape, you make the pirate aware of your position.\nGet ready to fight!\n")
                
                if "pirate crusher" in playership.inv:
                    print(green + "You use the pirate crusher to blast him across the universe\n")
                    time.sleep(1.5)
                    playership.reputation -= 1

                elif "the banhammer" in playership.inv:
                    print(green + "You smack the enemy ship with the banhammer and watch it blink out of existance\n")
                    time.sleep(2.5)
                    playership.reputation -= 1

                
                else:
                    fight()
                    playership.reputation += 2
            if dofight >= 3:
                print(green + "You fly into a nearby asteroid field. The pirate never notices you.\n")
                time.sleep(1.5)
            if "the god cube" in playership.inv:
                print(green + "the the god cube allowed you to escape\n")
        if selector == "2":
            print(green + "you chose to attack him.\n")
            if "pirate crusher" not in playership.inv:
                fight()
                playership.reputation += 2
            if "pirate crusher" in playership.inv:
                print(green + "you use the pirate crusher to blast him across the universe\n")
                time.sleep(1.5)
                playership.reputation -= 1
    def spacestation():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered spacestation\n')
        print(green +"An abandonded space station is left dormant in space.\n")
        print(lightblue + "do you want to, \n[1]:loot\n----------\n[2]:leave\n")
        selector = raw_input("selector:")
        if selector == "1":
            dofight = random.randint(1,30)
            print(dofight)
            if dofight <= 2:
                
                   
                if "pirate crusher" in playership.inv:
                    print(green + "oh no, there was an enemy! But you use the pirate crusher to blast the enemy across the universe\n")
                elif "the banhammer" in playership.inv:
                    print(green + "oh no, there was an enemy! But You smack the enemy ship with the banhammer and watch it blink out of existance\n")
                    time.sleep(2.5)

                
                else:
                    print(red + "It was a trap, admiral ackbar said so!\n")
                    fight()
            if "the god cube" in playership.inv:
                print(green +"the the god cube altered your future, to where there was loot in the station\n")
                time.sleep(2)
                dofight = 2
            if dofight >= 3:
                print(green + "You dock with the spacestation, and explore every room on it.\nYou find where they keep their goodies!t\n")
                earned = random.randint(75,125)
                print(yellow + "You found " + str(earned) + " currency points\n")
                playership.money += earned
                time.sleep(1.5)
        if selector == "2":
            print(green + "You decide the spacestation is not worth the hassle, and leave.\n")
            time.sleep(1.5)
    def research():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered research base\n')
        print(green + "A research base lies in space full of researchers.\n")
        print(lightblue + "do you want to, \n----------\n[1]:ask for hyperdrive upgrade(150)\n----------\n[2]:leave\n")
        selector = raw_input("selector:")
        if selector == "1":
            getdrive = random.randint(1,30)
            print(getdrive)
            if getdrive <= 2:
                print(red + "they apologize for not having a hyperdrive, and you leave\n")
                time.sleep(1.5)
            if "the god cube" in playership.inv:
                print(green + "the the god cube altered your destiny to where there was a hyperdrive in the research base\n")
                getdrive = 3
            if getdrive >= 3:
                if playership.money >= 150:
                    print(green +"They happen to have a very fine hyperdrive(and it was on sale too!)\n")
                    playership.flightdist += 1
                    playership.money -= 150
                    time.sleep(1.5)
                else:
                    print(red + "you don't have enough. you need 150 currency points\n")
        if selector == "2":
            print(green + "You chose leave.")
            time.sleep(1.5)
    def weapon():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered abandonded weapon\n')
        print(green + "As you are exploring space, your scanners pick up something odd.\nYou fly closer, and find an abandonded " + random.choice(["Px-70 laser cannon","Big bang rocket launcher","Davey Crocket rocket launcher","Px-80 bio laser"]) + "!\n----------\n[1]:ok\n")
        selector = raw_input("selector:")
        if selector == "1":
            print(green + "You turn on your abduction beam, and get the weapon.\n")
            playership.firepower += 10
            time.sleep(1.5)
    def distress():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered distress signal\n')
        print(green + "Your radio picks up some distress signal, while you were halfway into your favourite song.\n----------\n[1]:check it out\n----------\n[2]:leave it\n----------\n[3]:destroy and loot it")
        selector = raw_input("selector:")
        if selector == "1":
            istrap = random.randint(1,30)
            print(istrap)
            if "the god cube" in playership.inv:
                print(green + "the the god cube altered your destiny to where it was not a trap\n")
                istrap = 1
            if istrap <= 2:
                print(green + "You check it out, the distress signal is just some guy wanting fuel\n")
                time.sleep(1.5)
            if istrap >= 3:
                
                print(red + "It was a pirate.\n")
                if "the banhammer" in playership.inv:
                    print(green + "You smack the enemy ship with the banhammer and watch it blink out of existance\n")
                    time.sleep(2.5)
                    playership.reputation -= 1

                
                else:
                    fight()
        
        elif selector == "2":
            print(green + "you find this risky and leave.\n")
            time.sleep(1.5)
        else:
            print(green + "you decide to destroy the ship\n")
            earned = random.randint(50,125)
            print(red + "you got " + str(earned) + ", you jerk.")
            playership.money += earned
            playership.reputation -= 3
            time.sleep(1.5)
            
    def freighter():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered freighter\n')
        print(green + "You see a frieghter being attacked in the distance, do you want to\n----------\n[1]:defend it\n----------\n[2]:leave it\n----------\n[3]:destroy and loot it")
        selector = raw_input("selector:")
        if selector == "1":
            print(green + 'You decide to attack the gang of looters')
            b = raw_input('are you really sure you want to fight the several pirates?[y/n]\n')
            if b == 'y':
                for x in range(4):
                    fight()
                
        
        elif selector == "2":
            print(green + "You find this risky and leave.")
            time.sleep(1.5)
        else:
            print(yellow + "you decide to accompany the pirates and collect some wealth with them\n")
            earned = random.randint(50,200)
            print(red + "you got " + str(earned) + ", you jerk.\n")
            playership.money += earned
            playership.reputation -= 4
            time.sleep(1.5)
    def shop():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered shop\n')
        print(green + "you find a small shop set out in space, do you want to\n######\n[1]:check it out\n######\n[2]:leave it\n")
        selector = raw_input("selector:")
        if selector == "1":
            inshop = True
            while inshop == True:
                print(lightblue + '--------------------------\nYou pull your ship to the docking bay.\nYou then disembark.\n')
                b = raw_input('You can get:\n----------\n<crew>\n----------\n<weapons>\n----------\n<hyperdrive>\n----------\n<repair>\n----------\n<leave>')
                if b == 'crew':
                   print(yellow + "spending 100 currency points, are you okay with this?")
                                                       
                   if playership.money >= 100 and raw_input("y/n") == "y":
                       if len(playership.crew) <= playership.crewamount:
                           
                           if random.choice([True,False]) == True:
                               curspecies = random.choice(["dragon","human","dragonx","cat","Algonian"])
                           else:
                               curspecies = random.choice(allspecies)
                           name = str(random.choice(characternames) + '(' + random.choice(allspecies).replace('\n','') + ')')
                           crewgen = {'name':name,'health':100,'profession':random.choice(['engineer','pilot','gunner','to be useless']),'room':''}
                           playership.addcustomcrewmember(crewgen)
                           print(green + 'added ' + name + ' to crew.\n\n')
                           playership.money -= 100
                           with open(storydir,'a') as s:
                               s.write('recruited ' + crewgen['name'] +'\n')

                       else:
                           print(red + 'you can\'hold any more crew!\n')
                       
                   else:
                        print(red + "you need at least 100 currency points to buy crew\n")
                if b == "leave":
                    inshop = False
                if b == "hyperdrive":
                   if playership.money >= 600:
                      playership.flightdist += 3
                      print(green + "your ship can now fly further.\n")
                      playership.money -= 600
                   else:
                       print(red + "you have no money, how will you pay the mechanic! you need at least 600\n")
                if b == "repair":
                    if playership.money >= 100:
                        playership.health = playership.maxhealth
                        playership.money -= 100
                    else:
                        print(red + "you have no money, how will you pay the mechanic! you need at least 100\n")
                if b == "weapons":
                   if playership.money >= 175:
                        playership.firepower += 20
                        playership.money -= 175
                   else:
                        print(red + "you have no money, how will you pay the mechanic! you need at least 175\n") 
                

        if selector == "2":
            print(lightblue + "You decide you don't want to buy anything right now.\n")
            time.sleep(1.5)
    def defence():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered defences\n')
        print(green + "you find a space station. the owners ask you if you want to help them fix the defence system ,do you want to\n----------\n[1]:shoot at it\n----------\n[2]:leave it\n----------\n[3]:hack it to turn it off.")
        selector = raw_input("selector:")
        if selector == "1":
            print(red + 'you decide to shoot at it,\nthe defence system is destroyed, and you have to pay the repair bill.\n')
            playership.money -= 200
            playership.reputation -= 1
            time.sleep(1.5)
        if selector == "2":
            print(lightblue + "you decide to leave them with their own problem.\n")
            time.sleep(1.5)
            playership.reputation -= 1
        if selector == '3':
            engineers = []
            for x in range(len(playership.crew)):
                if playership.crew[x]['profession'] == 'engineer':
                    engineers.append(playership.crew[x]['name'] + ', ')
            print(green + 'you hack into the security system to turn it off, then your engineers, ' + str(engineers).replace('[','').replace(']','').replace("'",'').replace(',','') + ' fix it.')
            time.sleep(2)
    def asteroid():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered distress signal\n')
        print(green + "your radio picks up some distress signal near an asteroid field\n[1]:check it out\n----------\n[2]:leave it\n----------\n[3]:destroy and loot it")
        selector = raw_input("selector:")
        if selector == "1":
            istrap = random.randint(1,30)
            print(istrap)
            if "the god cube" in playership.inv:
                print(green + "the the god cube altered your destiny to where it was not a trap\n")
                istrap = 1
            if istrap <= 2:
                print(green + "you check it out, just some guy wanting fuel\n")
                time.sleep(1.5)
            if istrap >= 3:
                print(red + "it was a pirate.")
                if "the banhammer" in playership.inv:
                    print(green + "You smack the enemy ship with the banhammer and watch it blink out of existance\n")
                    time.sleep(2.5)
                    playership.reputation -= 1

                elif "Humor generator" in playership.inv:
                    print("Mr. Silly's humor generator summons a bit of sillyland, no litteraly a hunk of dirt from sillyland pops out of nowhere and hits the pirate ship destroying it.")
                    time.sleep(2.5)
                else:
                    fight()
        
        elif selector == "2":
            print(green + "you find this risky and leave.\n")
            time.sleep(1.5)
        else:
            print(green + "you decide to destroy the ship\n")
            earned = random.randint(50,125)
            print(red + "you got " + str(earned) + ", you jerk.")
            playership.money += earned
            playership.reputation -= 2
            time.sleep(1.5)
    def hdamage():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered distress signal\n')
        print(green + "your radio picks up some distress signal, a heavily damaged ship is in the distance,\nno life forms detected\n----------\n[1]:check it out\n----------\n[2]:leave it\n----------\n[3]:destroy and loot it")
        selector = raw_input("selector:")
        if selector == "1":
            
            print(yellow + "you check it out, there are some ores and money\n")
            if len(playership.inv) <= playership.cargosize:
                playership.inv.append(random.choice(['prismite','gold','iron','copper','rocks','Eximus','Mobedium']))
                playership.money += 200
                
            time.sleep(1.5)
            
        elif selector == "2":
            print(green + "you find this risky and leave.\n")
            time.sleep(1.5)
        else:
            print(green + "you decide to destroy the ship\n")
            earned = random.randint(50,125)
            print(green + "you got " + str(earned) + ", well, it had no life on it so...\n")
            playership.money += earned
            time.sleep(1.5)
    def blackmarket():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered distress signal\n')
        print(green + "your radio picks up some signal, there is a pirate looking ship in the distance offering a \"weapon\"\nso yeah, totally not suspicious at all!\n----------\n[1]:check it out\n----------\n[2]:leave it\n----------\n[3]:destroy and loot it")
        selector = raw_input("selector:")
        if selector == "1":
            
            istrap = random.randint(1,30)
            print(istrap)
            if "the god cube" in playership.inv:
                print(green + "the the god cube altered your destiny to where it was not a trap\n\n")
                istrap = 1
            if istrap <= 2:
                print(green + "you check it out, the alien was telling the truth, he enhances your weapons\n")
                playership.firepower += 10
                time.sleep(1.5)
            if istrap >= 3:
                print(red + "it was a pirate.\n")
                if "the banhammer" in playership.inv:
                    print(green + "You smack the enemy ship with the banhammer and watch it blink out of existance\n")
                    time.sleep(2.5)
                
                elif "Humor generator" in playership.inv:
                    print("Mr. Silly's humor generator summons a bit of sillyland, no litteraly a hunk of dirt from sillyland pops out of nowhere and hits the pirate ship destroying it.\n")
                    time.sleep(2.5)
                else:
                    fight()   
        elif selector == "2":
            print(green + "you find this risky and leave.\n")
            time.sleep(1.5)
        else:
            print(green + "you decide to destroy the ship\n")
            earned = random.randint(50,125)
            print(red + "you got " + str(earned) + ", well, you jerk, it could have been friendly!")
            playership.money += earned
            time.sleep(1.5)
            playership.reputation -= 2
    def stranded():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered distress signal\n')
        print(green + "your radio picks up some distress signal, it is coming from a nearby baren planet\n----------\n[1]:check it out\n----------\n[2]:leave it\n")
        selector = raw_input("selector:")
        if selector == "1":
        
            print(green + "you check it out, a person was stranded here for years.")
            b = raw_input('do you want to help him?[y/n]')
            if b == 'y':
                if len(playership.crew) <= playership.crewamount:
                   name = str(random.choice(characternames) + '(' + random.choice(allspecies).replace('\n','') + ')')
                   crewgen = {'name':name,'health':100,'profession':random.choice(['engineer','pilot','gunner','to be useless']),'room':''}
                   playership.addcustomcrewmember(crewgen)
                   print(green + 'added ' + name + ' to crew.')
                   with open(storydir,'a') as s:
                       s.write('recruited ' + crewgen['name'] +'\n')

                else:
                   print(green + 'you can\'hold any more crew! so you drop him off at the nearest space station.')
            else:
                print(red + 'the alien screams at you in anger while you leave him, I guess you weren\'t willing to take chances.')
                playership.reputation -= 1
            time.sleep(1.5)
            
        
        elif selector == "2":
            print(green + "you find this risky and leave.\n")
            time.sleep(1.5)
    def spiderz():
        global playership
        with open(storydir,'a') as s:
            s.write('discovered distress signal\n')
        print(green + "your radio picks up some distress signal, giant spiders are invading a space station\n----------\n[1]:check it out\n----------\n[2]:leave it\n")
        selector = raw_input("selector:")
        if selector == "1":
            istrap = random.randint(1,30)
            print(istrap)
            if "the god cube" in playership.inv:
                print(green + "the the god cube altered your destiny to where your crew live\n")
                istrap = 5
            if istrap <= 2:
                print(red + "you check it out, in trying to defend it a crew member was killed.\n")
                crewtokill = random.choice(playership.crew)
                print(crewtokill['name'] + ' was killed')
                playership.crew.remove(crewtokill)
                with open(storydir,'a') as s:
                    s.write(crewtokill['name'] + ' was killed')
                time.sleep(1.5)
            if istrap >= 3 and istrap <= 4:
                print(red + "it was a trap!.\n")
                if "the banhammer" in playership.inv:
                    print(green + "You smack the enemies with the banhammer and watch them blink out of existance\n")
                    time.sleep(2.5)
                
                elif "Humor generator" in playership.inv:
                    print("Mr. Silly's humor generator launches various things from sillyland at the enemies, someday there will be no sillyland because you keep on taking stuff from it!\n")
                    time.sleep(2.5)
                else:
                    fight()
        
        elif selector == "2":
            print(green+"you find this risky and leave.\n")
            time.sleep(1.5)
    
    def sldragon():
        global playership
        print(red+'you stumble on a crew slaver. they demand a member of your crew.\n----------\n[1]:destroy them\n----------\n[2]:save the slaves and destroy them\n----------\n[3]:give a crew member over')
        selector = raw_input("selector:")
        if selector == '1':
            print(green+'you refuse')
            if "the banhammer" in playership.inv:
                    print(red+"You smack the enemy ship with the banhammer and watch it blink out of existance\n")
                    time.sleep(2.5)
                    playership.reputation -= 1
            else:
                fight()
        elif selector == '2':
            print(green+'you attack them to save the slaves')
            if "the banhammer" in playership.inv:
                    print(green+"You smack the enemy ship with the banhammer and watch it blink out of existance, but the slaves did nothing to get a ban and where spared\n")
                    time.sleep(4)
                    playership.reputation += 2
            

            elif "Humor generator" in playership.inv:
                    print("Mr. Silly's humor generator summons a cop from sillyland, the cop arrests the slaver and returns to sillyland.\n")
                    time.sleep(2.5)
            else:
                fight()
            for x in range(3):
              if len(playership.crew) <= playership.crewamount:
                   name = str(random.choice(characternames) + '(' + random.choice(allspecies).replace('\n','') + ')')
                   crewgen = {'name':name,'health':100,'profession':random.choice(['engineer','pilot','gunner','to be useless']),'room':''}
                   playership.addcustomcrewmember(crewgen)
                   print(green+'added ' + name + ' to crew.')
                   with open(storydir,'a') as s:
                       s.write('recruited ' + crewgen['name'] +'\n')

              else:
                  print(green+'you can\'hold any more crew! so you drop him off at the nearest space station.')
        else:
            print(red+'you hand over a crew member to the slaver')
            crewtokill = random.choice(playership.crew)
            if crewtokill['profession'] != "captain":
                print(crewtokill['name'] + ' was enslaved')
                playership.crew.remove(crewtokill)
                with open(storydir,'a') as s:
                    s.write(crewtokill['name'] + ' was enslaved')
            time.sleep(1.5)
            playership.reputation -= 1

        #picks an event if the user didn't specify one
    if eventid == '':
        eventtochoose = random.randint(1,15)
    else:
        eventtochoose = eventid
    if eventtochoose == 1:
        pirateship()
    elif eventtochoose == 2:
        spacestation()
    elif eventtochoose == 3:
        research()
    elif eventtochoose == 4:
        weapon()
    elif eventtochoose == 5:
        distress()
    elif eventtochoose == 6:
        freighter()
    elif eventtochoose == 7:
        shop()
    elif eventtochoose == 8:
        defence()
    elif eventtochoose == 9:
        asteroid()
    elif eventtochoose == 10:
        hdamage()
    elif eventtochoose == 11:
        blackmarket()
    elif eventtochoose == 12:
        stranded()
    elif eventtochoose == 13:
        spiderz()
    elif eventtochoose == 14:
        sldragon()
    
    
    else:
        pass


#generates a random map.              
def generateworld():
    global map
    global starmap
    mapw = 80
    maph = 100
    map = []
    starmap = []
    
    for x in range(maph + 1):
        row = []
        for y in range(mapw + 1):
           row.append('.')
        map.append(row)
   
        
    for x in range(120):
        star = Star([],[])
        map[random.randint(0,maph)][random.randint(0,mapw)] = star.returnstarinfo()['name']
        starmap.append(star.returnstarinfo())
        print(lightblue+"generated star:" + star.returnstarinfo()['name'])
    
    (columns, rows) = getTerminalSize()
    
    map[0][0] =  'Sol'
    map[int(maph/2)][mapw] = 'Galeus' 
    map[0][mapw] =  'Usleatho'
    map[int(maph/2)][0] = 'Exluagtos'
    map[maph][mapw] = "Algira"
    map[maph][0] = "Dakara"
    starmap.append({'name':'Sol','color':'orange','size':3,'planets':sol})
    starmap.append({'name':'Galeus','color':'purple','size':5,'planets':galeus})
    starmap.append({'name':'Usleatho','color':'black','size':1,'planets':usleatho})
    starmap.append({'name':'Exluagtos','color':'green','size':4,'planets':exluagtos})
    starmap.append({'name':'Algira','color':'grey','size':5,'planets':Algira})
    starmap.append({'name':'Dakara','color':'(none)','size':6,'planets':Dakara})
    
    print(yellow+"generated star:Sol")
    print(lightblue+"generated star:Galeus")
    print(red+"generated star:Usleatho")
    print(green+"generated star:Exluagtos")
    
    print(green+"World generation complete, checking for errors/glitches")
    time.sleep(1)
    #detects it any stars have been hidden by other stars, if so remove the coverred star
    try:
        for stars in range(len(starmap) - 1):
            if starmap[stars]['name'] not in str(map):
                print(red+"missing star " + starmap[stars]['name'] + '\nremoving from game to prevent errors...')
            
                starmap.remove(starmap[stars])
    except IndexError:
        pass
  

#check if the save file exists, if so, load it, if not, make it.
if os.path.isfile(savedir):
    
    global planets
    global species
    global starcounter
    planets = 0
    try:
        save = datalib.load(savedir)
    except KeyError:
        datalib.dump(datalib.load(savebackdir),savedir)
    
    
    
    map,starmap = save["world"],save["stars"]
    #detects it any stars have been overlapped by other stars, if so remove the star that is being overlapped
    try:
        for stars in range(len(starmap) - 1):
            if starmap[stars]['name'] not in str(map):
                print(red+"missing star " + starmap[stars]['name'] + '\nremoving from game to prevent errors...')
            
                starmap.remove(starmap[stars])
    except IndexError:
        pass
    playershipimg = save['sprite']
    playershipstats = save['player']
    try:
        difficulty = save['difficulty']
    except:
        difficulty = "survival"
    playership = ship(playershipstats,playershipimg)
    
    playership.crew = save['crew']
    enemyhealthdef = save["enemy"]
    try:
        bosshealthdef = int(enemyhealthdef/10)
    except:
        bosshealthdef = 0
    try:
        starcounter = save['counter']
    except:
        starcounter = 0
    try:
        species = save['species']
    except:
        species = 'human'
    
    cquests = save['cquests']
    
    planets = 0

    for x in range(len(starmap)):
        for y in range(len(starmap[x]['planets'])):
            planets += 1
       
else:
    
    
    
    planets = 0
    starcounter = 0
    playershipimg = [
{"       ____,----._                                 "},
{"   ,--'| _|\" o;.  `.____        ____  ,,=====._   "},
{" .=|.':| U| ;:;:  .- \,,`-.===='}.,'\//       \"` "},
{"(]=|;: |o |  ,.  (  :;)::(     ):;::>}X==========- "},
{" `=| :;|  | ,: o  `-_/``,-`====.}___/\\       _,   "},
{"  `--.|__|_ .:  _,' \"""              ``=====''    "},
{"       ~  ~`----'                                  "},
]

    try:
        os.remove(storydir)
    except:
        pass
    enemyhealthdef = 300
    with open(storydir,'a') as s:
        s.write('started game\n')
    c = raw_input("do you want to make a basic, or advanced character? [b/a]:")
    if c == "b":
        print(lightblue+"choose species:")
        print(lightblue+
        """available races:
        human:earth dwelling creatures. they are very technologically advanced, oh wait, you're one of them, so no further explanation needed.
        dragon:these dragon like creatures are peaceful(unlike dragons), unless provoked and-or attacked. when angered, they can be quite vicious.
            dragons prefer to live underground, and space travel makes them feel unsafe.
        cat:these cute furry creatures are very playful, but good hunters. yes they are related to the feline earth creatures.
            In the year 2467, Scientists experamented on cats, Thus making cats highly intelligent space faring beings, but they don't care if the Algonians invade their
            Home world, as long as they bring plenty of paper balls for the cats to chase around.
        dragonX:these creatures are like dragons but cybernetically enhanced by the Algonians.
            In other words, dragonX's are the product of the most evil species in the known universe
        Algonian:these heartless cybernetic creatures are not very strong on their own. but, since they are one of the most technologically enhanced creatures, they cybernetically enhanced themselves.
            They carelessely destroy civilazations, then realize that the civilization that they just destroyed was the wrong one.
            And you thought some parts of humanity was pretty messed up.

        """)
        a = raw_input("pick species:[1:human/2:dragon/3:cat/4:dragonX/5:algonian]")
        if a == '1':
            species = 'human'
        elif a == '2':
            species = 'dragon'
        elif a == '3':
            species = 'cat'
        elif a == '4':
            species = 'dragonx'
        else:
            species = 'Algonian'
        
        
        namey = raw_input("what is your name or username:")
        namey = namey + str('(' + species + ')')
        bio = "|name|:" + namey + "\n|species|:" + species + "\n"
        shipname = raw_input("name your ship:")
        with open(storydir,'a') as s:
            s.write('recruited ' + namey + ' as captain of starship.\n')
        
    if c == "a":
        print(lightblue + "please type the name of your species")
        species = raw_input("species name:")
        print(lightblue + "please describe your species")
        desc = raw_input("desc:")
        print(lightblue + "please name your character")
        namey = raw_input("name:")
        namey = namey + str('(' + species + ')')
        print(lightblue + "please age your character")
        age = raw_input("age:")
        print(lightblue + "please gender your character:")
        gender = raw_input("gender:")
        print(lightblue + "please describe the appearance of your character")
        appearance = raw_input("appearance:")
        print(lightblue + "please write your character's backstory")
        backstory = raw_input("backstory:")

        bio = "|Name|:" + namey + "\n|Age|:" + age + "\n|Gender|:" + gender + "\n|Species|:" + species + "\n|Species Description|:" + desc + "\n|Appearance|:" + appearance + "\n|backstory|:" + backstory + "\n"
        shipname = raw_input("name your ship:")
        with open(storydir,'a') as s:
            s.write('recruited ' + namey + ' as captain of starship.\n')
    
    difficulty = raw_input("difficulty: survival(death is permanent) easy(death is not permanent)")
    print('\n')
    time.sleep(1)
    
    print(green + "generating cosmos and bright glowy things you see at night")
    
    Thread(target = generateworld()).start()
    for x in range(len(starmap)):
        for y in range(len(starmap[x]['planets'])):
            planets += 1
    playershipstats = [
    shipname,
    300,
    5,
    8,
    30,
    50,
    20,
    8,
    ['rocks',],
    [
    {'profession': 'engineer', 'health': 100, 'name': 'Harper(' + species + ')','room':'corridor'},
    {'profession': 'pilot', 'health': 100, 'name': 'Trinity(robot)','room':'bridge'},
    {'profession': 'gunner', 'health': 100, 'name': 'Levi(' + species + ')','room':'corridor'}],
    100,
    0,
    0,
    0, #the more colonies the more fleet you can have,
    300,
    [],
    15,
    0,
    0,
    random.choice(['a nobody doing work for your government.','a vigilante hero','a member of your government\'s spec ops forces','a generic member of your government\'s law enforcement agency']), 10]
    
    playership = ship(playershipstats,playershipimg)
    playership.addcustomcrewmember({'profession':'captain', 'health': 200, 'name': namey,'room':'corridor','bio':bio})
    cquests = []
    #playership.generatecrew()
    for x in range(len(playership.crew)):
        if playership.crew[x]["profession"] == "gunner":
            playership.firepower += 10
    for x in range(len(playership.crew)):
        if playership.crew[x]["profession"] == "captain":
            playership.firepower += 10
            playership.evade += 5
            playership.health += 10
    for x in range(len(playership.crew)):
        if playership.crew[x]["profession"] == "pilot":
            playership.evade += 5
    
    time.sleep(1)
    if species == 'human':
        print(yellow + 'Earth, the only habitable planet of Sol is being invaded by the Algonians. your mission is to stop them from taking Earth.\ngather supplies. Upgrade your ship, and stop them!\n')
    if species == 'Algonian':
        print(red + 'The federation has defied the Algonians for the last time! gather supplies, upgrade your ship, and help the Algonian capture sol and it\'s 9 planets\n')

    if species == 'cat':
        print(lightblue + 'Noah, the supreme ruler of all cats, has been kidnapped by the Algonians, you have been sent to get him back.\n')
   
    if species == 'dragon' or species == 'dragonX':
        print(red + "The dragon empire has decided that the Algonians have gone too far. gather supplies, upgrade your ship, and end them once and for all!")
    print(lightblue + 'Also you may need 20 or more fleet ships(around 14000 health in all) to defeat most bosses\nI wish you good luck!\n')
    raw_input("press RETURN or ENTER to continue")
#this is the quest sytem, pretty simple right?
def quest(ship,planet):
    if planet['quest'] != {}:
        cando = False
        if planet['name'] == 'Earth' or planet['name'] == 'Pluto' or planet['name'] == 'Mars' or planet['name'] == 'Venus' or planet['name'] == 'Mercury' or planet['name'] == 'Neptune' or planet['name'] == 'Saturn' or planet['name'] == 'Uranus'  or planet['name'] =='Jupiter':
            print(red + 'planets from sol don\'t have quests(yet)')
        else:
            
            if planet['name'] not in cquests:
                cando = True
            if cando == True:
                a = raw_input("want to do some work?[y/n/c]")
                if a == "y":
                    print(planet["quest"]["text"])
                if a == "n":
                    print(green + "ok :(")
                    
                if a == "c":
                    if planet["quest"]["type"] == "finditem":
                        if planet["quest"]["item"] in ship.inv:
                            earned = random.randint(100,175)
                            print(yellow + "very good. you get " + str(earned))
                            cquests.append(planet['name'])
                            ship.money += earned
                            ship.inv.remove(planet["quest"]["item"])
                        else:
                            print(red + "you don't have it? well keep looking")
                    if planet["quest"]["type"] == "mine":
                        if planet["quest"]["item"] in ship.inv:
                            earned = random.randint(100,175)
                            cquests.append(planet['name'])
                            print(yellow + "very good. you get " + str(earned))
                            ship.money += earned
                            ship.inv.remove(planet["quest"]["item"])
                        else:
                            print(red + "you don't have it? well keep looking")

            else:
                print(red + 'the quest here is already complete')
    else:
        print(red + "there are no quests here")
        
    #displays the map
def showmap():
    
    inmap = True
    print("\n\n\n")
    while inmap:
        for x in range(len(map)):
            print(Style.DIM + blue + str("".join(map[x])))
 
           #print(lightblue + str(map[x]).replace('[',lightblue+'').replace(']',lightblue+'').replace(',',lightblue+'').replace("'",lightblue+'').replace(".",blue +" ").replace("Sol",yellow+"Sol").replace("Galeus",Fore.MAGENTA + Style.DIM +"Galeus" + Style.NORMAL).replace("Exluagtos",green + Style.BRIGHT + "Exluagtos" + Style.NORMAL).replace("Usleatho",Fore.BLACK+Style.DIM + "Usleatho" + Style.NORMAL))
           
        print(yellow)
        a = raw_input('press ENTER to leave map.')
        break

#the stats of the scavenger and the goliath
scavengerstats = [
    'the scavenger',
    300,
    5,
    4,
    20,
    50,
    20,
    16,
    playership.inv,
    playership.crew,
    playership.money,
    playership.fleet,
    0,
    playership.colonies, #the more colonies the more fleet you can have,
    300,
    playership.allies,
    playership.flightdist + 5,
    playership.kills,
    playership.mined,
    "an explorer", playership.reputation]

goliathstats = [
    'the goliath',
    400,
    10,
    12,
    40,
    50,
    20,
    6,
    playership.inv,
    playership.crew,
    playership.money,
    playership.fleet + 1,
    0,
    playership.colonies, #the more colonies the more fleet you can have,
    400,
    playership.allies,
    playership.flightdist + 3,
    playership.kills,
    playership.mined,
    "a warrior", playership.reputation]

scavenger = ship(scavengerstats,sprites[0])
goliath = ship(goliathstats,sprites[1])
    #the infinite game loop,



print(lightblue + "for help type help for a list of commands or helpall for new players.")
raw_input("press ENTER or RETURN to continue")
while True:
    print(Style.BRIGHT) 
    if playership.kills >= 20:
        playership.role = 'warrior'
    elif playership.mined >= 100:
        playership.role = 'miner'
    elif playership.mined >= 100 and playership.kills >= 20:
        playership.role = 'miner/warrior'
    #detect if player has flown to 3 more stars, if so, reset the counter and make enemies more powerful
    if starcounter >= 3:
        starcounter = 0
        enemyhealthdef += (enemyhealthdef/8)
  
    with open(storydir,'r') as s:
        lines = s.readlines()
    
    if "Galactic domination\n" not in lines:
        if playership.colonies >= planets:
            print(yellow + "you have dominated the entire known universe, great job!")
            time.sleep(3)
            with open(storydir,'a') as s:
                lines = s.write("Galactic domination" + '\n')
                s.close()
    with open(storydir,'r') as s:
        lines = s.readlines()
    
    
 
    
                    
    
    s.close()
    try:
        print(mes)
    except:
        pass
            
    with open(storydir,'r') as s:
        lines = s.readlines()
    if "No empires" not in lines:
        with open(storydir,'r') as s:
            lines = s.readlines()
        if 'defeated the Algonians' in lines:
            if 'defeated the Cats' in lines:
                if 'defeated the Humans' in lines:
                    if 'defeated the dragons' in lines:
                        print(green+"No more humans,cats,algonians or dragons! Nothing else can stand in your way while you conquer the universe. Mwhahahahaha!")
                        with open(storydir,'a') as s:
                            lines = s.write("No empires" + '\n')

    scavengerstats = [
    'the scavenger',
    300,
    5,
    4,
    20,
    50,
    20,
    16,
    playership.inv,
    playership.crew,
    playership.money,
    playership.fleet,
    0,
    playership.colonies, #the more colonies the more fleet you can have,
    300,
    playership.allies,
    playership.flightdist + 5,playership.kills,playership.mined,"an explorer",playership.reputation]

    goliathstats = [
    'the goliath',
    400,
    10,
    12,
    40,
    50,
    20,
    6,
    playership.inv,
    playership.crew,
    playership.money,
    playership.fleet + 1,
    0,
    playership.colonies, #the more colonies the more fleet you can have,
    400,
    playership.allies,
    playership.flightdist + 3,playership.kills,playership.mined,"a warrior",playership.reputation]
    playershipstats = [playership.name,playership.health,playership.evade,playership.crewamount,playership.firepower,playership.speed,playership.armor,playership.cargosize,playership.inv,playership.crew,playership.money,playership.fleet,playership.colonies,playership.maxfleetmembers,playership.maxhealth,playership.allies,playership.flightdist,playership.kills,playership.mined,playership.role,playership.reputation]
    
   
    #if you see this, this is the thingy that saves the game
    save = {'difficulty':difficulty,'world':map,'stars':starmap,'player':playershipstats,'crew':playership.crew,'enemy':enemyhealthdef,'cquests':cquests,'sprite':playershipimg,'counter':starcounter,'species':species}
    datalib.dump(save,savedir)
    datalib.dump(save,savebackdir)
   
    for x in range(len(playership.sprite)):
        
        print(lightblue+ str('         ') + str(playership.sprite[x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
    print(yellow+"planets to colonize until galactic domination:" + str(planets - playership.colonies))
    
    a = raw_input('what do you want to do?:').lower()
    #checks if you entered the name of a star, if so, fly to it
    for x in range(len(starmap)):
        print(Style.BRIGHT)
        if a == starmap[x]['name'].lower():
           for row in range(len(map)):
               for col in range(len(map[row])):
                   if map[row][col] == starmap[x]['name']:
                       
                       pos = (col,row)
                   else:
                       pass               
           if pos[0] <= int(playership.flightdist) and pos[1] <= int(playership.flightdist):
               print(Style.BRIGHT)
               with open(storydir,'a') as s:
                   s.write('flew to star ' + a + '\n')
               #player has flown to a star, when it reaches 3 it resets and makes the enemies more powerful, so don't do very much travelling if you can help it!
               starcounter += 1
               randomevent('')
               playershipstats = [playership.name,playership.health,playership.evade,playership.crewamount,playership.firepower,playership.speed,playership.armor,playership.cargosize,playership.inv,playership.crew,playership.money,playership.fleet,playership.colonies,playership.maxfleetmembers,playership.maxhealth,playership.allies,playership.flightdist,playership.kills,playership.mined,playership.role,playership.reputation]
    
        
               save = {'difficulty':difficulty,'world':map,'stars':starmap,'player':playershipstats,'crew':playership.crew,'enemy':enemyhealthdef,'cquests':cquests,'sprite':playershipimg,'counter':starcounter,'species':species}
               datalib.dump(save,savedir)
               datalib.dump(save,savebackdir)
               
               instar = True
               while instar == True:
                   print(Style.BRIGHT)
                   print('\n')
                   #checks if the star is Usleatho
                   
                   if "Usleatho" in starmap[x]["name"]:
                       if species == 'dragon' or species == 'dragonX':
                           with open(storydir,'r') as f:
                               lines = f.readlines()
                               story = str(lines)
                           if not 'defeated Algonian flagship' in story:
                               
                               print(red + "The Algonians aren't to happy about your presence, they are not happy")
                               Algonianfight()
                               print(green+"you manage to cause the hyperdrive to activate in the Algonian ship, but the hyperdrive exploded while going light speed. The Algonians really need to improve their hyperdrives...")
                               with open(storydir,'a') as f:
                                   lines = f.readlines()
                                   story = str(lines)
                               f.write("defeated Algonian flagship\n")
                       
                            
                       if species == 'cat':
                           #opens the story.txt or your captains log
                           with open(storydir,'r') as f:
                               lines = f.readlines()
                               story = str(lines)
                           
                           if not 'saved noah' in story:
                              print(red+"You transmit the Algonians a message, demanding that they return noah.\nThey aren't too happy about it.")
                              Algonianfight()
                              print(green+"You teleport onto the ship, grab noah, teleport off, and finally, destroy the ship.")
                              with open(storydir,'a') as s:
                                  s.write("saved noah\n")
                              playership.crew.append({'name':"Noah(cat)",'health':350,'profession':random.choice(['engineer','pilot','gunner']),'room':random.choice(['bridge','corridor','gun room','hangar','lounge'])})

                   #checks if the star is Galeus
                   if "Galeus" in starmap[x]["name"]:
                       if species == "cat":
                           with open(storydir,'r') as f:
                               lines = f.readlines()
                               story = str(lines)
                           
                           if 'saved noah' in story:
                               if not "returned noah" in story:
                                   print(green+"You try to return noah to his home, however he decides to stay on your ship, the cats pay you handsomely")
                                   raw_input("press RETURN or ENTER to continue")
                                   playership.money += 10000
                                   with open(storydir,'a') as s:
                                      s.write("returned noah\n")
                       
                   #checks if the star is Sol
                   if "Sol" in starmap[x]["name"]:
                       if species == "human":
                           #opens the story.txt or your captains log
                           with open(storydir,'r') as f:
                               lines = f.readlines()
                               story = str(lines)
                            #if you haven't defeated the boss.
                           if not 'defeated Omega class Algonian SuperCapitol Ship' in story:
                               print(green+"you have finally found Sol!\nyour home lies here,\nit would suck if a pirate found you...\n")
                               print(red+'your scanners pick up a strange signal...\n\na giant space ship appears in the distance\n')
                               time.sleep(1)
                               print(red+'get ready\n')
                               time.sleep(1)
                               print(red+'the Omega class Algonian SuperCapitol Ship is approaching, to shred your ship')
                               finalfightl1()
                               print(red+"Because of the size of the ship, it was able to survive, But it took a beating.\n")
                               finalfightl2()
                               print(red+"Somehow this abomination is still chuggin...\n")
                               finalfightl3()
                               print(green+"After the ship is too broken to operate, the hyperdrive breaks, releasing antimatter into the ship. You watch as the ship is utterly destroyed.\n")
                               with open(storydir,'a') as f:
                                   
                                 
                                   f.write("defeated Omega class Algonian SuperCapitol Ship\n")
                       if species == "Algonian":
                           with open(storydir,'r') as f:
                               lines = f.readlines()
                               story = str(lines)
                           if not "defeated federation flagship" in story:
                               print(green+"You arive at Sol to assist the Algonians in capturing Sol.")
                               time.sleep(1)
                               print(red+"the federation flagship is coming to stop you")
                               time.sleep(1)
                               humanboss()
                               print(green+"You send a missle into the engines of the ship.\nIt gets jammed in the engines, and explodes.\nOnly a few shreds of metal remained of that flagship.")
                               with open(storydir,'a') as f:
                                   
                                 
                                   f.write("defeated federation flagship\n")
                   if "Exluagtos" in starmap[x]['name']:
                       if species == 'dragon' or species == 'dragonX':
                           with open(storydir,'r') as f:
                               lines = f.readlines()
                               story = str(lines)
                           if 'defeated Algonian flagship' in story and 'defeated Algonian' not in story:
                               
                               print(yellow+"The dragon empire awards you for your triumph.")
                               playership.money += 10000
                               with open(storydir,'a') as f:
                                   
                                 
                                   f.write("defeated Algonian\n")
                   if "Algira" in starmap[x]['name']:
                       with open(storydir,'r') as f:
                           lines = f.readlines()
                           story = str(lines)
                           if 'defeated Aeternum flagship' not in story:
                               print("You encounter a dormant flagship, upon approaching it, it jumps to life, and assumes you are hostile, it activates it's weapons, and fires at you, barely missing. EVen though it didn't hit you, a portion of your hull melted slightly.")
                               playership.health -= 200
                               aeternumfight()
                               print("You finally defeat the hostiles. Apparantly, they where holding a hostage, which managed to escape in the battle, an escape pod docks with your ship, it looks like you have found a new crewmember\n\n")
                               time.sleep(1)
                               playership.maxhealth += 2000
                               playership.money += 20000
                               playership.firepower += 1000
                               playership.crew.append({'name':"Erin (Aeternum)",'health':400,'profession':"engineer",'room':''})
                               with open(storydir,'a') as f:
                                   
                                   
                                 
                                   f.write("defeated Aeternum flagship\n")
                   #displays star's name, size and planets
                   print('name:' + str(starmap[x]['name']))
                   if starmap[x]['size'] == 1:
                       print(lightblue+'size:dwarf')
                   if starmap[x]['size'] == 2:
                       print(lightblue+'size:small')
                   if starmap[x]['size'] == 3:
                       print(yellow+'size:medium')
                   if starmap[x]['size'] == 4:
                       print(yellow+'size:large')
                   if starmap[x]['size'] == 5:
                       print(red+'size:giant')
                   if starmap[x]['size'] == 6:
                       print(red+'size:black hole')
                   print(lightblue+'color:' + str(starmap[x]['color']))
                   print('\n')
                   print(green+'planets:')
                   for p in range(len(starmap[x]['planets'])):
                       print(lightblue +str(starmap[x]['planets'][p]['name']))
                       if starmap[x]['planets'][p]['size'] == 1:
                           print(green+'size:planetoid')
                       if starmap[x]['planets'][p]['size'] == 2:
                           print(green+'size:small')
                       if starmap[x]['planets'][p]['size'] == 3:
                           print(green+'size:earth sized')
                       if starmap[x]['planets'][p]['size'] == 4:
                           print(green+'size:large')
                       if starmap[x]['planets'][p]['size'] == 5:
                           print(green+'size:huge')
                       if starmap[x]['planets'][p]['size'] == 6:
                           print(green+'size:gas giant')
                       if starmap[x]['planets'][p]['ishabitable'] == 1:
                           print(green+'habitable:yes')
                       else:
                           print(red + 'habitable:no')
                       print(yellow+'treasures:' + str(starmap[x]['planets'][p]['treasures']))
                       print(lightblue+'has a space station?:' + str(starmap[x]['planets'][p]['spacestation']))
                       
                       print(green+"colonies:" + str(starmap[x]['planets'][p]['colonies']))
                       try:
                           print(yellow+'known ores:' + str(starmap[x]['planets'][p]['ores'][0]))
                       except KeyError:
                           pass
                       print('\n\n')
                       if starmap[x]['name'] != 'Sol':
                           dofight = random.randint(1,20)
                       else:
                           dofight = random.randint(1,40)
                       for playercolonies in range(len(starmap[x]["planets"])):
                           if starmap[x]["planets"][p]["colonies"] == ["player colony"]:
                               if random.randint(1,30) == 7:
                                   print(red+"one of your colonies is being raided by pirates!")
                                   for pir in range(3):
                                       fight()
                                   print(green+"your colony has been saved!")
                       if playership.colonies >= planets:
                           rebel = random.randint(1,40)
                           if rebel == 10:
                               rebelfight()
                           else:
                               pass
                       if dofight == 5:
                           print(red+"a pirate is attacking!\n")
                           if 'the banhammer' in playership.inv:
                               print(green+"You smack the enemy ship with the banhammer and watch it blink out of existance")
                               time.sleep(2.5)
                           elif "pirate crusher" in playership.inv:
                               print(green+"you use the pirate crusher to blast him across the universe\n")
                               time.sleep(1.5)
                          

                          
                           else:
                               fight()
                            
                       if playership.reputation <= 0:
                           newrep = abs(playership.reputation)
                           ishunted = random.randint(1,40)
                           if ishunted < newrep:
                               print(red+"due to your poor reputation, you are a wanted man, and someone has found you, and wants to end you")
                               fight()
                               playership.reputation -= 2
                             
                   c = raw_input('what do you want to do?:')
                   if 'leave' in c or 'exit' in c:
                       
                       instar = False
                   if "destroy" in c:
                       if "God splitter" in playership.inv:
                           print(green+"what planet would you like to destroy?")
                           for plist in range(len(starmap[x]['planets'])):
                               print(green+starmap[x]['planets'][plist]["name"])
                           des = raw_input("planet to destroy?:")
                           try:
                               for plist2 in range(len(starmap[x]['planets'])):
                                   print(green+starmap[x]['planets'][plist2]["name"])
                                   if starmap[x]['planets'][plist2]["name"] in des:
                                       starmap[x]["planets"].remove(starmap[x]['planets'][plist2])
                                       print(green+"planet destroyed. \n have a nice day!")
                           except:
                               print(red+"Try actually entering the name of a planet ಠ_ಠ") 
                                    
                       else:
                           print(red+"you need a God splitter nuke to destroy a planet")
                   if "create" in c:
                       if "planet seed" in playership.inv:
                           newplanet = Planet(random.randint(1,6),'') #1 being dwarf(pluto sized), 2 being small(mars sized), 3 being average(earth sized),4 being large(neptune sized), 5 being giant(saturn sized), 6 being gas giant(jupiter sized)
                           newplanetstats = newplanet.returnplanetinfo()
                           print(green+newplanetstats)
                           starmap[x]["planets"].append(newplanetstats)
                           playership.inv.remove("planet seed")
                           print(green+"planet created!")
                           time.sleep(1.5)
                       else:
                           print(red+"you need to aquire a planet seed")
                           time.sleep(2)
                    
                   #checks if you are entering the name of a planet, if so, fly to it.
                   
                   for j in range(len(starmap[x]['planets'])):
                       if starmap[x]['planets'][j]['name'] in c:
                           with open(storydir,'a') as s:
                               s.write('flew to planet ' + c + '\n')
                           playershipstats = [playership.name,playership.health,playership.evade,playership.crewamount,playership.firepower,playership.speed,playership.armor,playership.cargosize,playership.inv,playership.crew,playership.money,playership.fleet,playership.colonies,playership.maxfleetmembers,playership.maxhealth,playership.allies,playership.flightdist,playership.kills,playership.mined,playership.role,playership.reputation]
    
                    
                           save = {'difficulty':difficulty,'world':map,'stars':starmap,'player':playershipstats,'crew':playership.crew,'enemy':enemyhealthdef,'cquests':cquests,'sprite':playershipimg,'counter':starcounter,'species':species}
                           datalib.dump(save,savedir)
                           datalib.dump(save,savebackdir)
                           inplanet = True
                           while inplanet == True:
                               print(green+starmap[x]['planets'][j]['notes'])
                               
                               b = raw_input('what do you want to do?:')
                               #all the commands
                               if b == 'leave':
                                   inplanet = False

                               
                               elif 'help' in b or 'hint' in b:
                                   print(lightblue+'leave:leaves the planet\nspacestation:if there is one, fly to it.\npurchase:purchases the alien colony\nbuy station:buys your colony a spacestation\nmine:it mines the planet for ores\ncolonize\nquest\nmineall:mines all ores, but destroys planet in process')

                               elif 'mineall' in b:
                                   if "Algonian mining laser" in playership.inv:
                                       if starmap[x]['planets'][j]['name'] not in ['Earth','Pluto','Mars','Venus','Mercury',"Neptune",'Saturn','Uranus','Jupiter','Meowileen','Makara','Yakara','Uleano']:
                                           playership.cargosize += 50
                                           for o in range(5):
                                               for o2 in range(len(starmap[x]['planets'][j]['ores'])):
                                                   playership.inv.append(starmap[x]['planets'][j]['ores'][o2].replace("\n",""))
                                           starmap[x]['planets'].pop(j)
                                           planets -= 1
                                           print(green+"you mined up the planet")
                                           time.sleep(3)
                                           break
                                       else:
                                           print(red+"Illegal Move")
                                           time.sleep(3)
                                   else:
                                       print(red+"You need the right artifact to do this.")
                                       time.sleep(3)
                             
                               elif "purchase" in b:
                                   if starmap[x]['planets'][j]['colonies'] != []:
                                       if starmap[x]['planets'][j]['colonies'] != ['player colony']:
                                           if playership.money >= starmap[x]['planets'][j]['size'] * 1000:
                                               print(yellow+"spending " + str(starmap[x]['planets'][j]['size'] * 1000) + ", is that okay with you?")
                                               if raw_input("y/n") == "y":
                                                   starmap[x]['planets'][j]['colonies'] = ['player colony']
                                           else:
                                               print(red+"You don't have enough money you need " + str(starmap[x]['planets'][j]['size'] * 1000) + ", currency points")
                                       else:
                                           print(red+"you cannot buy your own colony")
                                   else:
                                       print(red+"... there needs to be a colony here for you to buy it.")
                               elif "capture" in b or 'take colony' in b or 'fight' in b:
                                   if starmap[x]['planets'][j]['colonies'] != []:
                                       #detect if colony is NOT a unique colony, if it is unique, do the corosponding boss fight.
                                       if starmap[x]['planets'][j]['colonies'] != ["player colony"]:
                                           if starmap[x]['planets'][j]['colonies'] != ["cat colony"]:
                                               if starmap[x]['planets'][j]['colonies'] != ["dragon colony"]:
                                                   if starmap[x]['planets'][j]['colonies'] != ["algonian colony"]:
                                                       if starmap[x]['planets'][j]['colonies'] != ["human colony"]:
                                                           
                                                            for fights in range(3):
                                                                fight()
                                                            print(hreen+"The enemies surrender once you destroy their fleet.")
                                                            starmap[x]['planets'][j]['colonies'].pop(0)
                                           
                                                            starmap[x]['planets'][j]['colonies'].append("player colony")
                                                            playership.colonies += 1
                                                            with open(storydir,'a') as s:
                                                               s.write('captured alien colony on planet ' + starmap[x]['planets'][j]['name'] + '\n')
                                                            playership.reputation -= 2
                                                       else:
                                                           with open(storydir,'r') as f:
                                                               lines = f.readlines()
                                                               story = str(lines)
                                                           if not "defeated federation flagship" in story:
                                                               humanfight()
                                                               
                                                               with open(storydir,'a') as s:
                                                                  s.write('captured alien colony on planet ' + starmap[x]['planets'][j]['name'] + '\n')
                                                               starmap[x]['planets'][j]['colonies'].pop(0)
                                           
                                                               starmap[x]['planets'][j]['colonies'].append("player colony")
                                                               print(green+"captured planet")
                                                               playership.reputation -= 2
                                                           else:
                                                               print(green+"captured planet")
                                                               starmap[x]['planets'][j]['colonies'].pop(0)
                                                               starmap[x]['planets'][j]['colonies'].append("player colony")
                                                               playership.colonies += 1
                                                               with open(storydir,'a') as s:
                                                                  s.write('captured alien colony on planet ' + starmap[x]['planets'][j]['name'] + '\n')
                                                               playership.reputation -= 2

                                                        
                                                   else:
                                                        Algonianfight()
                                                        starmap[x]['planets'][j]['colonies'].pop(0)
                                           
                                                        starmap[x]['planets'][j]['colonies'].append("player colony")
                                                        print(green+"captured planet")
                                                        playership.reputation -= 2
                                                        
                                               else:
                                                    dragonfight()
                                                    starmap[x]['planets'][j]['colonies'].pop(0)
                                           
                                                    starmap[x]['planets'][j]['colonies'].append("player colony")
                                                    print(green+"captured planet")
                                                    playership.reputation -= 2
                                           else:
                                                catfight()
                                                starmap[x]['planets'][j]['colonies'].pop(0)
                                           
                                                starmap[x]['planets'][j]['colonies'].append("player colony")
                                                print(green+"captured planet")
                                                playership.reputation -= 2



                                                       
                                       
                               elif "colonize" in b:
                                   print(green+"You set up a small colony on this planet.")
                                   if starmap[x]['planets'][j]['colonies'] == []:
                                       starmap[x]['planets'][j]['colonies'].append("player colony")
                                       playership.colonies += 1
                                       with open(storydir,'a') as s:
                                           s.write('colonized planet ' + starmap[x]['planets'][j]['name'] + '\n')
                                   else:
                                       print(red+"There is already a colony here")
                               elif 'buy station' in b:
                                   if "player colony" in starmap[x]['planets'][j]['colonies']:
                                       print(yellow+"spending 1000 currency points, are you okay with this?")
                                       if starmap[x]['planets'][j]['spacestation'] == False:       
                                           if playership.money >= 1000 and raw_input("y/n") == "y":
                                               starmap[x]['planets'][j]['spacestation'] = True
                                       else:
                                           print(red+"There can only be one spacestation")
                                   else:
                                        print(red+"You cannot buy a spacestation here, there are no colonies of yours here")
                                       
                               elif 'ally' in b:
                                   if starmap[x]['planets'][j]['colonies'] != ['player colony']:
                                       if starmap[x]['planets'][j]['colonies'] != []:
                                           if starmap[x]['planets'][j]['colonies'] not in playership.allies:
                                               print(yellow+"do you wish to ally with this empire?[y/n] will cost 600:")
                                               c = raw_input("you:")
                                               if c == "y":
                                                     if playership.money >= 600:
                                                         playership.money -= 600
                                                         playership.allies.append(starmap[x]['planets'][j]['colonies'])
                                                         playership.fleet += 1
                                                         playership.maxfleetmembers += 1
                                                         #you may get a better ship than what you get from a space station, you might not.
                                                         newhealth = random.randint(500,900)
                                                         playership.health += newhealth
                                                         playership.maxhealth += newhealth
                                                     else:
                                                         print(red+"you can't afford it, you need 600")
                                           else:
                                               print(red+'you have already allied with this empire')
                                       else:
                                           print(red+"no empire here")
                                   else:
                                       print(red+"you cannot ally with yourself")
                               elif "quest"  in b:
                                    if starmap[x]['planets'][j]['name'] not in cquests:
                                        quest(playership,starmap[x]['planets'][j])
                                    else:
                                        print(red+'you\'ve already done the quest here')
                                         
                               elif "mine" in b:
                                   print(yellow + random.choice(["You turn on your ship's mining laser, and gather some ores.","You stumble upon an ancient mining quarry. \nYou explore it hoping to find supplies to trade"]))
                                   grid = []
                                   mining = True
                                   print(green+"type the row and column number and be sure to separate them by a space")
                                   for row in range(7):
                                      col = str(row + 1) + ' '
                                      for g in range(10):
                                          col = col + '+ '
                                      listcol = col.split(" ")
                                      grid.append(listcol)

                                   while mining == True:
                                       print(yellow+"0 1 2 3 4 5 6 7 8 9 10")
                                       for length in range(len(grid)):
                                           print(yellow+" ".join(grid[length]))

                                       a = input("cell id:")
                                       if a == 'leave':
                                          mining = False 
                                       inp = a.split(" ")
                                       if inp != "0 0":
                                           try:
                                               in1 = int(inp[0])
                                               in2 = int(inp[1]) + 1
                                           except:
                                               print(red+"illegal move, mining in a random spot instead")
                                               time.sleep(1)
                                           try:
                                               if grid[in1][in2] != ' ':
                                                  grid[in1 -1][in2 -1] = ' '
                                                  ores = []
                                                  for orelen in range(len(starmap[x]['planets'][j]['ores'])):
                                                      ores.append(starmap[x]['planets'][j]['ores'][orelen])
                                                  for rocks in range(len(starmap[x]['planets'][j]['ores'])):
                                                        ores.append("rocks")             
                                                  found = random.choice(ores)
                                                  if len(playership.inv) <= playership.cargosize:
                                                      print(yellow+ "you have found " + found)
                                                      playership.inv.append(found.replace("\n",""))
                                                      time.sleep(2)
                                                  else:
                                                      print(red+"you have no cargo space left")
                                                      time.sleep(2)
                                                      break
                                               else:
                                                  print(red+"you have already looked here!")
                                           except:
                                               print(red+"illegal move")
                                               time.sleep(1)
                                       else:
                                           print(red+"illegal move")
                                           time.sleep(1)
    


                                   
                                   if len(playership.inv) <= playership.cargosize:
                                       for ore in range(len(starmap[x]['planets'][j]['ores'])):
                                           playership.inv.append(starmap[x]['planets'][j]['ores'][ore].replace("\n",""))
                                           print(yellow+"mined " + starmap[x]['planets'][j]['ores'][ore])
                                   else:
                                       print(red+"no more room in your cargo bay")
                               elif "collect" in b:
                                   if len(playership.inv) <= playership.cargosize:
                                       #try:
                                       playership.inv.append(starmap[x]['planets'][j]['treasures'])
                                       print(yellow+"collected " + starmap[x]['planets'][j]['treasures'])
                                       starmap[x]['planets'][j]['treasures'] = ""
                                       #except IndexError:
                                       #    print("no treasures on this planet")
                                   else:
                                       print(red+"no more room in your cargo bay")
                               
                               elif "explore" in b:
                                   print(lightblue+"you step onto the teleporter pad")
                                   
                                   import exploration
                                   
                                   
                                   exploration.explorergame(starmap[x]["planets"][j],playership,storydir,allspecies)
                                   
                               elif 'spacestation' in b:
                                   if starmap[x]['planets'][j]['spacestation'] == True:
                                       
                                       print(lightblue+'you\'ve docked with a space station.\nhere you can  \n----------\n<help>\n----------\n<crew>\n----------\n<shiplook>\n----------\n<fuel>\n----------\n<upgrade>\n----------\n<trade>\n----------\n<fleet>\n\n----------\n<shipyard>')    
                                       instation = True
                                       
                                       while instation == True:
                                           a = raw_input('what do you want to do?:')
                                           if 'help' in a:
                                               print(lightblue+"you can  \n----------\n<crew>\n----------\n<shiplook>\n----------\n<fuel>\n----------\n<upgrade>\n----------\n<trade>\n----------\n<fleet>\n\n----------\n<shipyard>")
                                           if 'shipyard' in a:
                                               print(green+'available ships:')
                                               
                                               print(lightblue+"################################################################")
                                               scavenger.displayship('  ')
                                               print(yellow+'\n\n\n\nprice = 600\n\n\n\n#####################################')
                                               goliath.displayship('  ')
                                               print(yellow+'\n\n\n\nprice = 1100\n\n\n\n####################################')
                                               
                                               b = raw_input('ship to buy[1(scavenger)/2(goliath)/leave]:')
                                               if b == '1':
                                                   if playership.money >= 600:
                                                       
                                                       playershipstats = scavengerstats
                                                       playership.money = playership.money - 600
                                                       playership = ship(playershipstats,sprites[0])
                                                       playershipimg = sprites[0]
                                                       print(green+'you now have the scavenger cargoship')
                                                   else:
                                                       print(red+'you need 600 currency points to buy this ship')
                                               if b == '2':
                                                   if playership.money >= 1100:
                                                       playershipstats = goliathstats
                                                       
                                                       playership = ship(playershipstats,sprites[1])
                                                       playershipimg = sprites[1]
                                                       playership.money = playership.money - 1100
                                                       print(green+'you now have the goliath warship')
                                                   else:
                                                       print(red+'you need 1100 currency points to buy this ship')
                                               else:
                                                   pass
                                           
                                           elif 'shiplook'  in a:
                                               
                                               a = raw_input("what file(file is in c:/broken space/ships folder)\n")
                                               try:
                                                   shippy = str(open("C:/broken space/ships/" + a).read()).split("\n")
                                                  
                                                   print(green+"your ship has been changed\n")
                                                   time.sleep(1)
                                                   playershipimg = shippy
                                                   playership = ship(playershipstats,playershipimg)
                                               except:
                                                   print(red + "Error, that file does not exist")
                                                   time.sleep(2)
                                    
                                           
                                           elif 'crew'  in a:
                                               print(yellow+"spending 100 currency points, are you okay with this?\n")
                                               
                                               if playership.money >= 100 and raw_input("y/n") == "y":
                                                   if len(playership.crew) <= playership.crewamount:
                                                       name = str(random.choice(characternames) + '(' + random.choice(allspecies).replace('\n','') + ')')
                                                       crewgen = {'name':name,'health':100,'profession':random.choice(['engineer','pilot','gunner','to be useless']),'room':''}
                                                       playership.addcustomcrewmember(crewgen)
                                                       print(green+'added ' + name + ' to crew.')
                                                       playership.money -= 100
                                                       with open(storydir,'a') as s:
                                                           s.write('recruited ' + crewgen['name'] +'\n')

                                                   else:
                                                       print(red='you can\'hold any more crew!\n')
                                                       time.sleep(1)
                                               else:
                                                    print(red+"you need at least 100 currency points to buy crew\n")
                                                    time.sleep(1)
                                           elif "fleet"  in a:
                                               if playership.money >= 600:
                                                   if playership.fleet < playership.maxfleetmembers:
                                                       playership.fleet += 1
                                                       playership.money -= 600
                                                       playership.health += 800
                                                       playership.maxhealth += 800
                                                       with open(storydir,'a') as s:
                                                           s.write('added ship to fleet'+ '\n')

                                                   else:
                                                       print(red+"you can have only " + str(playership.maxfleetmembers) + " ships in your fleet.\n")
                                                       time.sleep(1)
                                               else:
                                                   print(red+"you have no money, how can you pay the mechanic, you need at least 600\n")
                                                   time.sleep(1)
                                                    
                                           
        
                                           elif "upgrade"  in a:
                                               print(lightblue+"crew\ncargo\nstorage\nrepair\nweapons\nhyperdrive\ntier")
                                               b = raw_input()
                                               if "crew"  in b:
                                                   if playership.money >= 250:
                                                      playership.crewamount += 2
                                                      print(green+"you can have +2 more crew!")
                                                      playership.money -= 250
                                                   else:
                                                       print(red+"you have no money, how will you pay the mechanic! you need at least 250\n")
                                                       time.sleep(1)
                                               elif 'tier' in b:
                                                   print(green+"""
                                                   you can upgrade your ship with a preset based on these ores:\n
                                                   ----------
                                                   
                                                   copper:+20

                                                   ----------
                                                   
                                                   gold:+30

                                                   ----------
                                                   
                                                   iron:+40

                                                   ----------
                                                   
                                                   silicon:+50

                                                   ----------
                                                   
                                                   Eximus:+60

                                                   ----------
                                                   
                                                   Adamantarium:+70

                                                   ----------
                                                   
                                                   Atlarite:+80

                                                   ----------
                                                   
                                                   Celengil:+90

                                                   ----------
                                                   
                                                   Mobedium:+100

                                                   ----------
                                                   
                                                   Traddium:+110

                                                   ----------
                                                   
                                                   Prismite:+120

                                                   ----------""")
                                                   ore = raw_input("ore:").lower()
                                                   if ore == "copper":
                                                       if "copper" in playership.inv:
                                                           playership.health += 20
                                                           playership.firepower += 20
                                                           playership.inv.remove("copper")
                                                           print(red+"ship given copper upgrade")
                                                           time.sleep(1)
                                                       else:
                                                           print(red+"you dont have that ore")
                                                           time.sleep(1)
                                                   if ore == "gold":
                                                       if "gold" in playership.inv:
                                                           playership.health += 30
                                                           playership.firepower += 30
                                                           playership.inv.remove("gold")
                                                           print(yellow+"ship given gold upgrade")
                                                           time.sleep(1)
                                                       else:
                                                           print(red+"you dont have that ore")
                                                           time.sleep(1)
                                                   if ore == "iron":
                                                       if "iron" in playership.inv:
                                                           playership.health += 40
                                                           playership.firepower += 40
                                                           playership.inv.remove("iron")
                                                           print(red+"ship given iron upgrade")
                                                           time.sleep(1)
                                                       else:
                                                           print(red+"you dont have that ore")
                                                           time.sleep(1)
                                                   if ore == "silicon":
                                                       
                                                       if "silicon" in playership.inv:
                                                           playership.health += 50
                                                           playership.firepower += 50
                                                           playership.inv.remove("silicon")
                                                           print(lightblue+"ship given silicon upgrade")
                                                           time.sleep(1)
                                                       else:
                                                           print(red+"you dont have that ore")
                                                           time.sleep(1)
                                                   if ore == "eximus":
                                                       if "Eximus" in playership.inv:
                                                           playership.health += 60
                                                           playership.firepower += 60
                                                           playership.inv.remove("Eximus")
                                                           print(lightblue+"ship given Eximus upgrade")
                                                           time.sleep(1)
                                                       else:
                                                           print(lightblue+"you dont have that ore")
                                                           time.sleep(1)
                                                   if ore == "adamantarium":
                                                       if "Adamantarium" in playership.inv:
                                                           playership.health += 70
                                                           playership.firepower += 70
                                                           playership.inv.remove("Adamantarium")
                                                           print(red+"ship given adamantarium upgrade")
                                                           time.sleep(1)
                                                       else:
                                                           print(red+"you dont have that ore")
                                                           time.sleep(1)
                                                   if ore == "atlarite":
                                                       if "Atlarite" in playership.inv:
                                                           playership.health += 80
                                                           playership.firepower += 80
                                                           playership.inv.remove("Atlarite")
                                                           print(yellow+"ship given atlarite upgrade")
                                                           time.sleep(1)
                                                       else:
                                                           print(red+"you dont have that ore")
                                                           time.sleep(1)
                                                   if ore == "celengil":
                                                       if "Celengil" in playership.inv:
                                                           playe
                                                           rship.health += 90
                                                           playership.firepower += 90
                                                           playership.inv.remove("Celengil")
                                                           print(green+"ship given celengil upgrade")
                                                           time.sleep(1)
                                                       else:
                                                           print(red+"you dont have that ore")
                                                           time.sleep(1)
                                                   if ore == "mobedium":
                                                       if "Mobedium" in playership.inv:
                                                           playership.health += 100
                                                           playership.firepower += 100

                                                           playership.inv.remove("Mobedium")
                                                           print(lightblue+"ship given mobedium upgrade")
                                                           time.sleep(1)
                                                       else:
                                                           print(red+"you dont have that ore")

                                                           time.sleep(1)
                                                   if ore == "traddium":
                                                       if "Traddium" in playership.inv:
                                                           playership.health += 110
                                                           playership.firepower += 110
                                                           playership.inv.remove("Traddium")
                                                           print(yellow+"ship given Traddium upgrade")
                                                           time.sleep(1)
                                                       else:

                                                           
                                                           print(red+"you dont have that ore")
                                                           time.sleep(1)
                                                   if ore == "prismite":
                                                       if "prismite" in playership.inv:
                                                           playership.health += 120
                                                           playership.firepower += 120
                                                           playership.inv.remove("prismite")
                                                           print(lightblue+"ship given prismite upgrade")
                                                           time.sleep(1)
                                                           
                                                       else:
                                                           print(red+"you dont have that ore")
                                                           time.sleep(1)
                                                   
                                               elif "cargo"  in b:
                                                   if playership.money >= 250:
                                                      playership.cargosize += 4
                                                      playership.money -= 250
                                                      print(green+"your cargo bay can hold +4 more items!")
                                                      
                                                      time.sleep(1)
                                                   else:
                                                       print(red+"you have no money, how will you pay the mechanic! you need at least 250")
                                               elif "hyperdrive"  in b:
                                                   if playership.money >= 600:
                                                      playership.flightdist += 1
                                                      print(green+"your ship has a better hyperdrive!")
                                                      playership.money -= 600
                                                      
                                                      time.sleep(1)
                                                   else:
                                                       print(red+"you have no money, how will you pay the mechanic! you need at least 600")
                                               elif "repair"  in b:
                                                   if playership.money >= (100 + playership.maxhealth/10):
                                                       playership.health = playership.maxhealth
                                                       playership.money -= (100 + playership.maxhealth/10)
                                                       print(green+"done!")
                                                       time.sleep(1)
                                                   else:
                                                       print(red+"you have no money, how will you pay the mechanic! you need at least 100")
                                               elif "health pack" in b:
                                                   if playership.money >= (300 + playership.maxhealth/10):
                                                       playership.inv.append("health pack")
                                                       playership.money -= (300 + playership.maxhealth/10)
                                                       print(green+"done!")
                                                       time.sleep(1)
                                                   else:
                                                       print(red+"you have no money, how will you pay the mechanic! you need at least 100")
                                               elif "weapons" in b:
                                                  if playership.money >= 175:
                                                       playership.firepower += 20
                                                       playership.money -= 175
                                                       print(green+"done!")
                                                       time.sleep(1)
                                                  else:
                                                       print(red+"you have no money, how will you pay the mechanic! you need at least 175") 
                                               
                                           elif "trade" in a:
                                                
                                                while True:
                                                    print(yellow+"you can trade:\n ----------\n<gold> for $30\n----------\n<prismite> for $60\n----------\n<iron> for $35\n----------\n<copper> for $17\n----------\n<silicon> for $50\n----------\nrocks for $15\n----------\nother for 10")
                                                    print(lightblue+"your inventory:")
                                                    print(lightblue+ " || ".join(playership.inv))
                                                    c = raw_input("you:")
                                                    if "leave"  in c:
                                                       break
                                                    elif "gold" in c:
                                                        if "gold" in playership.inv:
                                                            print(yellow+"you sold gold  for $30")
                                                            playership.inv.remove("gold")
                                                            playership.money += 30
                                                            playership.mined += 1
                                                    elif "prismite" in c:
                                                        if "prismite" in playership.inv:
                                                            print(yellow+"you sold prismite for $60")
                                                            playership.inv.remove("prismite")
                                                            playership.money += 60
                                                            playership.mined += 1
                                                    elif "iron" in c:
                                                        if "iron" in playership.inv:
                                                            print(yellow+"you sold iron for $35")
                                                            playership.inv.remove("iron")
                                                            playership.money += 35
                                                            playership.mined += 1
                                                    elif "copper" in c:
                                                        if "copper" in playership.inv:
                                                            print(yellow+"you sold copper for $17")
                                                            playership.inv.remove("copper")
                                                            playership.money += 17
                                                            playership.mined += 1
                                                    elif "silicon" in c:
                                                        if "silicon" in playership.inv:
                                                            print(yellow+"you sold silicon for $50")
                                                            playership.inv.remove("silicon")
                                                            playership.money += 50
                                                            playership.mined += 1
                                                    elif "rocks" in c:
                                                        if "rocks" in playership.inv:
                                                            print(yellow+"you sold rocks for $15")
                                                            playership.inv.remove("rocks")
                                                            playership.money += 15
                                                            playership.mined += 1
                                                    else:
                                                        if c in playership.inv:
                                                            print(yellow+"you sold " + c + " for $30")
                                                            playership.inv.remove(c)
                                                            playership.money += 30
                                                            playership.mined += 1
                                                
                                           elif 'leave' in a:
                                               
                                               instation = False
                                           time.sleep(0.5)

                                           
                                           
                               
               
                   if "help" in c:
                       print(lightblue+'\nleave:leaves this star system\n<planet name>:enters a planet\ncreate: creates a planet, if you have a planet seed.\n destroy, destroys a specific planet of your choosing, if you have a god splitter nuke')
                       raw_input("press RETURN or ENTER to resume")
                       
                  
           else:
               print(red+"Your ship is not equipped to fly that far, go to a spacestation or find a research base to upgrade your hyprdrive")

               time.sleep(5)
       
    #the starmap's commands
    
    if a == 'help':
        print(lightblue+'\n<starname>:enter a star\nmap:displays the map\ndestroyitem:destroys an item\nexploreship explores your ship\nfire:fires a crewmember\ntrain:trains a crewmember\nview:it views an item displaying it\'s image')
        raw_input("press RETURN or ENTER to resume")
        
        
    
    
    elif 'map' in a or 'list stars' in a or 'chart' in a:
        showmap()
                
    elif "destroyitem" in a:
        b = raw_input("item to destroy:")
        if b in playership.inv:
            playership.inv.remove(b)
        else:
            print(red+"there is no " + b + " in your cargo bay")
    elif "fire" in a:
        b = raw_input("who is being a terrible crewmember?:")
        
        for x in range(len(playership.crew)):
        #if b == any(playership.crew)["name"]:
           if b in playership.crew[x]["name"]:
               print(red+b + " banished to nearby space station.")
               
               time.sleep(2)
               playership.crew.pop(x)
               break
        #else:
        #    print(b + " is not in your crew")
    elif "train" in a:
        b = raw_input("who is useless and needs training:")
        for x in range(len(playership.crew)):
        #if b == any(playership.crew)["name"]:
           if b == playership.crew[x]["name"]:
               print(green+b + " is no longer useless.")
               playership.crew[x]["profession"] = random.choice(['engineer','pilot','gunner'])
        #else:
        #    print(b + " is not in your crew")

    elif "exec" in a:
        if "the god cube" in playership.inv:
            i = raw_input("code to execute:")
            try:
                exec(i)
            except Exception as e:
                print(red+"error, this code cannot be run")
                print(red + str(e))
        else:
            print(red+"obtain the needed artifact to perform this")

    elif "regenerate" in a:
        if "universe seed" in playership.inv:
            generateworld()
            playership.colonies = 0
            playership.mined = 0
            playership.killed = 0
            playership.reputation = 10
            enemyhealthdef = int(enemyhealthdef*1.5)
            os.remove(storydir)
            newS = open(storydir,'w')
            newS.close()
            playership.inv.remove("universe seed")
        else:
            print(red+"You must aquire the needed artifact in order to perform this action")
    elif "cheat" in a:
        
        print(red+"the commands are,\nhyperdrive\ntestfight\npirate crusher\nmoney\ngive\nevent\nclear\ncolony\nspecies")
        b = raw_input("command:")
        if b == "hyperdrive":
            
            playership.flightdist += 50
           
        if b == "testfight":
            fight()
        if b == "money":
            playership.money += 999999
        if b == "give":
            c = raw_input("item to give:")
            playership.inv.append(c)


        if b == 'event':
            c = raw_input('id of event[1-14]:')
            randomevent(int(c))

        if b == 'clear':
            playership.inv = []
        if b == "pirate crusher":
            playership.inv.append("pirate crusher")
        if b == "colony":
            playership.colonies += 1
        if b == "species":
            a = raw_input("species to change to:")
            species = a
        
        
                
        
    #displays the item's corrosponding sprite
    elif 'view' in a:
       b = raw_input('item:')
       if b in playership.inv:
           if 'axe' in b:
               for x in range(len(itemlist['axe'])):
                    print(Fore.CYAN +str(itemlist['axe'][x]).replace('\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'shovel' in b:
               for x in range(len(itemlist['shovel'])):
                    print(Fore.CYAN +str(itemlist['shovel'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'sword' in b:
               for x in range(len(itemlist['sword'])):
                    print(Fore.CYAN +str(itemlist['sword'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'pickaxe' in b:
               for x in range(len(itemlist['pickaxe'])):
                    print(Fore.CYAN +str(itemlist['pickaxe'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif ' statue' in b or 'artifact' in b:
               for x in range(len(itemlist['statue'])):
                    print(yellow+str(itemlist['statue'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'gem' in b:
               for x in range(len(itemlist['gem'])):
                    print(lightblue+str(itemlist['gem'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'object' in b or 'thing' in b:
               for x in range(len(itemlist['thing'])):
                    print(red+str(itemlist['thing'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'machine' in b:
               for x in range(len(itemlist['machine'])):
                    print(green+str(itemlist['machine'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'wheel' in b:
               for x in range(len(itemlist['wheel'])):
                    print(Style.BRIGHT + red+ str(itemlist['wheel'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}','') + Style.NORMAL)
               time.sleep(3)
           elif 'god' in b:
               for x in range(len(itemlist['cmd'])):
                    print(yellow+str(itemlist['cmd'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'noah' in b:
               for x in range(len(itemlist['noah'])):
                    print(yellow+str(itemlist['noah'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'pirate' in b:
               for x in range(len(itemlist['pirate'])):
                    print(lightblue+str(itemlist['pirate'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'hyper' in b:
               for x in range(len(itemlist['hyperdrive'])):
                    print(red+str(itemlist['hyperdrive'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)

           elif 'banhammer' in b:
               for x in range(len(itemlist['banhammer'])):
                    print(red+str(itemlist['banhammer'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'bow' in b:
               for x in range(len(itemlist['bow'])):
                    print(red+str(itemlist['bow'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'saw' in b:
               for x in range(len(itemlist['saw'])):
                    print(cyan+str(itemlist['saw'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif 'knife' in b:
               for x in range(len(itemlist['knife'])):
                    print(cyan+str(itemlist['knife'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3)
           elif "universe seed" in b:
               for x in range(len(itemlist['universeseed'])):
                    print(Fore.MAGENTA + Style.DIM+str(itemlist['universeseed'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}','') + Style.NORMAL)
               time.sleep(3)
           elif "health pack" in b:
               for x in range(len(itemlist['healthpack'])):
                    print(red+str(itemlist['healthpack'][x]).replace('{\'','').replace('{\"','').replace('\'}','').replace('"}',''))
               time.sleep(3) 
           else:
               print(red+"Error, that item does not have a sprite")
               time.sleep(3)
           
    elif a == "explore":
        print(red+"try typing the name of a star. type map to see the stars")
        time.sleep(5)
    elif "helpall" in a:
        print(green+helpmes)
        raw_input("press enter or return to continue")
    
                      
    elif "describe" in a:
        typesel = raw_input("creature or ore? [1/2]:")
        if typesel == "2":
            ore = raw_input("ore to describe?:")
            if ore == "gold":
                print(lightblue+"gold is a soft yellow metal")
            elif ore == "iron":
                print(lightblue+"metal is a sturdy redish gray metal")
            elif ore == "copper":
                print(lightblue+"copper is a soft red metal")
            elif ore == "silicon":
                print(lightblue+"silicon is a brittle silvery crystal")
            elif ore == "prismite":
                print(lightblue+"prismite is a nigh-indestructible  prismatic crystal.")
           




     
            elif ore == "Eximus":
                print(lightblue+"Eximus is a moldable purple metal")

            elif ore == "Atlarite":
                print(lightblue+"Atlarite is a yellow, highly radioactive metal")
            elif ore == "Adamantarium":
                print(lightblue+"Adamantarium is a red, very strong metal")

            elif ore == "Traddium":
                print(lightblue+"Traddium is an orange, extremely strong metal")

            elif ore == "Celengil":
                print(lightblue+"Celengil is a green, mildly radioactive metal")

            elif ore == "Mobedium":
                print(lightblue+"Mobedium is a black, brittle metal, or metallic graphite is a better term...")
            else:
                s = open("ores.txt","r").readlines()
                
                #print(ore in s)
                if ore + "\n" in s:
                    print(lightblue+oredesc(s.index(ore + "\n")))
                else:
                    print(red+"that ore doesn't exist")
        if typesel == "1":
            ore = raw_input("creature to describe?:")
            if ore == "human":
                print(green+"humans are a intelligent, sentient creature. They are native to earth.")
            elif ore == "cat":
                print(green+"originally from earth, humans modified housecats and made them sapient. Now they are a extremely strong empire.")
            elif ore == "dragon":
                print(green+"dragons are mutated birds. they are similar to dragons. they are not very intelligent. but are extremely rich.")
            elif ore == "algonian":
                print(green+"algonians are evil and greedy jerks. nuf said.")
            else:
                s = open("creatures.txt","r").readlines()
                
                #print(ore in s)
                if ore + "\n" in s:
                    print(green+creaturedesc(s.index(ore + "\n")))
                else:
                    print(red+"that creature doesn't exist")
    elif "stats" in a:
        print(lightblue+'||health:' + str(playership.health) + ' | | evade:' + str(playership.evade) + '||')
    
        print(lightblue+'||crew:' + str(playership.crewamount) + ' | | firepower:' + str(playership.firepower) + '||')
       
        print(lightblue+'||speed:' + str(playership.speed) + ' | | armor:' + str(playership.armor) + '||')
        print(lightblue+'||cargosize:' + str(playership.cargosize) + ' | | money:' + str(playership.money) + '||')
        print(lightblue+'||inv:' + green + " || ".join(playership.inv) + lightblue +' | | fleet size":' + str(playership.fleet) + '||')
        print(lightblue+'||colonies created:' + str(playership.colonies) + ' | | max fleet members:' + str(playership.maxfleetmembers) + '||')
        print(lightblue+"||allies:" + str(playership.allies) + ' | | flight distance:' + str(playership.flightdist) + " parsecs||")
        
        comquests = datalib.load(savedir)['cquests']
        print(lightblue+'\nquests done:' + str(comquests))
        print(lightblue+"role:" + playership.role)
        rep = ""
        if playership.reputation == 0:
            rep = red+"bad"
        elif playership.reputation >= 5 and playership.reputation <= 9:
            rep = yellow+"average"
        elif playership.reputation >= 10 and playership.reputation <= 19:
            rep = yellow+"decent"
        elif playership.reputation >= 20 and playership.reputation <= 29:
            rep = green+"good person"
        elif playership.reputation >= 30:
            rep = blue+"hero"
        elif playership.reputation <= -1 and playership.reputation >= -9:
            rep = red+"pretty bad"
        elif playership.reputation <= -10 and playership.reputation >= -19:
            rep = red+"despicable"
        elif playership.reputation <= -20:
            rep = red+"villain" 
        print("reputation:" + rep + "(" + str(playership.reputation) + ")")
    elif "crew" in a:
        i = 0
        for x in range(len(playership.crew)):
        
        
            try:
                print(lightblue+' name:' + playership.crew[i]['name'])
            except:
                pass
            try:
                print(lightblue+' health:' + str(playership.crew[i]['health']))
            except:
                pass
            try:
                print(lightblue+' profession:' + playership.crew[i]['profession'])
            except:
                pass
            try:
                print(lightblue+' location on ship:' + playership.crew[i]['room'])
            except:
                pass
            try:
                print(' \n')
            except:
                pass
            try:
                print(lightblue + "Bio:" + playership.crew[i]["bio"])
            except:
                pass
            i += 1
    elif "repair" in a:
        if "health break" in playership.inv:
            print(lightblue+"repairing ship")
            playership.health = playership.maxhealth
            tme.sleep(1)
            print(green +"done!")
            time.sleep(0.5)
            playership.inv.remove("health pack")
        else:
            print(red+"You need a health pack to repair your ship yourself!")
    elif "exploreship" in a:
        inship = True
        room = "Bridge"
        while inship:
            
            print(green + "\n\n\n\nYou are currently in the " + str(room) + " room.")
            if room == "Bridge":
                print(lightblue + "\n\nAround you are various control panels, and strange gizmos and gadgets that you have no idea what they do.\n A table to your right has a coffee maker and a stack of styrofoam cups, sugar, and creamer.\nTo your Left is a large sofa, and a large plasma TV set up on a TV stand in front of the sofa.\nBehind you, is the door to the rest of the ship.")
                r = raw_input("Do you go north, south, east or west or leave?:")
                if r == "north":
                    print(red + "\n\nYou cant go north. Unless you want to end up outside your ship.")
                    time.sleep(1)
                if r == "east":
                    print(green +"\n\nYou walk over to the coffee maker")
                    time.sleep(1)
                if r == "west":
                    print(green + "\n\nYou walk over to the sofa, sit on it and watch tv for a while")
                    time.sleep(1)
                if r == "south":
                    print(green + "\n\nYou exit the room")
                    time.sleep(1)
                    room = "Main Lobby"
                if r == "leave":
                    time.sleep(1)
                    inship = False
                    break
            if room == "Main Lobby":
                print(lightblue + "you enter the ship's main lobby, it is a rather calm, peaceful room, that has a odd resemblance of a lounge.")
                r = raw_input("Do you go north, south, east or west or leave?:")
                if r == "north":
                    print(green + "You go back to the bridge")
                    room = "Bridge"
                    time.sleep(1)
                if r == "east":
                    print(green + "You go to the gunnery station")
                    room = "Gunnery Station"
                    time.sleep(1)
                if r == "west":
                    print(green + "You go to the engine room")
                    room = "Engine room"
                    time.sleep(1)
                if r == "south":
                    print(green + "You go to the crew dorms area")
                    room = "Dorms"
                    time.sleep(1)
                if r == "leave":
                    time.sleep(1)
                    break
            if room == "Gunnery Station":
                print(lightblue + "You enter the gunnery station, several strange control panels fill the room, that control the ship's weapons, some shelves around the room have missiles and projectiles on them, alongside mechanisms to load the weapons.")
                r = raw_input("Do you go north, south, east or west or leave?:")
                if r == "north":
                    print(red + "you cant go north.")
                    time.sleep(1)
                if r == "east":
                    print(red + "You cant go east.")
                    time.sleep(1)
                if r == "west":
                    print(green + "You go back to the main lobby")
                    time.sleep(1)
                    room = "Main Lobby"
                if r == "south":
                    print(red + "You cant go south.")
                    
                    time.sleep(1)
                if r == "leave":
                    time.sleep(1)
                    break
                
            if room == "Engine room":
                print(lightblue + "You enter the engine room, like the rest of the ship, several strange stations and pieces of equipment fill the room, including the hyperdrive, the generators for the engine, and so on.")
                r = raw_input("Do you go north, south, east or west or leave?:")
                if r == "north":
                    print(red + "you cant go north.")
                    time.sleep(1)
                if r == "east":
                    print(green + "You go back to the main lobby.")
                    room = "Main Lobby"
                    time.sleep(1)
                if r == "west":
                    print(red + "You cant go west.")
                    time.sleep(1)
                if r == "south":
                    print(red + "you cant go south.")
                    time.sleep(1)
                if r == "leave":
                    time.sleep(1)
                    break   
            if room == "Dorms":
                print(lightblue + "You enter the dorms area. Here, are all the crew's rooms. Your current crew are:")
                i = 0
                for x in range(len(playership.crew)):
                
                
                    try:
                        print(lightblue+' name:' + playership.crew[i]['name'])
                    except:
                        pass
                    try:
                        print(lightblue+' health:' + str(playership.crew[i]['health']))
                    except:
                        pass
                    try:
                        print(lightblue+' profession:' + playership.crew[i]['profession'])
                    except:
                        pass
                    try:
                        print(lightblue+' location on ship:' + playership.crew[i]['room'])
                    except:
                        pass
                    try:
                        print(' \n')
                    except:
                        pass
                    i += 1
                r = raw_input("Do you go north, south, east or west or leave?:")
                if r == "north":
                    print(green + "You go back to the main lobby")
                    room = "Main Lobby"
                    time.sleep(1)
                if r == "east":
                    print(red + "you cant go east.")
                    time.sleep(1)
                if r == "west":
                    print(red + "you cant go west.")
                    time.sleep(1)
                if r == "south":
                    print(red + "you cant go south.")
                    time.sleep(1)
                if r == "leave":
                    time.sleep(1)
                    break   
    playershipstats = [playership.name,playership.health,playership.evade,playership.crewamount,playership.firepower,playership.speed,playership.armor,playership.cargosize,playership.inv,playership.crew,playership.money,playership.fleet,playership.colonies,playership.maxfleetmembers,playership.maxhealth,playership.allies,playership.flightdist,playership.kills,playership.mined,playership.role,playership.reputation]
    
        
    save = {'difficulty':difficulty,'world':map,'stars':starmap,'player':playershipstats,'crew':playership.crew,'enemy':enemyhealthdef,'cquests':cquests,'sprite':playershipimg,'counter':starcounter,'species':species}
    datalib.dump(save,savedir)
    datalib.dump(save,savebackdir)
    #print(save)
