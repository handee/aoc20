import re
from collections import defaultdict

def trace_tree(lo,icb,tar):
    if tar not in icb:
        return(lo)
    else:
        newtargets=icb[tar]
        lo.update(newtargets)
        for tars in newtargets:
            trace_tree(lo,icb,tars)



def part_one():
    total=0
    is_contained_by=defaultdict(list)
    target='shiny gold bag'
    with open('input/day7.1.txt') as fp:
        for line in fp:
            colours=re.findall('\w+ \w+ bag',line) 
            numbers=re.findall('\d+',line) 
            for colour in colours[1:]:
                is_contained_by[colour].append(colours[0])
    print(is_contained_by)
    set_output=set()
    trace_tree(set_output,is_contained_by,target)
    print(set_output)
    print(len(set_output))

def trace_tree_down(tots,lo,c,tar):
    newtargets=c[tar[0]]
    lo.append(newtargets)
    mult=tots[-1] # multiplier is the total on the prev level
    for tars in newtargets:
        tots.append(tars[1]*mult)
        tots[0]+=tars[1]*mult
        trace_tree_down(tots,lo,c,tars)


def part_two():
    contains={}
    is_contained_by=defaultdict(list)
    target='shiny gold bag'
    with open('input/day7.1.txt') as fp:
        for line in fp:
            colours=re.findall('\w+ \w+ bag',line) 
            numbers=re.findall('\d+',line) 
            clist=[]
            for n,colour in enumerate(colours[1:]):
                is_contained_by[colour].append(colours[0])
                if not colour=="no other bag":
                    clist.append((colour, int(numbers[n])))
            contains[colours[0]]=clist
    l=[]
    totes=[1]
    trace_tree_down(totes,l,contains,(target,1))
    totes[0]-=1
    print(totes)
#part_one()

part_two()


