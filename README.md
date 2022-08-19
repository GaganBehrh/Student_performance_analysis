![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Gagi Behrh,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
Happy coding!

### Student_Performance_Analysis

Student Performance analysis is the Python terminal project for the student receiving the maximum marks grade and score among different students.The marks can be imported from the worksheet, all the entries can be displayed on the terminal and the worksheet can also receive the data entered from the terminal. The inspiration of this project comes from Love Sandwiches project
PUT A LINK FROM AM I RESPONSIVE FROM HERE
## Scope
This project can be used by different academic schools, teachers principals to evaluate the performance of the students. 

## How to use
The user is  shown the welcome message where he is indicated that he can do the analysis of the marks of the students. He can do it choosing it from three different options presented on the terminal and give an input

![image](https://user-images.githubusercontent.com/63474017/185102272-668f7a70-b2aa-44ba-a207-655d3cb1132e.png)

## User Stories
1. As a user, I would like to be able to get a clear message about the kind of analysis i will be performing and what are my options 
2. As a user, I would like to see the entries from the worksheet on the terminal
3. As a user, I would like to know the total,  of each student
4. As a user, I would like to the student with maximum percentage and his/her respective grade
5. As a user, I would like to be able to enter the data entries and update the worksheet
 

## Features

Feature 1: See the existing marksheet
With this feature , user can see the existing data in a form of table obtained from the marksheet on the terminal  with the name of the students on the top and corresponding marks of respective student in each column, (in this case student analysis google spreadsheet)
![image](https://user-images.githubusercontent.com/63474017/185103022-162bf476-6202-4627-bef3-7879613e4ea9.png)

Feature 2: Get Averages/percentage for the students 
Here the user can choose to obtain the name, percentage and grade of the student with maximum score along wit the total of the marks obtained by each student

![image](https://user-images.githubusercontent.com/63474017/185103371-dc1676cd-80e5-45d6-a90f-437f7395f8c6.png)

Feature 3:With this feature user can enter the marks studentwise and update the result directly into the worksheet and is also able to see the recently added row with the existing one on the terminal in the form of a table

![image](https://user-images.githubusercontent.com/63474017/185104787-5ce0e8e7-f3d7-41ee-83e6-cbdf44d4232e.png)

![image](https://user-images.githubusercontent.com/63474017/185104859-47d6783a-69c6-4539-85fe-1772b704edad.png)

In case invalid data is added for example negative or values greater than 100 than the Error message is displayed
![image](https://user-images.githubusercontent.com/63474017/185105114-f9a90442-4ae2-4432-98cc-03584a44c153.png)

## Google Spreadsheet
The following google spreadsheet was used to carry out the student performance analysis
Link: https://docs.google.com/spreadsheets/d/179vDqBF4_Rv658tg0D_gaxc_WKxZBBC1_yv1GR5huKs/edit#gid=0
![image](https://user-images.githubusercontent.com/63474017/185106480-e3039041-491c-4b36-83c1-a14548958975.png)

Data Model:
I used StudentMarks Class as my model. It creates one instance through which we pass the worksheet.
This class stores the worksheet and has methods to print the data in the existing worksheet, calculate the percentage and average of the students and display which student got maximum score and also a function where user can input the result and update the existing worksheet only if valid values are entered

## Testing/Validator Testing:
1. Passed the code througha PEP8 linter and confirmed there are no problems
2. Tested in local terminal and Code insitute Heroku terminal

Testing of User Stories:
## 
1. As a user, I would like to be able to get a clear message about the kind of analysis i will be performing and what are my options 
Pass: There is a clear welcome message in the beginning of the program along with the options of different functionalities to perform
2. As a user, I would like to see the entries from the worksheet on the terminal
Pass: Option1 makes it possible
3. As a user, I would like to know the total of each student
Pass: Option2 makes it possible
4. As a user, I would like to the student with maximum percentage and his/her respective grade
Pass: Option2 makes it possibleh 
5. As a user, I would like to be able to enter the data entries and update the worksheet
Pass: Option3 makes it possible

## Deployment:
This project was deployed using Code Institite's mock terminal for Heroku

## Steps for deployment
1. Fork or clone this repository
2. Create a  new Heroku App
3. See the buildbacks to Python and NodeJS in that order
4. Link the Heroku app
5. Click on Deploy



## Credits
1. Mentor and slack community from Code institute
2. Inspiration of this project comes fom LOVE_SANDWICHES PROJECT












Pu details about data sheet as well
