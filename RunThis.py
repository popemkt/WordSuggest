from sklearn.neighbors import NearestNeighbors as nn
import csv
import Metric as mt
zero = 33
# ket qua co the thay doi neu chon zero la toa do khac, chua tim duoc zero toi uu
maxNum = 10
# do dai toi da cua chu nhap vao
nbNum = 4
# so luong tu muon goi y
def normData(data):
    # chuan hoa du lieu doc tu file csv duoi dang array cua toa do tung chu cai
    data.pop(0)
    for row in data:
        for idx, c in enumerate(row):
            row[idx] = mt.cvlct(c.lower()) if (c!="0") else zero


def getInput(input):
    # lay du lieu input roi chuan hoa
    for idx, c in enumerate(input):
        input[idx] = mt.cvlct(c)
    while len(input) < maxNum:
        input.append(zero)
    return [input]


def printResult(indices, data):
    # convert ket qua tu dang chuan hoa sang du lieu doc duoc
    for idx in indices:
        for c in data[idx]:
            print(mt.rvlct(c) if (c != zero) else "", end="")
        print(" ", end="")
    print("")


with open('Test2.csv', newline='\n') as csvfile:
    data = list(csv.reader(csvfile))

print("Number of words: %d" % len(data))
print("Max length: %d" % maxNum)
normData(data)
while True:
    word = getInput(input = list(input("Enter string: ").lower()))
    nb = nn(n_neighbors=nbNum, algorithm='brute', metric = mt.compare).fit(data)
    distance, indices  = nb.kneighbors(word)
    printResult(indices = indices[0], data = data)