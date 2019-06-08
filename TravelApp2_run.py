import pickle
from TravelApp2 import ReservedCost,UnreservedCost,Trip,new_or_edit,save_trip,create_trip
filename="pckl_test_file.pkl"

choice,vacations=new_or_edit(filename)
print("you chose to: "+choice)
trip_list=create_trip(choice,vacations)
print("Trip created")
# with open(filename, 'wb') as output:
#     pickle.dump(trip_list, output, -1)

# print("saving trip....")
save_trip(trip_list,filename)
# print("trip saved")
#
# trip = new_or_edit()
# save_trip(trip,'pckl_test_file.pkl')
