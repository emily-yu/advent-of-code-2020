import csv
data = []
with open('q2data.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        data += row

# parse data
for ind, line in enumerate(data):
    line = line.split(' ')

    start, end = line[0].split('-')
    # print(start, end)

    letter = line[1][0]
    # print(letter)

    password = line[2]
    # print(password)
    
    data[ind] = (int(start), int(end), letter, password)

# print(data)

# =========================================================================================================
def find_occurences(target, password, min, max):
    count = 0
    for letter in password:
        if count <= max:
            if letter == target:
                count += 1
        elif count > max: # not valid
            return False

    # never reached limit
    if count >= min and count <= max:
        return True
    return False

# question 1
def valid_passwords_range(data):   
    valid_count = 0
    for elem in data:
        is_valid = find_occurences(elem[2], elem[3], elem[0], elem[1])
        if is_valid:
            valid_count += 1
    return valid_count

print("valid: ", valid_passwords_range(data))

# question 2
def valid_passwords_index(data):   
    valid_count = 0
    for elem in data:
        start = elem[0] - 1
        end = elem[1] - 1
        target = elem[2]
        pw = elem[3]
        # check one equal
        if (pw[start] == target or pw[end] == target) and not (pw[start] == target and pw[end] == target):
            valid_count += 1
    return valid_count
        
print("valid: ", valid_passwords_index(data))