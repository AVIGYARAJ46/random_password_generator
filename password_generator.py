# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 00:19:20 2024

@author: avigy
"""

import random
import string

pass_len=8
charvalues=string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(pass_len):
    password+=random.choice(charvalues)
    
print("your password is",password)