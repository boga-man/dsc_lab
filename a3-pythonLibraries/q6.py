import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# create a dataframe with the days in a week and their corresponding attendance count
attendance = np.random.randint(60, 190, size=(1,7))
attendanceList = attendance[0].tolist()
df = pd.DataFrame({'Days':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
                     'Attendance':attendanceList})  
# print the dataframe
print("a. Dataframe: ")
print(df)
# sorting the dataframe according to the attendance count
sortedDf = df.sort_values(by=['Attendance'], ascending=True)
print("\n\nb. Sorted dataframe: ")
print(sortedDf)

# day with maximum attendance
print("\n\nc. Day with maximum attendance :")
print("Using the max() function: ")
print(df[df.Attendance == df.Attendance.max()])

# first two days of the week and the number of attendees
print("\n\nd. First two days of the week and the number of attendees: ")
print(df.head(2))

# plot the dataframe
print("\n\ne. Plotting the dataframe....")
df.plot(kind='bar', x='Days', y='Attendance')
plt.title('Day vs Attendance plot')
plt.show()

