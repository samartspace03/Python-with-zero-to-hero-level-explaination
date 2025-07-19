def countEle(tup, element):
    count = 0
    
    for x in tup:
        if(x == element):
            count = count + 1
    return count
tup = (1, 1, 3, 6,8,9,3,4 , 1)
enq = 1
enq2 = 3
print(countEle(tup, enq))
print(countEle(tup, enq2))