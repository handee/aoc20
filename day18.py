infile = 'input/day18.1.txt'
rounds=6
import numpy as np

def parse_data():
    ins=[]
    with open(infile) as fp:
        for line in fp:
            lo=list(line.strip())
            lo=[x for x in lo if x!=' ']
            ins.append(lo)
    return(ins)

def find_a_set_of_brackets_and_do_the_sum(s):
    rbracket_count=0
    lbracketloc=0
    rbracketloc=0
    i=0
    while rbracket_count == 0:
        if s[i]=='(':
            lbracketloc=i
        if s[i]==')':
            rbracket_count+=1
            rbracketloc=i
        i+=1
    sumbrac=do_sum(s[lbracketloc+1:rbracketloc])
    del s[lbracketloc+1:rbracketloc+1]
    s[lbracketloc]=sumbrac
    return(s)

def find_some_addition_and_do_the_sum(s):
    plusloc=0
    i=0
    while plusloc == 0:
        if s[i]=='+':
            plusloc=i
        i+=1
    sumplus=int(s[plusloc-1])+int(s[plusloc+1])
    del s[plusloc-1:plusloc+1]
    s[plusloc-1]=sumplus
    return(s)



def do_sum(s):
    # takes a sum with no brackets and returns the output
    t=int(s[0])
    i=1
    while i+1 < len(s):
        if s[i]=='*':
            i+=1
            t*=int(s[i])
            i+=1
        elif s[i]=='+':
            i+=1
            t+=int(s[i])
            i+=1
    return (t)

def find_a_set_of_brackets_and_do_the_sum_p2(s):
    rbracket_count=0
    lbracketloc=0
    rbracketloc=0
    i=0
    while rbracket_count == 0:
        if s[i]=='(':
            lbracketloc=i
        if s[i]==')':
            rbracket_count+=1
            rbracketloc=i
        i+=1
    sum_to_do=s[lbracketloc+1:rbracketloc]
    while '+' in sum_to_do:
        sum_to_do=find_some_addition_and_do_the_sum(sum_to_do)
    sumbrac=do_mult(sum_to_do)
    del s[lbracketloc+1:rbracketloc+1]
    s[lbracketloc]=sumbrac
    return(s)


def do_mult(s):
    # takes a sum with no brackets and returns the output
    t=int(s[0])
    i=1
    while i+1 < len(s):
        if s[i]=='*':
            i+=1
        t*=int(s[i])
        i+=1
    return (t)



def part_one():
    inp=parse_data()
    total=0
    for i in inp:
        while '(' in i:
            i=find_a_set_of_brackets_and_do_the_sum(i)
        out=do_sum(i)
        print(f"Total+= {out}")
        total+=out
    print(f"Final total = {total}")

def part_two():
    inp=parse_data()
    total=0
    for i in inp:
        print(i)
        while '(' in i:
            i=find_a_set_of_brackets_and_do_the_sum_p2(i)
        while '+' in i:
            i=find_some_addition_and_do_the_sum(i)
        print(i)
        out=do_mult(i)
        print(f"Total+= {out}")
        total+=out
    print(f"Final total = {total}")







#part_one()
part_two()


