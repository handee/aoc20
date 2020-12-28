infile = 'input/day22.1.txt'

def parse_data():
    p1=[]
    p2=[]
    phase=0
    with open(infile) as fp:
        for line in fp:
            if len(line)==1:
                phase+=1
            elif line[0]=='P':
                print(f"Reading in {line.strip()} data")
            elif phase==0:
                p1.append(int(line.strip()))
            elif phase==1:
                p2.append(int(line.strip()))
    return(p1,p2)


def play_round(p1,p2):
    c1=p1.pop(0)
    c2=p2.pop(0)
    print(f"Player 1's deck: {p1} playing {c1}")
    print(f"Player 2's deck: {p2} playing {c2}")
    if (c1>c2):
        p1.append(c1)
        p1.append(c2)
        print("Player 1 wins the round!")
    else:
        p2.append(c2)
        p2.append(c1)
        print("Player 2 wins the round!")
    return(p1,p2)

def calculate_score(deck):
    mult=len(deck)
    rv=0
    for i in deck:
        print(i,mult)
        rv+=i*mult
        mult-=1
    return(rv)

def part_one():
    p1,p2=parse_data()
    rnd=0
    while len(p1)!=0 and len(p2)!=0:
        rnd+=1
        print(f"-- Round {rnd} --")
        p1,p2=play_round(p1,p2)
        print(f"Player 1 has {len(p1)} cards left")
        print(f"Player 2 has {len(p2)} cards left")
    if len(p1)>0:
        score=calculate_score(p1)
    else:
        score=calculate_score(p2)
    print(f"The score is {score}")

def play_r_round(p1,p2):
    c1=p1.pop(0)
    c2=p2.pop(0)
   # print(f"Player 1's deck: {p1} playing {c1}")
   # print(f"Player 2's deck: {p2} playing {c2}")
    if c1<=len(p1) and c2<=len(p2):
   #     print("Playing a sub-game to determine the winner...")
        sd1=p1[:c1]
        sd2=p2[:c2]
        sd1,sd2=play_recursive_combat(sd1,sd2)
        if len(sd1)==0:
            p2.append(c2)
            p2.append(c1)
        #    print("The winner of the sub-game is p2")
        else:
            p1.append(c1)
            p1.append(c2)
        #    print("The winner of the sub-game is p1")
    else: # it's a normal round
        if (c1>c2):
            p1.append(c1)
            p1.append(c2)
        #    print("Player 1 wins the round!")
        else:
            p2.append(c2)
            p2.append(c1)
        #    print("Player 2 wins the round!")
    return(p1,p2)


def check_decks(p1,p2,d1,d2):
    terminate=False
    for i,deck in enumerate(d1):
        if p1==deck:
            # player one has had this deck before
            if p2==d2[i]:
                # so has player 2
                terminate=True
    return(terminate)

def play_recursive_combat(p1,p2):
    rnd=0
    d1=[]
    d2=[]
    terminate_early=False 
    while len(p1)!=0 and len(p2)!=0:
        rnd+=1
        #print(f"-- Round {rnd} --")
        p1,p2=play_r_round(p1,p2)
        terminate_early= check_decks(p1,p2,d1,d2)
        if terminate_early:
            #player one wins so just clear p2
        #    print("Terminating early, player one wins")
            p2.clear()
            break
       
        d1.append(p1.copy())
        d2.append(p2.copy())
        #print(f"Player 1 has {len(p1)} cards left")
        #print(f"Player 2 has {len(p2)} cards left")
    return(p1,p2)


def part_two():
    p1,p2=parse_data()
    p1,p2=play_recursive_combat(p1,p2)
    if len(p1)>0:
        score=calculate_score(p1)
    else:
        score=calculate_score(p2)
    print(f"The score is {score}")




#part_one()
part_two()


