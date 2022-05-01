*API Docummentation - Student TimeLog*
----
**student_save_time_logs**
* **URL - /student/email/\<str:student_email\>/save/**
* **Method:** - `POST`
* **Description** - To save the timesheets from Student view for the week
* **Input** - student_email (str)
* **Output** : Example

```
{
   "status":"success",
   "message":"retrieval successful for current week",
   "data":{
      "eppstudent":2,
      "uin":123,
      "student_email":"abc@xyz.com",
      "university_supervisor_email":"johnny@xyz.com",
      "university_supervisor":"John Paul",
      "cooperating_teacher_email":"moore@xyz.com",
      "cooperating_teacher":"Michael Moore",
      "principal":"",
      "site":"",
      "classroom_type":"",
      "semester":"spring",
      "semester_year":"2022",
      "field_experience_program":"",
      "placement":"",
      "beginning_date_experience":"2019-01-01",
      "ending_date_experience":"2022-01-01",
      "instructor":"",
      "timelogs":{
         "2022-04-25":{
            "student_uin":123,
            "student_email":"abc@xyz.com",
            "log_date":"2022-04-25",
            "notes":"current week monday",
            "hours_submitted":"1.0",
            "hours_approved":false,
            "approval_due_date":"2022-05-02",
            "semester":"sprng",
            "semester_year":"2022",
            "start_time":"2022-05-05T03:51:00Z",
            "end_time":"2022-05-05T04:51:00Z",
            "date_submitted":"2022-04-25"
         }
      },
      "student":{
         "first_name":"John",
         "middle_name":"C",
         "last_name":"Doe",
         "primary_email":"abc@xyz.com",
         "secondary_email":"johndoesec@xyz.com",
         "full_name":"John C Doe"
      },
      "current_week":{
         "monday":"2022-04-25",
         "tuesday":"2022-04-26",
         "wednesday":"2022-04-27",
         "thursday":"2022-04-28",
         "friday":"2022-04-29",
         "saturday":"2022-04-30",
         "sunday":"2022-05-01"
      },
      "start_date":"2022-04-25",
      "end_date":"2022-05-01"
   }
}
```

----
**student_submit_time_logs**
* **URL - /student/email/\<str:student_email\>/submit/**
* **Method:** - `POST`
* **Description** - To Submit the timesheets from Student view to the Coop Teacher for the week
* **Input** - student_email (str)
* **Output** : Example

```
{
   "status":"success",
   "message":"Entered time entries submitted successfully",
   "data":[
      {
         "student_uin":"123",
         "student_email":"abc@xyz.com",
         "log_date":"2022-04-25",
         "notes":"current week monday",
         "hours_submitted":"1.0",
         "hours_approved":false,
         "semester":"sprng",
         "start_time":"2022-05-05T03:51:00.000Z",
         "end_time":"2022-05-05T04:51:00.000Z",
         "approval_due_date":"2022-05-02",
         "semester_year":"2022",
         "created":false
      }
   ]
}
```
----
**student_email_get_time_logs**
* **URL - /student/email/\<student_email\>**
* **Method:** - `GET`
* **Description** - To view the current week timesheet of the Student
* **Input** - student_email (str)
* **Output** : Example

```
{
   "status":"success",
   "message":"retrieval successful for current week",
   "data":{
      "eppstudent":2,
      "uin":123,
      "student_email":"abc@xyz.com",
      "university_supervisor_email":"johnny@xyz.com",
      "university_supervisor":"John Paul",
      "cooperating_teacher_email":"moore@xyz.com",
      "cooperating_teacher":"Michael Moore",
      "principal":"",
      "site":"",
      "classroom_type":"",
      "semester":"spring",
      "semester_year":"2022",
      "field_experience_program":"",
      "placement":"",
      "beginning_date_experience":"2019-01-01",
      "ending_date_experience":"2022-01-01",
      "instructor":"",
      "timelogs":{
         "2022-04-25":{
            "student_uin":123,
            "student_email":"abc@xyz.com",
            "log_date":"2022-04-25",
            "notes":"current week monday",
            "hours_submitted":"1.0",
            "hours_approved":false,
            "approval_due_date":"2022-05-02",
            "semester":"sprng",
            "semester_year":"2022",
            "start_time":"2022-05-05T03:51:00Z",
            "end_time":"2022-05-05T04:51:00Z",
            "date_submitted":"2022-04-25"
         }
      },
      "student":{
         "first_name":"John",
         "middle_name":"C",
         "last_name":"Doe",
         "primary_email":"abc@xyz.com",
         "secondary_email":"johndoesec@xyz.com",
         "full_name":"John C Doe"
      },
      "current_week":{
         "monday":"2022-04-25",
         "tuesday":"2022-04-26",
         "wednesday":"2022-04-27",
         "thursday":"2022-04-28",
         "friday":"2022-04-29",
         "saturday":"2022-04-30",
         "sunday":"2022-05-01"
      },
      "start_date":"2022-04-25",
      "end_date":"2022-05-01"
   }
}
```
----
**student_email_sem_get_time_logs**
* **URL - /student/email/\<student_email\>/semester/\<semester_name\>**
* **Method:** - `GET`
* **Description** - To view the current week timesheet of the Student
* **Input** - student_email (str) , semester_name(str)
* **Output** : Example

```
{
   "status":"success",
   "message":"retrieval successful for current week",
   "data":{
      "timelogs":{
         "2022-04-25":{
            "student_uin":123,
            "student_email":"abc@xyz.com",
            "log_date":"2022-04-25",
            "notes":"current week monday",
            "hours_submitted":"1.0",
            "hours_approved":false,
            "approval_due_date":"2022-05-02",
            "semester":"sprng",
            "semester_year":"2022",
            "start_time":"2022-05-05T03:51:00Z",
            "end_time":"2022-05-05T04:51:00Z",
            "date_submitted":"2022-04-25"
         }
      },
      "student":{
         "first_name":"John",
         "middle_name":"C",
         "last_name":"Doe",
         "primary_email":"abc@xyz.com",
         "secondary_email":"johndoesec@xyz.com",
         "full_name":"John C Doe"
      },
      "current_week":{
         "monday":"2022-04-25",
         "tuesday":"2022-04-26",
         "wednesday":"2022-04-27",
         "thursday":"2022-04-28",
         "friday":"2022-04-29",
         "saturday":"2022-04-30",
         "sunday":"2022-05-01"
      },
      "start_date":"2022-04-25",
      "end_date":"2022-05-01"
   }
}

```
----
**student_email_start_get_time_logs**
* **URL - /student/email/<student_email>/start/\<start_date\>**
* **Method:** - `GET`
* **Description** - To view the timesheet of the Student from the start date entered
* **Input** - student_email (str) , start_date(str)
* **Output** : Example

```
{
   "status":"success",
   "message":"start date only provided",
   "data":{
      "eppstudent":2,
      "uin":123,
      "student_email":"abc@xyz.com",
      "university_supervisor_email":"johnny@xyz.com",
      "university_supervisor":"John Paul",
      "cooperating_teacher_email":"moore@xyz.com",
      "cooperating_teacher":"Michael Moore",
      "principal":"",
      "site":"",
      "classroom_type":"",
      "semester":"spring",
      "semester_year":"2022",
      "field_experience_program":"",
      "placement":"",
      "beginning_date_experience":"2019-01-01",
      "ending_date_experience":"2022-01-01",
      "instructor":"",
      "timelogs":{
         "2022-04-25":{
            "student_uin":123,
            "student_email":"abc@xyz.com",
            "log_date":"2022-04-25",
            "notes":"current week monday",
            "hours_submitted":"1.0",
            "hours_approved":false,
            "approval_due_date":"2022-05-02",
            "semester":"sprng",
            "semester_year":"2022",
            "start_time":"2022-05-05T03:51:00Z",
            "end_time":"2022-05-05T04:51:00Z",
            "date_submitted":"2022-04-25"
         }
      },
      "student":{
         "first_name":"John",
         "middle_name":"C",
         "last_name":"Doe",
         "primary_email":"abc@xyz.com",
         "secondary_email":"johndoesec@xyz.com",
         "full_name":"John C Doe"
      },
      "current_week":{
         "monday":"2022-04-25",
         "tuesday":"2022-04-26",
         "wednesday":"2022-04-27",
         "thursday":"2022-04-28",
         "friday":"2022-04-29",
         "saturday":"2022-04-30",
         "sunday":"2022-05-01"
      },
      "start_date":"2022-04-25",
      "end_date":"2022-04-30"
   }
}
```
----
**student_email_startend_get_time_logs**
* **URL - /student/email/<student_email>/start/\<start_date\>/end/\<end_date\>**
* **Method:** - `GET`
* **Description** - To view the timesheet of the Student between the start date and end date entered
* **Input** - student_email (str) , start_date(str) , end_date(str)
* **Output** : Example

```
{
   "status":"success",
   "message":"start date and end date provided",
   "data":{
      "eppstudent":2,
      "uin":123,
      "student_email":"abc@xyz.com",
      "university_supervisor_email":"johnny@xyz.com",
      "university_supervisor":"John Paul",
      "cooperating_teacher_email":"moore@xyz.com",
      "cooperating_teacher":"Michael Moore",
      "principal":"",
      "site":"",
      "classroom_type":"",
      "semester":"spring",
      "semester_year":"2022",
      "field_experience_program":"",
      "placement":"",
      "beginning_date_experience":"2019-01-01",
      "ending_date_experience":"2022-01-01",
      "instructor":"",
      "timelogs":{
         "2022-04-25":{
            "student_uin":123,
            "student_email":"abc@xyz.com",
            "log_date":"2022-04-25",
            "notes":"current week monday",
            "hours_submitted":"1.0",
            "hours_approved":false,
            "approval_due_date":"2022-05-02",
            "semester":"sprng",
            "semester_year":"2022",
            "start_time":"2022-05-05T03:51:00Z",
            "end_time":"2022-05-05T04:51:00Z",
            "date_submitted":"2022-04-25"
         },
         "2022-04-26":{
            "student_uin":123,
            "student_email":"abc@xyz.com",
            "log_date":"2022-04-26",
            "notes":"current week tuesday",
            "hours_submitted":"2.0",
            "hours_approved":false,
            "approval_due_date":"2022-05-02",
            "semester":"sprng",
            "semester_year":"2022",
            "start_time":"2022-05-06T19:42:00Z",
            "end_time":"2022-05-06T21:42:00Z",
            "date_submitted":"2022-04-25"
         }
      },
      "student":{
         "first_name":"John",
         "middle_name":"C",
         "last_name":"Doe",
         "primary_email":"abc@xyz.com",
         "secondary_email":"johndoesec@xyz.com",
         "full_name":"John C Doe"
      },
      "current_week":{
         "monday":"2022-04-25",
         "tuesday":"2022-04-26",
         "wednesday":"2022-04-27",
         "thursday":"2022-04-28",
         "friday":"2022-04-29",
         "saturday":"2022-04-30",
         "sunday":"2022-05-01"
      },
      "start_date":"2022-04-25",
      "end_date":"2022-04-26"
   }
}

```
----
**student_email_get_time_logs_prev**
* **URL - /student/email/<student_email>/prev**
* **Method:** - `GET`
* **Description** - To view the previous week timesheet of the Student
* **Input** - student_email (str)
* **Output** : Example

```
{
   "status":"success",
   "message":"start date and end date provided",
   "data":{
      "eppstudent":2,
      "uin":123,
      "student_email":"abc@xyz.com",
      "university_supervisor_email":"johnny@xyz.com",
      "university_supervisor":"John Paul",
      "cooperating_teacher_email":"moore@xyz.com",
      "cooperating_teacher":"Michael Moore",
      "principal":"",
      "site":"",
      "classroom_type":"",
      "semester":"spring",
      "semester_year":"2022",
      "field_experience_program":"",
      "placement":"",
      "beginning_date_experience":"2019-01-01",
      "ending_date_experience":"2022-01-01",
      "instructor":"",
      "timelogs":{
         "2022-04-25":{
            "student_uin":123,
            "student_email":"abc@xyz.com",
            "log_date":"2022-04-25",
            "notes":"current week monday",
            "hours_submitted":"1.0",
            "hours_approved":false,
            "approval_due_date":"2022-05-02",
            "semester":"sprng",
            "semester_year":"2022",
            "start_time":"2022-05-05T03:51:00Z",
            "end_time":"2022-05-05T04:51:00Z",
            "date_submitted":"2022-04-25"
         }
      },
      "student":{
         "first_name":"John",
         "middle_name":"C",
         "last_name":"Doe",
         "primary_email":"abc@xyz.com",
         "secondary_email":"johndoesec@xyz.com",
         "full_name":"John C Doe"
      },
      "current_week":{
         "monday":"2022-04-25",
         "tuesday":"2022-04-26",
         "wednesday":"2022-04-27",
         "thursday":"2022-04-28",
         "friday":"2022-04-29",
         "saturday":"2022-04-30",
         "sunday":"2022-05-01"
      },
      "start_date":"2022-04-25",
      "end_date":"2022-05-01"
   }
}
```
