#lets practice a mini-project: student grade filler 

# Student marks
students = {
    "Alex": 85,
    "Bob": 35,
    "Cathy": 67,
    "Dave": 29
}

# Filter passed students (>=40)
passed_students = {name: mark for name, mark in students.items() if mark >= 40}
failed_students = {name: mark for name, mark in students.items() if mark <40}
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)