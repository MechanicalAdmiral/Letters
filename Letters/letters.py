import os
import csv
import sys

rowlastnum = 0
if len(sys.argv) > 1:
    rowlastnum = int(sys.argv[1])

def dlog(val, filename, setting="w"):
    qwer = open(filename, setting)
    qwer.write(val)
    qwer.close()

def getlogaverage(filename):
    qwey = open(filename, "r")
    bigno = 0
    subno = 0
    for i in qwey:
        bigno += int(i)
        subno += 1
    if subno == 0:
        return "No average."
    return bigno / subno

with open('reddit_depression_suicidewatch.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    rownum = 0
    autoswitch = 0
    for row in csv_reader:
        if rownum < rowlastnum:
            rownum += 1
            continue
        os.system("cls")
        if(len(row[0].split(" ")) < 160 and not autoswitch):
            print("This post is less than the average amount of words. To enable autoswitch for these types of posts, type 'autoswitch'.")
        if(len(row[0].split(" ")) < 160 and autoswitch):
            rownum += 1
            continue
        if(autoswitch):
            print("Autoswitch is on.")
        print("Type 'quit' to quit.")
        print("Type 'skipto:NUMBER' to skip to a number.")
        print("Type 'cleanlog' to clean the word counter log.")
        print("Num = ", rownum)
        print("Label = ", row[1])
        print("Word Count = ", len(row[0].split(" ")))
        print("Word Average = ", getlogaverage("wordcounter.txt"))
        print(row[0])
        dlog(row[0], "lastdetails.txt")
        dlog(str(rownum), "lastno.txt")
        dlog(str(len(row[0].split(" "))) + "\n", "wordcounter.txt", "a")
        cont = input()
        if cont == "quit":
            break
        if cont.startswith("skipto:"):
            rowlastnum = int(cont.split(":")[1])
        if cont == "cleanlog":
            dlog("", "wordcounter.txt")
        if cont == "autoswitch":
            if (autoswitch):
                autoswitch = 0
            else:
                autoswitch = 1
        rownum += 1