import re
from collections import defaultdict

def trace_execution(prog):
    inf=False
    cur=0
    acc=0
    state=[0]*len(prog)
    while not inf:
        state[cur]+=1
        if state[cur]>1:
            inf=True
            break
        if prog[cur][0] =='nop' :
            cur+=1
        elif prog[cur][0]=='acc':
            acc+=prog[cur][1]
            cur+=1
        elif prog[cur][0]=='jmp':
            cur=cur+prog[cur][1]

    return(acc)


def part_one():
    prog=[]
    with open('input/day8.1.txt') as fp:
        for line in fp:
            instruction,number=line.split()
            prog.append((instruction,int(number)));
    print(prog)
    a=trace_execution(prog)
    print(a)

def trace_execution_and_fix(prog,nj):
    inf=False
    cur=0
    acc=0
    numj=0
    state=[0]*len(prog)
    stat=False
    while not inf:
        print(f"Current= {cur}, numj= {numj}, nj so far= {nj}")
        if cur>=len(prog):
            print("success!")
            stat=True
            break

        state[cur]+=1
        print(state)
        if state[cur]>1:
            print("infinite loop, try again")
            inf=True
            nj+=1
            break
        if prog[cur][0] =='nop' :
            if (numj==nj):
                #try flipping this one to be a jump
                cur+=prog[cur][1]
            else: 
                #treat it like a nop
                cur+=1
            numj+=1
        elif prog[cur][0]=='jmp':
            if (numj==nj):
                #try flipping this one to be a nop 
                cur+=1
            else: 
                #treat it like a jump 
                cur+=prog[cur][1]
            numj+=1
        elif prog[cur][0]=='acc':
            acc+=prog[cur][1]
            cur+=1
    
    return(acc,nj,stat)


def part_two():
    prog=[]
    c_nop=0
    c_jmp=0
    with open('input/day8.1.txt') as fp:
        for line in fp:
            instruction,number=line.split()
            prog.append((instruction,int(number)))
            if instruction=='nop':
                c_nop+=1
            if instruction=='jmp':
                c_jmp+=1
    print(c_nop, c_jmp)
    stat=0
    nj=0
    while stat==0: 
       a,nj,stat=trace_execution_and_fix(prog,nj)
    print(a)


#part_one()
part_two()


