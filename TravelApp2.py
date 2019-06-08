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

    def __str__(self):
        return(("sub_type={s}:company={c}\npointa={a}-pointb={b}:\nstartdate={sd} starttime={st}")
            .format(t=self.type,s=self.sub_type,a=self.pointa,
            b=self.pointb,sd=self.start_date, st=self.start_time,
            c=self.company,conf=self.conf))


class UnreservedCost():
    #type=[food,merch,fee]
    def __init__(self, type='', price='Unknown', item='', pay_method='',
        date='', loc='', misc=None
    ):
        self.type = type
        self.price = price
        self.item = item
        self.pay_method = pay_method
        self.date = date
        self.loc = loc
        self.misc = misc

    def __str__(self):
        return ("{i} ${p}\nFrom: {l}".format(i=self.item,p=self.price,\
        l=self.loc))


##to save classes, creat a file like '(a,b,c,d)' so it can be read back into a class later

class Trip():
    def __init__(self,destination, approx_date='None'):
        self.trip_plans = []
        self.destination = destination
        self.approx_date = approx_date

    #set up travel plans thru the appropriate classes here
    def __str__(self):
        return self.destination + ' '+ self.approx_date

    def add_reserved_cost(self,**kwargs):
        x = ReservedCost(**kwargs)
        self.trip_plans.append(x)
        # ny=Trip('New York')
        # ny.add_reserved_cost(price=20,pointa='Phx,Az',pointb='NewYork,NY',sub_type='flight',company='AmericanAir',start_time='11pm')
        # print(ny.trip_plans[0])

    def add_unreserved_cost(self,**kwargs):
        x = UnreservedCost(**kwargs)
        self.trip_plans.append(x)
        # ny=Trip('New York')
        # ny.add_unreserved_cost(price=20,loc='Phx,Az',item='lunch',type='food')
        # print(ny.trip_plans[0])

'''
####start program and read pre existing data
to open saved file or create a new one
'''

            # while choice != 'new' or choice !='edit' or choice !='quit':
            #     choice = input("enter 'new' or 'edit' ")
            #     if choice == 'quit':
            #         pass
            #     elif choice== 'new' or choice =='edit':

######add clause to pop off any None types

def create_trip(filename):
    try:
        with open(filename, 'rb') as f:
            vacations = pickle.load(f)
            # print(vacations)
            for t in vacations:
                print(t)
            #     print(t.destination)
            #     for p in range(len(t.trip_plans)):
            #         print(t.trip_plans[p])
            print("Would you like to create a new trip plan or edit an existing trip plan?")
            choice = input("enter 'new' or 'edit' ")

    except (FileNotFoundError,TypeError):
        print("No pre-existing trip plans file found\nPlease create a new one")
        choice = 'new'
    except:
        print('Program Error, Contact Administrator')
        print(sys.exc_info()[0]) #throws other errors, using to see error print
    finally:
        if choice.lower() == 'new':
            # option to create a new Trip obj
            name_trip=None
            while name_trip==None:
                trip_dest=input("Trip Destination: ")
                appr_name=input("Is this the correct destination? "+trip_dest)
                if appr_name.lower()[0]=='y':
                    name_trip=True

            print("What type of charge is it?\nTransport, Lodging, Event\nMeal, Merchandise, Fee")
            charge_type_full = input()
            charge_type=charge_type_full.lower()[0]
            trip = Trip(trip_dest)

            if charge_type=='t' or charge_type=='l' or charge_type=='e':
                #list of questions saved to input, final look to approve. otherwise redo
                print("Please complete the following fields.")
                type=charge_type#trnasport/Lodging
                sub_type=input("What is the charge for? ")
                price=input("Price: ")
                pay_method=input("Payment Method: ")
                pointa=input("Location: ")
                start_date=input("Start Date: ")
                start_time=input("Start Time: ")
                pointb=input("End Location: ")
                end_date=input("End Date: ")
                end_time=input("End Time: ")
                conf=input("Confirmation details: ")
                company=input("Company/Brand: ")
                misc=input("Misc. details: ")

                trip.add_reserved_cost(type=type, price=price, pay_method=pay_method,
                    pointa=pointa, start_date=start_date, start_time=start_time,
                    pointb=pointb, end_date=end_date, end_time=end_time,
                    sub_type=sub_type, conf=conf, company=company, misc=misc)

            elif charge_type=='meal' or charge_type=='merch' or charge_type=='fee':
                print("Please complete the following fields.")
                type=charge_type #transport/Lodging
                item = input("What is the charge for? ")
                price=input("Price: ")
                pay_method=input("Payment Method: ")
                loc=input("Location: ")
                date=input("Date: ")
                misc=input("Misc. details: ")

                trip.add_unreserved_cost(type=type,price=price,item=item,
                    pay_method=pay_method,date=date,loc=loc,misc=misc)

            print('\n')
            print(trip.trip_plans[0])

        elif choice.lower() == 'edit':
            #figure out how to edit Trip attributes
            print('What trip would you like to edit? ')
            vacay_list=[]
            for v in vacations:
                vacay_list.append(v.destination)
            print(vacay_list)
            trip_choice=None
            while trip_choice not in vacay_list:
                print('Please select a trip to edit')
                trip_choice=input()
            print(trip_choice)
            print(vacay_list.index(trip_choice))
            ### TODO: access list item with index and display trip details
                #Add ability to add new details or edit old ones



    # try:
    #     trip_list=vacations
    #     trip_list.append(trip)
    # except AttributeError:
    #     trip_list=[vacations,]
    #     trip_list.append(trip)
    # print(trip_list)
    # return trip_list

    # print(type(vacations))
def save_trip(trip_list, filename):
    #I want all trips to be in one file, read/edited/saved to
    #use pop() to remove edit file, to append later
    '''
    to save trip obj data to be accessed at opening of program
    combine obj's into a list to be uploaded to file
    '''
    try:
        with open(filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(trip_list, output, -1)
    except UnboundLocalError:
        print('Cannot Save Trip, Error')
    except:
        print('other error')
    # hawaii = Trip('Hawaii','Nov 2019') #example, convert to actual data string later
    # save_trip(hawaii, 'pckl_test_file.pkl')


#### TODO: split into smaller chunks of functions
