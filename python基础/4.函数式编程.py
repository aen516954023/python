# -*- coding utf-8 -*-


#=====高阶函数========
from functools import reduce
newList = [1,2,3,4,5,6,7,8,9]
#-------map -----------

def f(x):
    return x*x

r = map(f,newList)

#print(list(r))

res = list(map(str,newList))
#print(res)

#-------reduce-------

def add(x,y):
    return x+y

print(reduce(add,newList))

def fn(x,y):
    return x * 10 + y

print(reduce(fn,newList))

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(char2num,'13579')))

def str2int(s):
    return reduce(lambda x,y: x * 10 + y, map(char2num,s))
d = str2int('55')
print(d)
print(type(d))


# 练习 1.利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    return name[0].upper() + name[1:].lower()

e = list(map(normalize, ['lis','AAD']))
print(e)


# 练习2 Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)

#prod函数可以写成以下方式

def prod2(L):
    return reduce(lambda x,y:x*y, L)

print('3 * 5 * 7 * 9 =', prod2([3, 5, 7, 9]))
if prod2([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 练习 3 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str2float(d):
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    num = d.index('.')
    L1 = d[:num]
    L2 = d[num+1:]
    before = reduce(lambda x,y:x*10+y, map(lambda x:dic[x], L1))
    after = reduce(lambda x, y:x*10+y, map(lambda x:dic[x], L2)) / 10**len(L2)
    return before + after
dd = str2float('1234.456')
print(dd)
print(type(dd))


#---------- filter---------------

#---------- sorted---------------

#===========返回函数===========

#===========匿名函数===========

#===========装饰器===========

#===========偏函数===========



