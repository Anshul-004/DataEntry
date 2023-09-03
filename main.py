# make a program which saves the data you enter init, to a different text file , with time stamp

from datetime import datetime
import os

print("Enter Your Name : ")
name=input()

print("Enter Your Weight : ")
weight=input()

now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #returns dateandtime


f = open("weightlogs.txt", "a")
f.write(now+ "\t\t" +"Name : "+name+"\t"+"Weight : "+weight+"\n")