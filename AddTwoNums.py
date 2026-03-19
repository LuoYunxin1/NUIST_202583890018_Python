# Add Two Number in Pythen 
#Author :Luoyunxin
# Using a function 

# function to add two numbers 
def add (a,b):
 #converting input to float and adding
 result = float(a) + float(b)
 return result

#taking user input
a = input("Fiest Number:")
b = input("Second Number:")

#calling function
res = add (a,b)
print ("The Answer is:")
print (res)

