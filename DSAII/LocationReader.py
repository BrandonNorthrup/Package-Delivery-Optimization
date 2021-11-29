# Brandon Northrup
# Student ID: 001177877

import csv
from Hash import HashMap


# Opens the LocationData.csv file so that each element can read into the program
# The delimiter is used to separate values so that they can be used in the code through the use of indices
with open('LocationData.csv') as csv_location_file:
    read_location = csv.reader(csv_location_file, delimiter=',')

    # Creates a hash map using the HashMap class in Hash.py
    create_hash_map = HashMap()

    # Each of these is a list for the three different truck loads
    truck_1 = []
    truck_2 = []
    truck_1_trip_2 = []

    # Creates key-value pairs for each element in the list
    # O(N) complexity
    # This data structure organizes all of the packages into a nested dictionary
    # The nested dictionaries are used as hash map values
    for row in read_location:
        package_ID = row[0]
        address_row_val = row[1]
        city_row_val = row[2]
        state_row_val = row[3]
        zip_row_val = row[4]
        delivery_row_val = row[5]
        size_row_val = row[6]
        note_row_val = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'AT HUB'
        package_attributes = [package_ID,
                              address_location,
                              address_row_val,
                              city_row_val,
                              state_row_val,
                              zip_row_val,
                              delivery_row_val,
                              size_row_val,
                              note_row_val,
                              delivery_start,
                              delivery_status]
        key = package_ID
        attr = package_attributes

        # This section contains any extra rules needed for the packages loaded onto the trucks, such as those that
        # aren't going to arrive at the hub until after the first truck leaves or those that have the wrong address.
        # After the rule is set, it tells the program which truck to put the package on based on its attributes.
        if attr[6] != 'EOD':
            if 'Must' in attr[8] or 'None' in attr[8]:
                truck_1.append(attr)
        if 'Can only be' in attr[8]:
            truck_2.append(attr)
        if 'Delayed' in attr[8]:
            truck_2.append(attr)
        if '84104' in attr[5] and '10:30' not in attr[6] and 'Can only be' not in attr[8] and 'Delayed' not in attr[8]:
            truck_1_trip_2.append(attr)
        if '84117' in attr[5] and '10:30' in attr[6] and 'Can only be' not in attr[8] and 'Delayed' not in attr[8]:
            truck_2.append(attr)
        if 'Wrong address listed' in attr[8]:
            attr[2] = '410 S State St'
            attr[5] = '84111'
            truck_1_trip_2.append(attr)
        if attr not in truck_1 and attr not in truck_2 and attr not in truck_1_trip_2:
            if len(truck_2) > len(truck_1_trip_2):
                truck_1_trip_2.append(attr)
            else:
                truck_2.append(attr)

        # Adds each package to the hash map using the key-value pair
        create_hash_map.insert(key, attr)

    # Creates the initial hash map
    # O(1) complexity
    def get_hash_map():
        return create_hash_map

    # Each of these functions returns the list of packages on the corresponding truck
    # All are O(1) complexity
    def check_truck_1():
        return truck_1

    def check_truck_2():
        return truck_2

    def check_truck_1_trip_2():
        return truck_1_trip_2
