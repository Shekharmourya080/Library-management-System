from rest_framework.generics import GenericAPIView
from models import Book



class CreateOrUpdate(GenericAPIView):
    @staticmethod
    def BookCreateOrUpdate(self, data):
        instance = None
        if data.get('Book_id'):
            instance = Book.objects.filter(
                id=data.get('Book_id')
            ).last()

        if not instance:
            instance = Book()

        instance.Author_name = data.get(
            "Author-name") if "Author_name" in data else instance.Author_name if instance.Author_name else None
        instance.Book_Title = data.get(
            "Book-Title") if "Book_Title" in data else instance.Book_Title if instance.Book_Title else None
        instance.Book_Edition = data.get(
            "Book-Edition") if "Book_Edition" in data else instance.Book_Edition if instance.Book_Edition else None
        instance.publication = data.get(
            "publication") if "publication" in data else instance.publication if instance.publication else 0
        instance.Book_id = data.get(
            "Book-id") if "Book_id" in data else instance.Book_id if instance.Book_id else None
        instance.is_active = data.get(
            "is_active") if "is_active" in data else instance.is_active if instance.is_active else None
        instance.is_deleted = data.get(
            "is_deleted") if "is_deleted" in data else instance.is_deleted if instance.is_deleted else None
        instance.Received_date = data.get(
            "Received-date") if "is_active" in data else instance.Received_date if instance.Received_date else None
        instance.updated_date = data.get(
            "updated-date") if "updated_date" in data else instance.updated_date if instance.updated_date else None
        instance.save()
