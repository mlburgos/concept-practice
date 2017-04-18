 
# Your previous Plain Text content is preserved below:
# 
# You are given a list of commercial flight arrival and departure times sorted by tail number (plane), for a single day. Assume a given airport will have a similar schedule each day. You are to determine the number of gates a given airport should have so that no plane spends time waiting on the tarmac for a gate. 
# The input is passed to the program as a file that looks like this:
# 
# schedule.txt
# # Flight_No Tail_No Airport_Dep Airport_Arr Localtime_Dep Localtime_Arr
# VX001 N123VX SEA SFO 8:15 9:30
# VX023 N123VX  SFO SEA 11:45 14:10
# WN2344 N561WN LAS SFO 10:15 11:15
# WN2344 N561WN  SFO PHX 11:30 14:40
# AA200 N163AA BOS SFO  13:00 16:30
# AA251 N163AA  SFO JFK 16:45  01:30 
# 
# The program might be run like 
# gates <filename> <airport>, where airport is the airport code.
# gates schedule.txt SFO
# 
# 


# argv[] = arguments, where argv[1] is first argument after the command name

def get_lines(filename):
    # returns a list of lines of a text file
    pass

def time_in_minutes(string):
    _hr, _min = string.split(:)
    return _hr*60 + _min

def time_in_minutes(string):
    # returns time in minutes
    pass

    
    
airport = argv[2]


schedule = get_lines(argv[1])

# keep track of landing and departures for a given airport
# look at overlaps
# get the max number over laps at given time

# {tail_no: [land_time, depart_time]}

ground_time = {}

for line in schedule:
    flight_no, tail_no, airport_dep airport_arr, dep, arr = line.rstrip().split(' ')

#     check if airport_dep or airport_dep or airport_arr match given airport code
#     if so, store that info

#     I'm expecting that the data for a given airport arranged such that one plane will only go in an out of one airport once a day
    if airport_arr == airport:
        ground_time[tail_no] =  ground_time.get(tail_no, [,])
#         arr --> [hrs, mins]
        ground_time[tail_no][0] = [int(string) for string in arr.split(':')]
    
    if airport_dep == airport:
        ground_time[tail_no] =  ground_time.get(tail_no, [,])
        ground_time[tail_no][1] = dep.split(':')
    
#     should have:
#  {N123VX: [[9,30], [11,45]],
#   111111: [[11,15], [11,30]], ...}

max_count = 0 

for tail_no, time_info in ground_time.items():
#     test to see if arrival or departure lie within arrival and departure of other flights

    arrive = correct_format(time_info)
    arrive_hr = time_info[0][0]
    arrive_min = time_info[0][1]
#     to get time in an eaisly comparable state
    arrive_float = float(arrive_hr) + float(arrive_min)/60
    depart_hr = time_info[1][0]
    arriv_min = time_info[1][1]
    
    
    count = 0 
    
    for tail_no_test, time_info_test in ground_time.items():
        if tail_no != tail_no_test:
            mini = time_info_test[0]
            maxi = time_info_test[1]
            
            if (arrive > mini and arrive < maxi) or (depart > mini and less < maxi):
                count += 1
    
    if count > max_count:
        max_count = count


return max_count
        


