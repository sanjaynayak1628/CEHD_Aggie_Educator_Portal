# CEHD_Aggie_Educator_Portal
Aggie Educator Portal for students and cooperating teachers for College of Education and Human Development division of Texas A&amp;M University.

**Supervisor** - Strader, R Arlen

**Team Members**: Manisha Dixit, Sruti Patnaik, Rajesh Satpathy, Piyush Nayak, Sanjay Nayak

# Objective
The main objective of the project is to create an application to record, maintain and approve the time logs of the students.  This is a new application which is being designed to address the requirement of the College of Education and Human Development (CEHD) under the supervision of Strader, R Arlen (strader@tamu.edu). The students would be filling the time logs for each working day in the application, which would be notified via mail to the cooperating teacher for approval. In short, our application would help in digitalising the manual timesheet logging and approval process of the students. 

# Application details
As per the client requirements, the application would be developed in Django framework using Python as the language of choice. A relational database would be in used to retain the historical data and use it for further reporting. The features of the application will include a user interface for students to clock the time logs of the working days, a notification system notifying the teacher via mail to approve the aggregated weekly timesheet of the students, a reminder framework to send reminder alerts to both the student and teacher to fill and approve the timesheets respectively, allowing the users (student, teacher) to view the current as well as previously entered or approved time-logs. 


# Heroku Deployment
1. Connect Heroku-CLI with gitbash
2. heroku login (Authenticate and connect to your heroku account)
3. Go to the folder where you have your github repo set
5. heroku create
If more than one apps present in your heroku account and you want to use a particular app, use the following command else directly go to step 5
6. heroku git:remote -a \<app-name\>
7. heroku config:set DISABLE_COLLECTSTATIC=0
To push to heroku from a non-master btranch use the following command
8. git subtree push --prefix \<sub folder path to Django app\> heroku \<non-master branch-name\>:main

# run BDD Test case
1. Download the chrome driver based on the chrome version you have and update the path in the features/environment.py file
2. In the console, go to the project cehd folder and run `behave --no-capture` \<`--no-capture` allows the print statements to shown in the console during behave execution\>
