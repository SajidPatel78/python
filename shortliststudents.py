# Take number of student records
n = int(input("Enter No of records: "))

# List to store student tuples
students = []

# Input student details
for i in range(n):
    print(f"\nEnter Details of student-{i + 1}")

    name = input("Enter Student Name: ")
    education = input("Enter Higher Education: ")
    skill = input("Enter Primary Skill: ")
    year = input("Enter Year of Graduation: ")

    # Store details as a tuple
    student = (name, education, skill, year)

    # Add tuple to the list
    students.append(student)

# Job requirements
print("\nEnter Job Role Requirement")
req_skill = input("Enter Skill: ")
req_education = input("Enter Higher Education: ")
req_year = input("Enter Year of Graduation: ")

# Search for matching candidates
found = False

print("\nMatching Candidate(s):")
for student in students:
    if (student[1].lower() == req_education.lower() and
        student[2].lower() == req_skill.lower() and
        student[3] == req_year):

        print(student)
        found = True

# If no candidate found
if not found:
    print("No such candidate")