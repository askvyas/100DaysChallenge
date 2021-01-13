# file = open('tasks.txt')
# contents = file.read()
#
# print(contents)
# file.close()

with open("tasks.txt") as file:
    contents=file.read()
    print(contents)
#
# with open("tasks.txt",mode='w') as file:
#     file.write("Written using files")
#     print(contents)    //This deletes all the prev text inside the file

#
# with open("tasks.txt",mode='a') as file:
#     file.write("\nWritten using files")
#     print(contents)
#
# # Creating a file using w mode
#
# with open("new_file.txt",mode='w') as file:
#     file.write("I Created a file using python")

# working with files and paths
# # using absolute path
# with open("/Users/askvyas/Desktop/hello.txt" ) as file:
#     contents=file.read()
#     print(contents)

with open("../../../Desktop/hello.txt" ) as file:
    contents=file.read()
    print(contents)