#!/usr/bin/env python3

from utils import xor_fixed_length

a_string = '1c0111001f010100061a024b53535009181c'
b_string = '686974207468652062756c6c277320657965'

print(xor_fixed_length(a_string, b_string).hex())
