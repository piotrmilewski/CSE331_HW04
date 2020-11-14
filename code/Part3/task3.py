from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard")

p = session.process('ls -l /problems/overflow-1_2_305519bf80dcdebd46c8950854760999', shell=True)

print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
