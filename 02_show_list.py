import pymysql

con=pymysql.connect(host='bcv85imfyzcak2wsbdau-mysql.services.clever-cloud.com',user='uql5mxb4irdkx0un',password='9pGZODp4XaLeuo5cf8ym',database='bcv85imfyzcak2wsbdau')
curs=con.cursor()
curs.execute("select * from mobiles")
data=curs.fetchall()
print(data)
# data is tuple of tuples

for rec in data:
    print(rec) 

con.close()

