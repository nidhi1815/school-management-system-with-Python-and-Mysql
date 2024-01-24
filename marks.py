import marks
import mysql.connector as co
def MARKS_MENU():
     while True:
        print("\t\t.........................................................")
        print("\t\t************WELCOME TO SCHOOL MANAGEMENT SYSTEM*************")
        print("\t\t.........................................................")
        print("\n\t\t***********MARKS***********")
        print("1: Show marks")
        print("2: Search marks")
        print("3: Deletion of marks")
        print("4: update marks")
        print("5: Return")
        print("\t\t.........................................................")
        choice=int(input("Enter your choice"))
        if choice==1:
            marks.show_marks()
        elif choice==2:
            marks.search_marks()
        elif choice==3:
            marks.delete_marks()
        elif choice==4:
            marks.edit_marks()
        elif choice==5:
                  return
        else:
            print("Error: Invalid Choice try again.....")
            conti=input("Press any key to return to Main Menu")

def show_marks():
    mycon=co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor=mycon.cursor()
    cursor.execute("select * from marks" )
    data = cursor.fetchall()
    for row in data:
        print(row)

def search_marks():
    mycon=co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor=mycon.cursor()
    ac=input('Enter Admission no:')
    st ="select * from marks where adno='%s'"%(ac)
    cursor.execute(st)
    data = cursor.fetchall()
    print (data)

def delete_marks():
    mycon=co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor=mycon.cursor()
    ac=input('Enter Admission no:')
    st= "delete from marks where adno='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print ('Marks deleted successfully')

def edit_marks():
    mycon=co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor=mycon.cursor()
    ac=input('Enter Admission no:')
    nm=input('Enter correct marks')
    st= "update marks set stmarks='%s'where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print ('Marks updated successfully')
