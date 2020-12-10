infile='input/day10.test1.txt'

def part_one():
    with open(infile) as fp:
        jolts = [int(line.strip()) for line in fp]
    jolts.sort()
    jolts.insert(0,0) # add the starting voltage of the outlet
    ones=0
    threes=0
    for n,j in enumerate(jolts):
        if n+1>=len(jolts):
        # we're at the end
            threes+=1
            break
        elif jolts[n+1]-j == 1:
            ones+=1
        elif jolts[n+1]-j == 3:
            threes+=1
    print(f"{ones} is ones, {threes} is threes, {ones*threes} is the answer")


def is_valid(chargers):
    rv=True
    for n,j in enumerate(chargers):
        if n+1>=len(chargers):
            break
        if chargers[n+1]-j > 3 :
            print(chargers[n+1])
            print(j)
            rv=False
            break
    print(f"{chargers} is {rv}")
    return(rv)



def part_two_brute():
    cases=[]
    with open(infile) as fp:
        jolts = [int(line.strip()) for line in fp]
    jolts.sort()
    cases.append(jolts)
    stubs=[]
    stubs.append([0])
    for n,j in enumerate(jolts):
        #if n+1>=len(jolts):
        # we're at the end
        #    break
        x=len(stubs)
        for i in range(x):
            stub=stubs[i].copy()
            if j-stub[-1] <= 3:
                stub.append(j)
                stubs.append(stub)
        for m,stub in enumerate(stubs):
            if j-stub[-1] >=4:
               stubs.pop(m)
        x=len(stubs)
        print(j,n,x)
    ok=[]
    for stub in stubs:
        if (stub[-1]==jolts[-1]):
            #print(f"this is ook: {stub}")
            ok.append(stub)
        #else:
        #    print(f"this is not long enough: {stub}")
    print(len(ok))


def break_into_sublists(jolts,fragments):
    rot=True
    n=0
    frag=[]
    while n+1<len(jolts):
        j=jolts[n]
        if jolts[n+1]-j ==3 :
            if not rot:
                frag.append(j)
                fragments.append(frag.copy())
                frag.clear()
                rot=True
            else:
                frag.append(j)
            n+=1
        else:
            rot=False
            frag.append(j)
            n+=1
    frag.append(jolts[-1])
    fragments.append(frag.copy())

def calculate_orders(sublist):
    stubs=[]
    stub=[]
    stubs.append([sublist[0]])
    n=1
    while n < len(sublist):
         #if n+1>=len(jolts):
        # we're at the end
        #    break
        x=len(stubs)
        j=sublist[n]
        for i in range(x):
            stub=stubs[i].copy()
            if j-stub[-1] <= 3:
                stub.append(j)
                stubs.append(stub)
        for m,stub in enumerate(stubs):
            if j-stub[-1] >=4:
                stubs.pop(m)
        n+=1
    ok=[]
    print("these should be ok")
    for stub in stubs:
        if (stub[-1]==sublist[-1]):
            #print(f"this is ook: {stub}")
            ok.append(stub)
            print(stub)
        #else:
        #    print(f"this is not long enough: {stub}")
    return(len(ok))


def part_two():
    with open(infile) as fp:
        jolts = [int(line.strip()) for line in fp]
    jolts.sort()
    jolts.insert(0,0) # add the starting voltage of the outlet
    fragments=[]
    break_into_sublists(jolts,fragments)
                            
     
    total=1
    for frag in fragments: 
        print(frag)
        frag_perms=calculate_orders(frag)
        print(frag_perms)
        total=total*frag_perms
    print(total)
    



#part_one()
part_two()


