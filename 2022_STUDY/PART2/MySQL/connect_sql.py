#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
import pymysql

db = pymysql.connect(host="39.99.32.138", user="admin", password="Sxxzgyb3",
                     database='project1', charset='utf8')
cursor = db.cursor()
cursor.execute("select * from project1.city;")

# try:
#     cursor.execute("select * from project1.city;")
#     db.commit()
#     print('OK!')
# except Exception as e:
#     db.rollback()
#     print('已回滚!')

for i in cursor.fetchall():
    print(i)
db.commit()
cursor.close()
db.close()
