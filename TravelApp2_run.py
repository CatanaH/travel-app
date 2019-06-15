import pickle
from TravelApp2 import ReservedCost,UnreservedCost,Trip,new_or_edit,save_trip_list,create_new_trip,create_vacaylist_for_save,create_edit_trip
filename="pckl_test_file.pkl"

while True:
    #use while loop to keep active till quiting program
    choice,vacations=new_or_edit(filename)
    print("you chose to: "+choice)

    #need to check weather new or edit func
    if choice.lower() == 'new':
        trip= create_new_trip()
        print("new trip created")
        trip_list=create_vacaylist_for_save(vacations,trip,choice)
        print("new trip list created")

    elif choice.lower() == 'edit':
        print("\nnow edit function")
        trip,trip_num=create_edit_trip(choice,vacations)
        print("Trip created")
        trip_list=create_vacaylist_for_save(vacations,trip,choice,trip_num)
        print("new trip list created")
    else:
        #to grab 'quits' and other str
        pass

    print("saving trip....")
    save_trip_list(trip_list,filename)

    quit=input("would you like to quit?")
    if quit =="y":
        break
