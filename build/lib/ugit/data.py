import os
import hashlib

GIT_DIR = '.ugit'

def init ():
    os.makedirs (GIT_DIR)
    os.makedirs (f'{GIT_DIR}/objects')

def hash_object(data):
    #hashlib.sha1()用来计算 data 的 hash 值，hexdigest() 用于将算好的 hash 转换成 十六进制
    # 算好的十六进制字符串作为索引文件名
    oid = hashlib.sha1 (data).hexdigest ()
    # wb 是以二进制形式写文件，out 是打开文件的一个实例，类似于 java 里的 Scanner 的实例
    with open (f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write(data)
    
    return oid # 返回值是文件名
