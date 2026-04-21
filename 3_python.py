# string and string slicing 
name =  "Harsh Singh"

frontshort = name[0:4]
print(frontshort)
namechar = name[6]
print(namechar)

# negative slicing
print(name[-5:-2])

# skip slicing
print(name[0:9:2])  #in this it will print string from 0 to 8 by skippeing two strings 

# length of string
print(len(name))

print(name.endswith("gh"))  #This will tell weather the string ends with gh or not

print(name.startswith("Ha"))  #this will tell weather the string starts with Ha or not

# python program to display a user entered name followed by Good Afternoon using input () function.
fullname = input("Enter your name : ")
print(f"Good Afternoon {fullname} ! How are you")


# program to fill in a letter template given below with name and date.
letter = ''' Dear <|Name|>,             
You are selected! <|Date|> '''

print(letter.replace("<|Name|>","harsh singh").replace("<|Date|>","12/12/2012"))

# Python program to find remender
a = int(input("Enter a number by which you want to devide any number " ))
b = int(input("Enter a number which you want to devide by first number " ))
c = (b % a)
print(c)

