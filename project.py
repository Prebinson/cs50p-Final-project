import sys
import csv
def new_task():
    user=input("Name your new task")
    



def main():
    while True:
        try:
            print("1. New Task\n2. Update Progress\n3. Pending Task\n4. Failed Tasked\n5. Exit")
            opt=int(input("Please enter your choice"))
        except ValueError:
            print("Enter Valid Option")
            continue
        match opt:
            case 1:
                new_task()
            case 2:
                update_progress()
            case 3:
                pending_task()
            case 4:
                failed_tasked()
            case 5:
                exit()
            case _:
                print("Invalid")
                sys.exit()
if __name__=="__main__"
    main()
                


        

