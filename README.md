# Lab 5: Static Code Analysis — Conference Room & Equipment Scheduler

## Overview

This project focuses on identifying and fixing code quality, style, reliability, and security issues using static code analysis tools.

The application is a Python-based Conference Room and Equipment Scheduler. It books meeting rooms for specific time slots, allocates equipment, detects scheduling conflicts, logs double bookings, and exports the schedule to a JSON file.

The program initially contained several code quality and security issues. Pylint, Flake8, and Bandit were used to analyze the source code, identify potential problems, and verify improvements after fixing them.

## Objectives

- Understand the purpose of static code analysis.
- Identify programming errors and code quality issues.
- Detect security risks using automated analysis tools.
- Improve code readability, maintainability, and reliability.
- Fix identified issues without breaking the program's functionality.
- Generate reports and document the issues and their solutions.

## Technologies and Tools

- **Python** — Programming language.
- **Pylint** — Checks code quality, programming practices, naming conventions, and potential errors.
- **Flake8** — Checks Python style and reports common code issues.
- **Bandit** — Scans Python code for potential security vulnerabilities.
- **JSON** — Stores the exported room schedule.
- **Git and GitHub** — Version control and source code hosting.

## Project Structure

```text
L5_12_room_scheduler/
│
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

**Note:** The reports, schedule, and log files are generated or updated during execution. Some files may not exist until the corresponding steps have been completed.

## Application Features

- Schedule meetings in conference rooms.
- Allocate equipment, such as projectors and webcams.
- Detect and log double-booking conflicts.
- Export the room schedule to `schedule.json`.
- Record scheduling conflicts in `conflicts.log`.

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/anusha-g22/L5_12_room_scheduler.git
```

### 2. Navigate to the project directory

```bash
cd L5_12_room_scheduler
```

### 3. Create a virtual environment (recommended)

On Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, you can run the Python and analysis commands directly using the appropriate environment interpreter.

### 4. Install the required tools

```bash
python -m pip install pylint bandit flake8
```

## Running the Application

Run the scheduler:

```bash
python scheduler_system.py
```

Follow the prompt displayed by the program. Press Enter to use the default input, or enter your own value to test different scenarios.

Check the program output for scheduling results, equipment allocation, and conflict messages.

## Static Code Analysis

Run the following commands from the project directory.

### 1. Pylint

```bash
pylint scheduler_system.py > pylint_report.txt
```

Pylint evaluates code quality, naming conventions, documentation, programming practices, and potential errors.

### 2. Flake8

```bash
flake8 scheduler_system.py > flake8_report.txt
```

Flake8 checks Python style and reports violations of common style conventions and other code issues.

### 3. Bandit

```bash
bandit -r scheduler_system.py > bandit_report.txt
```

Bandit scans Python source code for potential security issues.

**Note:** Redirecting output to a file saves standard output. Some tools may also print messages to standard error, and their exit codes may indicate findings even when the analysis ran successfully.

## Issues Identified and Fixes

The initial source code was analyzed using Pylint, Flake8, and Bandit.

Issues investigated during the lab included:

- Missing module and function documentation.
- Missing final newline.
- Use of a mutable default argument.
- Use of the `global` statement.
- Inconsistent naming conventions.
- Unsafe shell-command execution for file operations.
- Missing or insufficient input validation.
- File encoding and exception-handling concerns.

The relevant findings, line numbers, severity, and proposed solutions are documented in `issues.md`.

The code was then updated to address the selected issues while preserving the scheduler's intended functionality.

## Verification

After modifying the source code, rerun all three tools:

```bash
pylint scheduler_system.py > pylint_report.txt
flake8 scheduler_system.py > flake8_report.txt
bandit -r scheduler_system.py > bandit_report.txt
```

Run the application again:

```bash
python scheduler_system.py
```

Review the reports and test the program to verify that the changes have not broken its functionality.

The target for this lab is a Pylint score above **9.5/10**.

The final Pylint score and remaining findings should be taken from the actual analysis reports rather than assumed in advance.

## Deliverables

| File | Description |
|---|---|
| `scheduler_system.py` | Updated scheduler implementation with corrected issues. |
| `issues.md` | Table documenting identified issues, severity, affected lines, descriptions, and fixes. |
| `reflection.md` | Answers to the four reflection questions provided in the lab handout. |
| `pylint_report.txt` | Pylint analysis report. |
| `flake8_report.txt` | Flake8 analysis report. |
| `bandit_report.txt` | Bandit security analysis report. |

## Learning Outcomes

Through this lab, I learned how static analysis tools help identify problems before software is deployed.

I also learned the importance of readable code, meaningful documentation, safe file handling, appropriate input validation, and automated code-quality checks.

Static analysis complements program execution and testing: it can identify potential issues without running the program, but it does not guarantee that every functional bug or security vulnerability has been found.

## Repository

GitHub repository:

https://github.com/anusha-g22/L5_12_room_scheduler