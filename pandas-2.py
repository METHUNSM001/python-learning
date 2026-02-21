'''# Voting List with Pandas

A simple Python script that takes user input and creates a **voting list** using **pandas DataFrame**.  

- Only users **older than 18** are added.  
- Displays their **name, age, course, and city** in a table.  

---

## How It Works

1. Asks the user to input their **name, age, course, and city**.  
2. Checks if the user is **eligible to vote** (age > 18).  
3. Adds eligible users to a **DataFrame**.  
4. Prints the **voting list**.  

---

## Example

**Input:**

Enter name: Rahul
Enter age: 20
Enter course: Science
Enter city: Delhi


**Output:**

Rahul, you are added to the voting list

Voting List:
name age course city
0 Rahul 20 Science Delhi


Purpose: Practice user input handling and DataFrame creation in Python.
'''
import pandas as pd

name_list = []
age_list = []
course_list = []
city_list = []

for i in range(1):
    
    name_input = input("Enter name: ")
    age_input = int(input("Enter age: "))
    course_input = input("Enter course: ")
    city_input = input("Enter city: ")

    if age_input > 18:
        print(f"{name_input}, you are added to the voting list ")
        name_list.append(name_input)
        age_list.append(age_input)
        course_list.append(course_input)
        city_list.append(city_input)
    else:
        print(f"Sorry {name_input}, you are not eligible to vote ")
data = {
    "name": name_list,
    "age": age_list,
    "course": course_list,
    "city": city_list
}

df = pd.DataFrame(data)

print("\nVoting List:")
print(df)