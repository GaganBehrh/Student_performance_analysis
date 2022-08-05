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
    """
    Gets the marks of the student
    """
    while True:
        print("Please enter the marks for 5 students in spanish subject")
        print("Data should be 5 numbers, separated by commas.")
        print("Example: 20,30,40,50,60\n")
        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data

def validate_data(values):
    """
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

def update_student_worksheet(data,worksheet):
    print(f"Updating the worksheet {worksheet}")
    update_worksheet=SHEET.worksheet(worksheet)
    update_worksheet.append_row(data)
    print(f"{worksheet} updated successfully")


def student_total_score():
    """to get the entries from each column and calculate the percentage of each student"""
    student_data=SHEET.worksheet("student").get_all_values()
    print(student_data)
    #student_total=[]
    print("Calculating student marks")
    #new_data = [[row[0] for row in student_data] for student in student_data]
    #print(new_data)
    # new_list = []
    # for row in student_data:
    #     student = []
    #     for i in row:
    #         student.append(i)
    #     new_list.append(student)
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

    
    

    # for item in student_data:
    #     for row in student_data:
    #         print(item[row])
    #for i in range(2,len(student)):
        #if i==0:
         #   continue
        #student_score=SHEET.worksheet("student").row_values(i)
        #student_sum=sum(SHEET.worksheet("student").col_values(i))
        #print(student_score)
        #student_total.append(student_sum)
        #print(student_total)
    #print(student)
    #df = pd.DataFrame(student)
    #print(df)
    #print(df)
    #sum_column = df.sum(axis=0)
    #print (sum_column)
    
def main():
    student_spanish_marks=get_students_marks()
    spanish_data=[int(marks) for marks in student_spanish_marks]
    update_student_worksheet(spanish_data,"student")
    student_total_score()

main()
