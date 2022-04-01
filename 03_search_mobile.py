import pymysql
try:
    con=pymysql.connect(host='bcv85imfyzcak2wsbdau-mysql.services.clever-cloud.com',user='uql5mxb4irdkx0un',password='9pGZODp4XaLeuo5cf8ym',database='bcv85imfyzcak2wsbdau')
    curs=con.cursor()

    md=input('Enter model name : ')
    curs.execute("select * from mobiles where prodid ='%s'" %md)
    data=curs.fetchall()

    for rec in data:
        print(rec)
except:
  print('not found')

con.close()
