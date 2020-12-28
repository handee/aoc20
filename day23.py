import cProfile
testcups='389125467'
mycups = '467528193'
iterations=10


def cut_n_from_circle(circ,n,location):
    if (location+n)<len(circ):
        clip=circ[location+1:location+n+1]
        rest=circ[:location+1]+circ[location+n+1:]
    elif (location+1==len(circ)):
        clip=circ[0:n]
        rest=circ[n:]
    else:
        endpart=circ[location+1:]
        firstpart=circ[0:n-len(endpart)]
        clip=endpart+firstpart
        rest=circ[n-len(endpart):location+1]
    return(clip,rest)


def insert_n_into_circle(circ,piece,location,i):
    if location<i:
        #print(f"needs to be inserted at {location} - before {i} - so need to shuffle")
        if location==len(circ):
            result=circ+piece
        elif (location==0):
            result=[circ[0]]+piece+circ[1:]
        else:
            result=circ[0:location+1]+piece+circ[location+1:]
        shift=min(3,len(circ)-i-1+3)
        
        #print(f"shifting by {shift} lencircminusi ={len(circ)-i}")
        circ=result[shift:]+result[0:shift]
    elif location==len(circ):
        circ=circ+piece
    else:
        circ=circ[0:location+1]+piece+circ[location+1:]
    return(circ)

def find_location(circ,clip,val):
    if val==min(circ):
        p=circ.index(max(circ))
    elif val-1 in clip:
        mindiff=val-1
        loc=0
        for i,v in enumerate(clip):
            if v<val:
                diff=val-v
                if diff<mindiff:
                    mindiff=diff
                    loc=i
        p=loc

    else:
        p=circ.index(val-1)
    return(p)

def find_locationinplace(val,clip,cups):
    if val==1:
        p=cups.index(max(cups))
    elif val-1 in clip:
        print(f"{val-1} is in the {clip}")
        nextlowest=val-2
        if nextlowest==0:
            nextlowest=max(cups)
        print(f"{nextlowest} is next lowest")
        while nextlowest in clip:
            print(f"{nextlowest} is in the {clip}")
            nextlowest-=1
            if nextlowest==0:
                nextlowest=max(cups)
        if nextlowest==0:
            nextlowest=max(cups)

        p=cups.index(nextlowest)

    else:
        p=cups.index(val-1)
    return(p)


def do_round(cups,i):
    print(f"{i}, {cups}")
    clip,rest=cut_n_from_circle(cups,3,i)
    print(f"i={i} cups[i]={cups[i]} clip={clip} rest={rest} ")
    place=find_location(rest,clip,cups[i])
    return(cups)



def do_round_inplace(cups):
    print (cups)
    cup=cups.pop(0)
    clip=cups[0:3]
    #del cups[0:3]
    print(clip)
    place=find_locationinplace(cup,clip,cups)
    print(f"cup={cup} copying forward in {cups} from {place}")
    print(f"are we near the end? {len(cups)-place}")
    end=[]
    if len(cups)-place<=3:
        end=cups[place+1:]
    cups[0:place+1]=cups[3:place+4]
    print(f"cups now {cups}")
    cups[place-2:place+1]=clip
    print(f"overwriting clip {clip} cups now {cups}")
    cups+=end
    print(f"cups now {cups} (added {end})")
    cups.append(cup)
    print (cups)
    return(cups)


def part_one():
    cupslist=[int(i) for i in list(testcups)]
    curr=0
    for j in range(iterations) :
       cupslist=do_round_inplace(cupslist)
    print(cupslist)
    oneloc=cupslist.index(1)
    l=cupslist[oneloc+1:]+cupslist[0:oneloc]
    s=map(str,l)
    print(''.join(s))
    

def part_two():
    cupslist=[int(i) for i in list(testcups)]
    rest=[i for i in range(len(cupslist)+1,1000001)]
    cupslist=cupslist+rest
    curr=0
    for j in range(iterations) :
       cupslist=do_round_inplace(cupslist)
    #print(cupslist)
    oneloc=cupslist.index(1)
    if oneloc+1<=len(cupslist):
        nextloc=oneloc+1
    else:
        nextloc=0
    if nextloc+1<=len(cupslist):
        nextnextloc=nextloc+1
    else:
        nextnextloc=0
    nexti=cupslist[nextloc]
    nextnexti=cupslist[nextnextloc]
    print(nexti,' ',nextnexti,"ans=",nextnexti*nexti)
 
#part_one()
cProfile.runctx('part_one()',globals(),locals())
