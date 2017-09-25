'''
Datei:        format_number.py
Beschreibung: Zahlen mit Trennzeichen formatieren
Autor:        Anton Neururer - jupiter-online.net
Ausführung:   import format_number
Lizenz:       Public Domain
'''


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
