# Python_portfolio_mini_scripts
3 basic robotic scripts built in Python

# Robot Control Scripts

This project contains three small but powerful Python scripts simulating basic robotic behaviors. These scripts are designed to demonstrate key programming concepts such as loops, conditionals, functions, error handling, and decision-making logic — all through the lens of robotics.

---

# Overview of Scripts

# 1. `movement_loop.py` — Simulate Repetitive Robot Arm Movements
- Demonstrates the use of `for` and `while` loops
- Simulates a robot performing repeated pick-and-place actions
- Useful for understanding basic repetition and cycle logic

# 2. `sensor_check.py` — Sensor Threshold Checking with Error Handling
- Accepts one or more sensor inputs and compares them to a safety threshold
- Handles invalid sensor values like strings or `None`
- Uses the `logging` module to record sensor behavior to a log file
- Demonstrates input validation, exception handling, and dictionary iteration

# 3. `robot_decision.py` — Robot Navigation Decision-Making
- Uses `if`/`elif`/`else` logic to decide how a robot should move
- Takes four obstacle sensor inputs: front, left, right, and back
- Logs decisions like “Move Forward”, “Turn Left”, “Backup”, or “Fully Blocked”
- Simulates real-world navigation choices

---

# Example Output

**Script 3 — Sample Decision Logic:**

```text
=== Scenario 5 ===
Turn Right

