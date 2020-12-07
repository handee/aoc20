
import math

def part_one():
    valid=0
    with open('input/day2.1.txt') as fp:
        for line in fp:
            r,c,p=line.split() 
            l,u=r.split('-')
            u=int(u)
            l=int(l)
            c=c[0]
            count=p.count(c)
            if (count<l) :
                print(f"Invalid! {p} contains {count} - not enough {c} (should be {l} to {u})")
            elif (count>u):
                print(f"Invalid! {p} contains {count} - too many {c} (should be {l} to {u})")
            else:
                print(f"Valid!! {p} contains {count} which is {l} to {u} instances of {c}")
                valid+=1

    print(valid)

def part_two():
    valid=0
    with open('input/day2.1.txt') as fp:
        for line in fp:
            r,c,p=line.split() 
            l,u=r.split('-')
            u=int(u)-1
            l=int(l)-1
            c=c[0]
            if p[u]==c or p[l]==c:
                valid+=1
            if p[u]==c and p[l]==c:
                valid-=1

    print(valid)

#part_one()
part_two()


