import sys
'''
    bytes() creates an immutable object so must use bytearray()
    random = bytearray(b'\xDD\xFF') => can add two objects of bytearray()
    access like regular array random[0] will output b'\xDD' can also set these elements
    XOR operation done using ^

    yo = "sdfsdf"
    list = [ord(x) for x in yo]
    list = [bin(x) for x in list]
    int(list[0], 2) # this the binary back to int bianry is base 2
    chr(*int*)      # this converts from int to char
    ''.join(listOfChr)  # returns a string 
    
'''
