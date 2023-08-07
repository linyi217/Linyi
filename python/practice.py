#c=6000
#a=int(input("请输入这个月的业绩："))
#if a >= 100000:
#    print("您的工资为:"+str(float(c+(a*0.10))))
#elif a>=80000:
#    print("您的工资为："+str(c+(a*0.08)))
#elif a>=50000:
#    print("您的工资为："+str(c+(a*0.06)))
#else:
#    print("您的工资为："+str(c))


#total=0
#for i in range(1,5):
#    for j in range(1,5):
#        for k in range(1,5):
#            if (i!=j)and(j!=k)and(k!=i):
#                print (i,j,k)
#                total+=1
#print(total)


#import itertools

#sum=0
#a=[1,2,3,4]
#for i in itertools.permutations(a,3):
#    print(i)
#    sum+=1
#print(sum)


# for i in range(1,5):
#     print(i)
#     if i==4:
#         print("hello")
#         i+=1

# a=input("输入你要计算的数字：")
# b=input("输入你要计算的数字：")
# print(a,'*',b,'=',float(a)*float(b))

# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''


# s1=72
# s2=85
# r=s2/s1*100-100
# '%s成绩提升了%.1f%%' %('小明',r)
# print('%s成绩提升了%.1f%%' %('小明',85/72*100-100))


# a = input("你的年龄：")
# #age = int(a)
# if a >= 18:
#     print("成年")
# else:
#     print("未成年")

# if 0:
#     print('True')

# h=float(input("输入你的身高："))
# w=float(input("输入你的体重："))
# bmi=w/h**2

# if bmi <18.5:
#     print("过轻")
# elif 18.5<bmi<25:
#     print("正常")
# elif  25<bmi<28:
#     print("过重")
# elif 28<bmi<32:
#     print("肥胖")
# else:
#     print("输入信息有误，请重新输入")


# aa = ['Michael', 'Bob', 'Tracy']

# for a in aa:
#     print(a)


# s = 1
# for x in range(101):
#     s = s + x
#     print(s)

# a=0
# z=99
# while z>0:
#     print(z)
#     a=a+z
#     z=z-2
# print(z)


# L = ['Bart','Lisa','Adam']
# for i in L:
#     print('hello,',i,'!')

# a=1
# while a<100:
#     if a>21:
#         break
#     print(a)
#     a=a+1
# print("end")


# a=0
# while a<10:
#     a=a+1
#     if a%2==0:
#         continue
#     print(a)

# a=0
# while a<1:
#     a=a+0
#     print(a)

# for i in range(1000000000*100000000):
#     print(i)

# a=0
# while a<100:
#     a=a+1
#     if a>10:     #当a大于10时，提前结束循环
#         break
#     print(a)


# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x

# def nop():
#     if nop >= 18:
#         pass

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>=0:
#         return x
#     else:
#         return -x
# print(my_abs('a'))

# import math

# def move(x,y,step,angle=0):
#     nx=x+step*math.cos(angle)
#     ny=y+step*math.sin(angle)
#     return nx,ny
# x, y=move(100,100,60,math.pi / 6)
# print(x,y)

# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

# import math

# def quadratic(a,b,c):
#     nx=(ax**2)+bx+c
#     ny=
#     return nx,ny

# 导入math模块

# import math

# # 定义函数，求解一元二次方程
# def quadratic_equation(a, b, c):
#     # 计算判别式
#     discriminant = b ** 2 - 4 * a * c
#     # 如果判别式大于0，则有两个实数根
#     if discriminant > 0:
#         root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#         root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#         return root1, root2
#     # 如果判别式等于0，则有一个实数根
#     elif discriminant == 0:
#         root1 = -b / (2 * a)
#         return root1
#     # 如果判别式小于0，则无实数根
#     else:
#         return "无实数根"
# # 输入参数
# a = 11
# b = 21
# c = 11
# # 调用函数，求解方程
# roots = quadratic_equation(a, b, c)
# # 输出结果
# print("方程的根为：", roots)


# def n(x):
#     a=1
#     while x>0:
#         x=x+a
#     return x
# print(n(2))

# def power(n,y):
#     n**y
#     return n,y
# print(power(5,2))

# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
# enroll('a','F',5)

# def f1(a,b,c=0,*args,**kw):
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

# def mul(x,y=1,**kw):
#     return x*y

# def mul(*numbers):
#     w=1
#     if numbers ==():
#         raise TypeError
#     for n in numbers:
#         w=n*w
#     return w

# def mul(*a):
#     if a==():
#         q=print('except TypeError')
#     else:
#         q=1
#         for z in a:
#             q=z*q
#     return q

# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('测试失败!')
# elif mul(5, 6) != 30:
#     print('测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         mul()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')

# def fact(n):
#     return fact_iter(n, 1)

# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)

# L=[]
# n=1
# while n<=99:
#     L.append(n)
#     print(n)
#     n=n+2

# def trim(s):
#     if s[0] ==" ":
#         s = trim(s[1:])
#     elif s[-1] == " ":
#         s= trim(s[:-1])
#     return s

# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# def fin(L):
#     for z,x in L:
#         z=min(L)
#         x=max(L)
#         return (z,x)


# if __name__ == '__main__':
#     str="hello,"
#     str2="world"
#     print('str','str2')
# if __name__ == '__main__':
 
# l = ["Regional Assembly Language","Autocode","FORTRAN","IPL (LISP的先驱)","FLOW-MATIC (COBOL的先驱)","COMTRAN (COBOL的先驱)","LISP","ALGOL 58","FACT (COBOL的先驱)","COBOL","APL","Simula","SNOBOL","CPL (C的先驱)","BASIC","PL/I","BCPL (C的先驱)","Logo","Pascal","Forth","C语言","Smalltalk","Prolog","ML","Scheme","SQL","Ada","C++","Common Lisp","MATLAB","Eiffel","Objective-C","Erlang","Perl","Tcl","FL (Backus)","Haskell","Python","Visual Basic","HTML","Ruby","Lua","CLOS (part of ANSI Common Lisp)","Java","Delphi (Object Pascal)","JavaScript","PHP","REBOL","D","C#","Visual Basic .NET","F#","Scala","Factor","Windows PowerShell","Rust","Clojure","Go"]
#     y = [1951, 1952, 1954, 1954, 1955, 1957, 1958, 1958, 1959, 1959, 1962, 1962, 1962, 1963, 1964, 1964, 1967 ,1968 ,1970 ,1970 ,1972 ,1972 ,1972 ,1973 ,1975 ,1978 ,1980 ,1983 ,1984 ,1984 ,1985 ,1986 ,1986 ,1987 ,1988 ,1989 ,1990 ,1991 ,1991 ,1991 ,1993 ,1993 ,1994 ,1995 ,1995 ,1995 ,1995 ,1997 ,1999 ,2001 ,2001 ,2002 ,2003 ,2003 ,2006 ,2006 ,2007 ,2009]
    # [print(l[i],'.',y[i]) for i in range(0,len(l))]
# [a,b for a in l for b in y  ]
# if __name__ == '__main__':
#     languages = ["Regional Assembly Language","Autocode","FORTRAN","IPL (LISP的先驱)","FLOW-MATIC (COBOL的先驱)","COMTRAN (COBOL的先驱)","LISP","ALGOL 58","FACT (COBOL的先驱)","COBOL","APL","Simula","SNOBOL","CPL (C的先驱)","BASIC","PL/I","BCPL (C的先驱)","Logo","Pascal","Forth","C语言","Smalltalk","Prolog","ML","Scheme","SQL","Ada","C++","Common Lisp","MATLAB","Eiffel","Objective-C","Erlang","Perl","Tcl","FL (Backus)","Haskell","Python","Visual Basic","HTML","Ruby","Lua","CLOS (part of ANSI Common Lisp)","Java","Delphi (Object Pascal)","JavaScript","PHP","REBOL","D","C#","Visual Basic .NET","F#","Scala","Factor","Windows PowerShell","Rust","Clojure","Go"]
#     years = [1951, 1952, 1954, 1954, 1955, 1957, 1958, 1958, 1959, 1959, 1962, 1962, 1962, 1963, 1964, 1964, 1967 ,1968 ,1970 ,1970 ,1972 ,1972 ,1972 ,1973 ,1975 ,1978 ,1980 ,1983 ,1984 ,1984 ,1985 ,1986 ,1986 ,1987 ,1988 ,1989 ,1990 ,1991 ,1991 ,1991 ,1993 ,1993 ,1994 ,1995 ,1995 ,1995 ,1995 ,1997 ,1999 ,2001 ,2001 ,2002 ,2003 ,2003 ,2006 ,2006 ,2007 ,2009]
#     for language in languages:
#         for year in years:
#             return language, ':', year

# import speech_recognition as sr

# harvard = sr.AudioFile('harvard.wav')
# with harvard as source:
#     audio = r.record(source)

# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return "done"
# <<<<<<< HEAD

# import speech_recognition as sr

# for index,name in enumerate(sr.Microphone.list_microphone_names()):
#     print(f'{index},{name}')

# =======
# >>>>>>> 10e7b16aacfb6c7a016bd6ef84f69d11dfcc0aef

# def trim(s):
#     if s[0:4]=="你好":
#         s=trim(s[5:])
#     return s

# text="你好，贾克斯"

# if "你好" in text:
#     w=(text.split("你好")[1])
#     print(w)

# import speech_recognition as sr
# for index,name in enumerate(sr.Microphone.list_microphone_names()):
#     print(f'{index},{name}')

# def prod(L):
#     return L*L

# L1 = ['adam', 'LISA', 'barT']
# def normalize(name):
#     return name.title()
# L2=list(map(normalize,L1))


# from functools import reduce
# def prod(L):
#     return reduce(lambda x,y:x*y,L)
# prod([3,5,7,9])

# def is_palindrome(n):
#     return str(n)==str(n)[::-1]

# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():' % func.__name__)
#         return func(*args,**kw)
#     return wrapper

# if __name__=='__main__':
#     print(__name__)

# class Student(object):

#     def __init__(self,name,score):
#         self.name=name
#         self.score=score

#     def print_score(self):
#         print("%s:%s" % (self.name,self.score))


# class Student():   #定义类
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score

#     def print_score(self):
#         print("%s:%s" % (self.name,self.score))
#     def get_grade(self):
#         if self.score>=90:
#             return "A"
#         elif self.score>=60:
#             return "B"
#         else:
#             return "C" 

#     def get_name(self):
#     	return self.name

#     def get_score(self):
#     	return self.score

#     def get_grade(self):
#         return self.get_grade()

#     def set_name(self,name):
#         self.name=name

#     def set_score(self,score):
#         self.score=score

#     def get_name(self):
#         return self.name

#     def get_score(self):
#         return self.

# import pymysql

# def db_conn():
#     conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset='utf8')
#     return conn


# def db_close(conn):
#     conn.close()

# def db_insert(conn,sql):
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     cursor.close()

# def db_select(conn,sql):   
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     cursor.close()
#     return result


# def main():
#     conn = db_conn()
#     sql = "insert into student(name,score) values(%s,%s)"
#     db_insert(conn,sql)
#     conn.close()

# class Student(object):
#     __slots__=(name)
#     def __init__(self,name):
#         self.name = name
        
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r=10/int('2')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e: 	# 自然的处理方式也可以处理任何可能的错误。也可以使用下面的代码以处理所有MRO不同的错误。 （例如，根本无法
#     print('ZeroDivisionError:', e) 	# 处理null的错误。 但是，如果你的代码能够处理任何错误，你可以这么做。) 	# 这个任务旨在展示所有不
# else:
#     print('no error')
# finally:
#     print('finally...')
# print('END')

# from xxlimited import foo

# try:
#     foo()
# except ValueError as e:
#     print('ValueError') 	# 如果foo没有被视为被处理的，则没有任何动作。
# except UnicodeError as e:
#     print('UnicodeError') 	# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in

# from asyncio import exceptions
# from logging import exception

# from asyncio import exceptions


# try:
#     print('try...') 	# 这是一个自然的处理方式也可以处理任何可能的错误
#     r=10/-1
#     print('result:',r)
# except Exception as e:	# 自然的处理方式也可以处理任何可能的错误，但是如果你
#     print('Exception:', e) 	# 看到Exceptions类似于class Exception，那么你可以写下面的代码

# def foo(s):
#     return 10/0
# def bar(s):
#     return foo(s)*2
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Exception:', e) 	
#     finally:
#         print('finally...')

# x=input("请输入一个数X")
# y=input("请输入一个数Y") 	# 这个函数也可以在你的代码中使用，但是
# z=input("请输入一个数Z")
# if z<x>y>z:
#     print(x,y,z)
# elif y<x>z>y:
#     print(x,z,y)
# elif z<y>x>z:
#     print(y,x,z)
# elif x<y>z>x:
#     print(y,z,x)
# elif y<z>x>y:
#     print(z,x,y)
# elif x<z>y>x:
#     print(z,y,x)
# else:
#     print('Error')
# l = []
# for i in range(3):
#     x = int(raw_input('integer:\n'))
#     l.append(x)
# l.sort()
# print(l)

# import logging


# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     bar('0')

# main()

# import logging


# def foo(s):
#     return 10/int(s)

# def bar(s):
#     return foo(s)*2

# def main():
#     try:
#         bar(0)
#     except Exception as e:
#         print('exception:',e)
#         # logging.exception(e)

# main()
# print('END')

# class FooError(ValueError):
#     pass

# def foo(s):
#     n=int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10/n

# foo('0')

# def foo(s):
#     n=int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' %s)
#     return 10/n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
# bar()

# try:
#     10/0
# except ZeroDivisionError:
#     raise ValueError('input error!')

# from functools import reduce


# def str2num(s):
#     return  float(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()

# def foo(s):
#     n=int(s)
#     print('>>> n = %d' % n)
#     return 10 / n

# def main():
#     foo('0')

# main()

# def foo(s):
#     n=int(s)
#     assert n!=0, 'n is zero!'
#     return 10/n

# def main():
#     foo('0')

# main()

# import logging
# import pdb

# logging.basicConfig(
#         level=logging.INFO,
#         filename='test.log',
#         datefmt='%Y-%m-%d %H:%M:%S',
#         format='(%(asctime)s %(levelname)s) %(lineno)d: %(message)s'
# )  #%(message)s is to add the)
# logging.debug('debug')
# logging.info('info')

# s='0'
# n=int(s)
# # pdb.set_trace()
# logging.info('n=%d'% n)
# print(10/n)

        
# import unittest

# from mydict import Dict

# class TestDict(unittest.TestCase):

#     def test_init(self):
#         d=Dict(a=1,b='test')
#         self.assertEqual(d.a,1)
#         self.assertEqual(d.b,'test')
#         self.assertTrue(isinstance(d,dict))

#     def test_key(self):
#         d=Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key,'value')

#     def test_attr(self):
#         d=Dict()
#         d.key='value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'],'value')

#     def test_keyerror(self):
#         d=Dict()
#         with self.assertRaises(KeyError):
#             value=d['empty']

#     def test_attrerror(self):
#         d=Dict()
#         with self.assertRaises(AttributeError):
#             value=d.empty

# if __name__=='__main__':
#     unittest.main()

# import unittest

# class TestDict(unittest.TestCase):

#     def setUp(self):
#         print('setUp...')

#     def tearDown(self):
#         print('tearDown...')

import unittest


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError
        if self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'
    
    

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()


