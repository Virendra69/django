from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskManagerTests(TestCase):
    def setUp(self):
        # Create two tasks for testing
        self.task1 = Task.objects.create(title="Task 1", description="Description 1", priority=1, due_date="2024-04-10")
        self.task2 = Task.objects.create(title="Task 2", description="Description 2", priority=2, due_date="2024-04-15")

    def test_index_page(self):
        # Test that the index page loads correctly and displays the list of tasks
        response = self.client.get(reverse('indexPage'))
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        self.assertTemplateUsed(response, 'index.html')  # Check if the correct template is used
        self.assertQuerysetEqual(response.context['all_tasks'], ['Task object (1)', 'Task object (2)'], transform=str)  # Check if the tasks are displayed correctly

    def test_create_task(self):
        # Test that a new task can be created
        initial_task_count = Task.objects.count()
        response = self.client.post(reverse('createTask'), {'title': 'New Task', 'desc': 'New Description', 'priority': 1, 'duedate': '2024-04-20'})
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.assertEqual(Task.objects.count(), initial_task_count + 1)  # Check if a new task is created
        new_task = Task.objects.last()
        self.assertEqual(new_task.title, 'New Task')  # Check if the new task has the correct title

    def test_create_duplicate_task(self):
        # Test that duplicate tasks cannot be created
        initial_task_count = Task.objects.count()
        response = self.client.post(reverse('createTask'), {'title': 'Task 1', 'desc': 'Description 1', 'priority': 1, 'duedate': '2024-04-10'})
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.assertEqual(Task.objects.count(), initial_task_count)  # Check if no new task is created
    
    def test_delete_task(self):
        # Test that a task can be deleted
        initial_task_count = Task.objects.count()
        response = self.client.post(reverse('deleteTask', args=(self.task1.id,)))
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.assertEqual(Task.objects.count(), initial_task_count - 1)  # Check if the task is deleted

    def test_delete_nonexistent_task(self):
        # Test that attempting to delete a nonexistent task returns a 404 error
        initial_task_count = Task.objects.count()
        response = self.client.post(reverse('deleteTask', args=(1000,)))  # Nonexistent task id
        self.assertEqual(response.status_code, 404)  # Check if the response is a 404 error
        self.assertEqual(Task.objects.count(), initial_task_count)  # Check if no task is deleted
