import pickle
from TravelApp2 import ReservedCost,UnreservedCost,Trip,create_trip,save_trip
filename="pckl_test_file.pkl"

trip_list=create_trip(filename)
print("Trip created")
# with open(filename, 'wb') as output:
#     pickle.dump(trip_list, output, -1)

print("saving trip....")
save_trip(trip_list,filename)
print("trip saved")
#
# trip = create_trip()
# save_trip(trip,'pckl_test_file.pkl')
