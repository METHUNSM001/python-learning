import pandas as pd

name_list = []
math_list = []
science_list = []
english_list = []

n = int(input("How many students? "))

for i in range(n):
    print(f"\nEnter details for student {i+1}")
    
    name = input("Enter name: ")
    math = int(input("Enter Math marks: "))
    science = int(input("Enter Science marks: "))
    english = int(input("Enter English marks: "))
    
    name_list.append(name)
    math_list.append(math)
    science_list.append(science)
    english_list.append(english)

data = {
    "Name": name_list,
    "Math": math_list,
    "Science": science_list,
    "English": english_list
}

df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Average"] = df["Total"] / 3


def grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 50:
        return "B"
    else:
        return "C"

df["Grade"] = df["Average"].apply(grade)

print("\nFull Result Table:")
print(df)

passed = df[df["Average"] >= 50]
print("\nPassed Students:")
print(passed)

#
topper = df[df["Total"] == df["Total"].max()]
print("\nTop Scorer:")
print(topper)