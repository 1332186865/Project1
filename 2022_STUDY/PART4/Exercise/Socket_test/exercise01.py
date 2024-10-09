"""
练习０１：　使用dict.txt 文件完成
创建一个数据库　dict  使用utf8格式

create database dict character set utf8;

在该数据库下创建一个数据表 words
id   word (varchar(30))   mean (text varchar(1024))

create table words(
id int primary key auto_increment,
word char(30),
mean text
);

将dict.txt单词本中的单词插入到该数据表
"""
import re

import pymysql


class Dict:
    def __init__(self):
        self.kwargs = {
                "user": "root",
                "password": "Sxxzgyb+3",
                "database": "dict",
                "charset": "utf8mb4"
                }
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()

    def get_data(self):
        data = []
        fr = open("dict.txt")
        # 方法1  字符串处理
        # for line in fr:
        #     word,mean = line.split(' ',1)
        #     data.append((word,mean.strip()))

        # 方法2 正则处理
        for line in fr:
            # [(word,mean)]
            data += re.findall("(\w+)\s+(.+)", line)
        fr.close()
        return data

    # 实际做事情
    def insert_word(self):
        data = self.get_data()
        try:
            # 　批量操作
            sql = "insert into words (word, mean) values (%s,%s);"
            self.cur.executemany(sql, data)
        except Exception as e:
            print(e)
            self.db.rollback()  # 事务回滚
        else:
            self.db.commit()  # 提交事务

    def close(self):
        # 关闭
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    dict = Dict()  # 实例化
    dict.insert_word()  # 调用方法
    dict.close()
