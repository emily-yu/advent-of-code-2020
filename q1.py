import csv
data = []
with open('q1data.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        data += row

print(data)

for elem in data:
    relative = str(2020 - int(elem))
    if relative in data:
        print("realtive", int(relative) * int(elem))


    