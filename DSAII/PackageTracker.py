# Brandon Northrup
# Student ID: 001177877

from LocationReader import get_hash_map
from LocationReader import check_truck_1
from LocationReader import check_truck_2
from LocationReader import check_truck_1_trip_2
from DistanceChecker import check_dist
from DistanceChecker import check_time_truck_1
from DistanceChecker import check_time_truck_2
from DistanceChecker import check_time_truck_1_trip_2
from DistanceChecker import check_current_dist
from DistanceChecker import calc_least_dist
from DistanceChecker import truck_1_index
from DistanceChecker import truck_1_list
from DistanceChecker import truck_2_index
from DistanceChecker import truck_2_list
from DistanceChecker import truck_1_trip_2_index
from DistanceChecker import truck_1_trip_2_list
import DistanceChecker
import datetime


# Each of these lists is to hold the total distance each truck has travelled
# Truck 1 has two separate lists, one for each trip
truck_1_dist_list = []
truck_2_dist_list = []
truck_1_trip_2_dist_list = []
# Each of these lists contains the delivery status of the packages
# delivery_3 is used for the first truck's second trip
delivery_1 = []
delivery_2 = []
delivery_3 = []
# Each of these times is when a truck leaves the hub
# time_3 is used for the first truck's second trip
time_1 = '8:00:00'
time_2 = '9:10:00'
time_3 = '11:00:00'

# Convert all times to use the HH:MM:SS format
(h, m, s) = time_1.split(':')
convert_time_1 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = time_2.split(':')
convert_time_2 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = time_3.split(':')
convert_time_3 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# For-loop used to update the delivery status once Truck 1 leaves the hub
# O(N) complexity
i = 0
for val in check_truck_1():
    check_truck_1()[i][9] = time_1
    delivery_1.append(check_truck_1()[i])
    i += 1
# For-loop used to check the addresses of the packages on Truck 1 and adds the addresses to the delivery list
# O(N^2) complexity
try:
    variable_count_1 = 0
    for j in delivery_1:
        for k in DistanceChecker.check_address():
            if j[2] == k[2]:
                truck_1_dist_list.append(k[0])
                delivery_1[variable_count_1][1] = k[0]
        variable_count_1 += 1
except IndexError:
    pass
# Use the algorithm to sort the delivery destinations in an efficient order
calc_least_dist(delivery_1, 1, 0)
# Initialize the total distance that Truck 1 has traveled on the first trip
truck_1_total_dist = 0
# For-loop used to calculate the total distance that Truck 1 has traveled on Trip 1
# O(N) complexity
truck_1_package_id = 0
for index in range(len(truck_1_index())):
    try:
        # Calculate the distance that Truck 1 has traveled
        truck_1_total_dist = check_dist(int(truck_1_index()[index]),
                                        int(truck_1_index()[index + 1]),
                                        truck_1_total_dist)
        # Calculate the distance traveled for each delivery
        delivery_distance = check_time_truck_1(check_current_dist(int(truck_1_index()[index]),
                                                                  int(truck_1_index()[index + 1])))
        truck_1_list()[truck_1_package_id][10] = (str(delivery_distance))
        get_hash_map().update(int(truck_1_list()[truck_1_package_id][0]), delivery_1)
        truck_1_package_id += 1
    except IndexError:
        pass

# For-loop used to update the delivery status once Truck 2 leaves the hub
# O(N) complexity
i = 0
for val in check_truck_2():
    check_truck_2()[i][9] = time_2
    delivery_2.append(check_truck_2()[i])
    i += 1
# For-loop used to check the addresses of the packages on Truck 2 and adds the addresses to the delivery list
# O(N^2) complexity
try:
    variable_count_2 = 0
    for j in delivery_2:
        for k in DistanceChecker.check_address():
            if j[2] == k[2]:
                truck_2_dist_list.append(k[0])
                delivery_2[variable_count_2][1] = k[0]
        variable_count_2 += 1
except IndexError:
    pass
# Use the algorithm to sort the delivery destinations in an efficient order
calc_least_dist(delivery_2, 2, 0)
# Initialize the total distance that Truck 2 has traveled on the first trip
truck_2_total_dist = 0
# For-loop used to calculate the total distance that Truck 2 has traveled on the first trip
# O(N) complexity
truck_2_package_id = 0
for index in range(len(truck_2_index())):
    try:
        # Calculate the distance that Truck 2 has traveled
        truck_2_total_dist = check_dist(int(truck_2_index()[index]),
                                        int(truck_2_index()[index + 1]),
                                        truck_2_total_dist)
        # Calculate the distance traveled for each delivery
        delivery_distance = check_time_truck_2(check_current_dist(int(truck_2_index()[index]),
                                                                  int(truck_2_index()[index + 1])))
        truck_2_list()[truck_2_package_id][10] = (str(delivery_distance))
        get_hash_map().update(int(truck_2_list()[truck_2_package_id][0]), delivery_2)
        truck_2_package_id += 1
    except IndexError:
        pass

# For-loop used to update the delivery status once Truck 1 leaves the hub for Trip 2
# O(N) complexity
i = 0
for val in check_truck_1_trip_2():
    check_truck_1_trip_2()[i][9] = time_3
    delivery_3.append(check_truck_1_trip_2()[i])
    i += 1
# For-loop used to check the addresses of the packages on Truck 1, Trip 2 and adds the addresses to the delivery list
# O(N^2) complexity
try:
    variable_count_3 = 0
    for j in delivery_3:
        for k in DistanceChecker.check_address():
            if j[2] == k[2]:
                truck_1_trip_2_dist_list.append(k[0])
                delivery_3[variable_count_3][1] = k[0]
        variable_count_3 += 1
except IndexError:
    pass
# Use the algorithm to sort the delivery destinations in an efficient order
calc_least_dist(delivery_3, 3, 0)
# Initialize the total distance that Truck 1 has traveled on the second trip
truck_1_trip_2_total_dist = 0
# For-loop used to calculate the total distance that Truck 1 has traveled on Trip 2
# O(N) complexity
truck_1_trip_2_package_id = 0
for index in range(len(truck_1_trip_2_index())):
    try:
        # Calculate the distance that Truck 1 has traveled on Trip 2
        truck_1_trip_2_total_dist = check_dist(int(truck_1_trip_2_index()[index]),
                                               int(truck_1_trip_2_index()[index + 1]),
                                               truck_1_trip_2_total_dist)
        # Calculate the distance traveled for each delivery
        delivery_distance = check_time_truck_1_trip_2(check_current_dist(int(truck_1_trip_2_index()[index]),
                                                                         int(truck_1_trip_2_index()[index + 1])))
        truck_1_trip_2_list()[truck_1_trip_2_package_id][10] = (str(delivery_distance))
        get_hash_map().update(int(truck_1_trip_2_list()[truck_1_trip_2_package_id][0]), delivery_3)
        truck_1_trip_2_package_id += 1
    except IndexError:
        pass


# Add the distances of all three trips to get the total
# O(1) complexity
def distance_total():
    total_dist = truck_1_total_dist + truck_2_total_dist + truck_1_trip_2_total_dist
    return total_dist
