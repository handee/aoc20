infile='input/day21.1.txt'
from collections import defaultdict

def parse_data():
    allergens={}
    definites={}
    ingredients=[]
    with open(infile) as fp:
        for line in fp:
            li,ag=line.strip().split(' (contains ')
            ag=ag.replace(',','')
            ag=ag.replace(')', '' )
            print(ag)
            print(li)
            ag=ag.split(' ')
            li=li.split(' ')
            print(ag)
            print(li)
            for ing in li:
                ingredients.append(ing)
            for a in ag:
                if a in allergens.keys():
                    print(f'considering {a}')
                    print(f'current list = {allergens[a]}')
                    # we only want to retain those ingredients which are 
                    # in both lists
                    toremove=[]
                    for ing in li:
                        if ing in definites:
                            toremove.append(ing)
                    for ing in toremove:
                        li.remove(ing)
                    toremove.clear()

                    for ing in allergens[a]:
                        print(f"could be...", end="")
                        print(f"{ing}", end="")
                        if ing not in li:
                            print(f" but that's not in this product")
                            toremove.append(ing)
                        else:
                            print(f" still ok")
                    for ing in toremove:
                        allergens[a].remove(ing)
                    print(f"list now = {allergens[a]}")
                    if len(allergens[a])==1:
                        definites[a]=allergens[a].copy()

                    
                else:
                    allergens[a]=li.copy()
            print(f"After {li} allergens = {allergens}")
            print(f"After {li} definites= {definites}")
    for a in definites:
        del allergens[a]
    return(allergens,definites,ingredients)

def part_one():
    ag,de,ingredients=parse_data()
    print(ag)
    toremove=[]
    for i in range(3):
    #while len(ag)>0:
        for a in de:
            toremove.append(de[a][0])
        print(toremove)
        for ing in toremove:
            for k,a in ag.items():
                print(k,a,ing)
                if ing in a:
                    a.remove(ing)
                print(k,a,ing,len(a))
                if len(a)==1:
                    de[k]=a.copy()
        for a in de:
            if a in ag:
                del ag[a]
        toremove.clear()
        print(f"de now: {de}")
        print(f"ag now: {ag}")

    print(ingredients)
    for a,l in de.items():
        if l[0] in ingredients:
            ingredients=[j for j in ingredients if j!=l[0]]
    for a,l in ag.items():
        for i in l:
            if i in ingredients:
                ingredients=[j for j in ingredients if j!=i]
    print(ingredients)
    print(len(ingredients))
 
def part_two():
    ag,de,ingredients=parse_data()
    print(ag)
    toremove=[]
    while len(ag)>0:
        for a in de:
            toremove.append(de[a][0])
        print(toremove)
        for ing in toremove:
            for k,a in ag.items():
                print(k,a,ing)
                if ing in a:
                    a.remove(ing)
                print(k,a,ing,len(a))
                if len(a)==1:
                    de[k]=a.copy()
        for a in de:
            if a in ag:
                del ag[a]
        toremove.clear()
        print(f"de now: {de}")
        print(f"ag now: {ag}")
    output=[]
    for a,i in de.items():
        print(i[0])
        output.append(a)
    output.sort()
    for o in output:
        print(f"{de[o][0]},",end="")

#part_one()
part_two()
