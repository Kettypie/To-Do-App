# Do It! – To-Do App

A simple and interactive To-Do List application built using **Python and PyQt5**.

Do It! helps you organize your tasks, keep track of what needs to be done, and manage your daily activities through a simple graphical interface.

## Features

- **Add Tasks:** Create new tasks using the input field.
- **Duplicate Detection:** Get a confirmation before adding a task that already exists.
- **Mark as Done:** Mark completed tasks with a strikethrough effect.
- **Undo Tasks:** Change completed tasks back to unfinished.
- **Delete Tasks:** Remove tasks with a confirmation dialog.
- **Task Counter:** Keep track of how many unfinished tasks remain.
- **Scrollable Task List:** Easily manage multiple tasks.
- **Keyboard Shortcut:** Press `Enter` to add a task.
- **Custom Styling:** A simple interface styled using Qt Style Sheets (QSS).

## Built With

- **Python** – Main programming language.
- **PyQt5** – GUI framework used to build the application.
- **Qt Style Sheets (QSS)** – Used for customizing the interface.

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kettypie/To-Do-App.git
```

### 2. Navigate to the project directory

```bash
cd To-Do-App
```

### 3. Install the required dependency

```bash
pip install PyQt5
```

### 4. Run the application

```bash
python "To do app.py"
```

## How to Use

1. Enter your task in the input field.
2. Click the **ADD** button or press `Enter`.
3. Click **Done** when you complete a task.
4. Click **Undone** if you want to mark it as unfinished again.
5. Click the trash icon to delete a task.

The task counter automatically updates whenever you add, complete, undo, or delete a task.

## Project Structure

```text
To-Do-App/
│
├── To do app.py
└── README.md
```

## What I Learned

This project helped me practice and improve my Python programming skills, especially:

- Object-Oriented Programming (OOP)
- Creating custom QWidget classes
- Working with PyQt5 layouts and widgets
- Connecting signals and slots
- Managing data using Python lists
- Handling user input and confirmation dialogs
- Applying custom styles using QSS
- Working with keyboard shortcuts

## Future Improvements

Some ideas for future updates:

- Save tasks so they remain available after closing the application.
- Add task editing functionality.
- Add deadlines and priorities.
- Improve the overall user interface.

## Author

**Kettypie**

GitHub: [@Kettypie](https://github.com/Kettypie)

---

*Built as a personal learning project while exploring Python and GUI development.*
