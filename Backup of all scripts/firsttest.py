from pwn import process
from datetime import datetime

can = process("candumphi.elf")

while True:
    output = str(datetime.now()) + can.recvline().decode("utf-8")
    with open("second_test.txt", "a+") as file:
        file.write(output)
