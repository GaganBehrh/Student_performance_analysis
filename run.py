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
    """
    Gets the marks of the student
    """
    while True:
        print("Please enter the marks for 5 students in spanish subject")
        print("Data should be 5 numbers, separated by commas.")
        print("Example: 20,30,40,50,60\n")
        dataStr = input("Enter your data here: ")
        salesData = dataStr.split(",")

        if validateData(salesData):
            print("Data is valid!")
            break

    return salesData

def validateData(values):
    """
    to validate the data
    """
    try:
        if len(values) != 5:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

def updateStudentWorksheet(data,worksheet):
    """
    to update the worksheet
    """
    print(f"Updating the worksheet {worksheet}")
    update_worksheet=SHEET.worksheet(worksheet)
    update_worksheet.append_row(data)
    print(f"{worksheet} updated successfully")


def studentTotalScore():
    """
    to get the entries from each column and calculate the sum of marks for each student
    """
    student_data=SHEET.worksheet("student").get_all_values()
    print(student_data)
    print("Calculating student total marks")
    #to get the number of students
    num_students = len(student_data[0])
    new_list = []
    for i in range(0, num_students):
        student = []
        for j, row in enumerate(student_data):
            if j == 0:
                continue
            #to append each row to the student list
            student.append(int(row[i]))
        new_list.append(sum(student))
    return new_list

def maxScore(scoreList):
    """
    to find the max score in an array
    """
    max=scoreList[0]
    maxScoreIndex=0
    for score in range(0,len(scoreList)):
        if(max<scoreList[score]):
          max=scoreList[score]
          maxScoreIndex=score+1
    print(f"student number with max score is student{maxScoreIndex} with max score of {max}")         
       
def main():
    studentSpanishMarks=getStudentsMarks()
    spanishData=[int(marks) for marks in studentSpanishMarks]
    updateStudentWorksheet(spanishData,"student")
    totalStudentScore=studentTotalScore()
    print(totalStudentScore)
    maxScore(totalStudentScore)

main()
