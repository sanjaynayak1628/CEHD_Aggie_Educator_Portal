*API Docummentation - Supervisor*
----
**supervisor_coop_view**
* **URL - /supervisor/email/\<str:super_email>**
* **Method:** - `GET`
* **Description** - Get the list of cooperating teachers under the supervisor
* **Input** - super_email (str) 
* **Output** : Example
```
{
	'status': 'success',
	'message': 'data retrieved',
	'data': {
		'university_supervisor_email': 'johnny@xyz.com',
		'cooperating_teachers': [{
			'cooperating_teacher': 'Kasey Moore',
			'cooperating_teacher_email': 'kaseymoore@xyz.com'
		}, {
			'cooperating_teacher': 'Michael Moore',
			'cooperating_teacher_email': 'moore@xyz.com'
		}],
		'years': ['2022'],
		'university_supervisor_name': 'John Paul'
	}
} 
```

**supervisor_coop**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>**
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
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/semester/\<str:semester>**
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
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/semester/\<str:semester>/year/\<str:year>**
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
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/year/\<str:year>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor
* **Input** - super_email (str), coop_email (str), year (str)
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

**supervisor_coop_dates**
* **URL - /supervisor/email/email/\<str:super_email>/coop/\<str:coop_email>/start/\<str:start_date>/end/\<str:end_date>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor
* **Input** - super_email (str), coop_email (str), start_date (str), end_date (str)
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

**supervisor_coop_sem_dates_year**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/semester/\<str:semester>/year/\<str:year>/start/\<str:start_date>/end/\<str:end_date>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor
* **Input** - super_email (str), coop_email (str), semester (str), year (str), start_date (str), end_date (str)
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

**supervisor_coop_sem_dates**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/semester/\<str:semester>/start/\<str:start_date>/end/\<str:end_date>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor
* **Input** - super_email (str), coop_email (str), semester (str), start_date (str), end_date (str)
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

**supervisor_coop_year_dates**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/year/\<str:year>/start/\<str:start_date>/end/\<str:end_date>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor
* **Input** - super_email (str), coop_email (str), year (str), start_date (str), end_date (str)
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

**supervisor_coop_export**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/export/\<str:export>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor and export them as a csv file
* **Input** - super_email (str), coop_email (str), export (str)
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

**supervisor_coop_sem_export**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/semester/\<str:semester>/export/\<str:export>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor and export them as a csv file
* **Input** - super_email (str), coop_email (str), export (str), semester (str), export (str)
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

**supervisor_coop_sem_year_export**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/semester/\<str:semester>/year/\<str:year>/export/\<str:export>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor and export them as a csv file
* **Input** - super_email (str), coop_email (str), export (str), semester (str), year (str), export (str)
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

**supervisor_coop_year_export**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/year/\<str:year>/export/\<str:export>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor and export them as a csv file
* **Input** - super_email (str), coop_email (str), export (str), year (str), export (str)
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

**supervisor_coop_dates_export**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/start/\<str:start_date>/end/\<str:end_date>/export/\<str:export>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor and export them as a csv file
* **Input** - super_email (str), coop_email (str), export (str), start_date (str), end_date (str)
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

**supervisor_coop_sem_dates_year_export**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/semester/\<str:semester>/year/\<str:year>/start/\<str:start_date>/end/\<str:end_date>/export/\<str:export>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor and export them as a csv file
* **Input** - super_email (str), coop_email (str), export (str), start_date (str), end_date (str), semester (str), year (str)
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

**supervisor_coop_sem_dates_export**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/semester/\<str:semester>/start/\<str:start_date>/end/\<str:end_date>/export/\<str:export>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor and export them as a csv file
* **Input** - super_email (str), coop_email (str), export (str), start_date (str), end_date (str), semester (str)
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

**supervisor_coop_year_dates_export**
* **URL - /supervisor/email/\<str:super_email>/coop/\<str:coop_email>/year/\<str:year>/start/\<str:start_date>/end/\<str:end_date>/export/\<str:export>**
* **Method:** - `GET`
* **Description** - GET function to get the time logs for each student against selected cooperating teacher under the supervisor and export them as a csv file
* **Input** - super_email (str), coop_email (str), export (str), start_date (str), end_date (str)
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
