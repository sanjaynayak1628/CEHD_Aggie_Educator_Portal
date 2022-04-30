*API Docummentation - Cooperating Teachers*
----
**coop_view_initial**
* **URL - /coop/email/\<str:coop_email\>/view**
* **Method:** - `GET`
* **Description** - Get function to fetch Coop, Year and students details for View Submitted Timesheet view for Coop Teachers
* **Input** - coop_email (str) 
* **Output** : Example
```
{ 
   "status":"success", 
   "message":"data retrieved", 
   "data":{ 
      "cooperating_teacher_email":"moore@xyz.com", 
      "students":[ 
         { 
            "student_full_name":"John C Doe", 
            "student_email":"abc@xyz.com" 
         } 
      ], 
      "years":[ 
         "2022" 
      ], 
      "cooperating_teacher_name":"Michael Moore" 
} 
```

----

**coop**
* **URL - coop/email/\<str:coop_email\>**
* **Method:** - `GET`
* **Description** - GET function to get the list of timesheets submitted for each date in last week approve/reject for Coop landing Page
* **Input** - coop_email (str) 
* **Output** : Example
```
{ 
   "data":{ 
      "cooperating_teacher_email":"moore@xyz.com", 
      "semester":"spring", 
      "semester_year":2022, 
      "students":[ 
         { 
            "first_name":"John", 
            "middle_name":"C", 
            "last_name":"Doe", 
            "primary_email":"abc@xyz.com", 
            "secondary_email":"johndoesec@xyz.com", 
            "full_name":"John C Doe" 
         } 
      ], 
      "university_supervisor_email":"johnny@xyz.com", 
      "university_supervisor":"John Paul", 
      "cooperating_teacher":"Michael Moore", 
      "approval_start_date":datetime.date(2022,5, 2), 
      "approval_end_date":datetime.date(2022, 5, 4), 
      "current_week":{ 
         "monday":"2022-04-25", 
         "tuesday":"2022-04-26", 
         "wednesday":"2022-04-27", 
         "thursday":"2022-04-28", 
         "friday":"2022-04-29", 
         "saturday":"2022-04-30", 
         "sunday":"2022-05-01" 
      }, 
      "timelogs":{ 
            "2022-04-27":{ 
            "student_uin":123, 
            "student_email":"abc@xyz.com", 
            "log_date":"2022-04-27", 
            "notes":"current week wednesday", 
            "hours_submitted":"1.0", 
            "hours_approved":false, 
            "approval_due_date":"2022-05-02", 
            "semester":"sprng", 
            "semester_year":"2022", 
            "start_time":"2022-05-07T00:50:00Z", 
            "end_time":"2022-05-07T02:50:00Z", 
            "date_submitted":"2022-04-27" 
         }...
      }, 
      "approve":"disabled" 
   } 
} 
```
----

**coop_student**
* **URL - coop/email/\<str:coop_email\>/view/student/\<str:student_email\>**
* **Method:** - `GET`
* **Description** - Get function to fetch all timesheets when student is selected from Student List in UI
* **Input** - coop_email (str), student_email (str)
* **Output** : Example
```
{ 
   "data":{ 
      "cooperating_teacher_email":"moore@xyz.com", 
      "students":[ 
         { 
            "student_full_name":"John C Doe", 
            "student_email":"abc@xyz.com" 
         } 
      ], 
      "years":[ 
         "2022" 
      ], 
      "cooperating_teacher_name":"Michael Moore", 
      "student_email_selected":"abc@xyz.com", 
      "student_full_name_selected":"John C Doe", 
      "timelogs":[ 

         { 
            "student_uin":123, 
            "student_email":"abc@xyz.com", 
            "log_date":"2022-04-04", 
            "notes":"submitted now test", 
            "hours_submitted":"4.0", 
            "hours_approved":false, 
            "approval_due_date":"2022-04-10", 
            "semester":"sprng", 
            "semester_year":"2022", 
            "start_time":"2022-05-04T17:11:00Z", 
            "end_time":"2022-05-04T21:11:00Z", 
            "date_submitted":"2022-04-08" 
         }...
     ] 
   } 
} 
```
----

**coop_student_sem**
* **URL - coop/email/\<str:coop_email\>/view/student/\<str:student_email\>/semester/\<str:semester\>**
* **Method:** - `GET`
* **Description** - Get function to fetch all timesheets when semester and student is selected from UI
* **Input** - coop_email (str), student_email (str), semester(str)
* **Output** : Example
```
{ 
   "data":{ 
      "cooperating_teacher_email":"moore@xyz.com", 
      "students":[ 
         { 
            "student_full_name":"John C Doe", 
            "student_email":"abc@xyz.com" 
         } 
      ], 
      "years":[ 
         "2022" 
      ], 
      "cooperating_teacher_name":"Michael Moore", 
      "student_email_selected":"abc@xyz.com", 
      "student_full_name_selected":"John C Doe", 
      "semester":"spring", 
      "timelogs":[ 
         { 
            "student_uin":123, 
            "student_email":"abc@xyz.com", 
            "log_date":"2022-04-29", 
            "notes":"current week friday", 
            "hours_submitted":"3.0", 
            "hours_approved":false, 
            "approval_due_date":"2022-05-02", 
            "semester":"sprng", 
            "semester_year":"2022", 
            "start_time":"2022-05-09T15:03:00Z", 
            "end_time":"2022-05-09T22:03:00Z", 
            "date_submitted":"2022-04-27" 
         }...
      ] 
   } 
} 
```
----

**coop_student_sem_year**
* **URL - coop/email/\<str:coop_email\>/view/student/\<str:student_email\>/semester/\<str:semester\>/year/\<str:year\>**
* **Method:** - `GET`
* **Description** - Get function to fetch all timesheets when year, semester and student is selected from UI
* **Input** - coop_email (str), student_email (str), semester(str), year(str)
* **Output** : Example
```
{ 

   "data":{ 

      "cooperating_teacher_email":"moore@xyz.com", 
      "students":[ 
         { 
            "student_full_name":"John C Doe", 
            "student_email":"abc@xyz.com" 
         } 
      ], 
      "years":[ 
         "2022" 
      ], 
      "cooperating_teacher_name":"Michael Moore", 
      "student_email_selected":"abc@xyz.com", 
      "student_full_name_selected":"John C Doe", 
      "semester":"spring", 
      "semester_year":"2022", 
      "timelogs":[ 
         { 
            "student_uin":123, 
            "student_email":"abc@xyz.com", 
            "log_date":"2022-04-04", 
            "notes":"submitted now test", 
            "hours_submitted":"4.0", 
            "hours_approved":false, 
            "approval_due_date":"2022-04-10", 
            "semester":"sprng", 
            "semester_year":"2022", 
            "start_time":"2022-05-04T17:11:00Z", 
            "end_time":"2022-05-04T21:11:00Z", 
            "date_submitted":"2022-04-08" 
         }...
      ] 
   } 
} 
```
----

**coop_student_year**
* **URL - coop/email/\<str:coop_email\>/view/student/\<str:student_email\>/year/\<str:year\>**
* **Method:** - `GET`
* **Description** - Get function to fetch all timesheets when year and student is selected from UI
* **Input** - coop_email (str), student_email (str), year(str)
* **Output** : Example
```
{ 
   "data":{ 
      "cooperating_teacher_email":"moore@xyz.com", 
      "students":[ 
         { 
            "student_full_name":"John C Doe", 
            "student_email":"abc@xyz.com" 
         } 
      ], 
      "years":[ 
         "2022" 
      ], 
      "cooperating_teacher_name":"Michael Moore", 
      "student_email_selected":"abc@xyz.com", 
      "student_full_name_selected":"John C Doe", 
      "semester_year":"2022", 
      "timelogs":[ 
         { 
            "student_uin":123, 
            "student_email":"abc@xyz.com", 
            "log_date":"2022-04-04", 
            "notes":"submitted now test", 
            "hours_submitted":"4.0", 
            "hours_approved":false, 
            "approval_due_date":"2022-04-10", 
            "semester":"sprng", 
            "semester_year":"2022", 
            "start_time":"2022-05-04T17:11:00Z", 
            "end_time":"2022-05-04T21:11:00Z", 
            "date_submitted":"2022-04-08" 
         }...
       ] 
   } 
}
```
----

**coop_student_dates**
* **URL - coop/email/\<str:coop_email\>/view/student/\<str:student_email\>/semester/\<str:semester\>/start/\<str:start_date\>/end/\<str:end_date\>**
* **Method:** - `GET`
* **Description** - Get function to fetch all timesheets when start date, end date, semester and student is selected from UI
* **Input** - coop_email (str), student_email (str), semester(str), start_date (str), end_date (str)
* **Output** : Example
```
{ 
   "data":{ 
      "cooperating_teacher_email":"moore@xyz.com", 
      "students":[ 
         { 
            "student_full_name":"John C Doe", 
            "student_email":"abc@xyz.com" 
         } 
      ], 
      "years":[ 
         "2022" 
      ], 
      "cooperating_teacher_name":"Michael Moore", 
      "student_email_selected":"abc@xyz.com", 
      "student_full_name_selected":"John C Doe", 
      "start_date":"2022-04-04", 
      "end_date":"2022-04-08", 
      "timelogs":[ 
         { 
            "student_uin":123, 
            "student_email":"abc@xyz.com", 
            "log_date":"2022-04-05", 
            "notes":"", 
            "hours_submitted":"5.0", 
            "hours_approved":false, 
            "approval_due_date":"2022-04-10", 
            "semester":"sprng", 
            "semester_year":"2022", 
            "start_time":"2022-05-05T10:19:00Z", 
            "end_time":"2022-05-05T15:19:00Z", 
            "date_submitted":"2022-04-08" 
         }, 
     ] 
   } 
} 
```
----

**coop_student_sem_dates_year**
* **URL - coop/email/\<str:coop_email\>/view/student/\<str:student_email\>/semester/\<str:semester\>/year/\<str:year\>/start/\<str:start_date\>/end/\<str:end_date\>**
* **Method:** - `GET`
* **Description** - Get function to fetch all timesheets when semester,  start date, end date, year and student is selected from UI
* **Input** - coop_email (str), student_email (str), semester(str), start_date (str), end_date (str), year (str)
* **Output** : Example
```
{ 
   "data":{ 
      "cooperating_teacher_email":"moore@xyz.com", 
      "students":[ 
         { 
            "student_full_name":"John C Doe", 
            "student_email":"abc@xyz.com" 
         } 
      ], 
      "years":[ 
         "2022" 
      ], 
      "cooperating_teacher_name":"Michael Moore", 
      "student_email_selected":"abc@xyz.com", 
      "student_full_name_selected":"John C Doe", 
      "semester":"spring", 
      "start_date":"2022-04-04", 
      "end_date":"2022-04-08", 
      "timelogs":[ 

         { 
            "student_uin":123, 
            "student_email":"abc@xyz.com", 
            "log_date":"2022-04-05", 
            "notes":"", 
            "hours_submitted":"5.0", 
            "hours_approved":false, 
            "approval_due_date":"2022-04-10", 
            "semester":"sprng", 
            "semester_year":"2022", 
            "start_time":"2022-05-05T10:19:00Z", 
            "end_time":"2022-05-05T15:19:00Z", 
            "date_submitted":"2022-04-08" 
         }, 
       ] 
   } 
}
```
----

**coop_student_sem_dates**
* **URL - coop/email/\<str:coop_email\>/view/student/\<str:student_email\>/semester/\<str:semester\>/start/\<str:start_date\>/end/\<str:end_date\>**
* **Method:** - `GET`
* **Description** - Get function to fetch all timesheets when start date, end date, semester and student is selected from UI
* **Input** - coop_email (str), student_email (str), semester(str), start_date (str), end_date (str)
* **Output** : Example
```
{ 
   "data":{ 
      "cooperating_teacher_email":"moore@xyz.com", 
      "students":[ 
         { 
            "student_full_name":"John C Doe", 
            "student_email":"abc@xyz.com" 
         } 
      ], 
      "years":[ 
         "2022" 
      ], 
      "cooperating_teacher_name":"Michael Moore", 
      "student_email_selected":"abc@xyz.com", 
      "student_full_name_selected":"John C Doe", 
      "start_date":"2022-04-04", 
      "end_date":"2022-04-08", 
      "timelogs":[ 
         { 
            "student_uin":123, 
            "student_email":"abc@xyz.com", 
            "log_date":"2022-04-05", 
            "notes":"", 
            "hours_submitted":"5.0", 
            "hours_approved":false, 
            "approval_due_date":"2022-04-10", 
            "semester":"sprng", 
            "semester_year":"2022", 
            "start_time":"2022-05-05T10:19:00Z", 
            "end_time":"2022-05-05T15:19:00Z", 
            "date_submitted":"2022-04-08" 
         }, 
     ] 
   } 
} 
```
----

**coop_student_year_dates**
* **URL - coop/email/\<str:coop_email\>/view/student/\<str:student_email\>/year/\<str:year\>/start/\<str:start_date\>/end/\<str:end_date\>**
* **Method:** - `GET`
* **Description** - Get function to fetch all timesheets when year, start date, end date and student is selected from UI
* **Input** - coop_email (str), student_email (str), year (str), start_date (str), end_date (str)
* **Output** : Example
```
{ 
   "data":{ 
      "cooperating_teacher_email":"moore@xyz.com", 
      "students":[ 
         { 
            "student_full_name":"John C Doe", 
            "student_email":"abc@xyz.com" 
         } 
      ], 
      "years":[ 
         "2022" 
      ], 
      "cooperating_teacher_name":"Michael Moore", 
      "student_email_selected":"abc@xyz.com", 
      "student_full_name_selected":"John C Doe", 
      "semester_year":"2022", 
      "start_date":"2022-04-04", 
      "end_date":"2022-04-08", 
      "timelogs":[ 

         { 
            "student_uin":123, 
            "student_email":"abc@xyz.com", 
            "log_date":"2022-04-05", 
            "notes":"",
            "hours_submitted":"5.0", 
            "hours_approved":false, 
            "approval_due_date":"2022-04-10", 
            "semester":"sprng", 
            "semester_year":"2022", 
            "start_time":"2022-05-05T10:19:00Z", 
            "end_time":"2022-05-05T15:19:00Z", 
            "date_submitted":"2022-04-08" 
         }, 
      ] 
   } 
} 
```
----

**coop_appr**
* **URL - coop/email/\<str:email\>/submit/approve/\<str:approve\>**
* **Method:** - `POST`
* **Description** - POST function to approve/reject timesheets into DB
* **Input** - coop_email (str), approve (str)
* **Output** : Example
```
{
   "status":"success",
   "message":"Time entries approved successfully",
   "data":[
      {
         "student_email":"abc@xyz.com",
         "log_date":"2022-04-18",
         "notes":"previous week monday",
         "student_uin":"123",
         "approval_due_date":"2022-04-25",
         "hours_submitted":"0.0",
         "semester":"sprng",
         "semester_year":"2022",
         "start_time":"2022-05-08T20:54:00.000Z",
         "end_time":"2022-05-08T11:54:00.000Z",
         "hours_approved":true,
         "created":false
      },
      {
         "student_email":"abc@xyz.com",
         "log_date":"2022-04-19",
         "notes":"previous week tuesday",
         "student_uin":"123",
         "approval_due_date":"2022-04-25",
         "hours_submitted":"4.0",
         "semester":"sprng",
         "semester_year":"2022",
         "start_time":"2022-05-09T11:59:00.000Z",
         "end_time":"2022-05-09T14:59:00.000Z",
         "hours_approved":true,
         "created":false
      },
      {
         "student_email":"abc@xyz.com",
         "log_date":"2022-04-20",
         "notes":"previous week wednesday",
         "student_uin":"123",
         "approval_due_date":"2022-04-25",
         "hours_submitted":"2.0",
         "semester":"sprng",
         "semester_year":"2022",
         "start_time":"2022-04-30T04:32:00.000Z",
         "end_time":"2022-04-30T06:32:00.000Z",
         "hours_approved":true,
         "created":false
      },
      {
         "student_email":"abc@xyz.com",
         "log_date":"2022-04-21",
         "notes":"previous week thursday",
         "student_uin":"123",
         "approval_due_date":"2022-04-25",
         "hours_submitted":"2.0",
         "semester":"sprng",
         "semester_year":"2022",
         "start_time":"2022-05-01T06:32:00.000Z",
         "end_time":"2022-05-01T09:32:00.000Z",
         "hours_approved":true,
         "created":false
      },
      {
         "student_email":"abc@xyz.com",
         "log_date":"2022-04-22",
         "notes":"previous week friday",
         "student_uin":"123",
         "approval_due_date":"2022-04-25",
         "hours_submitted":"1.0",
         "semester":"sprng",
         "semester_year":"2022",
         "start_time":"2022-05-02T07:32:00.000Z",
         "end_time":"2022-05-02T09:32:00.000Z",
         "hours_approved":true,
         "created":false
      }
   ]
}
```

