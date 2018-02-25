from django.test import TestCase

class Login_Test(TestCase):
    def test_login(self):
        response = self.client.post('/', {'username': 'py.dev.ib@gmail.com', 'password': 'admin123'})
        self.assertEqual(response.status_code, 200)

class Create_Group_Test(TestCase):
    def test_create_group_form(self):
        response = self.client.post('/group/add_group/',{'name': 'RR_Test'})
        self.assertEqual(response.status_code, 302)

class Add_Student_Test(TestCase):
    def test_add_student_form(self):
        response = self.client.post('/students/add_student/',
                                    {
                                        'get_name'    : 'Севрюков Антон Петрович',
                                        'date_of_birth': '12.10.1990',
                                        'student_card': 'RR-001',
                                        'group'       : 'RR_Test'
                                    })
        self.assertEqual(response.status_code, 302)
