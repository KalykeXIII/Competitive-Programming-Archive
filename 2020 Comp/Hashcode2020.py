# Hashcode 2020 

# =============================================================================
# File Data Extract
# =============================================================================
filename = ["a_example.txt","b_read_on.txt","c_incunabula.txt","d_tough_choices",
            "e_so_many_books.txt","f_libraries_of_the_world.txt"]
with open(filename[0],"r+") as f:
    data_set_example = f.read()
    f.close()
    
data_set_example = data_set_example.split("\n")

string = data_set_example[-1]
while len(string) == 0:
    del data_set_example[-1]
    string = data_set_example[-1]
    

for i in range(len(data_set_example)):
    data_set_example[i] = data_set_example[i].split(" ")
    data_set_example[i] = [int(data_set_example[i][j]) for j in range(len(data_set_example[i]))]
 
scoring_order = data_set_example[1]
lib_list = data_set_example[2:]    
new_lib_list = []


def score_lib(lib,s):
    score = 0
    
    for i in range(len(lib[1])):
            score += s[lib[1][i]]
    return score

def time_taken(lib, time):
    time_sign_up = lib[0][1][1]
    return time - 1 > time_sign_up
    
def time_per_lib(lib):
    return float(lib[0][1][0]/ lib[0][1][2]) + lib[0][1][1]


for i in range(0, len(lib_list), 2):
    new_lib_list = new_lib_list + [[lib_list[i],lib_list[i+1]]]

for i in range(len(new_lib_list)):
    new_lib_list[i] += [[score_lib(new_lib_list[i],scoring_order)]]


new_lib_list.sort(key = lambda x:sum(x[2]), reverse = True)

        
def time_taken(lib, time):
    time_sign_up = lib[0][1]
    time -= 1
    return time > time_sign_up
    
def time_per_lib(lib):
    return float(lib[0][0]/ lib[0][2]) + lib[0][1]


new_lib_list.sort(key = lambda x:sum(x[2]), reverse = True)



total_time = data_set_example[0][-1]

total_score = 0

dupe_lib = new_lib_list[:]



def re_score(lib,s):
    score = 0
    books = []
    for i in range(len(lib[1])):
        score += s[lib[1][i]]
        books += [lib[1][i]]
        s[lib[1][i]] = 0
    return score, s, books



books_used = []
libraries = []




while len(dupe_lib) > 0:
    time = time_taken(dupe_lib[0], total_time)
    
    if time == True:
        if total_time - time_per_lib(dupe_lib[0]) >= 0:
            libraries += [len(libraries)]
            lib_score = re_score(dupe_lib[0],scoring_order)
            books_used = books_used + [lib_score[2]]
            scoring_order = lib_score[1]
            lib_score = lib_score[0]      
            total_score += lib_score
        else:
            total_time -= dupe_lib[0][1][1]
            lib_score = re_score(dupe_lib[0],scoring_order)
            books_per_day = dupe_lib[0][1][2]
            books = []
            while books_per_day > 0:
                libraries += [len(libraries)]
                count = 0
                book = dupe_lib[0][0][count]
                while book == 0:
                    book = dupe_lib[0][0][count]
                    count += 1
                books += [book]
                total_score += scoring_order[book]
                books_per_day -= 1
            books_used = books_used + [books]
    dupe_lib = dupe_lib[1:]
    
print(libraries,books_used)

# =============================================================================
# Output Format
# =============================================================================

f = open("submissionfile_" + filename[1] ,"w+")
f.write(str(len(libraries)) + "\n")
for i in range(len(libraries)):
    f.write(str(libraries[i]) + " " + str(len(books_used[i])) + "\n")
    for j in range(len(books_used[i])):   
        f.write((str(books_used[i][j])) + " ")
    f.write("\n")
f.close()


    

