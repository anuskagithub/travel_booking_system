import sqlite3
import mysql.connector

def Add_BookingTour(Packgae_Name, Package_Type, Date_of_Journey, Visitor_Name, Age, Sex, Mobie_No, Email_ID, Address, Mem1_Name, Mem1_Age, Mem1_Sex, Mem2_Name, Mem2_Age, Mem2_Sex, Mem3_Name, Mem3_Age, Mem3_Sex, Mem4_Name, Mem4_Age, Mem4_Sex, Mem5_Name, Mem5_Age, Mem5_Sex):
    
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    
    add_booking = ("INSERT INTO Booking_Tour"
                   "(Packgae_Name, Package_Type, Date_of_Journey, Visitor_Name, Age, Sex, Mobie_No, Email_ID, Address, Mem1_Name, Mem1_Age, Mem1_Sex, Mem2_Name, Mem2_Age, Mem2_Sex, Mem3_Name, Mem3_Age, Mem3_Sex, Mem4_Name, Mem4_Age, Mem4_Sex, Mem5_Name, Mem5_Age, Mem5_Sex) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_booking = (Packgae_Name, Package_Type, Date_of_Journey, Visitor_Name, Age, Sex, Mobie_No, Email_ID, Address, Mem1_Name, Mem1_Age, Mem1_Sex, Mem2_Name, Mem2_Age, Mem2_Sex, Mem3_Name, Mem3_Age, Mem3_Sex, Mem4_Name, Mem4_Age, Mem4_Sex, Mem5_Name, Mem5_Age, Mem5_Sex)

    print(add_booking)
    
    print(data_booking)

    dataAdded=True    
    try:  
        # Insert new booking
       
        cursor.execute(add_booking, data_booking)
        # Make sure data is committed to the database
        cnx.commit()
        cursor.close()
        cnx.close()
        print("Data Save Success.")
       
    except: 
        cnx.rollback()
        cnx.close()
        print("Data Save Error.")
        dataAdded=False
        
        
    return dataAdded 


def Add_BookingHotel(Hotel_Name, Location, Check_In_Date, Check_Out_Date, Total_Room, Visitor_Name, Age, Sex, Mobie_No, Email_ID, Address, Mem1_Name, Mem1_Age, Mem1_Sex, Mem2_Name, Mem2_Age, Mem2_Sex, Mem3_Name, Mem3_Age, Mem3_Sex, Mem4_Name, Mem4_Age, Mem4_Sex, Mem5_Name, Mem5_Age, Mem5_Sex):
    
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    
    add_booking = ("INSERT INTO Booking_Hotel"
                   "(Hotel_Name, Location, Check_In_Date, Check_Out_Date, Total_Room, Visitor_Name, Age, Sex, Mobie_No, Email_ID, Address, Mem1_Name, Mem1_Age, Mem1_Sex, Mem2_Name, Mem2_Age, Mem2_Sex, Mem3_Name, Mem3_Age, Mem3_Sex, Mem4_Name, Mem4_Age, Mem4_Sex, Mem5_Name, Mem5_Age, Mem5_Sex) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_booking = (Hotel_Name, Location, Check_In_Date, Check_Out_Date, Total_Room, Visitor_Name, Age, Sex, Mobie_No, Email_ID, Address, Mem1_Name, Mem1_Age, Mem1_Sex, Mem2_Name, Mem2_Age, Mem2_Sex, Mem3_Name, Mem3_Age, Mem3_Sex, Mem4_Name, Mem4_Age, Mem4_Sex, Mem5_Name, Mem5_Age, Mem5_Sex)

    print(add_booking)
    
    print(data_booking)

    dataAdded=True    
    try:  
        # Insert new booking
       
        cursor.execute(add_booking, data_booking)
        # Make sure data is committed to the database
        cnx.commit()
        cursor.close()
        cnx.close()
        print("Data Save Success.")
       
    except: 
        cnx.rollback()
        cnx.close()
        print("Data Save Error.")
        dataAdded=False
        
        
    return dataAdded 

def Add_BookingFlight(Flight_Rout, Flight_Name, Journey_Date, Visitor_Name, Age, Sex, Mobie_No, Email_ID, Address, Mem1_Name, Mem1_Age, Mem1_Sex, Mem2_Name, Mem2_Age, Mem2_Sex, Mem3_Name, Mem3_Age, Mem3_Sex, Mem4_Name, Mem4_Age, Mem4_Sex, Mem5_Name, Mem5_Age, Mem5_Sex):
    
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    
    add_booking = ("INSERT INTO Booking_Flight"
                   "(Flight_Rout, Flight_Name, Journey_Date, Visitor_Name, Age, Sex, Mobie_No, Email_ID, Address, Mem1_Name, Mem1_Age, Mem1_Sex, Mem2_Name, Mem2_Age, Mem2_Sex, Mem3_Name, Mem3_Age, Mem3_Sex, Mem4_Name, Mem4_Age, Mem4_Sex, Mem5_Name, Mem5_Age, Mem5_Sex) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_booking = (Flight_Rout, Flight_Name, Journey_Date, Visitor_Name, Age, Sex, Mobie_No, Email_ID, Address, Mem1_Name, Mem1_Age, Mem1_Sex, Mem2_Name, Mem2_Age, Mem2_Sex, Mem3_Name, Mem3_Age, Mem3_Sex, Mem4_Name, Mem4_Age, Mem4_Sex, Mem5_Name, Mem5_Age, Mem5_Sex)

    print(add_booking)
    
    print(data_booking)

    dataAdded=True    
    try:  
        # Insert new booking
       
        cursor.execute(add_booking, data_booking)
        # Make sure data is committed to the database
        cnx.commit()
        cursor.close()
        cnx.close()
        print("Data Save Success.")
       
    except: 
        cnx.rollback()
        cnx.close()
        print("Data Save Error.")
        dataAdded=False
        
        
    return dataAdded 
 

def Get_AllTrourBookings():
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM Booking_Tour ORDER BY Booking_ID DESC")
    bookings = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    return bookings

def Get_AllTourBookingMonthWise():
    SQLText="SELECT YEAR(STR_TO_DATE(Date_of_Journey, '%M %d %Y')) as Book_Year, MONTH(STR_TO_DATE(Date_of_Journey, '%M %d %Y')) as Book_Month, Count(*) FROM Booking_Tour GROUP BY Book_Year, Book_Month ORDER BY Book_Year, Book_Month"
    
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    cursor.execute(SQLText)
    BookingsMonthWise = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    return BookingsMonthWise
 
def Get_AllHotelBookings():
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM Booking_Hotel")
    bookings = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    return bookings    

def Get_AllHotelBookingMonthWise():
    SQLText="SELECT YEAR(STR_TO_DATE(Check_In_Date, '%M %d %Y')) as Book_Year, MONTH(STR_TO_DATE(Check_In_Date, '%M %d %Y')) as Book_Month, Count(*) FROM Booking_Hotel GROUP BY Book_Year, Book_Month ORDER BY Book_Year, Book_Month"
    
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    cursor.execute(SQLText)
    BookingsMonthWise = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    return BookingsMonthWise
 
def Get_AllFlightBookings():
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM Booking_Flight")
    bookings = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    return bookings    

def Get_AllFlightBookingMonthWise():
    SQLText="SELECT YEAR(STR_TO_DATE(Journey_Date, '%M %d %Y')) as Book_Year, MONTH(STR_TO_DATE(Journey_Date, '%M %d %Y')) as Book_Month, Count(*) FROM Booking_Flight GROUP BY Book_Year, Book_Month ORDER BY Book_Year, Book_Month"
    
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    cursor.execute(SQLText)
    BookingsMonthWise = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    return BookingsMonthWise
    


def put_GlobalVal(GlobalVal,ValCategory='NA'):
   
    cnx = mysql.connector.connect(user='root', password='mysql123', 
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    add_GlobalValue = ("update GlobalValueTab set GlobalValue='"+GlobalVal+"', ValueCategory='"+ValCategory+"'")
    
    # Adding Global Value
    cursor.execute(add_GlobalValue)
    
    # Make sure data is committed to the database
    cnx.commit()
    
    cursor.close()
    cnx.close()
    
def get_GlobalVal():
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM GlobalValueTab")
    globalVal = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    return globalVal
    
def Add_Student(rollno,Stname,marks,age):
    
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    add_student = ("INSERT INTO student "
               "(roll, name, marks, age) "
               "VALUES (%s, %s, %s, %s)")
    
    data_student = (rollno, Stname, marks, age)
    
    # Insert new student
    cursor.execute(add_student, data_student)
    
    # Make sure data is committed to the database
    cnx.commit()
    
    cursor.close()
    cnx.close()
    
def Get_LastBookingID():
    
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    Query_GetLastID = "SELECT Booking_Id FROM booking ORDER BY Booking_Id DESC LIMIT 1"
    
    # Insert new student
    cursor.execute(Query_GetLastID)
    Query_result = cursor.fetchall()
           
    cursor.close()
    cnx.close()

    return Query_result[0][0]     
    
def AuthenticateUser(userName,password):
    
    #print(userName+"/"+password)
    
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    Query_usercount = "SELECT COUNT(*) from AdminUser where UserName=%s AND Password=%s"
    Data_usercount = (userName,password)
    #print(userName,password)
    # Insert new student
    cursor.execute(Query_usercount, Data_usercount)
    Query_result = cursor.fetchall()
    
    # Make sure data is committed to the database
       
    cursor.close()
    cnx.close()
    
    return Query_result

def Add_Gallery(GName,GPath):
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    add_gallery = ("INSERT INTO Gallery "
               "(GalleryName, GalleryPath) "
               "VALUES (%s, %s)")
    
    data_gallery = (GName,GPath)
    
    # Insert new Gallery
    cursor.execute(add_gallery, data_gallery)
    
    # Make sure data is committed to the database
    cnx.commit()
    
    cursor.close()
    cnx.close()
    
def Get_GalleryPath(galleryName):
   
    cnx = mysql.connector.connect(user='root', password='mysql123',
                              host='localhost',
                              database='mydc')
    cursor = cnx.cursor()
    
    Query_Gallery = "SELECT * from Gallery where GalleryName='" + galleryName+"'"
    #Data_Gallery = (galleryName)
    
    cursor.execute(Query_Gallery)
    Query_result = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    if len(Query_result)>0:
       return Query_result[0][1]  
    else:
       return ''
