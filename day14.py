infile = 'input/day14.1.txt'

def parse_data():
    ins=[]
    with open(infile) as fp:
        for line in fp:
            r=line.strip().split(' = ')
            if (r[0][1]=='e'): #it's a mem
                m=int(r[0].strip(']').split('[')[1])
                print(m)
                n=int(r[1])
                ins.append([m,n])
            else: # it's a mask
                ins.append(['m',r[1]])
        print(ins[-1])
    return(ins)
 
def write_data_to_memory(bitmask,num):
    print(bitmask)
    print(bin(num))
    #for i in range(len(bitmask)-1,-1,-1):
    for i in range(0,len(bitmask)):
        if bitmask[i]=='1':
            num=num | (1<<(len(bitmask)-i-1))
            print(f"Changed{i}, now {bin(num)}")
        elif bitmask[i]=='0':
            num=num & ~(1<<(len(bitmask)-i-1))
            print(f"Changed{i}, now {bin(num)}")
    print(f"done, num now: {bin(num)}")
    return(num)
 
def find_memory_addresses(bitmask,num):
    print(bitmask)
    print(bin(num))
    adds=[]
    #for i in range(len(bitmask)-1,-1,-1):
    for i in range(0,len(bitmask)):
        if bitmask[i]=='1':
            num=num | (1<<(len(bitmask)-i-1))
        #elif bitmask[i]=='0':
            #num=num & ~(1<<(len(bitmask)-i-1))
    print(f"initial phase done, num now: {bin(num)}")
    i=0
    adds.append(binary_fork(num,bitmask,adds,i))
    print(adds) 
    return(adds)

def binary_fork(num,bitmask,adds,j): 
    if j < len(bitmask):
        if bitmask[j]=='X':
            num1=num | (1<<(len(bitmask)-j-1))
            binary_fork(num1,bitmask,adds,j+1) 
            num0=num & ~(1<<(len(bitmask)-j-1))
            binary_fork(num0,bitmask,adds,j+1)
        else:
            binary_fork(num,bitmask,adds,j+1)
    else: 
        adds.append(num)
        return(adds)


def part_one():
    ins=parse_data()
    print(ins)
    bitmask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    mem={} # memory contents
    for i in ins:
        if i[0]=='m':
            bitmask=i[1]
        else:
            mem[i[0]]=write_data_to_memory(bitmask,i[1])
    print(mem)
    tot=0
    for item in mem:
        tot+=mem[item]
    print(tot)


def part_two():
    ins=parse_data()
    bitmask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    mem={} # memory contents
    for i in ins:
        if i[0]=='m':
            bitmask=i[1]
        else:
            adds=find_memory_addresses(bitmask,i[0])
            for a in adds:
                if a:
                    mem[a]=i[1]
    print(mem)
    tot=0
    for item in mem:
        tot+=mem[item]
    print(tot)




#part_one()
part_two()


