"""
examples
"""

from underscore import fo

print(fo(100000))
print(fo(100000, typ='hex'))
print(fo(100000, typ='bin'))

print(fo(1000000, sep=' '))
print(fo(1000000, typ='hex', sep=' '))
print(fo(1000000, typ='bin', sep=' '))

print(fo(-1000000, sep=' '))
print(fo(-1000000, typ='hex', sep=' '))
print(fo(-1000000, typ='bin', sep=' '))

print(fo(-1000000, sep='__'))
print(fo(-1000000, typ='hex', sep='__'))
print(fo(-1000000, typ='bin', sep='__ '))

print(fo(-9999999, sep='__', dis=0))
print(fo(-9999999, typ='hex', sep='__', dis=4))
print(fo(-9999999, typ='bin', sep='__ ', dis=8))
