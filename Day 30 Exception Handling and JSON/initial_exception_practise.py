
# BMI Calculation with an exception if a unrealistic number is entered
height = float(input("Height : "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")


bmi = weight / height ** 2
print(bmi)

# Keywords of Exceptions
# trying accessing a file which does not exist
# and getting data from a dictionary with a key which does not exist

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}

    print(a_dictionary["key"])
    # change key to sth else to check exception

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
    print("There was an error")


except KeyError as error_message:
    print(f"the key {error_message} does not exist")

else:
    content = file.read()
    print(content)


finally:
    file.close()
    print("File was closed")
    #raise KeyError
    #This always raises an error, no matter what happens.

# --------------------------------------------- #

# Short exception task

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):

    try:
        fruit = fruits[index]

    except IndexError:
        print("Fruit pie")

    else:
        print(fruit + " pie")

make_pie(4)

# --------------------------------------------- #

# Task to add an exception handling to make the code calculate the likes correctly

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)
