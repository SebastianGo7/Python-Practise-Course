# List comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
# print(new_list)


# This code takes the numbers of the numbers list
# and their squares are saved in the list squared_numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
# print(squared_numbers)


# This list comprehension creates a list, which only contains the even
# numbers of the numbers list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]
# print(result)


# This list comprehension takes 2 lists which have numbers
# then the numbers which are in both lists are added
# are added to new list

with open("file1.txt", mode="r") as file1:
    content_1 = file1.readlines()

with open("file2.txt", mode="r") as file2:
    content_2 = file2.readlines()

list_together = [int(number) for number in content_1 if number in content_2]
# print(list_together)


# create a random score between 0 and 100 and add them with the
# names in the list names to a dictionary
import random
names = ["Alex", "Beth", "Caroline", "Cave", "Eleanor", "Marvin"]
student_score = {name: random.randint(0, 100) for name in names}


# loop through students and create a new dictionary with the student
# names and their scores if their score is over 60
passed_students = {student: score for (student, score) in student_score.items() if score > 60}
# print(passed_students)


# this code takes a sentence and calculates the number of letters of each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for (word) in sentence.split()}
#print(result)


# convert a dictionary of temperatures of Celsius to
# a dictionary with temperatures of Fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {key: (value * 9/5)+32 for (key, value) in weather_c.items()}
# print(weather_f)



# use loops with pandas dataframe and iterate through them

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)


# print(student_data_frame)
# for (key, value) in student_data_frame.items():
#     print(key)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
        #print(row)
        #print(index)
# each row is is a panda series object




