import numpy as np
infile='input/day11.1.txt'
occupancy=5

def full_or_empty(matrix, i, j):
    region = matrix[max(0, i-1) : i+2,
                    max(0, j-1) : j+2]
    seatsful=np.sum(region) - matrix[i, j] 
    rv=matrix[i,j]
    if seatsful >= occupancy:
        rv=0
    elif seatsful==0:
        rv=1
    return(rv)
    
def update_occupancy(m):
    o=np.zeros_like(m)
    for x in range(0, m.shape[0]):
        for y in range(0, m.shape[1]):
            o[x,y]=full_or_empty(m,x,y)
    return(o)


def is_seat_or_empty(m,s,i,j,r,d):
    x=i+r
    y=j+d
    w,h=np.shape(m)    
    
    empty=True
    isseat=False
    while x >=0 and y>=0 and x<w and y<h:
    
        if m[x,y]==1:
            empty=False
            break
        if s[x,y]==1:
            isseat=True
            break
        x+=r
        y+=d
        
    if empty:
        if x <0 or y<0 or x>=w or y>=h:
            isseat=True
    #print(f"{isseat} {empty}: {r} {d} {i} {j}")
    if (isseat):
        return(1)
    else:
        return(0)
 
def full_or_empty_2(m, s, i, j):
    seats=0
    rv=m[i,j]
    seats+=is_seat_or_empty(m,s,i,j,-1,0)
    seats+=is_seat_or_empty(m,s,i,j,1,0)
    seats+=is_seat_or_empty(m,s,i,j,0,-1)
    seats+=is_seat_or_empty(m,s,i,j,0,1)
    seats+=is_seat_or_empty(m,s,i,j,-1,1)
    seats+=is_seat_or_empty(m,s,i,j,1,-1)
    seats+=is_seat_or_empty(m,s,i,j,-1,-1)
    seats+=is_seat_or_empty(m,s,i,j,1,1)
    #print (m+s)
    #print(f"{i} {j} can see {seats} empty")
    if 8-seats == 0:
        rv=1
    elif 8-seats >= occupancy:
        rv=0
    return(rv)
    
def update_occupancy_2(m,s):
    o=np.zeros_like(m)
    for x in range(0, m.shape[0]):
        for y in range(0, m.shape[1]):
            o[x,y]=full_or_empty_2(m,s,x,y)
    return(o)

def part_one():
    maxs=0
    indata=[]
    seats=[]
    with open(infile) as fp:
        # treat floor (.) as 0 for logic - they can
        # only ever be empty
        # have separate array of 0s which represent
        # floor 

        for line in fp:
            o=list(line.strip())
            print (o)
            f=[1]*len(o)
            for n,c in enumerate(o):
                if c=='.':
                    f[n]=0
            seats.append(f)

    s=np.array(seats)
    d=np.zeros_like((s))
    o=update_occupancy(d)*s
    changed=np.sum(d-o)
    d=o
    count=1
    while (changed!=0):
        o=update_occupancy(d)*s
        changed=np.sum(d-o)
        d=o
        count+=1
        print(f"Round: {count}, changed: {changed}")
    print(f"{np.sum(d)} seats are occupied")
     

def part_two():
    maxs=0
    indata=[]
    seats=[]
    with open(infile) as fp:
        # treat floor (.) as 0 for logic - they can
        # only ever be empty
        # have separate array of 0s which represent
        # floor 

        for line in fp:
            o=list(line.strip())
            print (o)
            f=[1]*len(o)
            for n,c in enumerate(o):
                if c=='.':
                    f[n]=0
            seats.append(f)

    s=np.array(seats)
    d=np.zeros_like(s)
    
    o=update_occupancy_2(d,s)*s
    changed=np.sum(d-o)
    d=o.copy()
    count=0
    #for p in range(2):
    while (changed!=0):
        o=update_occupancy_2(d,s)*s
        changed=np.sum(d-o)
        d=o.copy()
        count+=1
        print(f"Round: {count}, changed: {changed}")
        print(f"{np.sum(d)} seats are occupied")
     
#    while (changed!=0):



part_two()
