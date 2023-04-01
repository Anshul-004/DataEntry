# make a program which saves the data you enter init, to a different text file , with time stamp

from datetime import datetime
import os

print("Enter SPO2 level : ")
a=input()

print("Enter Pulse level : ")
b=input()

now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #returns dateandtime


f = open("logfile.txt", "a")
f.write(now+ "\t\t" +"SPO2 :"+a+"\t"+"Pulse :"+b+"\n")