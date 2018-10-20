# -*- coding: cp1252 -*-

import os
import time
import tkMessageBox
import random
import decimal
import httplib

r1 = 0
conn = ""
website = ""

def webcheck(website):
    website = raw_input("Welcome, what website would you like to hack? ")

a = 0
b = ""
limit = random.randint(500, 10000)
change = 100./limit
hackywords = ["Importing packets", "Uploading packets", "Opening packets", "Reciving sensitive information", "Reciving owner logins", "Bypassing security protocalls", "Logging in", "Downloading user information", "Downloading worker information", "Cleaning up", "Destroying data", "Website hacked"]
chars = """qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM<>?~@:{}[]#';./\,=-+_)(*&^%$£"!1234567890"""
c = 0
d = 0
i2 = 0
c2 = 0

os.system("title Website Hacker")

webcheck(website)

os.system("cls")
print("Preparing...")

for i in range(0, 100):
    i2 = i
    os.system("title " + str(i) + "%")
    time.sleep(0.01)
i2 = 0

os.system("cls")
print(hackywords[d]),
for i in range(1, random.randint(500, 999)):
    c += 1
    c2 += 1
    i2 += 0.1
    if c2 == 10:
        print("#"),
        c2 = 0
    os.system("title " + str(i2) + "%")
    if c == 100:
        c = 0
        d += 1
        print("")
        print("")
        print(hackywords[d]),
    time.sleep(decimal.Decimal(random.randrange(1, 500))/1000)

time.sleep(5)
os.system("cls")
os.system("title Error")
print("Error, malicious files have been intercepted from " + website +"!")
time.sleep(2)
print("Files are encoded, attempting to decode")
time.sleep(3)
os.system("cls")
for i in range(1, limit):
    a += change
    b = a
    print(chars[random.randint(1, len(chars) - 1)]),
    os.system("title Decoding at " + str(b)+ "%")
print("")
time.sleep(3)
os.system("cls")
print("Files decoded, running code now")
os.system("title Running Code")
time.sleep(1)
print("Warning, message boxes may appear")
time.sleep(3)
tkMessageBox.showinfo("", "Well done, you have found my website's, " + website + ", virus!")
tkMessageBox.showinfo("", "I will now break your computer!")
time.sleep(2)
tkMessageBox.showinfo("", "Wow! Ha! You thought I could hack a website! You're so gullible! Bye!")

