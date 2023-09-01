f = open('mydata.bin', 'wb')
print("文件打开成功")
f.write(b'hello')
f.write(b'hello\xe4\xb8\xad')
s = '我是汉字'
f.write(s.encode('utf-8'))
f.close()
