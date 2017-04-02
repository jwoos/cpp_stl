#! /usr/bin/env python3

import base64

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b_array = bytearray.fromhex(hex_string)

print(base64.b64encode(b_array))
