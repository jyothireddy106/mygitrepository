s=input("input string is:")
dig=0
letter=0
for i in s:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        letter+=1
print("digits in a string:",dig)
print("letters in a string:",letter)