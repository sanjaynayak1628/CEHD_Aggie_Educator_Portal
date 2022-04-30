*API Docummentation - Supervisor*
----
**SupervisorCoopView**
* **URL - http://127.0.0.1:8000/supervisor/email/email/<str:super_email>**
* **Method:** - `GET`
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

**SupervisorCoopView**
* **URL - http://127.0.0.1:8000/supervisor/email/email/<str:super_email>**
* **Method:** - `GET`
* **Input** - super_email (str) 
* **Output** : Example
```{
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
