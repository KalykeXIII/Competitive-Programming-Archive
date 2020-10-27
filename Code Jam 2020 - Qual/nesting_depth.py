# Question 2: Nesting Depth
#==============================================================================
#Initial functions
'''In this problem we nest each integer in an integer string, in parentheses 
equal to its numeric value; eg. 1 is translated to (1), 5 to (((((5))))). After 
doing this, the parentheses are the condensed if multiple numbers can be 
co-habitants of a parentheses pair; eg. 11 is (1)(1) which can then become 
(11). To do so we condense when )( appears in the translated string, allowing 
the process to be split into 2 functions: translation, condensation.

Alternatively, before adding to the 'new' string check from element new[-1] and
eliminate excess brackets before appending'''
#==============================================================================
# Translation Optimiser
def add(ex,ad,num):
    final = ''
    remove = 0
    if ex == '':
        return ex + ad
    elif ex[-1] != ")":
        return ex + ad
    elif ex != '':
        for i in range(len(ex)-1,0,-1):
            if ex[i] == ')' and remove < num:
                remove += 1
            else:
                ex = ex[:len(ex)-remove]
                ad = ad[remove:]
                final = ex+ad
                return final
        
# String Translator
def trans(string):
    new = ''
    s = len(string) # Take the length of the test case string (s)
    for i in range(s):  # For all integer elements in s test:
        if string[i] == '0':
            new += '0'
        elif string[i] == '1':
            new = add(new,'(1)',1)
        elif string[i] == '2':
            new = add(new,'((2))',2)
        elif string[i] == '3':
            new = add(new,'(((3)))',3)
        elif string[i] == '4':
            new = add(new,'((((4))))',4)
        elif string[i] == '5':
            new = add(new,'(((((5)))))',5)
        elif string[i] == '6':
            new = add(new,'((((((6))))))',6)
        elif string[i] == '7':
            new = add(new,'(((((((7)))))))',7)
        elif string[i] == '8':
            new = add(new,'((((((((8))))))))',8)
        elif string[i] == '9':
            new = add(new,'(((((((((9)))))))))',9)
    return new

# Solve a test case (iterated through t)
#==============================================================================
def solve(iteration):
    #iteration = integer in range(0,t)
    s = input()

    #perform necessary operations on grid to obtain Case #i answer
    sprime = trans(s)
    
    print("Case #{}: {}".format(iteration+1, sprime))          
#==============================================================================
t = int(input())
for i in range(t):
    solve(i)