# argparse 是 python 用于创建命令行接口的模块
import argparse
import os

# 导入 data 文件，将常用的函数都放在这里实现
from . import data

def main():
    args = parse_args ()
    args.func (args)

def parse_args ():
    # 创建主解析器的对象
    parser = argparse.ArgumentParser ()

    # 创建子命令解析器的对象
    commands = parser.add_subparsers (dest='command')
    commands.required = True

    init_parser = commands.add_parser ('init')
    init_parser.set_defaults (func=init)

    hash_object_parser = commands.add_parser ('hash-object')
    hash_object_parser.set_defaults (func=hash_object)
    # add_atgument 可以为该命令添加一个参数，这里添加 file 参数
    hash_object_parser.add_argument ('file')
# 返回的是一个简单的容器，是一个命名空间对象
    return parser.parse_args ()

def init (args):
    data.init ()
    print (f'Initalized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}')

def hash_object (args):
    # with 语句确保资源能够被安全的释放
    with open (args.file, 'rb') as f:
        print (data.hash_object (f.read()))
