from launchio import ln

token = ""
myid = ""
ttsin = ""
ttsout = ""
prefix = ""

def varset(): # 변수 설정
    global token
    global myid
    global ttsin
    global ttsout
    global prefix

    token  = ln("res", "security", "token.txt") .read()
    myid   = ln("res", "security", "myid.txt")  .read()
    ttsin  = ln("res", "security", "ttsin.txt") .read()
    ttsout = ln("res", "security", "ttsout.txt").read()
    prefix = ln("res", "prefix.txt").read()