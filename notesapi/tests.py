from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Note

class NoteAPITests(APITestCase):
    def setUp(self):
        # Create some initial notes for testing
        self.note1 = Note.objects.create(body="Test Note 1")
        self.note2 = Note.objects.create(body="Test Note 2")

    def test_get_routes(self):
        url = reverse('routes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions as needed

    def test_get_notes(self):
        url = reverse('notes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_note(self):
        # Test retrieving a single note
        note_id = self.note1.id  
        url = reverse('single-note', args=[note_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_note(self):
        url = reverse('create-note')
        data = {'body': 'New Test Note'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_note(self):
        note_id = self.note1.id 
        url = reverse('update-note', args=[note_id])
        data = {'body': 'Updated Test Note'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_note(self):
        note_id = self.note2.id 
        url = reverse('delete-note', args=[note_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from .models import Note

# # Create your tests here.
# class NoteAPITests(TestCase):
#     def setUp(self):
#         # Create some initial notes for testing
#         self.note1 = Note.objects.create(body="Test Note 1")
#         self.note2 = Note.objects.create(body="Test Note 2")

#     def test_get_routes(self):
#         url = reverse('routes')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # Add more assertions as needed

#     def test_get_notes(self):
#         url = reverse('notes')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # Add more assertions as needed

#     def test_get_single_note(self):
#         # Test retrieving a single note
#         note_id = self.note1.id  # Use the id of an existing note
#         url = reverse('single-note', args=[note_id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # Add more assertions as needed

#     def test_create_note(self):
#         url = reverse('create-note')
#         data = {'body': 'New Test Note'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         # Add more assertions as needed

#     def test_update_note(self):
#         note_id = self.note1.id  # Use the id of an existing note
#         url = reverse('update-note', args=[note_id])
#         data = {'body': 'Updated Test Note'}
#         response = self.client.put(url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_delete_note(self):
#         note_id = self.note2.id  # Use the id of an existing note
#         url = reverse('delete-note', args=[note_id])
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




# class NoteAPITests(TestCase):
#     def setUp(self):
#         # Set up test data (create initial notes)
#         self.client = APIClient()
#         self.notes_data = [
#             {'body': 'Note 1'},
#             {'body': 'Note 2'},
#             # Add more test data as needed
#         ]
#         for note_data in self.notes_data:
#             Note.objects.create(**note_data)

#     def test_get_all_notes(self):
#         # Test retrieving all notes
#         url = reverse('notes')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), len(self.notes_data))

#     def test_get_single_note(self):
#         # Test retrieving a single note
#         note_id = 2  # Adjust the note ID based on your test data
#         url = reverse('single-note', args=[note_id])

#         # Print the state of the database before the test
#         print("Database content before test:")
#         for note in Note.objects.all():
#             print(f"Note ID: {note.id}, Content: {note.body}")

#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # Print the state of the database after the test
#         print("Database content after test:")
#         for note in Note.objects.all():
#             print(f"Note ID: {note.id}, Content: {note.body}")

#         with self.assertRaises(Note.DoesNotExist) as context:
#             response = self.client.get(url)

#         # Check if the expected exception is raised
#         self.assertEqual(
#             str(context.exception),
#             'Note matching query does not exist.'
#         )

#     def test_create_note(self):
#         # Test creating a new note
#         new_note_data = {'body': 'New Note'}
#         url = reverse('create-note')
#         response = self.client.post(url, new_note_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         # Add more assertions as needed

#     def test_update_note(self):
#         # Test updating an existing note
#         note_id = 1  # Adjust the note ID based on your test data
#         updated_note_data = {'body': 'Updated Note'}
#         url = reverse('update-note', args=[note_id])
#         response = self.client.put(url, updated_note_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#         # Add more assertions as needed

#     def test_delete_note(self):
#         # Test deleting an existing note
#         note_id = 1  # Adjust the note ID based on your test data
#         url = reverse('delete-note', args=[note_id])
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)