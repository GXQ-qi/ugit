import argparse

# main 函数从 parse_args 接收返回的参数，然后调用参数对应的函数
# 这里注意的是 args 参数绑定了 func 函数
def main():
    args = parse_args ()
    args.func (args)

# parse_args 函数接受命令的参数
def parse_args ():
    # parser 是 argparse 的一个实例
    parser = argparse.ArgumentParser ()

    # commands 是一个 subparsers -- 子解释器的实例
    commands = parser.add_subparsers (dest='command')
    commands.required = True

    # 是 add_parser 返回的实例，类型是 argparse.ArgumentParser
    init_parser = commands.add_parser ('init')
    # set_defaults 方法是为解析器设置默认的参数值，但是作为子命令的方法，可以用来绑定子命令对应的处理函数。
    init_parser.set_defaults (func=init)

    return parser.parse_args ()

def init (args):
    print("you inited successfully")
