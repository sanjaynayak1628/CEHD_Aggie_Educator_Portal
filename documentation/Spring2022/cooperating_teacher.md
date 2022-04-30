*API Docummentation - Cooperating Teachers*
----
**coop_view_initial**
* **URL - /coop/email/\<str:coop_email\>/view**
* **Method:** - `GET`
* **Description** - Get the list of students under the cooperating teachers
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
* **URL - http://127.0.0.1:8000/supervisor/email/<str:super_email>/coop/<str:coop_email>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor
* **Input** - super_email (str), co_op email (str)
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
