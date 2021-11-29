# Brandon Northrup
# Student ID: 001177877

from LocationReader import get_hash_map
from PackageTracker import distance_total
import datetime


class Main:
    # Initial message when starting the program. This message tells the user how to use the interface.
    print('Welcome! Current route completed in', "{0:.2f}".format(distance_total(), 2), 'miles.')
    # If the user enters "1", they will be asked to provide a package ID, and a time to go with it
    # If the user enters "2", they will be asked to provide a time for which they want the status of all packages
    # O(N) complexity
    user_input = input("Please type '1' to search for a specific package, "
                       "'2' to view the status of all packages, "
                       "or 'exit' to close the application: ")
    # When the user wants the status of a specific package at a specific time:
    if user_input == '1':
        try:
            package_id = input("Please enter a package ID or type 'exit': ")
            if package_id.lower() == 'exit':
                print('\nYou entered:', package_id)
                exit()
            departure_time = get_hash_map().get_hash_value(str(package_id))[9]
            delivery_time = get_hash_map().get_hash_value(str(package_id))[10]
            package_status = input("Please enter a time (HH:MM:SS) or type 'exit': ")
            # Close the program when the user types "exit"
            if package_status.lower() == 'exit':
                print('\nYou entered:', package_status)
                exit()

            # Convert all times to use the HH:MM:SS format
            (h, m, s) = package_status.split(':')
            convert_input_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            (h, m, s) = departure_time.split(':')
            convert_departure_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            (h, m, s) = delivery_time.split(':')
            convert_delivery_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            # Check if the package is at the hub
            if convert_departure_time >= convert_input_time:
                get_hash_map().get_hash_value(str(package_id))[9] = 'Leaves at ' + departure_time
                get_hash_map().get_hash_value(str(package_id))[10] = 'AT HUB'
                print('\nPackage ID:',
                      get_hash_map().get_hash_value(str(package_id))[0],
                      '\nStreet Address:',
                      get_hash_map().get_hash_value(str(package_id))[2],
                      get_hash_map().get_hash_value(str(package_id))[3],
                      get_hash_map().get_hash_value(str(package_id))[4],
                      get_hash_map().get_hash_value(str(package_id))[5],
                      '\nRequired Delivery Time:',
                      get_hash_map().get_hash_value(str(package_id))[6],
                      '\nPackage Weight:',
                      get_hash_map().get_hash_value(str(package_id))[7],
                      '\nTruck Status:',
                      get_hash_map().get_hash_value(str(package_id))[9],
                      '\nDelivery Status:',
                      get_hash_map().get_hash_value(str(package_id))[10])
            elif convert_departure_time <= convert_input_time:
                # Check if the package is in transit
                if convert_input_time < convert_delivery_time:
                    get_hash_map().get_hash_value(str(package_id))[9] = 'Left at ' + departure_time
                    get_hash_map().get_hash_value(str(package_id))[10] = 'IN TRANSIT'
                    print('\nPackage ID:',
                          get_hash_map().get_hash_value(str(package_id))[0],
                          '\nStreet Address:',
                          get_hash_map().get_hash_value(str(package_id))[2],
                          get_hash_map().get_hash_value(str(package_id))[3],
                          get_hash_map().get_hash_value(str(package_id))[4],
                          get_hash_map().get_hash_value(str(package_id))[5],
                          '\nRequired Delivery Time:',
                          get_hash_map().get_hash_value(str(package_id))[6],
                          '\nPackage Weight:',
                          get_hash_map().get_hash_value(str(package_id))[7],
                          '\nTruck Status:',
                          get_hash_map().get_hash_value(str(package_id))[9],
                          '\nDelivery Status:',
                          get_hash_map().get_hash_value(str(package_id))[10])
                # Check if the package has been delivered
                # If the package has been delivered, show the time that it was delivered
                else:
                    get_hash_map().get_hash_value(str(package_id))[9] = 'Left at ' + departure_time
                    get_hash_map().get_hash_value(str(package_id))[10] = 'DELIVERED at ' + delivery_time
                    print('\nPackage ID:',
                          get_hash_map().get_hash_value(str(package_id))[0],
                          '\nStreet Address:',
                          get_hash_map().get_hash_value(str(package_id))[2],
                          get_hash_map().get_hash_value(str(package_id))[3],
                          get_hash_map().get_hash_value(str(package_id))[4],
                          get_hash_map().get_hash_value(str(package_id))[5],
                          '\nRequired Delivery Time:',
                          get_hash_map().get_hash_value(str(package_id))[6],
                          '\nPackage Weight:',
                          get_hash_map().get_hash_value(str(package_id))[7],
                          '\nTruck Status:',
                          get_hash_map().get_hash_value(str(package_id))[9],
                          '\nDelivery Status:',
                          get_hash_map().get_hash_value(str(package_id))[10])
            print('\nYou entered:', package_status)
        # Give an error message and close the program when the user types something invalid
        except ValueError:
            print('\nInvalid input')
            exit()
        exit()

    # When the user wants the status of all packages at a specific time:
    elif user_input == '2':
        try:
            package_status = input("Please enter a time (HH:MM:SS) or type 'exit': ")
            # Close the program when the user types "exit"
            if package_status.lower() == 'exit':
                print('\nYou entered:', package_status)
                exit()
            # Initialize the departure and delivery times before entering the for-loop below and
            # convert all times to use the HH:MM:SS format
            departure_time = 0
            delivery_time = 0
            (h, m, s) = package_status.split(':')
            convert_departure_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            convert_delivery_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            convert_input_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # For-loop to iterate through all packages
            # O(N^2) complexity
            for package_id in range(1, 41):
                try:
                    departure_time = get_hash_map().get_hash_value(str(package_id))[9]
                    delivery_time = get_hash_map().get_hash_value(str(package_id))[10]
                    # Convert all times to use the HH:MM:SS format
                    (h, m, s) = departure_time.split(':')
                    convert_departure_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    (h, m, s) = delivery_time.split(':')
                    convert_delivery_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                except ValueError:
                    pass
                # Check which packages are at the hub
                if convert_departure_time >= convert_input_time:
                    get_hash_map().get_hash_value(str(package_id))[9] = 'Leaves at ' + departure_time
                    get_hash_map().get_hash_value(str(package_id))[10] = 'AT HUB'
                    print('\nPackage ID:',
                          get_hash_map().get_hash_value(str(package_id))[0],
                          '\nStreet Address:',
                          get_hash_map().get_hash_value(str(package_id))[2],
                          get_hash_map().get_hash_value(str(package_id))[3],
                          get_hash_map().get_hash_value(str(package_id))[4],
                          get_hash_map().get_hash_value(str(package_id))[5],
                          '\nRequired Delivery Time:',
                          get_hash_map().get_hash_value(str(package_id))[6],
                          '\nPackage Weight:',
                          get_hash_map().get_hash_value(str(package_id))[7],
                          '\nTruck Status:',
                          get_hash_map().get_hash_value(str(package_id))[9],
                          '\nDelivery Status:',
                          get_hash_map().get_hash_value(str(package_id))[10]),
                elif convert_departure_time <= convert_input_time:
                    # Check which packages are in transit
                    if convert_input_time < convert_delivery_time:
                        get_hash_map().get_hash_value(str(package_id))[9] = 'Left at ' + departure_time
                        get_hash_map().get_hash_value(str(package_id))[10] = 'IN TRANSIT'
                        print('\nPackage ID:',
                              get_hash_map().get_hash_value(str(package_id))[0],
                              '\nStreet Address:',
                              get_hash_map().get_hash_value(str(package_id))[2],
                              get_hash_map().get_hash_value(str(package_id))[3],
                              get_hash_map().get_hash_value(str(package_id))[4],
                              get_hash_map().get_hash_value(str(package_id))[5],
                              '\nRequired Delivery Time:',
                              get_hash_map().get_hash_value(str(package_id))[6],
                              '\nPackage Weight:',
                              get_hash_map().get_hash_value(str(package_id))[7],
                              '\nTruck Status:',
                              get_hash_map().get_hash_value(str(package_id))[9],
                              '\nDelivery Status:',
                              get_hash_map().get_hash_value(str(package_id))[10])
                    # Check which packages have been delivered and show the time
                    else:
                        get_hash_map().get_hash_value(str(package_id))[9] = 'Left at ' + departure_time
                        get_hash_map().get_hash_value(str(package_id))[10] = 'DELIVERED at ' + delivery_time
                        print('\nPackage ID:',
                              get_hash_map().get_hash_value(str(package_id))[0],
                              '\nStreet Address:',
                              get_hash_map().get_hash_value(str(package_id))[2],
                              get_hash_map().get_hash_value(str(package_id))[3],
                              get_hash_map().get_hash_value(str(package_id))[4],
                              get_hash_map().get_hash_value(str(package_id))[5],
                              '\nRequired Delivery Time:',
                              get_hash_map().get_hash_value(str(package_id))[6],
                              '\nPackage Weight:',
                              get_hash_map().get_hash_value(str(package_id))[7],
                              '\nTruck Status:',
                              get_hash_map().get_hash_value(str(package_id))[9],
                              '\nDelivery Status:',
                              get_hash_map().get_hash_value(str(package_id))[10])
            print('\nYou entered:', package_status)
        # Give an error message and close the program if something goes wrong with the program
        except IndexError:
            print(IndexError)
            exit()
        # Give an error message and close the program when the user types something invalid
        except ValueError:
            print('\nInvalid input')
            exit()
        exit()
    # Close the program when the user types "exit"
    elif user_input.lower() == 'exit':
        print('\nYou entered:', user_input)
        exit()
    # Give an error message and close the program when the user types something invalid
    else:
        print('\nInvalid input')
        print('You entered:', user_input)
        exit()
