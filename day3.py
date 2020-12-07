
def part_one():
    trees=0
    row=0
    with open('input/day3.1.txt') as fp:
        for line in fp:
            l=len(line.strip())
            lo=list(line)
            index=(3*row)%l
            if line[index]=='#':
                trees+=1
                lo[index]='X'
            else: 
                lo[index]='0'
            row+=1
            print(lo)

    print(trees)

def part_two():
    treelist=[];
    slopes=[(1,1),(3,1),(5,1),(7,1),(1,2)]
    for slope in slopes:
        lines=0
        trees=0
        row=0
        with open('input/day3.1.txt') as fp:
            for line in fp:
                if lines%slope[1]==0:
                    l=len(line.strip())
                    index=(slope[0]*row)%l
                    if line[index]=='#':
                        trees+=1
                    row+=1
                lines+=1
        treelist.append(trees)
    print(treelist)
    res=1
    for num in treelist:
        res=res*num
    print(res)


part_two()


