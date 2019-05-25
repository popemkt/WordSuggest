import csv
import re
maxNum = 7


# cai nay de thao tac vs file database, khong can quan tam

def hasNonLetter(inputString):
    return bool(re.search(r'[^a-zA-Z\n]', inputString))

f = open("tdb.txt", "r")
flist = []
for x in f:
    print(x)
    if hasNonLetter(x)==False:
        row = list(str(x))
        length = len(row)
        row[length-1] = 0
        while len(row) < maxNum+1:
            row.append(0)
        if len(row)==maxNum+1:
            del row[maxNum]
            flist.append(row)
f.close()
print(len(flist))
print(len(flist[0]))
print(flist[0])
with open('test1.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    for row in flist:
        writer.writerow(row)