# Underscore
Underscore is a Python 3 module which can be used to format large decimal numbers with separator strings.
## Usage
First import the function "fo()" from the Underscore Module. 
```
from underscore import fo
```
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
## Examples
More examples can be found in file examples.py.
