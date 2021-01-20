# list comprehensions
# numbers=[1,2,3]
# new_list=[item+1 for item in numbers]
# print(new_list)

# Exercise one
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
sq_nums=[n**2 for n in numbers]
print(sq_nums)
# Exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result=[n for n in numbers if n%2==0]
print(result)


# Exercise 3
# use file 1 and file 2 text files
# f_1=open("file1.txt")
# list_1=[(line.strip()).split() for line in f_1]
# print(list_1)
with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

result=[int(n) for n in file1_data if n in file2_data]
print(result)

# Dictonary Comprhension's
# Exercise 1 sentence to dict of sentece and len of sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words=sentence.split()
len_di={key:len(key) for key in words}
print(len_di)

# Exercise 2 celcius to Farenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
temp_f={key:((value*9/5)+32) for (key,value) in weather_c.items()}
print(temp_f)
