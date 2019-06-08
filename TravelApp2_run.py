import pickle
from TravelApp2 import ReservedCost,UnreservedCost,Trip,create_trip,save_trip
filename="pckl_test_file.pkl"

trip_list=create_trip(filename)

# with open(filename, 'wb') as output:
#     pickle.dump(trip_list, output, -1)


save_trip(trip_list,filename)
#
# trip = create_trip()
# save_trip(trip,'pckl_test_file.pkl')
