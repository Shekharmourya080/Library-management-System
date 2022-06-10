from rest_framework.generics import GenericAPIView
from models import Book

class BookInfo(GenericAPIView):

    @classmethod
    def BookDetails(self, data):

        try:
            if data.get('Book_id'):
                instance = Book.objects.filter(id=data.get("Book_id")).last()

            if instance:
                id= instance.id
                Author_name = instance.Author_name
                Book_Title = instance.Book_Title
                Book_Edition = instance.Book_Edition
                Publication = instance.contact_name
                Book_id = instance.Book_id
        except Exception as e:
            message = str(e)

        return result



























































