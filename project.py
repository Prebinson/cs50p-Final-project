import sys
import datetime as dt
import pandas as pd
import csv


def new_task(user, time, goal):
    with open("task.csv", mode="a", newline="") as f:
        fieldname = ["Task", "Goal", "Progress", "Time"]
        writer = csv.DictWriter(f, fieldnames=fieldname)
        if f.tell()==0:
            writer.writeheader()
        writer.writerow({"Task": user, 
                         "Goal": goal,
                         "Progress": "Pending",
                         "Time": time.strftime("%d/%m/%Y")})


def update_progress(user):
    pro = {"1": "Start",
           "2": "Quarter",
           "3": "Half",
           "4": "Half and Quater",
           "5": "About to finish",
           "6": "Finished",
           "7": "Failed"}
    for key, value in pro.items():
        print(f"{key}: {value}")
    while True:
        try:
            pro_user = input("Where are you: ")
            if pro_user in pro:
                with open("task.csv", mode="r", newline="")as fi:
                    file = list(csv.reader(fi))
                    file[user][2] = pro[pro_user]
                with open("task.csv", mode="w", newline="")as fil:
                    writer = csv.writer(fil)
                    writer.writerows(file)
                print("Saved")
                break
            else:
                raise ValueError
        except ValueError:
            print("Enter valid option")
            continue


def pending_task():
    with open("task.csv", mode="r", newline="") as fi:
        file = csv.reader(fi)
        for i in file:
            if i and i[2] != "Finished":
                print(i)


def failed_tasked():
    with open("task.csv", mode="r", newline="") as fi:
        file = csv.reader(fi)
        for i in file:
            if i and i[2] == "Failed":
                print(i)


def main():
    while True:
        try:
            print(
                "1. New Task\n2. Update Progress\n3. Pending Task\n4. Failed Tasked\n5. Exit")
            opt = int(input("Please enter your choice: "))
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
                    user = int(input("Enter Which Task: "))
                    if user not in range(1, len(task_list)+1):
                        raise ValueError
                except (ValueError, pd.errors.EmptyDataError, TypeError, FileNotFoundError):
                    print("Enter valid Option")
                    continue
                update_progress(user)

            # pending task
            case 3:
                pending_task()
            # failed task
            case 4:
                failed_tasked()
            case 5:
                sys.exit("Thank you and wish you best of luck for your task")
            case _:
                print("Enter Valid Choice")


if __name__ == "__main__":
    main()
