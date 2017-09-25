"""
Program:     Underscore
Description: format large numbers with separator strings
Author:      Anton Neururer - jupiter-online.net
License:

Underscore is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as published by
the Free Software Foundation.

Underscore is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""


# format numbers with user specific separators
def fo(num, typ='dec', sep='_', dis=None):

    # check for integer
    if not isinstance(num, int):
        return num

    # decimal number
    if typ == 'dec':

        if num < 0:
            prefix = '-'
            num_string = str(num)[1:]
        else:
            prefix = ''
            num_string = str(num)

        dist = 3

    # hex number
    elif typ == 'hex':

        if num < 0:
            num_string = hex(num)[3:]
            prefix = '-0x'
        else:
            num_string = hex(num)[2:]
            prefix = '0x'

        dist = 2

    # binary number
    elif typ == 'bin':

        if num < 0:
            num_string = bin(num)[3:]
            prefix = '-0b'
        else:
            num_string = bin(num)[2:]
            prefix = '0b'

        dist = 4

    # check for user defined distance
    if dis != None and isinstance(dis, int) and dis >= 0:
        dist = dis

    # format number
    num_formated = ''
    for i, digit in enumerate(num_string[::-1]):
        if i > 0 and dist > 0 and i % dist == 0:
            num_formated += sep[::-1]
        num_formated += digit

    return prefix + num_formated[::-1]
