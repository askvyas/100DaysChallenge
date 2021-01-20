student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
df=pandas.read_csv('nato_phonetic_alphabet.csv')
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_name={row.letter.lower():row.code for (index,row) in df.iterrows()}
print(nato_name)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_inp=input("Enter Your Name")
ur_name=[l.lower() for l in user_inp]
res=[val for (key,val) in nato_name.items() if key in ur_name]
print(res)

