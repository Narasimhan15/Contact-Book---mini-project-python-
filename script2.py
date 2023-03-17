#Create empty dict
contact = {}

#defining func for display contact 
def display_contact():
    print("Name\t\tcontact number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))

# /t is tab spaces

while True:
    choice = int(input(": 1. add new cont \n 2. search cont \n 3. display cont \n 4. edit cont \n 5.delete \n what's your choice ?"))
    #checking for the choices 
    if choice == 1:
        name = input("what's your name ?")
        phone = input("your number ?")
        contact[name] = phone
    elif choice == 2:
        search_name = input("contact member's name ?")
        if search_name in contact:
            print(search_name," 's contact number is", contact[search_name])
        else:
            print("Not found")
    elif choice == 3:
        #checking whether dictionary is empty or not 
        if not contact:
            print("It's Empty")
        else:
            # call the function here 
            display_contact()
    elif choice == 4:
         edit_contact = input(" What has to be edited")
         # check the edit_contact present in contact
         if edit_contact in contact:
             phone = input("what's the Number ?")
             contact[edit_contact] = phone
             print("contact updated")
             #call the function 
             display_contact()
         else:
              print("It's not found in contact")
    elif choice == 5:
          del_contact = input(" which contact has to be deleted ?")
          #check the contact in dict 
          if del_contact in contact:
               confirm = input(" sure ou want to delete in contact ? tell yes/no")
               if confirm =='yes' or confirm == "YES" or confirm == "Yes":
                    contact.pop(del_contact)
               #call the function 
               display_contact()
          else:
              print("Not found")
    else:
          break 

#This is a Contact Book - mini project using Dictionary 
# Tech stack - Python 


    