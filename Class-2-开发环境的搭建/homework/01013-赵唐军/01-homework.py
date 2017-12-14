# -*-coding:utf-8 -*-


L = ['Hello', 'world', 101]
L1 = [x.upper() for x in L if isinstance(x,str) == 1]
print L1