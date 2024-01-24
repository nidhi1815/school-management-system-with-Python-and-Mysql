import student_data
import admission
import mysql.connector as co
def STU_MENU():
       while True:
          #student data.clrScreen()
          print("\t\t............................................")
          print("\t\t*******WELCOME TO SCHOOL MANAGEMENT SYSTEM*******")
          print("\t\t............................................")
          print("\n\t\t********Student Data Menu********")
          print("1: Add Student record")
          print("2: Show Student details")
          print("3: Search Student record")
          print("4: Delete Student records")
          print("5: Edit Student record")
          print("6: Exit")
          print("\t\t---------------------------------------------")
          choice=int(input("Enter your choice 1-6"))
          if choice==1:
              student_data.Add_Records()
          elif choice==2:
              student_data.Show_Stu_Details()
          elif choice==3:
              student_data.Search_Stu_Details()
          elif choice==4:
              student_data.Delete_Stu_Details()
          elif choice==5:
              student_data.Edit_Stu_Details()
          elif choice==6:
              return
          else:
              print("Error: Invalid Choice try again.....")
              conti="Press any key to return to Main Menu"

def Add_Records():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="", database="MPS")
        cursor=mycon.cursor()
        session=input('Enter academic session(eg,2020-21):')
        stname=input('Enter Student Name:')
        stclass=input('Enter class:')
        stsec=input('Enter section:')
        stroll=input('Enter roll no:')
        sub1=input('Enter subject1:')
        sub2=input('Enter subject2:')
        sub3=input('Enter subject3:')

        query=(
            "insert into student(session,stname,stclass,stsec,stroll,sub1,sub2,sub3) values (%s, %s, %s, %s, %s, %s, %s, %s)"
               )
        dataa = (session,stname,stclass,stsec,stroll,sub1,sub2,sub3)
        cursor.execute (query, dataa)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved in student table")
    except:
        print('error')


def Show_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor=mycon.cursor()
    cursor.execute("select * from student")
    data = cursor.fetchall()
    for row in data:
        print(row)


def Search_Stu_Details():
     mycon=co.connect(host="localhost", user= "root", passwd="", database="MPS")
     cursor=mycon.cursor()
     ac=input('Enter Rol Number')
     st="select * from student where stroll='%s'"%(ac)
     cursor.execute(st)
     data = cursor.fetchall()
     print(data)


def Delete_Stu_Details():
     mycon=co.connect(host="localhost", user="root", passwd="", database="MPS")
     cursor=mycon.cursor()
     ac=input('Enter Roll no:')
     st="delete from student where stroll='%s'"%(ac)
     cursor.execute(st)
     mycon.commit()
     print('Data deleted successfully')


def Edit_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor=mycon.cursor()

    print("1: Edit name")
    print("2: Edit section")
    print("3: Edit roll no")
    print("4: Return")
    print("\t\t-------------------------------------------------")
    choice=int(input("Enter your choice"))
    if choice==1:
        admission.edit_name()
    elif choice==2:
        student_data.edit_section()
    elif choice==3:
        student_data.edit_rollno()
    elif choice==4:
           return
    else:
       print("Error: Invalid choice try again.....")
       conti=input("Press any key to return to")


def edit_name():
    mycon=co.connect(host="localhost", user="root", password="", database="MPS")
    cursor=mycon.cursor()
    ac=input('Enter Session:')
    nm=input('Enter correct name')
    st= "update student set stname='%s'where session='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit("Name updated successfully")


def edit_section():
    mycon = co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Session:')
    nm = input('Enter correct section')
    st = "update student set stsec='%s'where session='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Section updated successfully')


def edit_rollno():
    mycon=co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Session:')
    nm = input("Enter correct Rollno")
    st = "update student set stroll='%s'where session='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print("Rollno updated successfully")
