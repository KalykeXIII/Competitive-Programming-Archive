#Hashcode 2018 Practice Problem
filename = "data_set_a.txt"
with open(filename,"r+") as f:
    data_set_example = f.read()
    f.close()
    
data_set_example = data_set_example.split("\n")
for i in range(len(data_set_example)):
    data_set_example[i] = data_set_example[i].split(" ")
    
print(data_set_example)

# =============================================================================
# Variables
# =============================================================================

#grid generation
row = int(data_set_example[0][0])
col = int(data_set_example[0][1])

#variable setup
grid_dimensions = (row,col)
fleet = int(data_set_example[0][2])
nrides = int(data_set_example[0][3])
bonus = int(data_set_example[0][4])
time = int(data_set_example[0][5])
ride = list(data_set_example[1:])
cars = []
for i in range(fleet):
    cars.append([0,0])

# =============================================================================
# #finds start coordinates of ride by ID num
# def start_coordinates(ride):
#     srow = int(data_set_example[ride+1][0])
#     scol = int(data_set_example[ride+1][1])
#   
# #finds end coordinates of ride by ID num
# def end_coordinates(ride):
#     frow = int(data_set_example[ride+1][2])
#     fcol = int(data_set_example[ride+1][3])
#   
# #find start time of ride by ID
# def start_time(ride):
#     start_time = int(data_set_example[ride+1][4])
# 
# #find end time of ride by ID
# def fin_time(ride):
#     end_time = int(data_set_example[ride+1][5])
# =============================================================================

# =============================================================================
# Solution formatting
# =============================================================================

#fleet_assignments = list(fleet * [])
fleet_assignments = [[0],[2,1]]

f = open("submissionfile.txt","w+")
for i in range(fleet):
  f.write(str(len(fleet_assignments[i]))+" ")
  for j in range(len(fleet_assignments[i])):
       f.write(str(fleet_assignments[i][j])+" ")
  f.write("\n")
f.close()


# =============================================================================
# Algorithm Features
# =============================================================================

def doable_ride(car,current_time):
    srow = int(data_set_example[car+1][0])
    scol = int(data_set_example[car+1][1])
    frow = int(data_set_example[car+1][2])
    fcol = int(data_set_example[car+1][3])
    start_time = int(data_set_example[car+1][4])
    end_time = int(data_set_example[car+1][5])
    
    arrival_dist = abs(cars[car][0]-srow)+abs(cars[car][1]-scol)
    dist = abs(srow-frow)+abs(scol-fcol)
    travel = arrival_dist + dist
    
    if travel + current_time > end_time:
        return False
    elif travel + current_time <= end_time and arrival_dist + current_time >= start_time:
        return True
    else:
        return False
    
import copy
index_ref_rides = copy.deepcopy(ride)

def job_order(lst):
    reverse = None
    lst.sort(key = lambda x: x[4])
    return lst


# =============================================================================
# for j in range(fleet):
#     #use i as array of length time
#     for i in range(time):
#       #how long car will take to arrive at ride start
#       arrdist = abs(cars[j][0]-srow)+abs(cars[j][1]-scol)
#       #length of the ride
#       dist = abs(srow-frow)+abs(scol-fcol)
#       arrtime=i+arrdist
#       fintime=arrtime+dist
# 
#       if fintime<fin:
#         #add ride to car array
#         #delete ride from ride array
#         #increase i to end time
#         i += fintime
# =============================================================================
