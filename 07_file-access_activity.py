# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:21:06 2019

@author: Jhonnathan
"""

file=open("devices.txt","a")
while True:
    x=input("Input a new device: ")
    newitem=x
    file.write(newitem+"/n")
    if x=="exit":
        print ("All done")
        break


    