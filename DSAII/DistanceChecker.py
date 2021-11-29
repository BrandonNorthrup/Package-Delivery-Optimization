# Brandon Northrup
# Student ID: 001177877

import csv
import datetime


# Opens the Addresses.csv file so that each element can read into the program
# The delimiter is used to separate values so that they can be used in the code through the use of indices
with open('Distances.csv') as csv_distance_file:
    read_distance = csv.reader(csv_distance_file, delimiter=',')
    read_distance = list(read_distance)

# Opens the Addresses.csv file so that each element can read into the program
# The delimiter is used to separate values so that they can be used in the code through the use of indices
with open('Addresses.csv') as csv_address_file:
    read_address = csv.reader(csv_address_file, delimiter=',')
    read_address = list(read_address)

    # Values are read from Distances.csv and used to calculate the distance between two locations
    # Adds the values together to be used for comparison of total distances between different potential routes
    # O(1) complexity
    def check_dist(row_value, column_value, sum_of_dist):
        dist = read_distance[row_value][column_value]
        if dist is '':
            dist = read_distance[column_value][row_value]
        sum_of_dist += float(dist)
        return sum_of_dist

    # Returns the distance from the current location to the next
    # O(1) complexity
    def check_current_dist(row_value, column_value):
        dist = read_distance[row_value][column_value]
        if dist is '':
            dist = read_distance[column_value][row_value]
        return float(dist)
    # Each of these times is when a truck leaves the hub
    # time_3 is used for the first truck's second trip
    time_1_list = ['8:00:00']
    time_2_list = ['9:10:00']
    time_3_list = ['11:00:00']

    # When checking the distance between the current location and the next location, this function will
    # create a new time based on how long the truck will take to get to the point (distance / 18 mph)
    # That time is then converted to the HH:MM:SS format and added to a list, which is used in the for-loop
    # to find the total time spent away from the hub
    # O(N) complexity
    def check_time_truck_1(distance):
        dist_time = distance / 18
        dist_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(dist_time * 60, 60))
        end_time = dist_in_minutes + ':00'
        time_1_list.append(end_time)
        time_sum = datetime.timedelta()
        for i in time_1_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            time_sum += d
        return time_sum

    def check_time_truck_2(distance):
        dist_time = distance / 18
        dist_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(dist_time * 60, 60))
        end_time = dist_in_minutes + ':00'
        time_2_list.append(end_time)
        time_sum = datetime.timedelta()
        for i in time_2_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            time_sum += d
        return time_sum

    def check_time_truck_1_trip_2(distance):
        dist_time = distance / 18
        dist_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(dist_time * 60, 60))
        end_time = dist_in_minutes + ':00'
        time_3_list.append(end_time)
        time_sum = datetime.timedelta()
        for i in time_3_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            time_sum += d
        return time_sum

    # Function used to return an address, which can be used to find the distance between addresses
    # O(1) complexity
    def check_address():
        return read_address

    # Each of these lists are used to hold the most efficient delivery routes
    truck_1_opt = []
    truck_1_opt_index = []
    truck_2_opt = []
    truck_2_opt_index = []
    truck_1_trip_2_opt = []
    truck_1_trip_2_opt_index = []

    # This algorithm uses recursion to optimize the delivery route for each trip that a truck takes.
    # The complexity is O(N^2) because of the two for-loops. It is a greedy algorithm.
    # The algorithm starts with a function that takes three arguments as seen below.
    # The first argument is an unsorted list of packages, second is the truck/trip number, third is the
    # location of the current truck.
    def calc_least_dist(truck_dist_list, truck_num, current_loc):
        # Base case of the algorithm - Used to stop the loop
        if len(truck_dist_list) == 0:
            return truck_dist_list
        else:
            try:
                # Set the low_val to 5000.0. This number needs to be higher than any potential distance that you might
                # have from one delivery to the next. In the instance of this project, the number only needs to be
                # 14.2 or higher. However, 5000 doesn't change the result and it allows any distance that a U.S. trucker
                # would realistically need to travel, allowing for scaling. Setting this below the needed number would
                # fail to account for all packages properly, leading to a lower, but inaccurate result.
                low_val = 5000.0
                new_loc = 0
                # For-loop used to iterate through every available location to check for a value lower than low_val.
                # Low_val will start at 5000, but will change to whatever the minimum distance is to another location.
                # This repeats until all possible locations have been checked.
                for i in truck_dist_list:
                    if check_current_dist(current_loc, int(i[1])) <= low_val:
                        low_val = check_current_dist(current_loc, int(i[1]))
                        new_loc = int(i[1])
                # Once the next location has been chosen, the corresponding package is added to the truck_#_opt and
                # truck_#_opt_index lists. The index is popped from the truck_dist_list so that it doesn't get used
                # again, and the next location is updated. The rest of the algorithm simply calls the same
                # calc_least_dist function from the next location, which allows for recursion until all of the packages
                # have been sorted.
                for i in truck_dist_list:
                    if check_current_dist(current_loc, int(i[1])) == low_val:
                        if truck_num == 1:
                            truck_1_opt.append(i)
                            truck_1_opt_index.append(i[1])
                            index_value = truck_dist_list.index(i)
                            truck_dist_list.pop(index_value)
                            current_loc = new_loc
                            calc_least_dist(truck_dist_list, 1, current_loc)
                        elif truck_num == 2:
                            truck_2_opt.append(i)
                            truck_2_opt_index.append(i[1])
                            index_value = truck_dist_list.index(i)
                            truck_dist_list.pop(index_value)
                            current_loc = new_loc
                            calc_least_dist(truck_dist_list, 2, current_loc)
                        elif truck_num == 3:
                            truck_1_trip_2_opt.append(i)
                            truck_1_trip_2_opt_index.append(i[1])
                            index_value = truck_dist_list.index(i)
                            truck_dist_list.pop(index_value)
                            current_loc = new_loc
                            calc_least_dist(truck_dist_list, 3, current_loc)
            except IndexError:
                pass

    # Insertions for the optimized lists
    # O(N) complexity
    truck_1_opt_index.insert(0, '0')
    truck_2_opt_index.insert(0, '0')
    truck_1_trip_2_opt_index.insert(0, '0')

    # Functions used to return the optimized lists
    # O(1) complexity
    def truck_1_list():
        return truck_1_opt

    def truck_1_index():
        return truck_1_opt_index

    def truck_2_list():
        return truck_2_opt

    def truck_2_index():
        return truck_2_opt_index

    def truck_1_trip_2_list():
        return truck_1_trip_2_opt

    def truck_1_trip_2_index():
        return truck_1_trip_2_opt_index
