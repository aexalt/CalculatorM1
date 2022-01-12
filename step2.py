#step2
import calc2

f = open("data.txt", mode='r')
total = 0
for line in f:
    data = line.split()
    total += calc2.calculate(data[1], int(data[2]), int(data[3]))
    print(total)
print("final total: " + '{:.2f}'.format(total))
f.close