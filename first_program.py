# print("Hello World!")
# # To print in multiple lines put in ''' or """
# print('''Hello World first line
# Second line''')
# ##or """
# print("""Printing multiple lines in 
# using doube quotes""")
##install external module use it (Here python text to speech)
# import pyttsx3
# pyttsx3.speak("I will speak this text")

##To print contens of a directory

import os
dir_path='C:/Users/a909920/Downloads'
contents=os.listdir(dir_path)
# print(contents)
for i in contents:
    print(i)
