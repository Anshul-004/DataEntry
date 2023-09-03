# make a program which saves the data you enter init, to a different text file , with time stamp

from datetime import datetime

while(1):
    print("1.Enter Details\n2.Check Logs\n3.Exit")
    ch= int(input())
    if ch==1:
        print("Enter Your Name : ")
        name=input()

        print("Enter Your Weight : ")
        weight=input()

        now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #returns dateandtime


        with open("weightlogs.txt", "+a") as f:
            f.write(now+ "\t\t" +"Name : "+name+"\t"+"Weight : "+weight+"\n")
    
    elif ch==2:
        with open("weightlogs.txt", "r") as f:
            content=f.read()

        print(content)
    
    elif ch==3:
        break

    else :
        print("Invalid Input")