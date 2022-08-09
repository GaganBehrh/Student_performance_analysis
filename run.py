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

def getStudentsMarks():
    print("Please enter the marks for 5 students individually")
    data_str1 = input("Enter your data here for Joe: ")
    data_str2 = input("Enter your data here for Ross: ")
    data_str3 = input("Enter your data here for Racheal: ")
    data_str4 = input("Enter your data here for Monica: ")
    data_str5 = input("Enter your data here for Christine: ")
    sales_data=[]
    sales_data.append(data_str1)
    sales_data.append(data_str2)
    sales_data.append(data_str3)
    sales_data.append(data_str4)
    sales_data.append(data_str5)
    print(sales_data)
    #if validateData((sales_data)):
       # print("Data is valid!")
    return sales_data

#def validateData(values):
 #   [int(value) for value in values]
  #  if value<0:
   #  print("value should be greater than 0")
       
            
def updateStudentWorksheet(data,worksheet):
    """
    to update the worksheet
    """
    update_worksheet=SHEET.worksheet(worksheet)
    update_worksheet.append_row(data)
    print("Here is the updated data")
    student_data=SHEET.worksheet("student").get_all_values()
    print(student_data)

def show_data():
    student_data=SHEET.worksheet("student").get_all_values()
    print("Here is the existing data")
    print(student_data)


def studentTotalScore():
    """
    to get the entries from each column and calculate the sum of marks for each student
    """
    print("Calculating student total marks")
    grade=''
    
    #to get the number of students
    student_data=SHEET.worksheet("student").get_all_values()
    num_students = len(student_data[0])
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
    maxScoreIndex=0
    for score in range(0,len(new_list)):
        if(max<=new_list[score]):
          max=new_list[score]
          avg=max/(len(student))
          maxScoreIndex=score+1
          if(avg<65):
            grade='C'
          elif(avg<75 and avg>65):
            grade='B'
          else:
            grade='A'

    print(f"Max score is {max} and the percentage is {avg}% with {grade} grade of student {maxScoreIndex}")
        
          
    
def main():

    print("Welcome to Student performance analysis")
    print("What would like to perform?")
    print("1. See the existing Marksheet")
    print("2.Enter New Data")
    print("3.Get Averages/percentage for the students")
    print("4.Show updated results")
    choice=int(input("Please Enter your choice"))
    totalStudentScore=[]
   
    if(choice==1):
        show_data()
    elif (choice==2):
        studentSpanishMarks=getStudentsMarks() 
        spanishData=[int(marks) for marks in studentSpanishMarks]
    elif (choice==3):
        totalStudentScore=studentTotalScore()
        
       # maxScore(totalStudentScore)
    elif (choice==4):
        studentSpanishMarks=getStudentsMarks()
        spanishData=[int(marks) for marks in studentSpanishMarks]
        updateStudentWorksheet(spanishData,"student")
    else:
        print("Invalid choice, it has to be in between 1 and 4, no zeros or negative values are allowed")
    
main()
