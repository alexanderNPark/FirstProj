#----------------------------------------------
#Name: tax
#Purpose: Collect Tax
#Author: Alex Park
#Date: 10/1/17
#----------------------------------------------
"""
To receive price and multiply tax to find overall price with tax
"""
value = float(input("Please Enter in Price in $:"))
RATE = 0.0875
print("Sales Tax: $%.2f" %(value*RATE)) # .2f i am sure is a floating point mechanism that exists in C therefore in Python
print("Total Cost:$%.2f"%(value*(1+RATE)))