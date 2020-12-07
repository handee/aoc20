import math

def part_one():
    maxs=0
    with open('input/day5.1.txt') as fp:
        for line in fp:
            r=line[:7]
            c=line[7:]
            r=r.replace('B','1',)
            r=r.replace('F','0',)
            c=c.replace('R','1',)
            c=c.replace('L','0',)
            r=int(r,2)
            c=int(c,2)
            if (r*8+c)>maxs:
                maxs=r*8+c
            print(r,c,r*8+c,maxs)
    print(f"{maxs} is the max seat id")

def part_two():
    maxs=964
    occupied=[0]*maxs
    with open('input/day5.1.txt') as fp:
        for line in fp:
            r=line[:7]
            c=line[7:]
            r=r.replace('B','1',)
            r=r.replace('F','0',)
            c=c.replace('R','1',)
            c=c.replace('L','0',)
            r=int(r,2)
            c=int(c,2)
            occupied[r*8+c]=1
    for n,seat in enumerate(occupied):
        if seat==0:
            print(n)
    print(f"{maxs} is the max seat id")



#part_one()
part_two()


