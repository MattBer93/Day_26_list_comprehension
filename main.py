#DICTIONARIES

# import random
#
# # new_dict = {new_key:new_value for (key, value) in <dict>.items() if <condition>}
#
# students = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {student:random.randint(0, 101) for student in students}
# # My solution (it works!):
# # passed_students = {student:students_score[student] for student in students_score if students_score[student] >= 60}
# #teacher's solution:
# passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
#
# items = students_scores.items()
# print(items)
#
# #Exercise:
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list = sentence.split()
# result = {word: len(word) for (word) in list}
# print(result)

#Excercise 2:
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: temp_c * 9/5 + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

#PANDAS DATAFRAMES
# import pandas
#
# students_dict = {
#     'student': ['Angela', 'James', 'Lily'],
#     'score': [56, 76, 98]
# }
#
# students_data_frame = pandas.DataFrame(students_dict)
#
# #loop through rows of data frame
# new_list = []
# for (index, row) in students_data_frame.iterrows():
#     if row.student == 'Angela':
#         print(row.score)

#NATO ALPHABET EXERCISE
#TODO 1:Create a dictionary in format:
    #{"A": "Alpha"}
import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2: Create a list of phonetic code words rom a word that the user inputs
user_input = input("Spell your word with the NATO alphabet:\n").upper()
output_list = [nato_dict[letter] for letter in user_input]
print(output_list)


