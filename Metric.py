import math as m



maxNum = 7;
def compare(x,y):
    # ham tinh khoang cach giua 2 phim tren ban phim dua vao toa do
    total = 0
    for i in range(0,maxNum):
        fx = int(x[i])%10
        lx = int(x[i])/10
        fy = int(y[i])%10
        ly = int(y[i])/10
        total += m.sqrt((fx -  fy)**2+(lx-ly)**2)
    return total/maxNum



def cvlct(a):
    # convert location: chuyen ky tu ve toa do tren ban phim querty
    if a=="q":
        return 0
    if (a=="w"):
        return 1
    if (a=="e"):
        return 1
    if (a == "r"):
        return 3
    if (a == "t"):
        return 4
    if (a == "y"):
        return 5
    if (a == "u"):
        return 6
    if (a == "i"):
        return 7
    if (a == "o"):
        return 8
    if (a == "p"):
        return 9
    if (a == "a"):
        return 10
    if (a == "s"):
        return 11
    if (a == "d"):
        return 12
    if (a == "f"):
        return 13
    if (a == "g"):
        return 14
    if (a == "h"):
        return 15
    if (a == "j"):
        return 16
    if (a == "k"):
        return 17
    if (a == "l"):
        return 18
    if (a == "z"):
        return 20
    if (a == "x"):
        return 21
    if (a == "c"):
        return 22
    if (a == "v"):
        return 23
    if (a == "b"):
        return 24
    if (a == "n"):
        return 25
    if (a == "m"):
        return 26


def rvlct(a):
    # revert location: chuyen toa do ky tu ve ky tu tren ban phim querty
    if a==0:
        return "q"
    if (a==1):
        return "w"
    if (a==2):
        return "e"
    if (a == 3):
        return "r"
    if (a == 4):
        return "t"
    if (a == 5):
        return "y"
    if (a == 6):
        return "u"
    if (a == 7):
        return "i"
    if (a == 8):
        return "o"
    if (a == 9):
        return "p"
    if (a == 10):
        return "a"
    if (a == 11):
        return "s"
    if (a == 12):
        return "d"
    if (a == 13):
        return "f"
    if (a == 14):
        return "g"
    if (a == 15):
        return "h"
    if (a == 16):
        return "j"
    if (a == 17):
        return "k"
    if (a == 18):
        return "l"
    if (a == 20):
        return "z"
    if (a == 21):
        return "x"
    if (a == 22):
        return "c"
    if (a == 23):
        return "v"
    if (a == 24):
        return "b"
    if (a == 25):
        return "n"
    if (a == 26):
        return "m"
