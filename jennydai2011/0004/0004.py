#!"C:\Python35\python.exe"

# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数

from collections import Counter
import re

def statistics(filename):
    f = open(filename, 'r').read()
    f = re.findall(r'[\w\-\_\.\]+', f)
    print(len(f))
    return 0
   

if __name__ == "__main__":
    filename = 'test.txt'
    statistics(filename)