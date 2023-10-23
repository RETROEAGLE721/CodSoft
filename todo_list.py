from datetime import datetime,date
import pandas as pd

class TODO_list:


    def __init__(self):
        try:
            self.todo_list = pd.read_csv(str(date.today())+"_TODO_list.csv")
        except:
            self.todo_list = pd.DataFrame()

    def add(self):
        task_list_name = []
        priority_list = []
        due_date_list = []
        while True:
            print('Enter "done" when all task are inserted')
            task_name = input("Enter task :-")
            if task_name == "done" or task_name == "Done":
                break
            priority = input("Enter task priority(h-high, m-medium, l-low) :- ")
            due_date = datetime.strptime(input("Enter task Due Date(DD-MM-YYYY) :- "), '%d-%m-%Y').date() 
            task_list_name.append(task_name)
            priority_list.append(priority)
            due_date_list.append(due_date)
        task_list_name = {'Tasks':task_list_name,'Priority':priority_list, 'Complete' : [0]*len(task_list_name),"Due Date" : due_date_list}
        todo_list = pd.DataFrame(task_list_name)

        if self.todo_list.empty:
            self.save_list(todo_list)
        else:
            todo_list = pd.concat([self.todo_list,todo_list],ignore_index=True)
            self.save_list(todo_list)


    def view(self):
        self.__init__()
        print(self.todo_list)


    def save_list(self,todo_list):
        todo_list.to_csv(str(date.today())+"_TODO_list.csv",index=False)
        self.__init__()



    def remove(self):
        try :

            user_input = int(input("Enter task number to remove task :- "))
            self.todo_list = self.todo_list.drop(user_input)
            self.save_list(self.todo_list)

        except:
            print("Please enter the number from mention above")


    def mark_completetion(self):
        user_input = int(input("Enter task number to Mark task as completed :- "))
        self.todo_list.loc[user_input,'Complete'] = 1
        self.save_list(self.todo_list)


s1 = TODO_list()

while True:

    print("1. Add task\n"+
        "2. View task\n"+
        "3. Remove task\n"+
        "4. Mark Complete task\n"+
        "5. Exit\n"
        )
    
    try :
        user_input = int(input("Enter Number"))
    except:
        print("Please enter number ")
    
    if user_input == 1:
        s1.add()

    elif user_input == 5:
        exit()

    elif s1.todo_list.empty:
        print("Please add task")

    elif user_input == 2:
        s1.view()

    elif user_input == 3:
        s1.remove()

    elif user_input == 4:
        s1.mark_completetion()

    else:
        print("Please enter from number mention above ")