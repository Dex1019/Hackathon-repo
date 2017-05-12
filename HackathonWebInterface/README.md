# APIWebInterface
This project is to give access to the people who want to conduct the exam.

## Module Division
1. Login and Signup
2. Two factor Authentication
3. CRUD Exam
4. Report generation

## 1. Login and signup
This module is responsible to authenticate the user and perform the sign up.<br>
The functionality is provided in AuthPortal Model
We have divided the webpage into 7 subpages:
1.Base (Contains the header that is included in the page.) 
2.Authportal (Contains base.html and body.html)
3.Body (Contains the navbar.html and loginsection.html)
4.Navbar (Used as navigation bar for the page)
5.Login Section (Contains the div containter that contains signup.html)
6. Signup (Contains the top signup or login and calls the signup form)
7. Signup form(Contains the autheticaion and signup form)

### Explanation of the views.py in AuthPortal

We have two views here: <br>
1. Signup
2. Login 

#### Signup 
<br> This view works on the post method. 
We wull first create the object of UserForm.
Then we will validate the form request.<br>
If sucessfull we will check for errors and for website already exists, phone number already exists, email already exists.
If the form is not valid or is first time acess then a portal.html is rendered with context as signup = True<br>

#### Login
This method will work on post method <br>
We will try to authenticate the user<br>
If none is returned then either user have entered invalid credential or he have been blocked<br>
Else the user will be logged on. <br>


