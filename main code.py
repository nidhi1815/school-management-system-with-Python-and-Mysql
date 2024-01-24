import admission
import student_data
import marks
import result
while True:
    #main_menu.clrscreen()
    print("\t\t.............................................................................")
    print("\t\t******************WELCOME TO SCHOOL MANAGEMENT SYSTEM************************")
    print("\t\t.............................................................................")
    print("\n\t\t.................Kendriya Vidyalaya Range Hills Estste ......................")
    print("\t\t.............................................................................")
    print("1: Admission")
    print("2: Student Data")
    print("3: Marks")
    print("4: Result")
    print("5: Exit")
    print("\t\t.............................................................................")
    choice=int(input("Enter your choice"))
    if choice==1:
        admission.ADM_MENU()
    elif choice==2:
        student_data.STU_MENU()
    elif choice==3:
        marks.MARKS_MENU()
    elif choice ==4:
        result.RESULT_MENU()
    elif choice==5:
        break
    else:
        print("Error:INVALID choice try again.......")
        conti=input("Press any key to continue")
