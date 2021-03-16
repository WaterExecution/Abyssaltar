#!/usr/bin/env python3
#https://zachgrace.com/posts/attacking-ecb/
#Really good explanation for ECB
import sys
from Crypto.Hash import SHA256
from Crypto.Cipher.AES import AESCipher
import base64

flag = "THIS_IS_AN_INCREDIBLY_LONG_STRING_FOR_TEST_PURPOSES_AS_THE_FLAG_MAY_ALSO_BE_LONG" #83
block_size = 16 # CAN BE 8 OR MULTIPLE OF 16

def get_key(flag):
 flag = flag.encode('utf-8')
 h = SHA256.new()
 h.update(flag)
 key = h.digest()
 return key

key = get_key(flag)
text = str(sys.argv[1])
UserInput = text + flag
padding = block_size - (len(text) % block_size)
UserInput += 'P' * padding  # must be divisible by 16 total length
cipher = AESCipher(key).encrypt(UserInput)
print(str(base64.b64encode(cipher))[2:-1])
