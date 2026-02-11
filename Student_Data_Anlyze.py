import pandas as pd
import numpy as np


data = pd.read_csv("Student_performance.csv")

# shape of data
print(data.shape)
print(data.info())


# complating data

data["Study_Hours_Per_Day"] = data["Study_Hours_Per_Day"].fillna(data["Study_Hours_Per_Day"].mean())
data["Attendance_Percentage"] = data["Attendance_Percentage"].fillna(data["Attendance_Percentage"].mean())

data["Age"] = data["Age"].clip(lower=10, upper=30)
data["Attendance_Percentage"] = data["Attendance_Percentage"].clip(lower=0, upper=100)

# removing duplicate row

print(data.duplicated().sum())

# data has no duplicat rows

Avg_final_city = data.groupby("City")["Final_Score"].mean()
print("\nAverage fainal score per city : \n", Avg_final_city)

max_Final_Score = data["Final_Score"].max()
print("\nMaximum final score per city : \n", max_Final_Score)


# specific student

sp_Student = (data["Attendance_Percentage"]) > 90 & (data["Study_Hours_Per_Day"] > 5)
print("\n student with more attendance and more lerning : \n", sp_Student)

# high attendence and more study == more score ?

low_Study = (data["Attendance_Percentage"] < 65) & ( data["Study_Hours_Per_Day"] < 5)
mid_Study = (data["Attendance_Percentage"] < 70) & (data["Study_Hours_Per_Day"] < 6)
high_Study = (data["Attendance_Percentage"] > 70) & (data["Study_Hours_Per_Day"] > 7)

print("low student : \n", low_Study)
print("mid student : \n", mid_Study)
print("High student : \n", high_Study)

lw_avg_score = data.loc[low_Study, "Final_Score"].mean()
md_avg_score = data.loc[mid_Study, "Final_Score"].mean()
hw_avg_score = data.loc[high_Study, "Final_Score"].mean()

print("Low attendance and less study student average score : \n", lw_avg_score)
print("Mid attendance and mid study student average score : \n", md_avg_score)
print("High attendance and high study student average score : \n", hw_avg_score)

# finding mean meadian and std using numpy

sh_mean = np.mean(data["Study_Hours_Per_Day"])
sh_median = np.median(data["Study_Hours_Per_Day"])
sh_std = np.std(data["Study_Hours_Per_Day"])

print("Mean of study hour : \n",sh_mean)
print("Median of study hour : \n",sh_median)
print("Std of study hour : \n",sh_std)



fs_mean = np.mean(data["Final_Score"])
fs_median = np.median(data["Final_Score"])
fs_std = np.std(data["Final_Score"])

print("Mean of final score : \n",fs_mean)
print("Median of final score : \n",fs_median)
print("Std of final score : \n",fs_std)

data["Sh_normalize"] = data["Study_Hours_Per_Day"]/data["Final_Score"]
data["fs_normalize"] = data["Final_Score"]/data["Sh_normalize"]

print("after adding normalization column the database is : \n", data.head())

# adding performance level

data["Performance_Level"] = pd.cut(
    data["Final_Score"],
    bins=[0,40,70,100],
    labels=["low","Midium","High"]
)

print("Data after adding performance level : \n" ,data.head())

# adding pass fail column

data["pass/fail"] = pd.cut(
    data["Final_Score"],
    bins=[0,39,100],
    labels=["fail","pass"],
    include_lowest=True
)

print("After adding pass/fail column : \n",data.head())

# seprating


X = data.drop("Final_Score", axis=1)

y = data["Final_Score"]

print("x : ",X.head())
print("Y : " ,y.head())

# convert categrical data into numerical data

city_dummis = pd.get_dummies(data["City"])
print("City dummis : ",city_dummis.head())

# saving the file

data.to_csv("student_performance_cleaned.csv", index=False)











