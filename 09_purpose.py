from logging import exception
import pymysql as my

try:
    con = my.connect(host='bcv85imfyzcak2wsbdau-mysql.services.clever-cloud.com',user='uql5mxb4irdkx0un',password='9pGZODp4XaLeuo5cf8ym',database='bcv85imfyzcak2wsbdau')
    curs=con.cursor()
    mod = input('Enter Model Name of mobile : ')
    curs.execute("select * from mobiles where modelname = '%s'" %mod)
    data = curs.fetchall()
    if data:
        pur = input('Enter the purpose of mobile : ')
        curs.execute("update mobiles set purpose='%s' where modelname='%s'" %(pur, mod))
        con.commit()
        print('Purpose added successfully')
    else:
        print('Mobile not found')
except Exception as e:
    print('Error : %s' %e)