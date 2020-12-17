infile = 'input/day17.1.txt'
rounds=6
import numpy as np

def parse_data():
    ins=[]
    with open(infile) as fp:
        for line in fp:
            lo=list(line.strip())
            l=[0]*len(lo)
            for n,i in enumerate(lo):
                if i=='#':
                    l[n]=1
            ins.append(l)
    return(ins)

def run_generation4d(a):
    a=np.pad(a,2,mode='constant')
    
    sumarray=np.zeros_like(a)
    cube=np.zeros_like(sumarray)

    for i in range(1,a.shape[0]):
        for j in range(1,a.shape[1]):
            for k in range(1,a.shape[2]):
                for m in range(1,a.shape[3]):
                    sumarray[i,j,k,m]=np.sum(a[i-1:i+2,j-1:j+2,k-1:k+2,m-1:m+2])
                    if a[i,j,k,m]==1:
                        sumarray[i,j,k,m]-=1
                        if 2<=sumarray[i,j,k,m]<=3 :
                            cube[i,j,k,m]=1
                    elif sumarray[i,j,k,m]==3 :
                            cube[i,j,k,m]=1

    return(cube.copy())


def run_generation(a):
    a=np.pad(a,2,mode='constant')
    
    sumarray=np.zeros_like(a)
    cube=np.zeros_like(sumarray)

    for i in range(1,a.shape[0]):
        for j in range(1,a.shape[1]):
            for k in range(1,a.shape[2]):
                sumarray[i,j,k]=np.sum(a[i-1:i+2,j-1:j+2,k-1:k+2])
                if a[i,j,k]==1:
                    sumarray[i,j,k]-=1
                    if 2<=sumarray[i,j,k]<=3 :
                        cube[i,j,k]=1
                elif sumarray[i,j,k]==3 :
                        cube[i,j,k]=1

    return(cube.copy())



def part_one():
    ins=parse_data()
    print(ins)
    a=np.array([ins])
    for r in range(rounds):
        a=run_generation(a)
        print(np.sum(a))
    print(np.sum(a))


def part_two():
    ins=parse_data()
    print(ins)
    a=np.array([[ins]])
    for r in range(rounds):
        a=run_generation4d(a)
        print(np.sum(a))
    print(np.sum(a))



#part_one()
part_two()


