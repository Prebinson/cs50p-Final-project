# Task Study Manager
#### Video Demo:  <"https://youtu.be/HIAa-3lXfI8?si=3q7npWxxUNT9k0hM">
#### Description:

Task Study Manager is a simple command-line Python program I built to keep track of my study tasks, goals, and deadlines. As a student, it is easy to lose track of what I still need to finish or what I completely missed, so I wanted a fast terminal tool where I could log my tasks and check my progress without needing a heavy app or an internet connection. Everything gets saved locally in a CSV file (`task.csv`), so my tasks stay there even after I close the program.

## How It Works

When you run `project.py`, the program gives you a menu with five options:

1. **New Task (`new_task`)**: Asks for the task name, the goal you want to hit, and the target completion date. It saves this new entry into `task.csv` with the progress automatically set to `"Pending"`. If `task.csv` does not exist yet or is empty, the function writes the column headers (`Task`, `Goal`, `Progress`, `Time`) first.
2. **Update Progress (`update_progress`)**: Lets you pick a task and change its status. Instead of typing out custom text every time, you choose from a numbered list: `Start`, `Quarter`, `Half`, `Half and Quater`, `About to finish`, `Finished`, or `Failed`.
3. **Pending Task (`pending_task`)**: Uses `pandas` to read `task.csv` and print out every task that is not marked as `"Finished"`, so you can immediately see what is still left to do.
4. **Failed Tasked (`failed_tasked`)**: Reads `task.csv` and filters for tasks marked as `"Failed"`. This helps me look back at what I missed so I can reschedule it.
5. **Exit**: Stops the loop and exits the program cleanly using `sys.exit`.

## Project Files

- **`project.py`**: Holds the `main()` menu loop and the four core functions (`new_task`, `update_progress`, `pending_task`, and `failed_tasked`). It uses Python's built-in `csv`, `datetime`, and `sys` modules along with `pandas` to filter and display the table data.
- **`test_project.py`**: Contains four `pytest` unit tests (`test_new_task`, `test_update_progress`, `test_pending_task`, and `test_failed_tasked`). I used `tmp_path`, `monkeypatch`, and `capsys` so the tests run in a temporary folder, simulate user inputs, and check the printed output without messing up my real `task.csv` file.
- **`requirements.txt`**: Lists the two external libraries needed for the project and its tests: `pandas` and `pytest`.
- **`task.csv`**: The file where all task records are stored.

## Design Choices and Challenges

I chose to store everything in a CSV file instead of setting up a SQLite database because a CSV is lightweight and I can open it directly in VS Code or Excel whenever I want to inspect the raw data. Using Python's `csv.DictWriter` made it straightforward to append new rows, while `pandas` made filtering pending and failed tasks much cleaner than writing manual loops.

One design choice I made early on was forcing progress updates to use numbered options instead of free text. If users typed their own statuses, a small typo would break the filtering in `pending_task()` and `failed_tasked()`. Locking the statuses to fixed options prevented that issue.

The hardest part of the project was writing the unit tests in `test_project.py`. At first, running `pytest` would either interact with my actual `task.csv` or fail because the functions expected terminal input. Learning how to use `monkeypatch.chdir(tmp_path)` to isolate the file system and `capsys` to capture printed output solved this and made all four tests pass reliably.
## How to Run

1. Install the required packages: `pip install -r requirements.txt`
2. Start the program: `python project.py`
3. Run the unit tests: `pytest`