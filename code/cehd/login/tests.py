from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

client = Client()


class DatabaseConnectionTest(TestCase):
    """
    This class is for testing the database connection to Postgres server in AWS
    """
    # databases = {'dev'}
    def test_checkConnection(self):
        """
        This function is used to check the postgres connection
        return: None
        """
        from django.db import connection

        check = False
        try:
            self.c = connection.cursor()
            check = True
            self.c.close()
        except Exception as e:
            print("Exception occurred")
            check = False
        self.assertEqual(check, True)

    def test_login_page(self):
        """
        Test to check the accessibility to login page
        """
        response = client.get(reverse("login"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_page(self):
        """
        Test to check the accessibility to register page
        """
        response = client.get(reverse("register"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_page(self):
        """
        Test to check the accessibility to logout page
        """
        response = client.get(reverse("logout"))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
