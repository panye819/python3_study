#!/user/bin/python3
# -*- coding:utf-8 -*-

"""
    需求1：
        希望你的脚本可以接受任何用户认为最简单的输入方式，包括将命令行的输出通过管道传递给该脚本
        重定向文件到该脚本，或者在命令行中传递一个文件名或者文件名列表给该脚本
        可以使用Python内置的fileinput模块
"""
import argparse


parser = argparse.ArgumentParser(description='Search some files')

parser.add_argument(dest='filenames', metavar='filename', nargs='*')

parser.add_argument('-p', '--pat', metavar='pattern', required=True,
                    dest='patterns', action='append',
                    help='text patterns to search for')
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose model')
parser.add_argument('-o', dest='outfile', action='store', help='output file')
parser.add_argument('--speed', dest='speed', action='store', choices={'slow', 'fast'},
                    default='slow', help='search speed')

args = parser.parse_args()

print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)
