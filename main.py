#!/usr/bin/env python3

# import os

# def main():
#     print("Items exists: " + str(os.path.exists("demo.txt")))
#     print("Items exists: " + str(os.path.isdir("demo.txt")))
#     print("Is item a directory: " + str(os.path.isfile("demo.txt")))
#     print("Item exists: " + str(os.path.realpath("demo.txt")))
#     print("Items path and name: " + str(os.path.split(os.path.realpath("demo.txt"))))

#     t*time.ctime()



# if __name__ == "__main__":
#     main()


# import os

# def check_spotify_in_downloads():
#    
#     downloads_path = os.path.expanduser("~/Downloads")
#     spotify_app_path = os.path.join(downloads_path, "/Users/uche/Downloads/Install Spotify.app")

#  
#     if os.path.exists(spotify_app_path):
#         return True
#     else:
#         return False

# def main():
#     if check_spotify_in_downloads():
#         print("Spotify is located in your Downloads directory.")
#     else:
#         print("Spotify is not located in your Downloads directory.")

# if __name__ == "__main__":
#     main()


# import os
# import time
# from datetime import datetime

# def check_spotify_in_downloads():
    
#     downloads_path = os.path.expanduser("~/Downloads")
#     spotify_app_path = os.path.join(downloads_path, "/Users/uche/Downloads/Install Spotify.app")

    
#     if os.path.exists(spotify_app_path):
#         creation_time = os.path.getctime(spotify_app_path)
#         return creation_time
#     else:
#         return None

# def main():
#     creation_time = check_spotify_in_downloads()
#     if creation_time:
        
#         creation_date = datetime.fromtimestamp(creation_time)
#         current_date = datetime.now()
#         days_since_download = (current_date - creation_date).days

#         print(f"Spotify was downloaded {days_since_download} days ago.")
#     else:
#         print("Spotify is not located in your Downloads directory.")

# if __name__ == "__main__":
#     main()


# import pandas as pd
# import os


# csv_file = "NASDAQ - CSV Copy - Copy.csv"
# txt_file = "car-inventory.txt"
# json_file = "data.json"


# print(f"CSV file exists: {os.path.exists(csv_file)}")
# print(f"TXT file exists: {os.path.exists(txt_file)}")
# print(f"JSON file exists: {os.path.exists(json_file)}")


# try:
#     data_csv = pd.read_csv(csv_file)
#     print("CSV Data:")
#     print(data_csv)
# except FileNotFoundError:
#     print("CSV file not found.")
# except pd.errors.EmptyDataError:
#     print("CSV file is empty.")
# except Exception as e:
#     print(f"An error occurred while reading the CSV file: {e}")


# try:
#     data_txt = pd.read_csv(txt_file, sep="\t")
#     print("\nTXT Data:")
#     print(data_txt)
# except FileNotFoundError:
#     print("TXT file not found.")
# except pd.errors.EmptyDataError:
#     print("TXT file is empty.")
# except Exception as e:
#     print(f"An error occurred while reading the TXT file: {e}")


# try:
#     data_json = pd.read_json(json_file)
#     print("\nJSON Data:")
#     print(data_json)
# except FileNotFoundError:
#     print("JSON file not found.")
# except ValueError:
#     print("JSON file is empty or contains invalid data.")
# except Exception as e:
#     print(f"An error occurred while reading the JSON file: {e}")


# if os.path.exists(csv_file):
#     with open(csv_file, 'r') as file:
#         content = file.read()
#         print("\nCSV File Content:")
#         print(content)

# if os.path.exists(txt_file):
#     with open(txt_file, 'r') as file:
#         content = file.read()
#         print("\nTXT File Content:")
#         print(content)


# if os.path.exists(json_file):
#     with open(json_file, 'r') as file:
#         content = file.read()
#         print("\nJSON File Content:")
#         print(content)


# class shape:
#     def calculate_area_of_rectangle(self, l, b):
#         result=l*b
#         print(result)
#     calculate_area_of_rectangle(3, 4, 6)

#     def calculate_area_of_triangle(self, b, h):
#         result=1/2*b*h
#         print(result)
#     calculate_area_of_triangle(3,4,6)

#     def calculate_volume_of_cone(self, r, h):
#         result = (1/3) * 3.14159 * r * r * h
#         print(result)
#     calculate_volume_of_cone(3, 3, 4)

#     def calculate_volume_of_cylinder(self, r, h):
#         result = 3.14159 * r * r * h
#         print(result)
#     calculate_volume_of_cylinder(3,4,6)



# class car:
#     def run(self):
#         print("My car has run")

# def main():
#     toyota=car()
#     toyota.run()

# class Student:
#     def __init__(self, name, roll_number, laptop_brand, laptop_cpu, laptop_hd):
#         self.name = name
#         self.roll_number = roll_number
#         self.laptop = LapTop(laptop_brand, laptop_cpu, laptop_hd)

#     def show(self):
#         print("This is my id card showing", self.name, self.roll_number)

#     def talk(self):
#         print("I have talked")

# class LapTop:
#     def __init__(self, brand, CPU, HD):
#         self.brand = brand
#         self._CPU = CPU
#         self._HD = HD


# student1 = Student("Jude Peter", "12345", "Dell", "Intel i5", "500GB")
# student1.show()  # This is my id card showing John Doe 12345
# student1.talk()  # I have talked

# print(f"Laptop Brand: {student1.laptop.brand}")
# print(f"Laptop CPU: {student1.laptop._CPU}")
# print(f"Laptop HD: {student1.laptop._HD}")


# if __name__ == '__main__':main()



# import pandas as pd
# from tabulate import tabulate

# # Create a DataFrame
# data = {
#     'Name': ['Nkwocha Franklin', 'Peter Paul', 'Johnson James', 'Prince Jude'],
#     'Matric No': ['A12345', 'B23456', 'C34567', 'D45678'],
#     'Course': ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering'],
#     'Project Title': ['Software Engineering', 'Web development', 'Robotics', 'Product Design'],
#     'Expected Grad Year': [2024, 2023, 2025, 2024],
#     'Outstanding Fee': [500, 0, 150, 200]
# }

# # Convert the dictionary to a DataFrame
# df = pd.DataFrame(data)

# # Display the DataFrame using tabulate for better formatting
# print(tabulate(df, headers='keys', tablefmt='pretty'))



# import pandas as pd
# data=pd.DataFrame({
#     'A1':[1,2,3],
#     'A2':[4,5,6],
#     'A3':[7,8,9]
# }, index=['X', 'Y','Z'])

# print(data)

# import pandas as pd 

# data = pd.DataFrame({
#     'Name': ['Uche', 'Chioma', 'Peter', 'Deji'],
#     'Age': [18, 19, 20, 10],
#     'Salary': [1000000, 100, 10200, 2000],
#     'Department': ['Tech', 'Doctor', 'Science', 'Engineering']
# })

# sorted_data = data.sort_values(by='Salary')

# #print(sorted_data)


# sorted_data_ascending = data.sort_values(by='Salary', ascending=False)

# print(sorted_data_ascending)

# import pandas as pd
# import numpy as np
# from scipy import stats

# data = pd.DataFrame({
#     'Student': ['Joe', 'Ben', 'Tim', 'Jim', 'Kim', 'Yun', 'Hun', 'Ada', 'Eze', 'Obi'],
#     'Maths': [73, 40, 71, 25, 40, 58, 60, 62, 64, 60],
#     'Biology': [49, 71, 72, 39, 73, 72, 42, 42, 61, 60],
#     'C.Science': [59, 72, 73, 42, 59, 58, 80, 37, 73, 72]
# })

# mean = data[['Maths', 'Biology', 'C.Science']].mean()898

# median = data[['Maths', 'Biology', 'C.Science']].median()

# mode = data[['Maths', 'Biology', 'C.Science']].mode().iloc[0]

# std_dev = data[['Maths', 'Biology', 'C.Science']].std()


# variance = data[['Maths', 'Biology', 'C.Science']].var()


# print("Student Scores DataFrame:")
# print(data)
# print("\nMean:")
# print(mean)
# print("\nMedian:")
# print(median)
# print("\nMode:")
# print(mode)
# print("\nStandard Deviation:")
# print(std_dev)
# print("\nVariance:")
# print(variance)

# import matplotlib.pyplot as plt

# x_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_value = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# plt.plot(x_value, y_value, marker='o', linestyle='-', color='g')

# plt.title('Sample Line Plot')
# plt.xlabel('X values')
# plt.ylabel('Y values')


# plt.grid(True)

# plt.show()


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Scrollable Canvas Example")


canvas = Canvas(root, scrollregion=(0, 0, 640, 480), bg='white')
canvas.grid(row=0, column=0, sticky='nsew')

xscroll = ttk.Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
xscroll.grid(row=1, column=0, sticky='ew')

yscroll = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)
yscroll.grid(row=0, column=1, sticky='ns')
canvas.config(yscrollcommand=yscroll.set)


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


canvas.create_oval(50, 50, 300, 300, fill="green")

root.mainloop()





