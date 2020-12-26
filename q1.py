import csv
data = []
with open('q1data.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        data += row

data = [int(x) for x in data]
data.sort()
# print(data)

# question 1: twosum
def twoSum(target, data):
    for elem in data:
        relative = target - elem
        if relative in data:
            return (relative, elem)
    return None

result = twoSum(2020, data)
print('answer q1a: ', result[0] * result[1])

# question 2: threesum
'''
doomed no way to do 1 pass
[35, 50, 60, 70, 1855, 1900]
[1985, 1970, 1960, 165, 120]

[1, 2, 5, 8, 9, 10], search for 16
{
    1: []
    2: []
    5: []
    8: []
    9: []
    10: []
}
1 and 10; gap = 5
    find (5) and put in tracking arr
    5 is in arr
    @ n/2 = 8
    8 > 5; pick left
    [1, 2, 5]

[2, 5, 8, 9, 10]

1 - run from left
2 and 10; gap = 4
    find (4) combinations
    [2]
    none
5 and 10; gap = 1
    find (1) combo
    []
    none
8 and 10; gap = -2
    8 and 9; gap = -1
        5 and 8; gap = 3
            find (3) combinations;
            [2]
            none
        
2 - run from right
2 and 10

dataset = set(data)
# generate gap array
gaps = [0] * len(data)
for i in range(1, len(data)):
    # print(data[i-1], data[i])
    # print(gaps)
    # print()
    gaps[i] = gaps[i-1] + (data[i] - data[i-1])
print(gaps)

print("asdf")
start = data[0]
end = data[len(data) - 1]

# 2020 - 52 = 1968
# 2020 - 2010 = 10
# is 1968 in array? is there a 2sum that is 52?

gap = start - end
print(start, end, gap)

# initial gap
for i in range(0, gap):
    print(i)
    # if i in gaps:
    #     print(data[0], data[len(data) - 1], data[i])
    #     break
'''
def threeSum(target, data):
    for base in data:
        # print(base)
        first = target - base
        search = twoSum(first, data)
        if search is not None:
            second, third = search
            return (base, second, third)
    return None

result = threeSum(2020, data)
print("answer q1b: ", result[0] * result[1] * result[2])
