from tkinter.messagebox import YES
import pymysql

con=pymysql.connect(host='bcv85imfyzcak2wsbdau-mysql.services.clever-cloud.com',user='uql5mxb4irdkx0un',password='9pGZODp4XaLeuo5cf8ym',database='bcv85imfyzcak2wsbdau')
curs=con.cursor()

prodid=input('Enter product id : ')
curs.execute("select * from mobiles where prodid='%s'" %prodid)
data=curs.fetchall()

if data:
    ch=input('Do you want to delete ')
    if ch.lower()=='yes':
        curs.execute("delete from mobiles where prodid='%s'" %prodid)
        con.commit()
        print('mobiles deleted successfully')
else:
    print('mobiles does not exist')

con.close()
