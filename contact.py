import pandas as pd

global user_input

class Contact:
    
    
    def __init__(self) -> None:
        try:
            self.contact_info = pd.read_csv('Contact.csv')
        except:
            self.contact_info = pd.DataFrame(columns=['Name', 'Phone Number', 'Email Address',"Address"])
    
    def add_contact(self):
        while True: 
            print('Enter "Done" after adding all contactes')
            user_name = input("Enter Name :- ")
            if user_name == "Done" or user_name == "done":
                self.save_changes()
                break
            else:
                phone_number = input("Enter Phone Number :- ")
                email_address = input("Enter Email Address :- ")
                address = input("Enter Address :- ")
                self.contact_info.loc[len(self.contact_info)] = [user_name, phone_number, email_address, address]
    
    def view_contact(self):
        if self.contact_info.empty:
            print()
            return "Please insert Contacts and try again"
        else:
            print()
            return self.contact_info
            
    def search_contact(self):
        global user_input
        print()
        user_input = input("Enter Contact name or number :-")
        if self.contact_info[(self.contact_info['Name']==user_input) | (self.contact_info['Phone Number']==user_input)].empty:
            print()
            return "No contact found"
        else:
            print()
            return self.contact_info[(self.contact_info['Name']==user_input) | (self.contact_info['Phone Number']==user_input)]
        
    def update_contact(self):
        global user_input
        user_input = self.search_contact()
        if user_input is "No contact found":
            print("No contact found")
            return ""
        print()
        print(user_input)
        while True:
            print()
            print("Enter the corresponding number of detail to change \n 1.Name  2.Phone number  3.Email address  4.Address  5.Exit")
            try:
                user_input2 = int(input())
                if user_input2 not in range(1,5):
                    raise Exception
            except:
                print()
                print("Please enter from above given number and try again")
            
            if user_input2 == 5:
                self.save_changes()
                break
            changed_value = input("Enter new value :- ")
            if user_input2 == 1:
                user_input['Name'] = changed_value
            elif user_input2 == 2:
                user_input['Phone Number'] = changed_value
            elif user_input2 == 3:
                user_input['Email Address'] = changed_value
            elif user_input2 == 4:
                user_input['Address'] = changed_value
            self.contact_info.update(user_input)
            print()
            print("Update successful. Updated contact information is :-")
            print(user_input)
            
    def delete_contact(self):
        global user_input
        user_input = self.search_contact()
        if user_input is "No contact found":
            print("No contact found")
            return ""
        print()
        self.contact_info.drop(user_input.index,inplace=True)
        print("Data Deleted Successfull")
        self.save_changes()
        print()

    def save_changes(self):
        self.contact_info.to_csv('Contact.csv',index=False)

s1 = Contact()
while True:
    print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delect Contact\n6. Exit")
    try:
        user_input = int(input())
        if user_input not in range(1,7):
            raise Exception
    except:
        print("Please enter number from above given list and try again")
        continue
    if user_input == 6:
        break
    elif user_input == 1:
        s1.add_contact()
    elif user_input == 2:
        print(s1.view_contact())
        print()
    elif user_input == 3:
        print(s1.search_contact())
        print()
    elif user_input == 4:
        s1.update_contact()
    elif user_input == 5:
        s1.delete_contact()
exit()