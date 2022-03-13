from django.test import TestCase


# Create your tests here.
class DatabaseConnectionTest(TestCase):
    """
    This class is for testing the database connection to Postgres server in AWS
    """

    databases = {'dev'}

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self) -> None:
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def tearDown(self) -> None:
        print("tearDown: Run once for every test method to setup clean data.")
        pass

    def test_checkConnection(self):
        """
        This function is used to check the postgres connection
        return: None
        """
        from django.db import connections

        check = False
        try:
            self.c = connections['dev'].cursor()
            check = True
            self.c.close()
        except Exception as e:
            print("Exception occured")
            check = False
        self.assertEqual(check, True)
