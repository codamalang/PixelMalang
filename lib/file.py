from launchio import ln, lndir

def ismemo(filename: str):
    name = ln("community", "memo", filename, form="txt")
    return name.isfile()

def openfile(cmd: str, filename: str, newfile=False):
    name = ln("community", cmd, filename, form="txt") # cmd+os.path.sep+filename+".txt"
    if name.isfile(): # os.path.isfile(name):
        return name.read() # with open(name, "r", encoding="utf8") as file:
        #     return file.read()
    else:
        if newfile:
            name.write()
        return ''

def editfile(cmd: str, filename: str, memo: str):
    name = ln("community", cmd, filename, form="txt")
    name.write(memo, 'w')

def appendfile(cmd: str, filename: str, memo: str):
    name = ln("community", cmd, filename, form="txt")
    name.write(memo, 'a')

def delfile(cmd: str, filename: str):
    name = ln("community", cmd, filename, form="txt")
    if name.isfile():
        name.remove()

def listsplit(cmd: str, filename: str):
    name = ln("community", cmd, filename, form="txt")
    return name.readlines()

def rev(folder: str, filename: str, memo: str):
    dr = lndir("community", folder, filename)# folder+os.path.sep+filename
    revv = 0
    if not dr.isdir():
        dr.makedirs()
    else:
        revv = int(dr.chifile("rev.txt").read())
        revv += 1

    dr.chifile("rev.txt").write(str(revv))
    dr.chifile(f"rev{revv}.txt").write(memo)

def isrev(folder: str, filename: str, ver):
    return ln("community", folder, filename, f"rev{ver}.txt").isfile()

def openrev(folder: str, filename: str, ver):
    return ln("community", folder, filename, f"rev{ver}.txt").read()

def getver(folder: str, filename: str):
    return ln("community", folder, filename, "rev.txt").read()

def memover(tp: str, name: str, rev):
    return tp + " - " + name + f"(rev {rev})"