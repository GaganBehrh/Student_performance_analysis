import gspread
from google.oauth2.service_account import Credentials

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
        print("Data should be Spamish followed by 5 numbers, separated by commas.")
        print("Example: Spanish,20,30,40,50,60\n")

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
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
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
        

student_spanish_marks=get_students_marks()
spanish_data=[int(marks) for marks in range(0,len(student_spanish_marks))]
update_student_worksheet(spanish_data,"student")
