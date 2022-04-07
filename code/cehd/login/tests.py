from django.test import TestCase


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
