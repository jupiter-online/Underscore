# Underscore
Underscore is a Python 3 module which can be used to format large decimal numbers with separator strings. 
## Usage
First import the function "fo()" from the Underscore module. 
```
from underscore import fo
```
The function fo() has 4 arguments:
```
fo(num, typ='dec', sep='_', dis=None)
```
num: decimal number to be formated
typ: output number as "dec", "hex" or "bin"
sep: separator string
dis: distance for insertion of separator string, defaults: dec: 3, hex: 2, bin: 4
## Examples
Format a number with underscores:
```
print(fo(100000))
```
Output:
```
100_000
```
Format a number with spaces in hex format:
```
print(fo(1000000, typ='hex', sep=' '))
```
Output:
```
0xf 42 40
```
Format a number with double underscores in binary format, use distance 8:
```
print(fo(-9999999, typ='bin', sep='__', dis=8))
```
Output:
```
-0b10011000__10010110__01111111
```
More examples can be found in file examples.py.
