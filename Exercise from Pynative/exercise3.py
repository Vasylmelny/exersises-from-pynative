# Write a Python code to accept a string from the user and display characters present at an even index number.
#
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

stri=input("Enter a text:")
for i in range(0,len(stri),2):
    print(stri[i],end=" ")
