from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_creating_user_with_email(self):
        ''' TESTING USER CREATION WITH EMAIL. '''
        email = "anubhav@google.com"
        password = "abcd"
        User = get_user_model()
        user = User.objects.create_user(email = email, password= password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        '''
            'USERNAME' FIELD IS NONE FOR ABSTRACT-USER & 'USERNAME' FIELD DOESN'T EXIST FOR ABSTRACT-BASE-USER.
        '''

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        '''
            SOME OTHER VALIDATION CHECKS FOR THE CUSTOM CREATE USER METHOD ON THE USER MANAGER.
        '''

        with self.assertRaises(TypeError):
            user = User.objects.create_user()
        
        with self.assertRaises(TypeError):
            user = User.objects.create_user(email = '')

        with self.assertRaises(ValueError):
            user = User.objects.create_user(email = '', password = '')

    def test_creating_super_user(self):
        ''' TESTING USER IS SUPERUSER WHEN CREATED USING CREATE-SUPER-USER METHOD '''

        email = "anubhav@google.com"
        password = "abcd"
        User = get_user_model()
        admin_user = User.objects.create_superuser(email = email, password= password)

        self.assertEqual(admin_user.email, email)
        self.assertTrue(admin_user.check_password(password))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        '''
            'USERNAME' FIELD IS NONE FOR ABSTRACT-USER & 'USERNAME' FIELD DOESN'T EXIST FOR ABSTRACT-BASE-USER.
        '''

        try:
            self.assertIsNone(self.username)
        except AttributeError:
            pass

        '''
            SOME OTHER VALIDATION CHECKS FOR THE CUSTOM CREATE USER METHOD ON THE USER MANAGER.
        '''




        


