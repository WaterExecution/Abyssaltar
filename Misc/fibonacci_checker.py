from pwn import *
import math

def checkPerfectSquare(n):
    sqrt = int(math.sqrt(n))
    if pow(sqrt, 2) == n:
        return True
    else:
        return False

def isFibonacciNumber(n):
    res1 = 5 * n * n + 4
    res2 = 5 * n * n - 4
    if checkPerfectSquare(res1) or checkPerfectSquare(res2):
        return True
    else:
        return False

def sendfibo():
    out = str(chall.recv(1024))
    print(out)
    outre = re.search(reg, out).group()
    outparsed = outre[1:-1]
    outparsedlist = outparsed.split(",")
    for x in outparsedlist:
        if isFibonacciNumber(int(x)):
            chall.sendline(x)
    print(chall.recv(1024))

chall = remote("umbccd.io", 6000)
reg = re.compile(r'\[([^]]+)\]')

while True:
    sendfibo()
