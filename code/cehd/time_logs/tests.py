import json

from django.test import TestCase
import requests


class StudentviewTest(TestCase):
    """
    This class is for testing the Student View APIs
    """

    # @classmethod
    # def setUpTestData(cls):
    #     pass
    #
    # def setUp(self) -> None:
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass
    #
    # def tearDown(self) -> None:
    #     print("tearDown: Run once for every test method to setup clean data.")
    #     pass

    def test_save(self):
        """
        This function is used to check the correctness of Student View APIs
        return: Correct Response
        """
        url = "http://127.0.0.1:8000/timelogs/student/save/"
        data = {
            "data": [
                {
                    "student_uin": 126,
                    "student_email": "srutipatnaik@xyz.com",
                    "log_date": "2022-04-01",
                    "notes": "submitted",
                    "hours_submitted": 40,
                    "hours_approved": False,
                    "approval_due_date": "2022-04-03",
                    "semester": "fall",
                    "start_time": "2022-04-03T12:20:10.233",
                    "end_time": "2022-04-03T20:20:10.233"
                }
            ]
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=url, data=data, headers=headers)
        print(response)
        self.assertEqual(response.status_code, 200)
