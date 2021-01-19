import pandas as pd

# # #
# # # # with open('weather_data.csv') as data_file:
# # # #     data=data_file.readlines()
# # # #     print(data)
# # # #
# # # #
# # #
# # #
# # # df=pd.read_csv('weather_data.csv')
# # # # print(df)
# #
# # # import csv
# # import pandas as pd
# #
# # #
# # # with open('weather_data.csv') as data_file:
# # #     data = csv.reader(data_file)
# # #     temperature = []
# # #
# # #     for row in data:
# # #         if row[1] != "temp":
# # #             temperature.append(int(row[1]))
# # #     print(temperature)
# #
# #
# # df = pd.read_csv('weather_data.csv')
# # # print(df)
# #
# # df_dict = df.to_dict()
# # print(df_dict)
# #
# # # temp_list=df["temp"].to_list()
# # # print(temp_list)
# # # print(sum(temp_list)/len(temp_list))
# # print(df["temp"].mean())
#
# print(df["temp"].max())
#
# # Get Data in colums
# # print(df["condition"])
# # or
# print(df.condition)
#
# # get data in a row
# print(df[df.day == "Monday"])
#
# # row which has max temp
# print(df[df['temp'] == df['temp'].max()])
#
# monday = df[df.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_f=monday_temp*9/5 +32
#
# print(monday_temp_f)

# using the squirrel Data to create a cs called as Squirrel count
sq_d = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# clrs=["Gray","Cinnamon","White"]
# col = ["Fur Color", "Count"]
# sq_n = pd.DataFrame(columns=col)
# tmp_s=sq_d["Primary Fur Color"]
# # for item in clrs:
# #     sq_n["Fur Color"]=item
# #
# #     sq_n["Count"]=tmp_s.str.count(item)
# sq_l=sq_d.groupby("Primary Fur Color").size()

# print(sq_l)

grey_sq= len(sq_d[sq_d["Primary Fur Color"]=="Gray"])
cin_sq= len(sq_d[sq_d["Primary Fur Color"]=="Cinnamon"])
blk_sq= len(sq_d[sq_d["Primary Fur Color"]=="Black"])

print(grey_sq)
print(cin_sq)
print(blk_sq)

data_dict ={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_sq,cin_sq,blk_sq]
}

df=pd.DataFrame(data_dict)
df.to_csv('squirel_count.csv')