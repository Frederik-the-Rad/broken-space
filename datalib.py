def load(file):
    return eval(open(file,'r').read())

def dump(data,file):
    with open(file,"w") as x:
        x.write(str(data))


