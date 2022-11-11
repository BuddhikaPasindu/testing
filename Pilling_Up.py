T = int(input('T: '))
#Taking the input


for i in range(T):
    n = int(input('n: '))
    block = list(map(int, input('Numbers: ').split(' ')))

    pile = []
    while len(block)>0:
        first = block[0]
        last = block[-1]

        if len(pile)==0:    
            if (first==last):
                pile.append(first)
                block.pop(0)
            elif (first>last):
                pile.append(first)
                block.pop(0)
            else:
                pile.append(last)
                block.pop(-1)
        else:
            top = pile[-1]
            if (first==last and first<=top):
                pile.append(first)
                block.pop(0)
            elif (first>last and first<=top):
                pile.append(first)
                block.pop(0)
            elif (last>first and last<=top):
                pile.append(last)
                block.pop(-1)
            else:
                print('No')
                break
    if (len(block)==0):
        print('Yes')
    print(pile)
                
                
        


