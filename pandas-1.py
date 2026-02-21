'''# Pandas DataFrame Practice: Car Data

This repository contains a simple Python script that demonstrates how to use **pandas DataFrames** to store, manipulate, and display tabular data.

---

## Project Description

#In this practice, we:

#- Created a **dictionary** to hold car information (`cars`, `price`, `milage`).
#- Converted the dictionary into a **pandas DataFrame**.
#- Added a new column `city` to the DataFrame.
#- Displayed only selected columns (`cars`, `price`, `city`).

---

## Files

#- `car_dataframe.py` – Python script with the DataFrame practice.

#---

## Code Example
'''
import pandas as pd

data = {
    "cars" : ["bmw","ms","mb","rr"],
    "price" : ["2cr","3cr","4cr","5cr"],
    "milage" : [3,3,3.5,2]
}
df = pd.DataFrame(data)


df ["city"] = ["delhi","mumbai","kolkata","chennai"]


print(df[["cars","price","city"]])
