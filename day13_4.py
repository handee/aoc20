infile = 'input/day13.1.txt'

def parse_data():
    with open(infile) as fp:
        r=int(fp.readline().strip())
        b=fp.readline().strip().split(',')
        v=[int(i) for i in b if i != 'x']
    return(r,v)
 
def parse_data2():
    d=[]
    r=[]
    with open(infile) as fp:
        fp.readline() # chuck first line
        b=fp.readline().strip().split(',')
        for n,i in enumerate(b):
            if i != 'x':
                d.append(int(i)) 
                r.append(int(i)-n)
                while r[-1]<=0:
                    r[-1]+=int(i)
    print(len(d))
    return(d,r)
 

def part_one():
    r,v=parse_data()
    print (r,v)
    earliest=max(v)+r
    for i in v:
        nexti=(r - (r%i)) +i 
        if nexti < earliest:
            earliest=nexti
            fastestbus=i
        print (f"The next number {i} will be at {nexti} " )
    minuteswait=earliest-r
    print(f"You have {minuteswait} wait for the {fastestbus}");
    print(f"The answer is {minuteswait*fastestbus} wait");
    

def find_next_bus(start,n1):
    i1=n1 + (start//n1 * n1)
    return(i1)

def mmi(a,m):
    # Returns modulo inverse of a with respect to m using extended 
 # Euclid Algorithm. Refer below post for details: 
 # https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/ 
    m0 = m 
    x0 = 0 
    x1 = 1 
    if m == 1:
       return(0) 
  
    # Apply extended Euclid Algorithm 
    while a > 1:
        # q is quotient 
        q = a // m 
        t = m 
  
        # m is remainder now, process same as 
        # euclid's algorithm 
        m = a % m 
        a = t
        t = x0
  
        x0 = x1 - q * x0 
  
        x1 = t
  
    # Make x1 positive 
    if (x1 < 0) :
       x1 += m0 
    return(x1)
  

def part_two():
    d,r=parse_data2()
    print (d, r)
    prod=1
    pp=[]
    invs=[]
    time=0
    for bus in d:
        prod*=bus
    for i,bus in enumerate(d):
        print(bus)
        pp.append(prod//bus)
        invs.append(mmi(pp[-1],bus))
        time+=(r[i]*pp[-1]*invs[-1])
    print(prod,pp,invs) 
    print(time)
    print(time%prod)

    for i,bus in enumerate(d):
        print(bus,time%bus-bus,r[i],r[i]-bus)



#part_one()
part_two()


