This repository contains a simple Python script demonstrating fundamental concepts such as string operations, slicing, user input, formatting, and basic arithmetic. It is ideal for beginners who are learning Python and want hands-on examples.

🚀 Features Covered
🔤 String Manipulation
Accessing characters using indexing
String slicing (positive and negative)
Skipping characters while slicing
Checking string properties:
startswith()
endswith()
📏 String Length
Finding the length of a string using len()
🧑‍💻 User Input
Taking input from users using input()
Displaying personalized messages
📨 Template Formatting
Replacing placeholders in a predefined string template using replace()
➗ Arithmetic Operation
Calculating remainder using modulus operator %
📂 File Structure
3_python.py   # Main Python script demonstrating all concepts
🧠 Concepts Demonstrated
1. String Slicing
name = "Harsh Singh"
print(name[0:4])   # Output: Hars
print(name[-5:-2]) # Negative slicing
2. Skipping Characters
print(name[0:9:2]) # Output: HrhSnh
3. String Functions
print(name.endswith("gh"))
print(name.startswith("Ha"))
4. User Input Example
fullname = input("Enter your name: ")
print(f"Good Afternoon {fullname}! How are you?")
5. Template Replacement
letter = ''' Dear <|Name|>,             
You are selected! <|Date|> '''
print(letter.replace("<|Name|>", "Harsh Singh").replace("<|Date|>", "12/12/2012"))
6. Remainder Calculation
a = int(input("Enter divisor: "))
b = int(input("Enter number: "))
print(b % a)
🛠️ How to Run
Install Python (if not already installed)

Clone this repository:

git clone <your-repo-url>

Navigate to the project folder:

cd <repo-folder>

Run the script:

python 3_python.py
🎯 Purpose

This script is created for:

Beginners learning Python basics
Practicing string operations and input/output
Understanding how small programs work step by step
📌 Future Improvements
Add more string methods
Include conditional statements
Expand into mini-projects
👤 Author

Harsh Kumar
