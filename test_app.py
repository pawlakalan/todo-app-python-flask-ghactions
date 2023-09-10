import unittest
from flask import url_for
from app import app, todos

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        todos.clear()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_todo(self):
        response = self.app.post('/add', data={'todo': 'Test Todo'})
        self.assertEqual(response.status_code, 302)  # Redirect after adding
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]['task'], 'Test Todo')
        self.assertFalse(todos[0]['done'])

    def test_edit_todo(self):
        todos.append({'task': 'Existing Todo', 'done': False})
        response = self.app.post('/edit/0', data={'todo': 'Updated Todo'})
        self.assertEqual(response.status_code, 302)  # Redirect after editing
        self.assertEqual(todos[0]['task'], 'Updated Todo')

    def test_check_todo(self):
        todos.append({'task': 'Test Todo', 'done': False})
        response = self.app.get('/check/0')
        self.assertEqual(response.status_code, 302)  # Redirect after checking
        self.assertTrue(todos[0]['done'])

    def test_delete_todo(self):
        todos.append({'task': 'Test Todo', 'done': False})
        response = self.app.get('/delete/0')
        self.assertEqual(response.status_code, 302)  # Redirect after deleting
        self.assertEqual(len(todos), 0)

if __name__ == '__main__':
    unittest.main()
