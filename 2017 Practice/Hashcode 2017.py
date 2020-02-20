with open("videos_worth_spreading.in","r+") as f:
    data_set = f.read()
    f.close()
    
data_set = data_set.split("\n") 

properties = data_set[0]   

video_line = data_set[1]

video_line = video_line.split(" ")

data_set = data_set[2:]

for i in range(len(data_set)):
    data_set[i] = data_set[i].split()
    
data_set = data_set[:621]

        

endpoints = []
endpoint_latencies = []
endpoint_cache_ref = [[]]
#must have same amount of empty sublists as number of endpoints

while len(data_set) > 0:
    num_of_cache_servers = int(data_set[0][1])
    base = num_of_cache_servers
    endpoint = []
    endpoint_latencies.append(int(data_set[0][0]))
    while base > 0:
        endpoint_cache_ref[len(endpoints)].append(data_set[base])
        endpoint += [data_set[base]]
        base -= 1
    endpoint_cache_ref.append([])
    data_set = data_set[num_of_cache_servers + 1:]
    endpoints += [endpoint]
endpoint_cache_ref = endpoint_cache_ref[:-1]

#print(len(endpoints))
#print(endpoint_latencies)
#print(endpoint_cache_ref)

 

