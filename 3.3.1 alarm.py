#Students = ["zaine","zay","zuko","zofia","zander","zack","ben","boolbilly", "brycen", "brooke", "blake", "Mike", "Maddox", "Marshall", "Marshawn", "Mickey", "Melissa"]
Students = ["zaine","zay","zuko"]
Present = []
Absent = []


def check_attendance():
    global Students, Present, Absent
    for stud in range(len(Students)):
        question = "Is " + Students[stud] + " here?"
        answer = input(question)

        if answer == "y":

            Present.append(Students[stud])

        else:
            Absent.append(Students[stud])


def change_attendance(change_student, status):
    global Absent, Present
    if status == "y":
        Present.append(change_student)
        Absent.remove(change_student)

    else:
        Absent.append(change_student)
        Present.remove(change_student)

''' def Print_attendance():
    for Students in Absent

    print(" you printed attendance ")
    print(Present)

    print(Absent)



    print(" Make a choice from the following list.")
'''

print("1. Check Attendance")
print("2. Change Attendance")
print("3. Print Attendence ")
print("0. Exit Program")

choice = int(input(" What would you like to do today? "))

while choice != 0:
    if choice == 1:
        check_attendance()
    if choice == 2:
        student = input("What is the student's name?")
        here = input(" Are they here?  1 = y or 2 = n ")
        change_attendance(student, int(here))
    if choice == 3:
        for students in Absent:
            print(students)

        for students in Present:
            print(students)



    '''if choice == 3:
        Print_attendance()'''

    choice = int(input(" What would you like to do today? "))

