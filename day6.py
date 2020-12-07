import math
from collections import Counter

def part_one():
    answers=set()
    total=0
    with open('input/day6.1.txt') as fp:
        for line in fp:
            letters=list(line.strip())
            if (len(letters)==0):
                total=total+len(answers)
                print(f"this group answered {len(answers)}")
                answers.clear()
            else:
                answers.update(letters)
        total=total+len(answers)
        print(f"this group answered {len(answers)}")
    print(f"{total} is the total no of answers")

def all_answered(answers, groupsize):
    all_answered=0
    print(answers)
    for answer in answers.most_common():
        if answer[1] ==groupsize:
            all_answered+=1
        else:
            break
    print(f"size of group ={groupsize}, group's count={all_answered}!")
    return(all_answered)
     
def part_two():
    answers=Counter()
    total=0
    groupsize=0
    with open('input/day6.1.txt') as fp:
        for line in fp:
            letters=list(line.strip())
            if (len(letters)==0):
                total+=all_answered(answers,groupsize)
                answers.clear()
                groupsize=0
            else:
                groupsize+=1
                for letter in letters:
                    answers[letter]+=1
        total+=all_answered(answers,groupsize)
    print(f"{total} is the total no of answers")

#part_one()


part_two()


