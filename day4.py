import math
import re 

def part_one():
    passports=[]
    criteria=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    with open('input/day4.1.txt') as fp:
        cp={}
        for line in fp:
            pairs=line.strip().split()
            if (len(pairs)>0):
                for pair in pairs:
                    p=pair.split(':')
                    cp[p[0]]=p[1]
            else:
                current_passport=cp.copy()
                passports.append(current_passport)
                cp.clear()
        current_passport=cp.copy()
        passports.append(current_passport)
    valid=0
    for passport in passports:
        curr=1
        for data in criteria:
            if data not in passport.keys():
                curr=0
                break
        valid+=curr

    print(valid)

def part_two():
    passports=[]
    criteria=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    with open('input/day4.1.txt') as fp:
        cp={}
        for line in fp:
            pairs=line.strip().split()
            if (len(pairs)>0):
                print(len(pairs))
                if (len(pairs)>7):
                    print(pairs)
                for pair in pairs:
                    p=pair.split(':')
                    cp[p[0]]=p[1]
            else:
                current_passport=cp.copy()
                passports.append(current_passport)
                cp.clear()
        current_passport=cp.copy()
        passports.append(current_passport)
    valid=0
    vp=[]
    for n,passport in enumerate(passports):
        print(f"passport number {n} ",end="")
        curr=1
        for data in criteria:
            if data not in passport.keys():
                print("is missing a key")
                curr=0
                break
            if data == "byr":
                if int(passport[data]) < 1920 :
                    print("is for a person too old")
                    curr=0
                    break
                if int(passport[data]) > 2002 :
                    print("is for a person too young")
                    curr=0
                    break
            if data == "iyr":
                if int(passport[data]) < 2010 :
                    print("was issued too long ago")
                    curr=0
                    break
                if int(passport[data]) > 2020 :
                    print("is issued in future")
                    curr=0
                    break
            if data == "eyr":
                if int(passport[data]) < 2020 :
                    print("expired in the past")
                    curr=0
                    break
                if int(passport[data]) > 2030 :
                    print("expired too far in future")
                    curr=0
                    break
            if data == "hgt":
                units=passport[data][-2:]
                if units == "cm" or units == "in":
                    ht=int(passport[data][:-2])
                    if units=="cm":
                        if ht<150:
                            print("is for a person too short")
                            curr=0
                            break
                        if ht>193:
                            print("is for a person too tall")
                            curr=0
                            break
                    if units=="in":
                        if ht<59:
                            print("is for a person too short (in)")
                            curr=0
                            break
                        if ht>76:
                            print("is for a person too tall (in)")
                            curr=0
                            break
                else:
                    print("has the height in the wrong units")
                    curr=0
                    break

            if data == "hcl":
                if len(passport[data]) !=7:
                    print("has the wrong length haircolour code")
                    curr=0
                    break
                if passport[data][0] !='#':
                    curr=0
                    print("has a haircolour which doesn't start with a #")
                    break
                if not re.match(r'[0-9a-f]{6}',passport[data][1:]):
                    print("has a haircolour not hex")
                    curr=0
                    break

            if data == "pid":
                if len(passport[data]) !=9:
                    print("has the wrong length pid")
                    curr=0
                    break
                if not re.match(r'\d{9}',passport[data]):
                    print("has a pid not in digits")
                    curr=0
                    break
            if data == "ecl":
                if passport[data] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    print("has an unknown eye color")
                    curr=0
                    break

        if curr>0:
            print("is valid")
        valid+=curr
    print(valid)


part_two()
part_one()


