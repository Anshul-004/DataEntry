# make a program which saves the data you enter init, to a different text file , with time stamp

import time
import os

print("Enter SPO2 level : ")
a=input()

f = open("logfile.txt", "a")
f.write(a+"\n")
