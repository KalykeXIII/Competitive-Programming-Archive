# Question 3: Parenting Partnering
#==============================================================================
def allocate(events,p1,p2,string):
    for i in range(len(events)):
        if check(p1,events[i])  ==  True:
            p1.append(events[i])
            string += 'C'
        elif check(p2,events[i]) == True:
            p2.append(events[i])
            string += 'J'
        elif check(p1,events[i]) == False and check(p2,events[i]) == False:
            return "IMPOSSIBLE"
    return string

def check(person,event):
    if person == []:
        return True
    for j in range(len(person)):
        if event[0] in range(person[j][0],person[j][1]) or event[1] in range(person[j][0],person[j][1]):
            return False
    return True

#==============================================================================
def solve(iteration):
    #iteration = integer in range(0,t)
    n = int(input())
    activities = []
    for i in range(n):
        activities.append(list(map(int, input().split())))
    c = []
    j = []
    order = ''
    
    sorted_activities = sorted(activities)   
    indices = sorted(range(len(activities)),key=activities.__getitem__)
    
    #perform necessary operations on grid to obtain Case #i answer
    y = allocate(sorted_activities,c,j,order)
    z = ''
    if y != "IMPOSSIBLE":
        for i in range(len(activities)):
            z += y[indices.index(i)]
        print("Case #{}: {}".format(iteration+1, z))   
    else:
        print("Case #{}: {}".format(iteration+1, y))        
#==============================================================================
t = int(input())
for i in range(t):
    solve(i)