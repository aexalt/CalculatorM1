#step3
import calc2

f = open("goto.txt", mode='r')
data = f.read().splitlines()
i = 0
completedlist = []

print(i)
completedlist.append(data[i])
currentline = data[i].split()
print(currentline)

if data[1] == "calc":
    #do calc
    i = calc2.calculate(data[2], int(data[3]), int(data[4]))
else:
    #goto line data[1] in file
    i = data[1]



f.close