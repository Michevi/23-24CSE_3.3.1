Students = ["zaine","zay","zuko","zofia","zander","zack","ben","boolbilly", "brycen", "brooke", "blake", "Mike", "Maddox", "Marshall", "Marshawn", "Mickey", "Melissa"]
Present = []
Absent = []


def check_attendance():
    for stud in range(len(Students)):
        question = "Is " + Students[stud] + " here?"
        answer = input(question)

        if answer == "yes":

            Present.append(Students[stud])

        else:
            Absent.append(Students[stud])

check_attendance()






