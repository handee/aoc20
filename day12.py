infile = 'input/day12.1.txt'
import numpy as np

def rotate(way,d):
    if (d[0]=='R') :
        d[1]=-d[1]
    print(f"Rotating {way} counterclockwise by {d}")
    rads=np.radians(d[1])
    r=np.array([[np.cos(rads),-np.sin(rads)],[np.sin(rads),np.cos(rads)]])
    m=np.dot(r,way)
    m=np.rint(m)
    return ([m.T[0],m.T[1]])

def move_towards_waypoint(way,loc,d):
    print(f"moving {loc} towards {way} by {d}")
    dx=way[0]-loc[0]
    dy=way[1]-loc[1]
    loc[0]+=d[1]*dx
    loc[1]+=d[1]*dy
    way=[loc[0]+dx,loc[1]+dy]
    return(way,loc)


def turn90(lr,d):
    if lr=='R': 
        print(f"Turning 90 Right from {d['F']}")
        if d['F']==[0,1]: #n->e
            d['F']=[1,0]
        elif d['F']==[1,0]: #e->s
            d['F']=[0,-1]
        elif d['F']==[0,-1]: #s->w
            d['F']=[-1,0]
        else :
            d['F']=[0,1] #w->n
    else:
        print(f"Turning 90 Left from {d['F']}")
        if d['F']==[0,1]: #n->w
            d['F']=[-1,0]
        elif d['F']==[1,0]: #e->n
            d['F']=[0,1]
        elif d['F']==[0,-1]: #s->e
            d['F']=[1,0]
        else :
            d['F']=[0,-1] #w->s

    return(d)

def part_one():
    ins=[]
    with open(infile) as fp:
        for line in fp:
            r=line[0]
            c=int(line[1:])
            ins.append([r,c])
    loc=[0,0]
    # cardinal directions + F for current direction
    dirs={'N':[0,1],'E':[1,0],'S':[0,-1],'W':[-1,0],'F':[1,0]}
    for i in ins:
        print(f'Instruction: {i[0]}, Distance: {i[1]}')
        if i[0]=='L' or i[0]=='R':
            n=int(i[1]/90)
            for j in range(n):
                turn90(i[0],dirs)
        else:
            print(dirs[i[0]],' ',i[1]*dirs[i[0]][0],' ',i[1]*dirs[i[0]][1])
            loc[0]+=i[1]*dirs[i[0]][0]
            loc[1]+=i[1]*dirs[i[0]][1]
            print(f"now at loc {loc}")

    print(loc)
    print(abs(loc[0])+abs(loc[1]))


def part_two():
    ins=[]
    with open(infile) as fp:
        for line in fp:
            r=line[0]
            c=int(line[1:])
            ins.append([r,c])
    loc=[0,0]
    way=[10,1]
    # cardinal directions for current direction
    dirs={'N':[0,1],'E':[1,0],'S':[0,-1],'W':[-1,0]}
    for i in ins:
        print(f'Instruction: {i[0]}, Distance: {i[1]}')
        if i[0]=='L' or i[0]=='R':
            # work out waypoint relative to ship
            rel_way=[way[0]-loc[0],way[1]-loc[1]]
            # rotate waypoint relative to ship
            new_rel_way=rotate(rel_way,i)
            # transform back to world coords
            way=[new_rel_way[0]+loc[0],new_rel_way[1]+loc[1]]
        elif i[0]=='F':
            way,loc=move_towards_waypoint(way, loc, i)
        else:
            way[0]+=i[1]*dirs[i[0]][0]
            way[1]+=i[1]*dirs[i[0]][1]
        print(f"now at loc {loc} way {way}")

    print(loc)
    print(abs(loc[0])+abs(loc[1]))

#part_one()
part_two()


