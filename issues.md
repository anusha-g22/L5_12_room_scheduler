# Lab 5: Static Code Analysis — Issues and Fixes

## Overview

The initial version of `scheduler_system.py` was analyzed using Pylint, Flake8, and Bandit.

The tools were used to identify potential security risks, programming issues, and code quality problems. The following table documents the issues investigated and the approaches used to address them.

**Note:** Line numbers refer to the original version of the source code. Confirm the exact line numbers against the original file or saved analysis reports before submission.

## Issue Table

| **Issue** | **Type** | **Line(s)** | **Description** | **Fix Approach** |
|---|---|---|---|---|
| Unsafe shell-command execution | High — Security | Verify original line | Executing a shell command using dynamically constructed input can introduce command-injection risks. | Replaced shell-command execution with safer Python file-handling operations using `pathlib`. |
| Mutable default argument | Medium — Reliability | Verify original line | A mutable default argument, such as an empty list, can be shared between function calls and cause unexpected behavior. | Changed the default to `None` and initialized the list inside the function. |
| Insufficient input validation | Medium — Reliability | Verify original lines | Unexpected or invalid input can cause incorrect scheduling behavior or runtime errors. | Added appropriate input checks and handled invalid input. |
| Inadequate exception handling | Medium — Reliability | Verify original lines | File operations and other potentially failing operations can terminate the program if exceptions are not handled appropriately. | Added suitable exception handling for expected error conditions. |
| Missing module docstring | Low — Maintainability | 1 | The file did not contain a module-level docstring explaining its purpose. | Added a module docstring describing the scheduler. |
| Missing function docstrings | Low — Maintainability | 11 and other affected functions | Functions lacked documentation explaining their purpose, inputs, or behavior. | Added meaningful docstrings to the relevant functions. |
| Use of the `global` statement | Low — Maintainability | 12 | Modifying global state inside a function can make the program harder to understand, test, and maintain. | Reviewed the use of global state and retained or refactored it as appropriate for the program's design. |
| Inconsistent function naming | Low — Style | Verify original line | A function used camelCase instead of the preferred `snake_case` naming convention. | Renamed `logConflicts` to `log_conflicts` and updated its references. |
| Missing final newline | Low — Style | 119 in the original report | The source file did not end with a newline character. | Added a final newline to the file. |
| File encoding not specified | Low — Portability | Verify original line | Depending on the environment's default encoding can cause inconsistent file-handling behavior. | Specified UTF-8 encoding explicitly where appropriate. |

## Verification After Fixing

After modifying `scheduler_system.py`, the analysis tools were run again.

### Pylint

Command:

```bash
pylint scheduler_system.py > pylint_report.txt
```

Purpose: Verify code quality, documentation, naming conventions, and potential programming issues.

### Flake8

Command:

```bash
flake8 scheduler_system.py > flake8_report.txt
```

Purpose: Verify Python style and identify remaining reported issues.

### Bandit

Command:

```bash
bandit -r scheduler_system.py > bandit_report.txt
```

Purpose: Check for potential security issues.

## Conclusion

Static analysis helped identify potential problems involving security, reliability, maintainability, and coding style.

The selected issues were addressed, and the application was tested again to check that its intended functionality remained intact.

The final analysis reports should be reviewed to confirm which findings were resolved and whether any warnings remain.