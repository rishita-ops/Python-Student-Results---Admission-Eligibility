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
