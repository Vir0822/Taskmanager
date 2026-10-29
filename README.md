# Task Manager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)
![Status](https://img.shields.io/badge/status-in%20development-yellow)

A command-line task manager written in Python. Add tasks, list them, mark them as completed and delete them from an interactive menu. Tasks are saved to a JSON file, so they are still there the next time you open the program.

## Demo

First session: add two tasks and complete one.

```
--- Smart Task Manager ---
1. Add task
2. List tasks
3. Complete task
4. Delete task
5. Exit
Choose an option: 1
Description of the task: upload my code to GitHub
Task added: upload my code to GitHub

Choose an option: 1
Description of the task: write the README
Task added: write the README

Choose an option: 3
ID of the task to complete: 2
Task work completed:[X] 2: write the README

Choose an option: 5
Goodbye!
```

Second session: the tasks were saved.

```
Choose an option: 2
[ ] 1: upload my code to GitHub
[X] 2: write the README
```

## Features

- **Add** tasks with a description
- **List** every task with its ID and status (`[ ]` pending, `[X]` completed)
- **Complete** a task by its ID
- **Delete** a task by its ID
- **Persistence**: tasks are saved to `tasks.json` after every change and loaded when the program starts
- **Input validation**: empty descriptions, non-numeric IDs and unknown menu options show a message instead of crashing
- **Zero dependencies**: only the Python standard library

## Getting started

### Requirements

- Python 3.10 or higher (the menu uses `match` statements)

### Run it

1. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1      # Windows (PowerShell)
   source .venv/bin/activate       # macOS / Linux
   ```

2. From the project folder, run the program:

   ```bash
   python main.py
   ```

Choose an option by typing its number and pressing Enter. To complete or delete a task, enter the ID shown at the beginning of its line. Choose `5` to exit.

> Run the program from the project folder. `tasks.json` is read from and written to the current working directory, so running it from another folder starts with a different (empty) task list.

## Menu options

| Option | Action | What you enter |
|---|---|---|
| `1` | Add task | A description (cannot be empty) |
| `2` | List tasks | Nothing |
| `3` | Complete task | The task ID |
| `4` | Delete task | The task ID |
| `5` | Exit | Nothing |

## Project structure

```
.
├── main.py           # Interactive menu, input validation and entry point
├── task_manager.py   # Task and TaskManager classes, JSON load/save
├── tasks.json        # Saved tasks (created at runtime, git-ignored)
├── .gitignore
└── README.md
```

## Design

- **`Task`** represents a single task: its `id`, `description` and `completed` state, plus a readable string representation (`[X] 2: write the README`).
- **`TaskManager`** owns the list of tasks and exposes `add_task`, `list_tasks`, `complete_task` and `delete_task`. It loads the saved tasks in its constructor (`load_tasks`) and writes them back after every change (`save_tasks`).
- **`main.py`** only handles the menu and user input. It validates what the user types and delegates the real work to `TaskManager`, so the logic can be reused or tested without the interface.

## What this project demonstrates

- Object-oriented design with separated responsibilities
- Interactive CLI flow with `match` / `case` (structural pattern matching)
- File persistence with JSON (serializing and deserializing objects)
- Defensive input handling
- Project hygiene: virtual environment, `.gitignore`, documentation

## Known limitations

- If `tasks.json` is edited by hand and becomes invalid JSON, the program stops with an error on startup. Fix or delete the file to recover.
- The next ID is calculated from the last task in the file. If you delete the most recent task and restart the program, its ID is given to the next task you add.

## Roadmap

- [x] Save tasks to a file so they persist between runs
- [ ] Priorities and due dates
- [ ] Sort and filter the task list
- [ ] Automated tests

## Author

Made by [Vir0822](https://github.com/Vir0822).
