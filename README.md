# PLP Python Week 3 Assignment: Conditions and Loops

## File Descriptions
- `grade_reporter.py`: Calculates letter grades, total pass/fail counts, and the rounded average for a list of test scores using loops and conditional logic.
- `bug_hunt.py`: Features a fixed Python script originally containing syntax, logic, and type errors, along with inline `# BUG:` comments explaining each fix.

## Reflection on Debugging
The logic bug where the loop condition was set to `count < 5` instead of `count <= 5` was the hardest bug to find. Because Python executed the script without raising an explicit error message or crashing, the program appeared to run successfully at first glance. I knew something was wrong because the calculated output was `10` instead of the expected sum of `15`, which prompted me to trace the loop iterations manually to find that the number 5 was being excluded.
