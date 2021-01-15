# import  pandas as pd
#
# # with open('weather_data.csv') as data_file:
# #     data=data_file.readlines()
# #     print(data)
# #
# #
#
#
# df=pd.read_csv('weather_data.csv')
# # print(df)

# import csv
import pandas as pd

#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)


df = pd.read_csv('weather_data.csv')
# print(df)

df_dict = df.to_dict()
print(df_dict)

# temp_list=df["temp"].to_list()
# print(temp_list)
# print(sum(temp_list)/len(temp_list))
print(df["temp"].mean())

print(df["temp"].max())

# Get Data in colums
# print(df["condition"])
# or
print(df.condition)

# get data in a row
print(df[df.day == "Monday"])

# row which has max temp
print(df[df['temp'] == df['temp'].max()])

monday = df[df.day == "Monday"]
monday_temp = monday.temp
monday_temp_f=monday_temp*9/5 +32

print(monday_temp_f)