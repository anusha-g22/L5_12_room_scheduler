# Lab 5: Static Code Analysis — Conference Room & Equipment Scheduler

## 1. Overview

This project demonstrates the use of static code analysis tools to identify and fix code quality, programming, style, and security issues in a Python application.

The Conference Room & Equipment Scheduler books meeting rooms for specific time slots, allocates equipment such as projectors and webcams, detects scheduling conflicts, logs double bookings, and exports the schedule to a JSON file.

The original program contained several issues that were identified using Pylint, Flake8, and Bandit. The source code was improved based on the findings, and the tools were run again to evaluate the changes.

## 2. Objectives

- Identify code quality and style issues.
- Detect potential security vulnerabilities.
- Improve code readability and maintainability.
- Fix identified issues without breaking functionality.
- Generate static analysis reports.
- Document issues, solutions, and lessons learned.

## 3. Technologies Used

| Tool | Purpose |
|---|---|
| Python | Implements the scheduling application. |
| Pylint | Identifies code quality issues, naming problems, missing documentation, and potential programming errors. |
| Flake8 | Checks Python style and reports common code issues. |
| Bandit | Identifies potential security vulnerabilities in Python code. |
| JSON | Stores the exported room schedule. |
| Git and GitHub | Track and host the project source code. |

## 4. Application Features

- Books conference rooms for meeting time slots.
- Allocates equipment such as projectors and webcams.
- Detects and logs scheduling conflicts.
- Exports the schedule to `schedule.json`.
- Records conflicts in `conflicts.log`.

## 5. Project Structure

```text
L5_12_room_scheduler/
├── scheduler_system.py
├── issues.md
├── reflection.md
├── pylint_report.txt
├── flake8_report.txt
├── bandit_report.txt
├── schedule.json
├── conflicts.log
├── README.md
└── .gitignore
```

Note: Generated files may appear after running the program and analysis tools. The `reflection.md` and `issues.md` files must be created and completed as part of the lab.

## 6. Installation and Setup

### Clone the repository

```bash
git clone https://github.com/anusha-g22/L5_12_room_scheduler.git
```

### Navigate to the project folder

```bash
cd L5_12_room_scheduler
```

### Create a virtual environment

On Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

### Install the analysis tools

```bash
python -m pip install pylint bandit flake8
```

## 7. Run the Application

Execute the program:

```bash
python scheduler_system.py
```

Follow the input prompt. Press Enter to use the default input or enter your own values to test the program.

Observe the scheduling results, equipment allocation, and conflict messages.

## 8. Static Code Analysis

Run the following commands from the project directory.

### Pylint

```bash
pylint scheduler_system.py > pylint_report.txt
```

Pylint evaluates code quality, naming conventions, documentation, programming practices, and potential errors.

### Flake8

```bash
flake8 scheduler_system.py > flake8_report.txt
```

Flake8 checks Python style and reports style violations and other code issues.

### Bandit

```bash
bandit -r scheduler_system.py > bandit_report.txt
```

Bandit scans Python code for potential security issues.

The reports are saved in text files for review and comparison.

## 9. Issues Identified and Fixes

The source code was reviewed for issues including:

- Unsafe shell-command execution.
- Use of a mutable default argument.
- Missing module and function docstrings.
- Use of the `global` statement.
- Inconsistent function naming.
- Missing final newline.
- File-handling and encoding concerns.
- Input validation and exception-handling concerns.

The identified issues, severity, affected lines, descriptions, and proposed solutions are documented in `issues.md`.

The source code was then modified to address selected issues while preserving the intended functionality of the scheduler.

## 10. Verification

After modifying the source code, rerun the analysis tools:

```bash
pylint scheduler_system.py > pylint_report.txt
flake8 scheduler_system.py > flake8_report.txt
bandit -r scheduler_system.py > bandit_report.txt
```

Run the application again:

```bash
python scheduler_system.py
```

Review the reports and test the application to confirm that the changes have not broken its functionality.

The target Pylint score for this lab is above 9.5/10.

The final score and remaining findings should be based on the actual generated reports.

## 11. Deliverables

| File | Description |
|---|---|
| `scheduler_system.py` | Updated scheduler implementation. |
| `issues.md` | Table of identified issues and their fixes. |
| `reflection.md` | Answers to the four reflection questions in the lab handout. |
| `pylint_report.txt` | Pylint analysis report. |
| `flake8_report.txt` | Flake8 analysis report. |
| `bandit_report.txt` | Bandit security analysis report. |

## 12. Learning Outcomes

This lab demonstrates how static analysis tools help identify potential software problems without executing the program.

It also highlights the importance of documentation, meaningful naming, safe file handling, appropriate input validation, and consistent coding practices.

Static analysis complements execution and testing. It can identify potential problems, but it does not guarantee that every functional bug or security vulnerability will be detected.

## 13. GitHub Repository

Repository: https://github.com/anusha-g22/L5_12_room_scheduler