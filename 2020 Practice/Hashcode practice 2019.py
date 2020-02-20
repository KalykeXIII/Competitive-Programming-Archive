filename = "a_example.in"
with open(filename,"r+") as f:
    data_set_example = f.read()
    f.close()

data_set_example = data_set_example.split("\n")


for i in range(len(data_set_example)):
    data_set_example[i] = data_set_example[i].split(" ")


del data_set_example[-1]

for i in range(len(data_set_example)):
    for j in range(len(data_set_example[i])):
        data_set_example[i][j] = int(data_set_example[i][j])

target = data_set_example[0][0]
pno = data_set_example[0][1]
plist = data_set_example[1]

current_slices = 0
pused = 0
pwhich = []
space = target - current_slices

for i in range(pno -1,-1,-1):
    if current_slices + plist[i] <= target:
        current_slices+=plist[i]
        pused += 1
        pwhich.insert(0,i)

print(target,pno,plist)

f = open("submissionfile.in","w+")
f.write(str(pused)+"\n")
for i in range(len(pwhich)-1):
    f.write(str(pwhich[i])+" ")
f.write(str(pwhich[-1]))
f.close()