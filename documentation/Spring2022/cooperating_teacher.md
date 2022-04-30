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

**supervisor_coop**
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

**supervisor_coop_sem**
* **URL - http://127.0.0.1:8000/supervisor/email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor
* **Input** - super_email (str), coop_email (str), semester (str)
* **Output** : Example
```
{
	'status': 'success',
	'message': 'data retrieved',
	'data': {
		'university_supervisor_email': 'johnny@xyz.com',
		'cooperating_teacher_email': 'moore@xyz.com',
		'cooperating_teachers': [{
			'cooperating_teacher': 'Kasey Moore',
			'cooperating_teacher_email': 'kaseymoore@xyz.com'
		}, {
			'cooperating_teacher': 'Michael Moore',
			'cooperating_teacher_email': 'moore@xyz.com'
		}],
		'years': ['2022'],
		'university_supervisor_name': 'John Paul',
		'cooperating_teacher_selected': 'Michael Moore',
		'cooperating_teacher_email_selected': 'moore@xyz.com',
		'timelogs': [{
			'student_uin': 123,
			'student_email': 'abc@xyz.com',
			'log_date': '2022-04-04',
			'notes': 'submitted now test',
			'hours_submitted': '4.0',
			'hours_approved': False,
			'approval_due_date': '2022-04-10',
			'semester': 'sprng',
			'semester_year': '2022',
			'start_time': '2022-05-04T17:11:00Z',
			'end_time': '2022-05-04T21:11:00Z',
			'date_submitted': '2022-04-08',
			'student_name': 'John C Doe'
		}, ...]
	}
}
```
----

**supervisor_coop_sem_year**
* **URL - http://127.0.0.1:8000/supervisor/email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/year/<str:year>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor
* **Input** - super_email (str), coop_email (str), semester (str), year (int)
* **Output** : Example
```
{
	'status': 'success',
	'message': 'data retrieved',
	'data': {
		'university_supervisor_email': 'johnny@xyz.com',
		'cooperating_teacher_email': 'moore@xyz.com',
		'cooperating_teachers': [{
			'cooperating_teacher': 'Kasey Moore',
			'cooperating_teacher_email': 'kaseymoore@xyz.com'
		}, {
			'cooperating_teacher': 'Michael Moore',
			'cooperating_teacher_email': 'moore@xyz.com'
		}],
		'years': ['2022'],
		'university_supervisor_name': 'John Paul',
		'cooperating_teacher_selected': 'Michael Moore',
		'cooperating_teacher_email_selected': 'moore@xyz.com',
		'timelogs': [{
			'student_uin': 123,
			'student_email': 'abc@xyz.com',
			'log_date': '2022-04-04',
			'notes': 'submitted now test',
			'hours_submitted': '4.0',
			'hours_approved': False,
			'approval_due_date': '2022-04-10',
			'semester': 'sprng',
			'semester_year': '2022',
			'start_time': '2022-05-04T17:11:00Z',
			'end_time': '2022-05-04T21:11:00Z',
			'date_submitted': '2022-04-08',
			'student_name': 'John C Doe'
		}, ...]
	}
}
```
----

**supervisor_coop_year**
* **URL - http://127.0.0.1:8000/supervisor/email/<str:super_email>/coop/<str:coop_email>/year/<str:year>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor
* **Input** - super_email (str), coop_email (str), semester (str), year (int)
* **Output** : Example
```
{
	'status': 'success',
	'message': 'data retrieved',
	'data': {
		'university_supervisor_email': 'johnny@xyz.com',
		'cooperating_teacher_email': 'moore@xyz.com',
		'cooperating_teachers': [{
			'cooperating_teacher': 'Kasey Moore',
			'cooperating_teacher_email': 'kaseymoore@xyz.com'
		}, {
			'cooperating_teacher': 'Michael Moore',
			'cooperating_teacher_email': 'moore@xyz.com'
		}],
		'years': ['2022'],
		'university_supervisor_name': 'John Paul',
		'cooperating_teacher_selected': 'Michael Moore',
		'cooperating_teacher_email_selected': 'moore@xyz.com',
		'timelogs': [{
			'student_uin': 123,
			'student_email': 'abc@xyz.com',
			'log_date': '2022-04-04',
			'notes': 'submitted now test',
			'hours_submitted': '4.0',
			'hours_approved': False,
			'approval_due_date': '2022-04-10',
			'semester': 'sprng',
			'semester_year': '2022',
			'start_time': '2022-05-04T17:11:00Z',
			'end_time': '2022-05-04T21:11:00Z',
			'date_submitted': '2022-04-08',
			'student_name': 'John C Doe'
		}, ...]
	}
}
```
