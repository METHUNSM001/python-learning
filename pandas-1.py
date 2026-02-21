import pandas as pd

data = {
    "cars" : ["bmw","ms","mb","rr"],
    "price" : ["2cr","3cr","4cr","5cr"],
    "milage" : [3,3,3.5,2]
}
df = pd.DataFrame(data)


df ["city"] = ["delhi","mumbai","kolkata","chennai"]

print(df[["cars","price","city"]])