
#* list comprehension

# numbers = [1,2,3,4,5]
# name = "Kashish"

# add1_list = [x+1 for x in numbers]
# new_list = [letter for letter in name]

# print(add1_list)
# print(new_list)


# range(1,5)
# range_list = [x+x for x in range(1,5)]
# print(range_list)


# names = ["Kashish", "Aman", "Rohit", "Ankush", "Sahil"]
# new_names = [name.upper() for name in names if len(name) > 5]
# print(new_names)


#* dictionary comprehension
# import random

# names = ["Kashish", "Aman", "Rohit", "Ankush", "Sahil"]
# new_dict = {name:random.randint(1,100) for name in names}

# passed_students = {name:marks for (name, marks) in new_dict.items() if (marks > 40)}

# print(new_dict)
# print(passed_students)


#* loop through a dataframe
import pandas

students_dict = {
    "student": ["Kashish", "Aman", "Rohit", "Ankush", "Sahil"],
    "score": [45, 78, 56, 89, 34]
}

student_df = pandas.DataFrame(students_dict)
print(student_df)

for (index, row) in student_df.iterrows():
    print(row)