infile = 'input/day15.1.txt'

def parse_data():
    with open(infile) as fp:
        b=fp.readline().strip().split(',')
        v=[int(i) for i in b]
    return(v)
 

def part_one():
    v=parse_data()
    lastseen={}
    last=0
    for i,n in enumerate(v):
        lastseen[n]=i+1
        last=n
    target = 30000000
    del lastseen[last]
    ncount=len(lastseen)+1
    #now last is the last number, and lastseen is the time all the numbers
    #before (but not including) that number have been seen
    while ncount<=target:
        if last in lastseen:
            new=ncount-lastseen[last]
        else:
            new=0

        lastseen[last]=ncount
        oldlast=last
        last=new
        ncount+=1
    print(f"{ncount-1} {oldlast}")



part_one()
#part_two()


