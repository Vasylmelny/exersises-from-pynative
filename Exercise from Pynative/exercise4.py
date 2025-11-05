# Write a Python code to remove characters from a string from 0 to n and return a new string.

def remove_chars(word, n):
    if n < len(word):
        print('Original string:', word)
        x = word[n:]
        return x
    else:
        print("Oops! n is too big")

print(remove_chars("hello",2))
