'''Write Script which extracts All Email Addresses from "sample.txt" file
and return list of emails , handle exception if file not found 

Output:
    ['test@gmail.com', 'admin@yahoo.com']'''
########################################################################################################
import re

try:
    with open("sample.txt", "r") as file:
        data = file.read()
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', data)
        print(emails)
except FileNotFoundError:
    print("File 'sample.txt' not found.")