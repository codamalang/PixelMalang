import os
import sys
from typing import Literal

sep = os.path.sep

pathname = sep.join(__file__.split(sep)[:-1])+sep

class ln:
    def __init__(self, *args, form = ""):
        if len(form) == 0:
            self.path = pathname + sep.join(args)
        else:
            self.path = pathname + sep.join(args) + "." + form

    def __str__(self):
        return self.path

    def isfile(self):
        return os.path.isfile(self.path)
    
    def open(self, mode:Literal['r', 'w', 'a']='r', encoding="utf8"):
        return open(self.path, mode, encoding=encoding)
    
    def read(self):
        readfile = self.open()
        cont = readfile.read()
        readfile.close()
        return cont
    
    def readlines(self):
        readfile = self.open()
        cont = readfile.readlines()
        readfile.close()
        return cont

    def write(self, cont='', mode:Literal['w', 'a']='w'):
        editfile = self.open(mode)
        editfile.write(cont)
        editfile.close()

    def remove(self):
        os.remove(self.path)
    
class lndir:
    def __init__(self, *args):
        self.path = pathname + sep.join(args)

    def __str__(self):
        return self.path
    
    def isdir(self):
        return os.path.isdir(self.path)
    
    def makedirs(self):
        os.makedirs(self.path, exist_ok=True)

    def removedirs(self):
        os.removedirs(self.path)

    def pardir(self):
        pard = lndir()
        pard.path = sep.join(self.path.split(sep)[:-1])
        return pard
    
    def chidir(self, name):
        chid = lndir()
        chid.path = self.path+sep+name
        return chid
    
    def chifile(self, *args, form = ""):
        chfl = ln()
        if len(form) == 0:
            chfl.path = self.path + os.path.sep + os.path.sep.join(args)
        else:
            chfl.path = self.path + os.path.sep + os.path.sep.join(args) + "." + form
        print(chfl)
        return chfl
    
    def listdir(self):
        return os.listdir(self.path)

def setpath():
    sys.path.append(pathname[:-1])

if __name__ == "__main__":
    print("bot launch lib info")
    print("="*60)
    print(f"pathname : {pathname}")
    print(ln("res", "about.md"))
    if ln("res", "about", form="md").isfile():
        print("o")
    print(ln("res", "security", "securityfiles", form="txt"))
    aa = ln("test", "test01", form="txt")
    aa.write('테스트?')
    print(aa.read())
    aa.remove()
    print(lndir("test", "test01").pardir())