import result
import mysql.connector as co


def RESULT_MENU():
    while True:
        # result.clrScreen()
        print("\t\t.............................................................................")
        print("\t\t******************WELCOME TO SCHOOL MANAGEMENT SYSTEM************************")
        print("\t\t.............................................................................")
        print("\n\t\t**************RESULT**********************")
        print("1.Add result")
        print("2.Show result")
        print("3.Search result")
        print("4.Deletion of result")
        print("5.Update result")
        print("6.Return")
        print("7. Percent")
        print("\t\t.............................................................................")
        choice = int(input("Enter your choice"))
        if choice == 1:
            result.add_result()
        elif choice == 2:
            result.show_result()
        elif choice == 3:
            result.search_result()
        elif choice == 4:
            result.delete_result()
        elif choice == 5:
            result.edit_result()
        elif choice == 6:
            return
        elif choice == 7:
            result.percent()
        else:
            print("Error:INVALID choice try again.......")
            conti = input("Press any key to return to Main Menu")


def add_result():
    try:
        mycon = co.connect(host="localhost", user="root", password=
        "", database="MPS")
        cursor = mycon.cursor()
        stname = input("Enter student name :")
        PT1 = int(input("Enter PT1 marks"))
        PT2 = int(input("Enter PT2 marks"))
        PT3 = int(input("Enter PT3 marks"))
        FINALS = int(input("Enter FINALS marks"))


        query = (
            "insert into result(stname,PT1,PT2,PT3,FINALS) values (%s, %s, %s, %s, %s)"
        )
        data = (stname, PT1, PT2, PT3, FINALS)
        cursor.execute(query, data)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved in result table")
    except:
        print("error")


def show_result():
    mycon = co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor()
    cursor.execute("select * from result")
    data = cursor.fetchall()
    for row in data:
        print(row)


def search_result():
    mycon = co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter student name: ')
    st = "select * from result where stname ='%s' " % (ac)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)


def delete_result():
    mycon = co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter stname:')
    st = "delete from result where stname='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print('Data deleted successfully')


def edit_result():
    mycon = co.connect(
        host="localhost",
        user="root",
        password = "",
        database = "MPS")
    cursor = mycon.cursor()

    print("1: Edit name")
    print("2: Edit PT1")
    print("3: Edit PT2")
    print("4: Edit PT3")
    print("5: Edit FINALS")
    print("6: Return")
    print("\t\t-------------------------------------------------")
    choice = int(input("Enter your choice"))
    if choice == 1 :
        result.edit_stname()
    elif choice == 2 :
        result.edit_PT1()
    elif choice == 3 :
        result.edit_PT2()
    elif choice == 4 :
        result.edit_PT3()
    elif choice == 5:
        result.edit_FINALS()
    elif choice == 6:
        return
    else :
        print("Error: Invalid choice try again.....")
        conti = "Press any key to return to"


def edit_stname():
    mycon = co.connect(host="localhost", user="root", passwd="", database=
    "MPS")
    cursor = mycon.cursor()
    ac = input('Enter studentname:')
    nm = input('Enter correct name')
    st = "update result set stname='%s'where studentname='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Name updated successfully')


def edit_PT1():
    mycon = co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter stname:')
    nm = input('Enter correct marks of PT1')
    st = "update result set PT1='%s'where stname='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('PT1 marks updated successfully')

def edit_PT2() :
    mycon = co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter stname:')
    nm = input('Enter correct marks of PT2')
    st = "update result set PT2='%s'where stname='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('PT2 marks updated successfully')

def edit_PT3() :
    mycon = co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter stname:')
    nm = input('Enter correct marks of PT3')
    st = "update result set PT3='%s'where stname='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('PT3 marks updated successfully')

def edit_FINALS() :
    mycon = co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter stname:')
    nm = input('Enter correct marks of FINALS')
    st = "update result set FINALS='%s'where stname='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('finals marks updated successfully')

def percent():
    mycon = co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor()
    ac = input("Enter the name of student: ")
    nm = "select sum(PT1 + PT2 + PT3 + FINALS)/4  from result where stname='%s' " % (ac)
    cursor.execute(nm)
    data = cursor.fetchall()
    print(ac, "has secured",data[0][0],"%")
    if data[0][0]<35:
        print(ac, "is fail.")
    print(ac, "is pass.")
    mycon.commit()

