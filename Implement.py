from sklearn.neighbors import NearestNeighbors as nn
import csv
import Metric
zero = 70;


def normData(data):
    data.pop(0)
    for row in data:
        for idx, c in enumerate(row):
            row[idx] = ord(c) if (c!="0") else zero
    return;


def getInput(input):
    for idx, c in enumerate(input):
        input[idx] = ord(c)
    while len(input) < 7:
        input.append(zero)
    print(input)
    return [input]


def printResult(indices, data):
    for idx in indices:
        for c in data[idx]:
            print(chr(c) if (c != zero) else "", end="")
        print(" ", end="")
    print("")


with open('db.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))


normData(data)
print(data)
while True:
    word = getInput(input = list(input("Enter string: ").lower()))
    print(word)
    nb = nn(n_neighbors=3, algorithm='kd_tree').fit(data)
    distance, indices  = nb.kneighbors(word)
    printResult(indices = indices[0], data = data)