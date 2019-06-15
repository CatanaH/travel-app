import pickle
'''
travel app, flight, housing, entertainment, transport, food, merch.
use classes to sort and organize and call data as needed

#organizes on calendar, shows what has not been booked for dates, ex. no hotel wednesday night

enter ahead of time:
flight:price, datetime,airline, airports, conf# seat#?
housing: price, dates, location, conf#
transport: price, dates, company, pickup/dropoff, conf#
entertainment: event, price, datetime, conf#, location

track as u go:
food: price, datetime
merch: item, location, price
Fee:
'''


class ReservedCost():
    #type: transport,lodging,event; sub_type:[flight,train,boat],[hotel,bnb,camping]
    def __init__(
    self,type='', price='Unknown', pay_method='', pointa='',
        start_date='', start_time='', pointb='', end_date='',
        end_time='', sub_type='', conf='', company='', misc=None
    ):
        self.type=type
        self.price=price
        self.pay_method=pay_method
        self.pointa=pointa
        self.start_date=start_date
        self.start_time = start_time
        self.pointb = pointb
        self.end_date = end_date
        self.end_time = end_time
        self.sub_type = sub_type
        self.conf = conf
        self.company = company
        self.misc=misc


    def edit_cost(self):
        #should maybe be using a dictionary here? for printing and item assignment instead of list?
        edit_lst=[]
        for i in [(self.type,'type'),(self.price,'price'),(self.pay_method,'payment method'),(self.pointa,'pointa'),(self.start_date,'start_date'),(self.start_time,'start_time'),(self.pointb,'pointb'),(self.end_date,'end_date'),(self.end_time,'end_time'),(self.sub_type,'sub_type'),(self.conf,'conf'),(self.company,'company'),(self.misc,'misc')]:
            print("{}={}\ttype new info or 'enter' to skip".format(i[1],i[0]))
            edited_ans=input()
            if edited_ans =='':
                edit_lst.append(i[0])
            else:
                edit_lst.append(edited_ans)

        if len(edit_lst) ==13:
            self.type=edit_lst[0]
            self.price=edit_lst[1]
            self.pay_method=edit_lst[2]
            self.pointa=edit_lst[3]
            self.start_date=edit_lst[4]
            self.start_time = edit_lst[5]
            self.pointb = edit_lst[6]
            self.end_date = edit_lst[7]
            self.end_time = edit_lst[8]
            self.sub_type =edit_lst[9]
            self.conf = edit_lst[10]
            self.company = edit_lst[11]
            self.misc=edit_lst[12]
            print("All updated")
        else:
            print("error, could not update")




    def __str__(self):
        return(("type= {}\nprice={}\npay_method={}\npointa={}\nstart_date={}\nstart_time= {}\npointb= {}\nend_date= {}\nend_time= {}\nsub_type= {}\nconf= {}\ncompany= {}\nmisc= {}").format(self.type,\
            self.price, self.pay_method, self.pointa, self.start_date,\
            self.start_time, self.pointb, self.end_date,self.end_time,\
            self.sub_type, self.conf, self.company, self.misc))





class UnreservedCost():
    #type=[food,merch,fee]
    def __init__(self, type='', price='Unknown', item='', pay_method='',
        date='', loc='', misc=None
    ):
    #migth be able to change preassignment to '' and remove the whole kwargs thing
    #and edit variables only thru the edit_cost()
        self.type = type
        self.price = price
        self.item = item
        self.pay_method = pay_method
        self.date = date
        self.loc = loc
        self.misc = misc

    def edit_cost(self):
        #couldnt get loop asignment to work,
        #saved answers to list for asignment after loop
        edit_lst=[]
        for i in [(self.type,'type'),(self.price,'price'),(self.item,'item'),(self.pay_method,'pay_method'),(self.date,'date'),(self.loc,'loc'),(self.misc,'misc')]:
            print("{}={}\ttype new info or 'enter' to skip".format(i[1],i[0]))
            edited_ans=input()
            if edited_ans =='':
                edit_lst.append(i[0])
            else:
                edit_lst.append(edited_ans)

        if len(edit_lst) ==7:
            i=edit_lst
            self.type = i[0]
            self.price = i[1]
            self.item = i[2]
            self.pay_method = i[3]
            self.date = i[4]
            self.loc = i[5]
            self.misc = i[6]
            print("All updated")
        else:
            print("error, could not update")



    def __str__(self):
        return ("type= {}\nprice= {}\nitem= {}\npay_method= {}\ndate= \
            {}\nloc = {}\nmisc = {}".format(self.type,self.price,self.item,
            self.pay_method,self.date,self.loc,self.misc
            ))



class Trip():
    def __init__(self,destination, approx_date='None'):
        self.trip_plans = []
        self.destination = destination
        self.approx_date = approx_date

    def __str__(self):
        return self.destination + ' '+ self.approx_date

    def remove_cost(self, index_place):
        confirm = input("are you sure you want to delete this cost:\n{}\n[Y/n]".format(self.trip_plans[index_place]))
        if confirm == 'Y':
            self.trip_plans.pop(index_place)
            print("trip cost has been deleted")
        else:
            print("action cancelled\n")

    def update_trip_title(self):
        edit_lst=[]
        for i in [(self.destination,'destination'),(self.approx_date,'approximate date range')]:
            print("{}={}\ttype new info or 'enter' to skip".format(i[1],i[0]))
            edited_ans=input()
            if edited_ans =='':
                edit_lst.append(i[0])
            else:
                edit_lst.append(edited_ans)

        if len(edit_lst) ==2:
            self.destination = edit_lst[0]
            self.approx_date = edit_lst[1]
            print("All updated")
        else:
            print("error, could not update")

    #set up travel plans thru the appropriate classes here

    def add_reserved_cost(self,**kwargs):
        x = ReservedCost(**kwargs)
        x.edit_cost()
        self.trip_plans.append(x)

    def add_unreserved_cost(self,**kwargs):
        x = UnreservedCost(**kwargs)
        x.edit_cost()
        self.trip_plans.append(x)

    def add_cost(self):
        print("What type of charge is it?\nTransport, Lodging, Event\nMeal, Merchandise, Fee")
        charge_type_full = input()
        charge_type=charge_type_full.lower()[0]
        #add something to auto assign type to charge_type

        if charge_type=='t' or charge_type=='l' or charge_type=='e':
            self.add_reserved_cost()

        elif charge_type=='meal' or charge_type=='m' or charge_type=='f':
            self.add_unreserved_cost()

        # print('\n')
        # print(self.trip_plans[0])

'''
####start program and read pre existing data
to open saved file or create a new one
'''

def load_trip_files(filename):
    with open(filename, 'rb') as f:
        vacations = pickle.load(f)
        return vacations

def vacay_trips_display(vacations):
    for num,trip in enumerate(vacations):
        print(str(num)+'. '+trip.destination+" "+trip.approx_date)
    print("--end of Vacations list--\n") #test line/ delete later

def new_or_edit(filename):
    try:
        vacations = load_trip_files(filename)
        # print(vacations)
        vacay_trips_display(vacations)
        print("Would you like to create a new trip plan or edit an existing trip plan?")
        choice = input("enter 'new' or 'edit' ")
        #add logic for inf input not new or edit
        choice=choice.lower()

    except (FileNotFoundError,TypeError):
        print("No pre-existing trip plans file found\nPlease create a new one")
        choice = 'new'
    except:
        print('Program Error, Contact Administrator')
        print(sys.exc_info()[0]) #throws other errors, using to see error print
        choice=None
    finally:
        return choice,vacations

charge_options = ['Transport','Lodging','Event','Meal','Merchandise','Fee']
#possibly make charge opt a dict with keys as type and vaule list as subtype


def create_new_trip():
        name_trip=None
        while name_trip==None:
            trip_dest=input("Trip Destination: ")
            appr_name=input("Is this the correct destination? "+trip_dest+" ")
            if appr_name.lower()[0]=='y':
                name_trip=True
            approx_date=input("trip date")

        trip = Trip(trip_dest,approx_date) #creating a trip object with new name
        # trip.add_cost()
        #when creating new trip, nedd to loop options at end to add more at one time

        return trip

def create_edit_trip(choice,vacations):
    if choice.lower() == 'edit':
        vacay_trips_display(vacations)
        print('which trip would you like to open? ')

        while True:
            trip_num=input('please enter the number') #using number choices to grab vs typed names
            try:
                trip_num=int(trip_num)
                if trip_num < len(vacations):
                    break
            except:
                if trip_num =='quit':
                    break

        if trip_num =='quit':
            return None

        trip=vacations[trip_num]
        print('\n')
        print(trip)
        def trip_plans_display(trip):
            for num,cost in enumerate(trip.trip_plans):
                print(str(num)+': '+cost.type)
            print("end of scheduled plans\n")

        trip_plans_display(trip) #summary to help make descision
        while True:
            edit_trip=input("Details: view, add, edit, delete cost, renametrip, delete trip, quit/done")

            if edit_trip=='add':
                print("add chosen")
                trip.add_cost()
                print(trip.trip_plans[-1]) #prints most recently added detail

            elif edit_trip.lower()[0]=='r':
                trip.update_trip_title()
                print(trip)

            elif edit_trip=='quit' or edit_trip=='done':
                print("Quit chosen, loop breaking")
                break


            elif edit_trip == 'delete trip':
                    print(trip)
                    trip_plans_display(trip)
                    confirm=input("are you sure you want to delete this entire trip? [Y/n]")
                    if confirm=='Y':
                        vacations.pop(trip_num)
                        print("trip removed from vacation database")
                        return vacations
                    else:
                        print("action cancelled")



            else:
                trip_plans_display(trip)
                print("end of nested function") #just for testing/ delete later
                print('which cost would you like to {}? '.format(edit_trip))

                while True:
                    cost_num=input('please enter the number') #using number choices to grab vs typed names
                    #clean up int(cost_num) into one variable?
                    #have to fix so int() doesnt break str
                    try:
                        cost_num=int(cost_num)
                        if int(cost_num) < len(trip.trip_plans):
                            break
                    except:
                        if cost_num =='quit' or cost_num=='done':
                            edit_trip='quit'#doesnt actually quit, just continues loop to then quit
                            #sloppy exit but isnt breaking, find better way if possible
                            break

                if edit_trip=='edit':
                    print("\nedit chosen")
                    trip.trip_plans[int(cost_num)].edit_cost()
                    print(trip.trip_plans[int(cost_num)])

                elif edit_trip =='view':
                    print(trip.trip_plans[int(cost_num)])
                elif edit_trip=="delete cost":
                    trip.remove_cost(int(cost_num))


        print('Full trip details:')
        for t in trip.trip_plans: #print full summary after
            print(t)
        print("end of full trip summary\n")

    return (trip,trip_num)


###### this is for saving trip
def create_vacaylist_for_save(vacations,trip,choice,trip_num=None):

    if vacations == None:
        trip_list=trip

    elif choice == 'edit':
        #should have prior writen logic to index trip to be edited, use same here
        vacations[trip_num]=trip
        trip_list=vacations

    elif choice == 'new':
        try: #if list has any Nonetype objects remove them
            trip_list=vacations
            trip_list.append(trip)
            for i in trip_list:
                if i == None:
                    trip_list.pop(trip_list.index(i))
        except AttributeError: #if vacations is only one item, convert to list
            trip_list=[vacations,]
            trip_list.append(trip)

    elif choice == 'quit' or choice == 'done':
        return None

    else:
        print('Failure adding item to vacations list\n')
        return None #to avoid breaking if this clause runs

    vacay_trips_display(trip_list)
    return trip_list  #Comment out when testing to avoid saving changes


def save_trip_list(trip_list, filename):
    '''
    to save trip obj data to be accessed at opening of program
    combine obj's into a list to be uploaded to file
    #I want all trips to be in one file, read/edited/saved to
    '''
    if trip_list == None:
        print("No Data to save\nCancelling operation.")
    else:
        try:
            with open(filename, 'wb') as output:  # Overwrites any existing file.
                pickle.dump(trip_list, output, -1)
                print('trip list officially saved')
        except UnboundLocalError:
            print('Cannot Save Trip, Error')
        except:
            print('other error')


#### TODO: split into smaller chunks of functions

#add logic to customize class per charge type

## ?whole containing loop looking for any inputs that say quit? to end program immediatly?
# set up count for tracking costs total


## added tuple unpacking on line 19 of _run to then feed into next function, but having problem with it returning a NOnetype when 'quit' i think line 289ish
