import csv
data = []
# with open('q3exdata.txt', 'r') as fd:
with open('q3data.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        data += row

data = [list(x) for x in data]
# print(data)

# question 1
print(data[0])
print(len(data[0]))
def count_trees(slopex, slopey, data):
    x = 0
    y = 0
    mx = slopex
    my = slopey

    treecount = 0
    while y < len(data):
        # print((x, y))
        # print(data[y])
        xcoord = x % len(data[0])
        elem = data[y][xcoord]
        if elem == '#':
            # data[y][xcoord] = 'X'
            treecount += 1
        # else:
            # data[y][xcoord] = '0'
        # print(data[y])
        
        # increment
        x += mx
        y += my
    return (treecount, data)

for line in data:
    print(' '.join(line))

count, result = count_trees(3, 1, data)
for line in result:
    print(' '.join(line))

print(count)

# question 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
count = 1
for slope in slopes:
    print(slope)
    count *= count_trees(slope[0], slope[1], data)[0]
    print(count)
print(count)