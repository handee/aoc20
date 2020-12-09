import re
from collections import deque

#target_official=25918798
infile='input/day9.1.txt'
window=25

def is_valid(q,t):
    r=False
    for i,n in enumerate(q):
        for j in range(i+1,len(q)):
            #print(f"is {t} equal to {n}+{q[j]}?",end="")
            if t == n+q[j]:
            #    print("...yes")
                r=True
            #else:
            #    print(" no")
    return(r)

def part_one():
    preamble=deque()
    with open(infile) as fp:
        for line in fp:
            n=int(line.strip())
            if len(preamble)==window:
                if is_valid(preamble,n):
                    preamble.popleft()
                    preamble.append(n)
                else: 
                    print(f"The problem is {n}")
                    break
            else:
                preamble.append(n)
            print(preamble)


def find_sum_to_bug(l,b):
    ret=0
    for n,c in enumerate(l):
        tot=c
        mini=c
        maxi=c
        for i in range(n+1,len(l)):
            if (l[i]<mini):
                mini=l[i]
            elif (l[i]>maxi):
                maxi=l[i]
            tot+=l[i]
            if tot==b:
                print(f"sums to {b} {mini}+{maxi} == {mini+maxi}")
                ret=(c+l[i])
                break
            elif tot>b:
                continue
    return(ret)

def part_two():
    bug=0
    preamble=deque()
    prog=[]
    with open(infile) as fp:
        for line in fp:
            n=int(line.strip())
            prog.append(n)
            if len(preamble)==window:
                if is_valid(preamble,n):
                    preamble.popleft()
                    preamble.append(n)
                else: 
                    bug=n
                    break
            else:
                preamble.append(n)
    print(f"Found a bug, {bug}, now let's find the sum")
    find_sum_to_bug(prog,bug)

#part_one()
part_two()


