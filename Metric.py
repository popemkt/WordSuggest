import math as m
zero = 33
maxNum = 10;

dict = {
    0:[0,0],
    1:[0,1],
    2:[0,2],
    3:[0,3],
    4:[0,4],
    5:[0,5],
    6:[0,6],
    7:[0,7],
    8:[0,8],
    9:[0,9],
    10:[1,0],
    11:[1,1],
    12:[1,2],
    13:[1,3],
    14:[1,4],
    15:[1,5],
    16:[1,6],
    17:[1,7],
    18:[1,8],
    20:[2,0],
    21:[2,1],
    22:[2,2],
    23:[2,3],
    24:[2,4],
    25:[2,5],
    26:[2,6],
    zero:[4,4]
}
def compare(x,y):
    # ham tinh khoang cach giua 2 phim tren ban phim dua vao toa do
    total = 0
    for i in range(0,maxNum):
        # fx = int(x[i])%10
        # lx = int(x[i])/10
        # fy = int(y[i])%10
        # # ly = int(y[i])/10
        # print(int(x[i]))
        # print(int(y[i]))
        total += m.sqrt((dict[int(x[i])][0] -  dict[int(y[i])][0])**2+(dict[int(y[i])][1]-dict[int(x[i])][1])**2)
    return total/maxNum



def cvlct(a):
    # convert location: chuyen ky tu ve toa do tren ban phim querty
    if a=="q":
        return 0
    if (a=="w"):
        return 1
    if (a=="e"):
        return 2
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
