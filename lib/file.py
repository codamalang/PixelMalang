from launchio import ln, lndir

def ismemo(filename):
    name = ln("memo", filename, form="txt")
    return name.isfile()

def openfile(cmd, filename, newfile=False):
    name = ln(cmd, filename, form="txt") # cmd+os.path.sep+filename+".txt"
    if name.isfile(): # os.path.isfile(name):
        return name.read() # with open(name, "r", encoding="utf8") as file:
        #     return file.read()
    else:
        if newfile:
            name.write()
        return ''

def editfile(cmd, filename, memo):
    name = ln(cmd, filename, form="txt")
    name.write(memo, 'w')

def appendfile(cmd, filename, memo):
    name = ln(cmd, filename, form="txt")
    name.write(memo, 'a')

def delfile(cmd, filename):
    name = ln(cmd, filename, form="txt")
    if name.isfile():
        name.remove()

def listsplit(cmd, filename):
    name = ln(cmd, filename, form="txt")
    return name.readlines()

def rev(folder, filename, memo):
    dr = lndir(folder, filename)# folder+os.path.sep+filename
    revv = 0
    if not dr.isdir():
        dr.makedirs()
    else:
        revv = int(dr.chifile("rev.txt").read())
        revv += 1

    dr.chifile("rev.txt").write(str(revv))
    dr.chifile(f"rev{revv}.txt").write(memo)

def isrev(folder, filename, ver):
    return ln(folder, filename, f"rev{ver}.txt").isfile()

def openrev(folder, filename, ver):
    return ln(folder, filename, f"rev{ver}.txt").read()

def getver(folder, filename):
    return ln(folder, filename, "rev.txt").read()

def memover(tp, name, rev):
    return tp + " - " + name + f"(rev {rev})"