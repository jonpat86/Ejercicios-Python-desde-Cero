# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:27:31 2019

@author: Jhonnathan
"""

aclnum=int(input("What is the IPv4 ACL number? "))
if aclnum>=1 and aclnum<=99:
    print("This is a standard IPv4 ACL")
elif aclnum >=100 and aclnum<=199:
    print("This is a extended IPv4 ACL")
else:
    print("This is not a standard or extended IPv4 ACL")