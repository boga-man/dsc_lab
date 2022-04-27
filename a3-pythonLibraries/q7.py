import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading the dataset from the csv file
df = pd.read_csv("./Salary_Data.csv")
print("a. Dataset read from the csv: ")
print(df);

# Display the information related to the dataset such as the number of rows and columns
print("\n\nb. Information related to the dataset: ")
print("Number of rows: ", df.shape[0])
print("Number of columns: ", df.shape[1])

# display the head of dataframe
print("\n\nc. Head of the dataframe: ")
print(df.head())

# describe the dataframe
print("\n\nd. Describe the dataframe: ")
print(df.describe())

# Display a random sample of the dataframe
print("\n\ne. Display a random sample of the dataframe: ")
print(df.sample(6))


