infile='input/day20.1.txt'
import numpy as np
from collections import defaultdict

def parse_data():
    tiles={}
    with open(infile) as fp:
        ins=[]
        name=''
        for line in fp:
            lo=line.strip()
            if  len(lo)<=1:
                tiles[name]=np.array(ins)
                ins.clear()
            elif (lo[0]=='T'):
                l=lo.split(' ') 
                name=l[1]
                name=name[:-1]
            else :
                l=[0]*len(lo)
                for n,i in enumerate(lo):
                    if i=='#':
                        l[n]=1
                ins.append(l)
        tiles[name]=np.array(ins)
        ins.clear()
    return(tiles)

def test_sides(t1,t2,i1,i2):
    s1=get_side(t1,i1)
    s2=get_side(t2,i2)
    rv=False
    if (s1==s2).all():
        rv=True
    elif (s1==(s2[::-1])).all():
        rv=True
    return(rv)

def get_side(t,i):
    if (i==0):
        return(t[0,:])
    if (i==1):
        return(t[-1,:])
    if (i==2):
        return(t[:,0])
    if (i==3):
        return(t[:,-1])
    # 0=top, 1=bottom, 2=left, 3=right

def part_one():
    tiles=parse_data()
    tilesleft=tiles.copy()
    matched=defaultdict(list)
    todelete=[]
    sidesums={}
    for i,t in tiles.items():
        st=np.sum(t[0,:]) #sumtop
        sb=np.sum(t[-1,:]) #sumbottom
        sl=np.sum(t[:,0]) #sumleft
        sr=np.sum(t[:,-1]) #sumright
        sidesums[i]=[st,sb,sl,sr]
    for i,t in tiles.items():
        for j,t2 in tilesleft.items():
            if j==i:
                continue
            for ctr,s in enumerate(sidesums[i]):
                for ctr2,s2 in enumerate(sidesums[j]):
                    if (s==s2):
                        if test_sides(t,t2,ctr,ctr2):
                            print(f"found a matching side: {i} {j} {ctr} {ctr2}")
                            if i not in matched[j]:
                                matched[i].append(j)
                                matched[j].append(i)
                                if len(matched[j]) == 4:
                                    todelete.append(j)
                                if len(matched[i]) == 4:
                                    todelete.append(i)
        for todel in todelete:
            del tilesleft[todel]
        todelete.clear()
        print(f"we have {len(tilesleft)} tiles left")
    prod=1
    for tile,ids in matched.items():
        print(tile,ids,end="")
        if len(ids)==2:
            prod*=int(tile)
            print("corner")
        print("")
    print(prod)




part_one()
