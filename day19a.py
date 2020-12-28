infile = 'input/day19.test2.txt'
import os 

headers=["import json", "from pyleri import Choice", "from pyleri import Grammar", "from pyleri import Keyword", "from pyleri import Sequence", "\n", "class MyGrammar(Grammar):"]

def write_out_rule(rn,rbody):
    if (rn=='r0'):
        rn='START'
    if len(rbody)==1:
        if rbody[0]=='a' or rbody[0]=='b':
            s="    "+rn+"=Keyword(\'"+rbody[0]+"\')"
        else:
            s="    "+rn+"=Sequence(r"+rbody[0]+")"
    elif "|" in rbody:
        s="    "+rn+"=Choice("
        if len(rbody)==3:
            s+='r'+rbody[0]+', r'+rbody[2]
        if len(rbody)==4:
            s+='r'+rbody[0]+', Sequence(r'+rbody[2]+', r'+rbody[3]+')'
        elif len(rbody)==5:
            s+='Sequence(r'+rbody[0]+', r'+rbody[1]+')'
            s+=','
            s+='Sequence(r'+rbody[3]+', r'+rbody[4]+')'
        elif len(rbody)==6:
            s+='Sequence(r'+rbody[0]+', r'+rbody[1]+')'
            s+=','
            s+='Sequence(r'+rbody[3]+', r'+rbody[4]+', r'+rbody[5]+')'
      
        s+=")"
    else:
        s="    "+rn+"=Sequence("
        for r in rbody: 
            s+='r'+r+', '
        s=s[:-2]
        s+=")"
    return(s)


def order_rules(r):
    orderedrules={} #python3.7+ dicts retain insertion order 
    while len(r)>0:
        todel=[]
        for inr,rbody in r.items():
            print(inr,rbody)
            if len(rbody)==1:
                if rbody[0][1]=='a' or rbody[0][1]=='b':
                    #it is a statement so can go straight in the new dict
                    orderedrules[inr]=rbody[0][1]
                    todel.append(inr)
                elif 'r'+rbody[0] in orderedrules:
                    orderedrules[inr]=rbody
                    todel.append(inr)
            else:
                i=0
                allfound=True
                circular=False
                while i < len(rbody):
                    if rbody[i]=='|':
                        i+=1
                        continue
                    if 'r'+rbody[i] not in orderedrules:
                        allfound=False
                        if 'r'+rbody[i]==inr:
                            print(f"circular! {rbody[i]} {inr}")
                            circular=True 
                        break
                    else:
                        i+=1
                if allfound or circular:
                    orderedrules[inr]=rbody
                    todel.append(inr)
        for d in todel:
            del r[d]
    return(orderedrules)



def process_rules(r):
    listrules=order_rules(r)
    print(listrules)
    fout="MyGrammar.py"
    if os.path.exists(fout):
        os.remove(fout)
    with open(fout,"w") as fp:
        print("Opened file")
        for h in headers:
            print(f"Writing {h}")
            fp.write(h+'\n')
        for rule in listrules:
            print(f"Writing {rule}")
            s=write_out_rule(rule,listrules[rule])
            fp.write(s+'\n')


def parse_data():
    strs=[]
    inputrules={}
    phase=0
    with open(infile) as fp:
        for line in fp:
            print(line)
            if len(line)==1:
                phase=1
            elif phase==0:
                print("rules section")
                lo=line.strip().split(' ')
                r='r'+lo[0]
                r=r[:-1]
                inputrules[r]=lo[1:]
    process_rules(inputrules)

    return(strs)


strs=parse_data()


#part_two()


