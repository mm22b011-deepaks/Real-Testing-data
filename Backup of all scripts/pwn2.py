from pwn import *

p = process("./candump.sh")


while 1 :
	inp = p.recvline()
	print(inp)
