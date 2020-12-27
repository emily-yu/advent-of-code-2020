count = 0
with open('q4data.txt', 'r') as fd:
    lst = fd.read().split('\n\n')
    passports = [x.replace('\n', ' ').split() for x in lst]
    for passport in passports:
        if len(passport) == 8:
            count += 1
            continue

        cid = False
        print(passport)
        
        for field in passport:
            if field[0:3] == 'cid':
                cid = True
        
        if not cid and len(passport) == 7:
            count += 1

print(count)