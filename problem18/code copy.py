f = open('input.txt', 'r')
import ast
num = []
for x in f:
    x = x.rstrip()
    num.append(x)

def stringindex(func, string, start):
    for char in range(len(string)-start):
        if func(string[char+start]):
            return char+start
    return -1
        

def snailadd(a,b):
    pair = "[" + a + "," + b +"]"
    # print(pair)
    done = False
    while not done:
        if pair.count("[")!= pair.count("]"):
            print('panic')
            print(pair)
            input()
        # print(pair)
        # input()
        
        done = True
        index = -1
        depth = 0
        for char in pair:
            index += 1
            # print(depth, index, char)
            if char == "[":
                depth +=1
            elif char ==']':
                depth -= 1
            elif depth == 5 and char !=',':
                # print("doing replacement")
                # print(pair)
                # print(char, index)
                num1, num2 = tuple(map(int, pair[index:pair.find(']', index)].split(",")))
                prevnumstart = index - (stringindex(lambda a: a.isdecimal(), pair[:index][::-1], 0)+1)
                while(pair[prevnumstart-1].isdecimal()):
                    prevnumstart -=1
                # input()
                if prevnumstart != index +1:
                    if prevnumstart==index or prevnumstart == index-1:
                        # print("horribly wrong")
                        pass
                    else:
                        prevnumslength = stringindex(lambda b: b == ',' or b == ']', pair[prevnumstart:], 0)
                        prevnum = int(pair[prevnumstart: prevnumslength+prevnumstart])
                        newnum = num1+prevnum
                        pair = pair[:prevnumstart] + str(newnum) + pair[prevnumstart+prevnumslength:]
                        index += (len(str(newnum)) - len(str(prevnum)))
                # print(pair.find(']', index))
                # print(pair)
                nextnumstart = stringindex(lambda a: a.isdecimal(), pair[pair.find(']', index):], 0) + pair.find(']', index)
                # print(nextnumstart, pair[nextnumstart])
                if nextnumstart != -1:
                    nextnumslength = stringindex(lambda b: b == ',' or b == ']', pair[nextnumstart:], 0)
                    prevnum = int(pair[nextnumstart: nextnumslength+nextnumstart])
                    newnum = num2+prevnum
                    pair = pair[:nextnumstart] + str(newnum) + pair[nextnumstart+nextnumslength:]
                pair = pair[:index-1] + "0" + pair[pair.find(']', index)+1:]
                done = False
                break
        if done:
            # do splits
            for index in range(len(pair)-1):
                if pair[index].isdecimal() and pair[index+1].isdecimal():
                    numstart = index
                    numlength = stringindex(lambda b: b == ',' or b == ']', pair[numstart:], 0)
                    prevnum = int(pair[numstart: numlength+numstart])
                    left = prevnum // 2
                    right = (prevnum+1) //2
                    pair = pair[:index] + "[" + str(left) + "," + str(right) + ']' + pair[index+numlength:]
                    done = False
                    break
    return pair
def magnitude(pair):
    if isinstance(pair, int):
        return pair
    else:
        return 3*magnitude(pair[0])+2*magnitude(pair[1])

# pair = snailadd("[[9,3],[[9,9],[6,[4,9]]]]", "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]")
maxval = 0
for i in range(len(num)):
    for j in range(len(num)):
        if i == j:
            continue
        else:
            pair = snailadd(num[i], num[j])
            maxval = max(magnitude(ast.literal_eval(pair)), maxval)
            print(num[i], num[j], pair, magnitude(ast.literal_eval(pair)))
print(len(num))
print(maxval)





                
                



