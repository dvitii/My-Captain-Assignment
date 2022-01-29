import csv

def write_into_csv(info):
    with open('student_csv.csv', 'a', newline="") as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
                writer.writerow(["Name", "age", "contact_number", "email-id"])

        writer.writerow(info)

if __name__ == '__main__':
    condition = True
    student_number = 1
    while(condition):
        student_info = input("Please enter information for student number {} in the format (name age contact_number email-id)\n".format(student_number))
        student_info_list = student_info.split(" ")

        print("\nThe entered information is\nname: {}\nage: {}\ncontact number: {}\nemail id: {}\n"
              .format(student_info_list[0],student_info_list[1], student_info_list[2], student_info_list[3]))
        correct = str(input("Is the above information correct? (yes/no)\n"))
        if correct == "yes":
            write_into_csv(student_info_list)
            student_number = student_number + 1
            add_more = input("Do you want to enter information for another student? (yes/no)\n")

            if add_more == "yes":
                condition = True
            elif add_more == "no":
                condition = False
            else:
                print("Please enter a valid response!")
        elif correct == "no":
            print("please re-enter the values!")