import pytest
from django.test import Client
from notes.models import Note


@pytest.mark.django_db
class TestProfiles:
    def test_notes_index_view(self):
        client = Client()

        response = client.get("/")
        assert response.status_code == 200


    def test_notes_add_view(self):
        client = Client()

        resource = client.post("/", {"title": "test", "text": "test"}, follow=True)
        assert resource.status_code == 200
        assert Note.objects.count() == 1
