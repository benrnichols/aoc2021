f = open('input.txt', 'r')

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
def matchbeacons(baselist, beacons, pairs, ordering):
    if len(pairs) == 0:
        for i in range(len(beacons)):
                for k in range(len(baselist)):
                    for l in range(len(beacons[i])):
                        for order in possibleorderings:
                            newpairobject=((None, baselist[k]), [i, beacons[i][l]])
                            result = matchbeacons(baselist, beacons, [newpairobject], order)
                            if not isinstance(result, bool):
                                return result
    else:
        beacon1 = baselist
        beacon2 = pairs[0][1][0]
        baseb1 = pairs[0][0][1]
        baseb2 = pairs[0][1][1]
        diff1 = set(map(lambda x: tuple(map(lambda y: x[y]-baseb1[y], [z for z in range(3)])), baselist))
        diff2 = set(map(lambda x: tuple(map(lambda y: (x[ordering[y][0]]-baseb2[ordering[y][0]])* ordering[y][1], [z for z in range(3)])),  beacons[beacon2]))
        if len(diff1.intersection(diff2))>=12:
            return pairs, ordering            
        return False

baselist = beacons.pop(0)
scanners = [(0,0,0)]
while len(beacons)!=0:
    print(len(beacons))
    result = matchbeacons(baselist, beacons,[], None)
    ## unify the two beacons, using ordering to translate
    beacon1 = baselist
    beacon2 = beacons.pop(result[0][0][1][0])
    ordering = result[1]
    ref1 = result[0][0][0][1]
    ref2 = result[0][0][1][1]
    diffx = ref1[0] - ref2[ordering[0][0]]
    diffy = ref1[1] - ref2[ordering[1][0]]
    diffz = ref1[2] - ref2[ordering[2][0]]
    for toplace in beacon2:
        calcx = ref1[0] + (toplace[ordering[0][0]] - ref2[ordering[0][0]])*ordering[0][1]
        calcy = ref1[1] + (toplace[ordering[1][0]] - ref2[ordering[1][0]])*ordering[1][1]
        calcz = ref1[2] + (toplace[ordering[2][0]] - ref2[ordering[2][0]])*ordering[2][1]
        # print(beacon1)
        # print(beacon2)
        # print(ordering)
        # print(ref1)
        # print(ref2)
        # print(toplace)
        # print((calcx, calcy, calcz))
        if (calcx, calcy, calcz) not in beacon1:
            baselist.append((calcx, calcy, calcz))
    sensorplace = (0,0,0)
    calcx = ref1[0] + (sensorplace[ordering[0][0]] - ref2[ordering[0][0]])*ordering[0][1]
    calcy = ref1[1] + (sensorplace[ordering[1][0]] - ref2[ordering[1][0]])*ordering[1][1]
    calcz = ref1[2] + (sensorplace[ordering[2][0]] - ref2[ordering[2][0]])*ordering[2][1]
    scanners.append((calcx, calcy, calcz))

maxmandist = 0
for i in range(len(scanners)):
    for j in range(i):
        maxmandist = max(maxmandist, (abs(scanners[i][0] - scanners[j][0]) + abs(scanners[i][1] - scanners[j][1])+ abs(scanners[i][2] - scanners[j][2])))
print(maxmandist)
print(len(beacons))
print(len(baselist))