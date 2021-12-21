f = open('testinput.txt', 'r')

beacons = []
possibleorderings = [((0,1),(1,1),(2,1)),((0,1),(1,-1),(2,-1)),((0,-1),(1,1),(2,-1)),((0,-1),(1,-1),(2,1)),((0,-1),(1,-1),(2,-1)),\
                     ((0,1),(2,1),(1,1)),((0,1),(2,1),(1,-1)),((0,1),(2,-1),(1,1)),((0,1),(2,-1),(1,-1)),((0,-1),(2,1),(1,1)),((0,-1),(2,1),(1,-1)),((0,-1),(2,-1),(1,1)),((0,-1),(2,-1),(1,-1)),\
                     ((1,1),(0,1),(2,1)),((1,1),(0,1),(2,-1)),((1,1),(0,-1),(2,1)),((1,1),(0,-1),(2,-1)),((1,-1),(0,1),(2,1)),((1,-1),(0,1),(2,-1)),((1,-1),(0,-1),(2,1)),((1,-1),(0,-1),(2,-1)),\
                     ((1,1),(2,1),(0,1)),((1,1),(2,1),(0,-1)),((1,1),(2,-1),(0,1)),((1,1),(2,-1),(0,-1)),((1,-1),(2,1),(0,1)),((1,-1),(2,1),(0,-1)),((1,-1),(2,-1),(0,1)),((1,-1),(2,-1),(0,-1)),\
                     ((2,1),(0,1),(1,1)),((2,1),(0,1),(1,-1)),((2,1),(0,-1),(1,1)),((2,1),(0,-1),(1,-1)),((2,-1),(0,1),(1,1)),((2,-1),(0,1),(1,-1)),((2,-1),(0,-1),(1,1)),((2,-1),(0,-1),(1,-1)),\
                     ((2,1),(1,1),(0,1)),((2,1),(1,1),(0,-1)),((2,1),(1,-1),(0,1)),((2,1),(1,-1),(0,-1)),((2,-1),(1,1),(0,1)),((2,-1),(1,1),(0,-1)),((2,-1),(1,-1),(0,1)),((2,-1),(1,-1),(0,-1))]

for x in f:
    x = x.rstrip()
    if x.count(",")==2:
        beacons[-1].append(tuple(map(int,x.split(','))))
    elif len(x) !=0:
        beacons.append([])

# pairs
# list of pairs of beacons
# each element of the list is a tuple, with the first element representing the member of the base list and the second member the list being paired against
# the members are tuples where the first element is the beacon number they are percieved from and the second element is the ordered pair
#the orderings are a three tuple of tuples where the first element of each tuple is whether it represents x,y, or z (0,1,2) 
# and the second is whether it is inverted or not (-1,1)
def matchbeacons(beacons, pairs, ordering):
    if len(pairs) == 0:
        for i in range(len(beacons)):
            for j in range(i):
                for k in range(len(beacons[i])):
                    for l in range(len(beacons[j])):
                        for order in possibleorderings:
                            newpairobject=((i, beacons[i][k]), [j, beacons[j][l]])
                            result = matchbeacons(beacons, [newpairobject], order)
                            if not isinstance(result, bool):
                                return result
    else:
        beacon1 = pairs[0][0][0]
        beacon2 = pairs[0][1][0]
        baseb1 = pairs[0][0][1]
        baseb2 = pairs[0][1][1]
        print()
        diff1 = set(map(lambda x: tuple(map(lambda y: x[y]-baseb1[y], [z for z in range(3)])), beacons[beacon1]))
        diff2 = set(map(lambda x: tuple(map(lambda y: (x[ordering[y][0]]-baseb2[ordering[y][0]])* ordering[y][1], [z for z in range(3)])),  beacons[beacon2]))
        if len(diff1.union(diff2))>=12:
            return pairs, ordering            
        return False


while len(beacons)!=1:
    print(len(beacons))
    result = matchbeacons(beacons,[], None)
    ## unify the two beacons, using ordering to translate
    beacon1 = beacons.pop(result[0][0][0][0])
    beacon2 = beacons.pop(result[0][0][1][0])
    ordering = result[1]
    ref1 = result[0][0][0][1]
    print(ref1)
    ref2 = result[0][0][1][1]
    diffx = ref1[0] - ref2[ordering[0][0]]
    diffy = ref1[1] - ref2[ordering[1][0]]
    diffz = ref1[2] - ref2[ordering[2][0]]
    for toplace in list(filter(lambda x: x not in [y[1][1] for y in result[0]], beacon2)):
        calcx = ref1[0] + (toplace[ordering[0][0]] - ref2[ordering[0][0]])*ordering[0][1]
        calcy = ref1[1] + (toplace[ordering[1][0]] - ref2[ordering[1][0]])*ordering[1][1]
        calcz = ref1[2] + (toplace[ordering[2][0]] - ref2[ordering[2][0]])*ordering[2][1]
        print(ordering)
        print(ref1)
        print(ref2)
        print(toplace)
        print((calcx, calcy, calcz))
        if (calcx, calcy, calcz) not in beacon1:
            beacon1.append((calcx, calcy, calcz))
    beacons = [beacon1] + beacons
print(len(beacons))
print(len(beacons[0]))