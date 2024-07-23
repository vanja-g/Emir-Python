def main():
    above_70 = {}
    under_70 = {}
    while True:
        student_name = input("Enter student name: ")
        students_grade = int(input("Enter student grade: "))

        if students_grade == -1:
            num_of_students = len(above_70) + len(under_70)
            percentage_fail = (len(under_70) / num_of_students) * 100
            print("percent of students who failed ",percentage_fail,"%")
            print("higher ",above_70)
            print("lower: ", under_70)
            break
        else:
            if students_grade >= 70:
                above_70[student_name] = students_grade
            else:
                under_70[student_name] = students_grade




main()