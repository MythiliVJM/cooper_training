
option={1:"Owner", 2: "Tenant", 3:"Approver"}
mylist_house=[]
add_house=[]
class main_class:
    # def __init__(self):
    print("WELCOME!!!\n")
    
    def available_houses(self):
        print()
        if len(mylist_house)==0:
            print("Not available!")
            return False
        for index,house in enumerate(mylist_house):
            print("House No:{0} Details:{1}".format(index,house))
        return True
    
        
class Owner:
    
    def house_details(self):
        house={}
        house["City"]=input("Enter City:")
        house["type_house"]=input("\nEnter type:")
        house["Sqft"]=input("Enter Square Feet:")
        house["Rent"]=input("Enter Rent:")
        mylist_house.append(house)
        print("\nHouse detail added Successfully!!")
        self.user_options(1)
        
    def remove_house(self):
        print("\nAvailable houses:")
        if self.available_houses():
            house_no=int(input("Enter house number to remove: "))
            mylist_house.pop(house_no)
            print("\nHouse Removed Successfully!!")
        self.user_options(1)
        
    def view_HouseDetails(self):
        print("\nRental Requests:")
        if len(add_house)==0:
            print("Not available")
        else:
            for index,request in enumerate(add_house):
                print("Request No: {0} Request: {1}".format(index,request))
        self.user_options(1)



class Tenant:
    
    def rent_request(self):
        self.available_houses()
        request={}
        request["Name"]=input("\nEnter Name: ")
        request["House No"]=input("Enter House No: ")
        request["House location"]=input("Enter house location: ")
        
        add_house.append(request)
        print("\nRequest Submitted Successfully!!")
    

class choice(main_class,Owner,Tenant):
    houses=[]
    def options(self):
        for key,val in option.items():
            print("{0}. {1}".format(key,val))
        choice_user=int(input("Enter option:"))
        print("\nWelcome {0}".format(option[choice_user]))
        self.user_options(choice_user)
        
    
        
    def user_options(self,user_type):
        if user_type==1:
            print("\nowner Options:")
            print("1. House details")
            print("2. Remove")
            print("3. View details")
            option=int(input("\nEnter option number:"))
            if option==1:
                self.house_details()
            elif option==2:
                self.remove_house()
            elif option==3:
                self.view_HouseDetails()
            
            
            
        elif user_type==2:
            print("\nOptions:")
            print("1. Request for house")
            print("2. Quit")
            option=int(input("Enter option number: "))
            if option==1:
                self.rent_request()
            else:
                self.options()
        
        
       

                       
if __name__=="__main__":
    x=choice()
    x.options()
    
