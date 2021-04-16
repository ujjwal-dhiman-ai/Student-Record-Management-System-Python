from os import system,name
import os
import ast

def menu():
    print("\nWelcome To Student Record Management System In Python\n")
    print("<--:MENU:-->")
    print("[1] : Add Record.")
    print("[2] : View Record.")
    print("[3] : Search Record.")
    print("[4] : Delete Record.")
    print("[5] : Exit.")
    choice = 0
    choice = int(input("Enter Appropriate Choice :--> "))
    return choice

def add():
    system('cls')
    print("\nWelcome To Student Record Management System In Python\n")
    print("<--:ADD RECORD:-->")
    record = []
    name = str(input("Enter Name : "))
    record.append(name)
    roll_no = int(input("Enter Roll No : "))
    record.append(roll_no)
    mob_no = str(input("Enter Mobile No : "))
    record.append(mob_no)
    std = int(input("Enter Standard : "))
    record.append(std)
    with open("student_records.txt","a") as fileObj:
        fileObj.write(str(record))
        fileObj.write("\n")
    input("Press enter to continue...")
    system('cls')
    
def view():
    system('cls')
    print("\nWelcome To Student Record Management System In Python\n")
    print("<--:VIEW RECORD:-->\n")
    print("S.No   Name of Student       Roll No     Mobile No       Class")
    print("--------------------------------------------------------------")
    with open("student_records.txt","r") as fileObj:
        records = fileObj.readlines()
        i = 1
        for record in records:
            record = ast.literal_eval(record)
            print("%-7s%-22s%-12d%-16s%-13d" % (i,record[0],record[1],record[2],record[3]))
            # print("\n")
            i+=1

    input("Press enter to continue...")
    system('cls')

def search():
    system('cls')
    print("\nWelcome To Student Record Management System In Python\n")
    print("<--:SEARCH RECORD:-->\n")
    stname = str(input("Enter Name Of Student To Search : "))
    with open("student_records.txt","r") as fileObj:
        for record in fileObj:
            record = ast.literal_eval(record)
            if(stname == record[0]):
                print("\nName : ",record[0])
                print("Roll No : ",record[1])
                print("Mobile No : ",record[2])
                print("Class : ",record[3])
                break
        else:
            print("No Record Found For ",stname)

    input("Press enter to continue...")
    system('cls')

def delete():
    system('cls')
    print("\nWelcome To Student Record Management System In Python\n")
    print("<--:DELETE RECORD:-->\n")
    name = str(input("Enter name of student to delete record : "))
    with open("student_records.txt","r") as fileObj:
        with open("modified.txt","w") as writeObj:
            for record in fileObj:
                record = ast.literal_eval(record)
                if record[0] != name:
                    writeObj.write(str(record))
                    writeObj.write("\n")
    os.remove("student_records.txt")
    os.rename(r'modified.txt',r'student_records.txt')
    print("\nRecord deleted successfully.\n")
    input("Press enter to continue...")
    system('cls')