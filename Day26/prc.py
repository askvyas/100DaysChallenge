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