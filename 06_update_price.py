import pymysql

con=pymysql.connect(host='bcv85imfyzcak2wsbdau-mysql.services.clever-cloud.com',user='uql5mxb4irdkx0un',password='9pGZODp4XaLeuo5cf8ym',database='bcv85imfyzcak2wsbdau')
curs=con.cursor()

prodid=input('Enter product id : ')

curs.execute("select * from mobiles where prodid='%s'" %prodid)
data=curs.fetchall()

if data:
    pr=float(input('Enter price : '))
    curs.execute("update mobiles set price =%f where prodid='%s'" %(pr,prodid))
    con.commit()
    print('price updated')
else:
    print('mobile does not exist')
con.close()
