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
def count_trees(startx, starty, data):
    x = startx
    y = starty
    mx = 3
    my = 1

    treecount = 0
    while y < len(data):
        # print((x, y))
        # print(data[y])
        xcoord = x % len(data[0])
        elem = data[y][xcoord]
        if elem == '#':
            data[y][x] = 'X'
            treecount += 1
        else:
            data[y][x] = '0'
        print(data[y])
        
        # increment
        x += mx
        y += my
    return (treecount, data)

for line in data:
    print(' '.join(line))

count, result = count_trees(0, 0, data)
for line in result:
    print(' '.join(line))

print(count)