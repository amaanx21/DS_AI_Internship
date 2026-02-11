#task1

import pandas as pd
products=pd.Series([700,150,300],index=["Laptop","Mouse","Keyboard"])
laptop_price = products["Laptop"]
first_two = products.iloc[0:2]
print("Full Series:\n")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products(Positional Indexing):")
print(first_two)

#task2

import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])

print("Original Series:\n")
print(grades)

print("\nMissing Values (True means missing):\n")
print(grades.isnull())

filled_grades = grades.fillna(0)

print("\nSeries After Filling Missing Values:\n")
print(filled_grades)

high_scores = filled_grades[filled_grades > 60]

print("\nScores Greater Than 60:\n")
print(high_scores)

#task3

import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

print("Original Usernames:\n")
print(usernames)
cleaned_usernames = usernames.str.strip().str.lower()

print("\nCleaned Usernames:\n")
print(cleaned_usernames)

contains_a = cleaned_usernames.str.contains('a')

print("\nNames Containing Letter 'a':\n")
print(contains_a)
