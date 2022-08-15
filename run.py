import gspread
from google.oauth2.service_account import Credentials
from pandas import ExcelWriter
from pandas import ExcelFile 
import pandas as pd
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Student_analysis')

def get_students_marks():
    print("Please enter the marks for 5 students individually")
    data_str1 = int(input("Enter your data here for Joe:"))
    data_str2 = int(input("Enter your data here for Ross: "))
    data_str3 = int(input("Enter your data here for Racheal: "))
    data_str4 = int(input("Enter your data here for Monica: "))
    data_str5 = int(input("Enter your data here for Christine: "))
    sales_data=[]
    sales_data.append(data_str1)
    sales_data.append(data_str2)
    sales_data.append(data_str3)
    sales_data.append(data_str4)
    sales_data.append(data_str5)
    print(f"The data you entered is {sales_data}")
    return sales_data         

def update_student_worksheet(data,worksheet):
    """
    to update the worksheet
    """
    flag=False
    update_worksheet=SHEET.worksheet(worksheet)
    for entries in data:
        if(entries>0 and entries<100 ):
            flag=True
        else:
            flag=False
            print("Invalid values added, it should lie in betwwen zero and humdred, please restart and the datasheet wont be updated")
            break
    if(flag==True):
        print("You entered the valid values")
        update_worksheet.append_row(data)
        print("Hence,Here is the updated data")
        student_data=SHEET.worksheet("student").get_all_values()
        print(student_data)


def show_data():
    """
    to show the existing data
    """
    student_data=SHEET.worksheet("student").get_all_values()
    print("Here is the existing data")
    print(student_data)


def student_total_score():
    """
    to get the entries from each column and calculate the sum of marks for each student
    """
    print("Here are the total marks obtained by each student")
    grade=''
    #to get the number of students
    student_data=SHEET.worksheet("student").get_all_values()
    num_students = len(student_data[0])
    print(student_data[0])
    new_list = []
    for i in range(0, num_students):
        student = []
        for j, row in enumerate(student_data):
            if j == 0:
                continue
            student.append(int(row[i]))
        new_list.append(sum(student))
    print(new_list)
    max=new_list[0]
    name=""
    maxScoreIndex=0
    for students in student_data[0]:
        for score in range(0,len(new_list)):
            if(max<=new_list[score]):
                max=new_list[score]
                avg=max/(len(student))
                name=students
                if(avg<65):
                    grade='C'
                elif(avg<75 and avg>65):
                    grade='B'
                else:
                    grade='A'
    print(f"Here are the details of the topper of the class: {name}, Max score :{max}, Percentage:{round(avg)}%, Grade:{grade}")
        
          
    
def main():
    print("Welcome to Student performance analysis")
    print("What would like to perform?")
    print("1. See the existing Marksheet")
    print("2. Get Averages/percentage for the students and know the grade of the student")
    print("3. Enter the data and show the updated results")
    choice=int(input("Please Enter your choice"))
    total_student_score=[]
    if(choice==1):
        show_data()  
    elif (choice==2):
        student_total_score()
    elif (choice==3):
        student_spanish_marks=get_students_marks()
        spanish_data=[int(marks) for marks in  student_spanish_marks]
        update_student_worksheet(spanish_data,"student")
    else:
        print("Invalid choice, it has to be in between 1 and 3, no zeros or negative values are allowed")  
main()
