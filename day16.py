infile = 'input/day16.1.txt'
import re

def parse_data():
    regs={}
    tix=[]
    ticket=[]
    phase=0
    with open(infile) as fp:
        for line in fp:
            if len(line)==1:
                phase+=1
            elif phase==0:
                s,p,t=line.partition(':')
                p1,p2=t.strip().split(' or ')
                mi,ma=p1.split('-')
                r1=[int(mi),int(ma)]
                mi,ma=p2.split('-')
                r2=[int(mi),int(ma)]
                regs[s]=[r1,r2]
            elif phase==1:
                if line[0]=='y':
                    print("your ticket")
                else:
                    t=line.strip().split(',')
                    ticket=[int(i) for i in t]
            elif phase==2:
                if line[0]=='n':
                    print("nearby ticket")
                else:
                    t=line.strip().split(',')
                    t=[int(i) for i in t]
                    tix.append(t)

    return(regs,ticket,tix)
 

def part_one():
    regs,ticket,tix=parse_data()
    print(f"my ticket: {ticket}")
    print(f"the regs:")
    print(regs)
    invalid=[]
    for t in tix:
        for i in t:
            v=0
            print(f"checking {i}")
            for k,reg in regs.items():
                if (i <= reg[0][1] and i >= reg[0][0]) or \
                        (i <= reg[1][1] and i >= reg[1][0]):
                       v+=1
            print(f"this matches {v} out of {len(regs)} regs")
            if v==0:
                invalid.append(i)
    sumi=0
    for i in invalid :
        print(i)
        sumi+=i
    print(f"The sum of the invalid values is {sumi}")


def part_two():
    regs,ticket,tix=parse_data()
    invalid=[]
    poss={}
    allregs=[]
    for reg in regs:
        allregs.append(reg)
    for i,t in enumerate(ticket):
        poss[i]=allregs.copy()


    for t in tix:
        valid=True
        for i in t:
            v=0
            for k,reg in regs.items():
                if (i <= reg[0][1] and i >= reg[0][0]) or \
                        (i <= reg[1][1] and i >= reg[1][0]):
                       v+=1
            if v==0:
                invalid.append(i)
                valid=False
        if (valid) :
            for slot,i in enumerate(t):
                for k,reg in regs.items():
                    if not ((i <= reg[0][1] and i >= reg[0][0]) or \
                            (i <= reg[1][1] and i >= reg[1][0])):
                        # this slot can't contain this reg
                        if k in poss[slot]: 
                            poss[slot].remove(k)

    definites={} 
    while len(definites)<len(poss):
        for k,v in poss.items():
            if len(v)==1: # there's only one here
                definites[k]=v[0]
                for j,o in poss.items():
                    if definites[k] in poss[j]:
                        poss[j].remove(definites[k])
    print("now the definites are...")

    print(definites)
    ans=1
    for k,t in definites.items():
        if t[0]=='d' and t[1]=='e':
            print(f"{t} = {ticket[k]}")
            ans=ans*ticket[k]

    print(f"The ansswer is {ans}")



#part_one()
part_two()


