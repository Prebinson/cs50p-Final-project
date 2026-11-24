import sys
import datetime as dt
import pandas as pd
import csv


def new_task(user, time, goal):
    with open("task.csv", mode="a", newline="") as f:
        fieldname = ["Task", "Goal", "Progress", "Time"]
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        writer.writerow({"Task": user, "Goal": goal,
                        "Progress": "Pending",
                         "Time": time.strftime("%d/%m/%Y")})
        


def update_progress(user):
    pro = {"1": "Start",
           "2": "Quarter",
           "3": "Half",
           "4": "Half and Quater",
           "5": "About to finish",
           "6": "Finished"}
    for key, value in pro.items():
        print(f"{key}: {value}")
    while True:
        try:
            pro_user = input("Where are you: ")
            for key, value in pro.items():
                if pro_user == key:
                    with open("task.csv", mode="r")as fi:
                        file = list(csv.reader(fi))
                        file[user][2] = value
                    with open("task.csv", mode="w")as fi:
                        writer = csv.writer(fi)
                        writer.writerows(file)
                        break
                else:
                    raise ValueError
        except ValueError:
            print("Enter valid option")
            continue

    def pending_task():
        with open("task.csv") as fi:
            file = csv.reader(fi)
            while True:
                for i in file:
                    if i[3] != "Finished":
                        print(i)


def main():
    while True:
        try:
            print(
                "1. New Task\n2. Update Progress\n3. Pending Task\n4. Failed Tasked\n5. Exit")
            opt = int(input("Please enter your choice"))
        except ValueError:
            print("Enter Valid Option: ")
            continue
        match opt:

            # task1
            case 1:
                user = input("Name your new task: ")
                while True:
                    try:
                        time = input(
                            "Expexted time to finished. Format dd/mm/yyyy: ")
                        date = dt.datetime.strptime(time, "%d/%m/%Y")
                        break
                    except ValueError:
                        print("give imformation in the correct format")
                        continue
                goal = input("Whats you goal? ")
                new_task(user, date, goal)

            # task2
            case 2:
                try:
                    task_list = pd.read_csv("task.csv")
                    task_list.index = range(1, len(task_list)+1)
                    print(task_list)
                    user = int(input("Enter Which Task"))
                    if user > len(task_list)+1:
                        raise ValueError
                except pd.errors.EmptyDataError:
                    print("No Task is has been created")
                    continue
                except ValueError:
                    print("Enter valid Option")
                    continue
                update_progress(user)

            # pending task
            case 3:
                pending_task()
            case 4:
                failed_tasked()
            case 5:
                exit()
            case _:
                print("Invalid")
                sys.exit()


if __name__ == "__main__":
    main()
