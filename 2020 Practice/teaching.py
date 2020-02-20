#Problem 1

##total = 0
##for i in range(1000):
##    if i%3 == 0:
##        total+=i
##    elif i%5 == 0:
##        total+=i
##print(total)

#Problem 2

##fib = [1,2]
##tally = 0
##while fib[-1]<4000000:
##    fib.append(fib[-1]+fib[-2])
##for i in range(1,len(fib),3):
##    tally+=fib[i]
##print(tally)

##i = 1
##j = 2
##tally = 0
##while j < 4000000:
##    if j%2 == 0:
##        tally+=j
##        j_new = i+j
##        i = j
##        j = j_new
##    else:
##        j_new = i+j
##        i = j
##        j = j_new
##print(tally)
