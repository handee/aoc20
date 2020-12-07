import math

def part_one():
    e=[]
    with open('input/day1.1.txt') as fp:
        e=[int(line.strip()) for line in fp]
    
    l = len(e)
    print(l)
    a=0
    b=0
    for c,num in enumerate(e):
        print (c,num)
        for i in range(c+1,l):
            if (num+e[i])==2020:
                a=num
                b=e[i]
                break;

    print(f"The numbers which add up to 2020 are {a} and {b} and their product is {a*b}.")

def part_two():
    e=[]
    with open('input/day1.1.txt') as fp:
        e=[int(line.strip()) for line in fp]
    
    l = len(e)
    print(l)
    a=0
    b=0
    for ct,num in enumerate(e):
        print (ct,num)
        for i in range(ct+1,l):
            for j in range(i+1,l):
                if (num+e[i]+e[j])==2020:
                    a=num
                    b=e[i]
                    c=e[j]
                    break;

    print(f"The numbers which add up to 2020 are {a} and {b} and {c} and their product is {a*b*c}.")


#part_one()
part_two()


