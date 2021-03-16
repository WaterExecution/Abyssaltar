# solution
from subprocess import PIPE, Popen
import textwrap
import binascii
import base64


###run local file###
def run(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

estimateCharacter = 100                 # guess flag size ignore if flag size is smaller than 100
blockSize = 16                          # change to block size of encryption !!!IMPORTANT!!!
guesses = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ" # possible characters in flag
found = ""
flag = ""

for i in range(1, estimateCharacter):
 block1="A"*blockSize                   # X is just padding to fill in the 16 blockSize 
 block2="A"*blockSize                   # AAAABBBBCCCCDDDD AAAABBBBCCCCDDDD FLAGXXXXXXXXXXXX // hash{block1} = hash{block2} 
                                        # AAAABBBBCCCCDDD? AAAABBBBCCCCDDDF LAGXXXXXXXXXXXXX // Guess ? in order to get hash{block1} = hash{block2} 
 if len(flag) >= blockSize:
  block1 = flag[-blockSize+1:]          # SUPERDUPERLONGFL AAAABBBBCCCCDDDD SUPERDUPERLONGFL AGXXXXXXXXXXXXX  // when flag is longer than 16
 else:                                  # UPERDUPERLONGFL? AAAABBBBCCCCDDDS UPERDUPERLONGFLA GXXXXXXXXXXXXXX
  block1 = block1[:-i]
 block2 = block2[:-(i%blockSize)]
  
 for char in guesses:
  if len(flag) >= blockSize:
   guessBlock = block1 + char + block2
  else:
   guessBlock = block1 + found + char + block2                  # AAAABBBBCCCCDDF? AAAABBBBCCCCDDFL // Adds previously found to block1

  b64cipher = str(run("python3 server.py " + guessBlock))[2:-3] # local file
    
  # p = remote("137.137.137.137","1337")
  # p.send("guessBlock")
  # p.recv()
  # x = p.recv()
    
  cipher = base64.b64decode(b64cipher)                          # local/server (adjust if needed)
  hex = str(binascii.hexlify(cipher))[2:-1]                     # gets hash
  focusedBlock = (len(flag)//blockSize+1)*32                    # move to next block if flag is longer than 16
  if str(hex)[:32] == str(hex)[focusedBlock:focusedBlock+32]:
   print(char)
   found += char
   flag += char
   if len(found) >= blockSize:
    found = ""
   break
   
