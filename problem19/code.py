f = open('testinput.txt', 'r')

beacons = []
for x in f:
    x = x.rstrip()
    if x.count(",")==2:
        beacons[-1].append(tuple(map(int,x.split(','))))
    elif len(x) !=0:
        beacons.append([])




