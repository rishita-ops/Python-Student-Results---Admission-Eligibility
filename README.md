
# Python — Student Result & Admission Eligibility

A command-line program that adds bonus marks to a student's score, decides pass or fail, and checks admission eligibility based on age and result.

---

## Problem Statement

Take a student's name, age and marks. Then:

1. Add **5 bonus marks** to the original marks.
2. The student **passes** if final marks are at least **40**.
3. The student is **eligible for admission** only if they are **18 or older and passed**.
4. Print a formatted result report.

**Example**

```
Enter student's name: Aarav
Enter student's age: 18
Enter student's marks: 36

--- STUDENT RESULT ---
Student Name:    Aarav
Original Marks:  36.0
Bonus Marks:     5
Final Marks:     41.0
Exam Status:     PASS
Eligibility:     Eligible for Admission
```

---

## Solution

```python
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
original_marks = float(input("Enter student's marks: "))

passing_marks = 40

bonus_marks = 5

final_marks = original_marks + bonus_marks

has_passed = final_marks >= passing_marks

is_eligible = age >= 18 and has_passed

print("\n--- STUDENT RESULT ---")
print(f"Student Name:   ",name)
print(f"Original Marks: ",original_marks)
print(f"Bonus Marks:    ",bonus_marks)
print(f"Final Marks:    ",final_marks)

if has_passed:
    print("Exam Status:     PASS")
else:
    print("Exam Status:     FAIL")

if is_eligible:
    print("Eligibility:     Eligible for Admission")
else:
    print("Eligibility:     NOT Eligible")
```

---

## The Critical Idea

The program separates **computing** from **printing**. The decisions are stored as booleans first:

```
has_passed  = final_marks >= passing_marks
is_eligible = age >= 18 and has_passed
```

Eligibility reuses `has_passed` instead of repeating the marks comparison. The output section only reads these values.

---

## How the Logic Works

| Variable           | Type  | Meaning                      |
| ------------------ | ----- | ---------------------------- |
| `original_marks` | float | Marks entered by the user    |
| `bonus_marks`    | int   | Fixed grace marks (5)        |
| `final_marks`    | float | `original + bonus`         |
| `has_passed`     | bool  | `final_marks >= 40`        |
| `is_eligible`    | bool  | `age >= 18 and has_passed` |

`and` is true only when **both** sides are true, so an adult who failed, or a minor who passed, is not eligible.

---

## Pseudocode

```
read name, age, original_marks
final_marks = original_marks + bonus_marks
has_passed  = final_marks >= passing_marks
is_eligible = age >= 18 and has_passed
print report
```

---

## Dry Run

| Age | Original | Final | Passed          | Eligible         |
| --- | -------- | ----- | --------------- | ---------------- |
| 18  | 36       | 41    | True            | True             |
| 18  | 35       | 40    | True (boundary) | True             |
| 18  | 34       | 39    | False           | False            |
| 16  | 80       | 85    | True            | False (underage) |
| 16  | 20       | 25    | False           | False            |

---

## Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## Edge Cases

| Case                       | Behaviour                               |
| -------------------------- | --------------------------------------- |
| Final marks exactly 40     | Passes (`>=`)                         |
| Age exactly 18             | Eligible if passed (`>=`)             |
| Marks above 100 or below 0 | Accepted, since there is no range check |
| Non-numeric age or marks   | `ValueError` crash                    |
| Decimal age (`17.5`)     | `int()` raises `ValueError`         |

---

## Code-Quality Notes

- `print(f"Student Name:   ",name)` uses an f-string with no placeholder. Either write `print(f"Student Name:   {name}")` or drop the `f`.
- Validate that marks are between 0 and 100.
- Wrap numeric input in `try/except`.
- Name the constants in capitals (`PASSING_MARKS`, `BONUS_MARKS`) to show they don't change.

---

## Natural Extension

- Add **grades** (A/B/C) with `elif`.
- Process **multiple students** in a loop and store results in a list of dictionaries.
- Calculate **class average** and **topper**.
- Cap final marks at 100 after the bonus.

---

## Repository Structure

```
python-practice/
├── student_result.py
└── README.md
```

---

## How to Run

```bash
python student_result.py
```

---

## Key Concepts

- Type casting (`int`, `float`)
- Boolean variables
- Logical operator `and`
- Comparison operators
- Formatted printing

---

## Why This Problem Matters

Storing conditions as named booleans makes code readable and reusable. The same habit helps in validation layers, permission checks and business-rule engines.

---

## Contributing

Suggestions and improvements are welcome. Fork the repo, make your change and open a pull request.

---

## License

This project is open source and available under the MIT License.
