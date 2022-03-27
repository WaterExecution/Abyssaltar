from pwn import *
import re
numbers = []
s = remote("c1.lagncrash.com", 9007)
for i in range(65):
    for i in range(10):
        s.recvuntil("Enter a number(or 'exit' to exit the program):")
        s.send('1')
        text = s.recvline().decode()
        num = re.findall("\d+", text)[0]
        numbers.append(int(num))
    s.send('y')

import random
from mt19937predictor import MT19937Predictor
predictor = MT19937Predictor()

for i in numbers:
    predictor.setrandbits(i,32)
for i in range(10):
    predict = predictor.getrandbits(32)
    s.recvuntil("Enter a number(or 'exit' to exit the program):")
    s.send(str(predict))
    print(s.recvline().decode())

print(s.recv().decode())
