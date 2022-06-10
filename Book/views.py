from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from return_type.response import Errors
from rest_framework.permissions import IsAuthenticated
from Book.serializers import *
from Book.create_or_update import CreateOrUpdate
from info import BookInfo
from drf_yasg import openapi



class BookView(GenericAPIView):
    """
        Book Packages APIs
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = BookCreateSerializer

    response_schema_dict = {
        "400": openapi.Response(
            description="custom 400 description",
            examples={
                "application/json": {
                    "error": "frontend error"
                }
            },
            schema=KeyErrorSerializer
        ),
        "200": openapi.Response(
            description="custom 200 description",
            examples={
                "application/json":
                    [
                        {
                            "id": 0,
                            "message": "Book Saved sucessfully."
                        }
                    ]
            },
            schema=BookCreateSerializer
        ),
    }

    @classmethod
    def post(self, data, *args):
        response = {}
        data = args[0]

        data_validation = BookCreateSerializer(data=data)
        is_valid_data = data_validation.is_valid()

        if is_valid_data:
            data = data_validation.validated_data
            instance = CreateOrUpdate.BookCreateOrUpdate(
                self,
                data
            )
            response["id"] = instance.id
            response['message'] = "Book Saved sucessfully."
            status_code = 200

        else:
            status_code = 400
            errorlist = [data_validation.errors]
            response["errors"] = Errors.combine_allErrors(errorlist)
            response["status"] = status_code

        return Response(response, status=status_code)

    response_schema_dict = {
        "400": openapi.Response(
            description="custom 400 description",
            examples={
                "application/json": {
                    "error": "frontend error"
                }
            },
            schema=KeyErrorSerializer
        ),
        "200": openapi.Response(
            description="custom 200 description",
            examples={
                "application/json":
                    [
                        {
                            "id": 0,
                            "message": "Book Updated sucessfully."
                        }
                    ]
            },
            schema=BookCreateSerializer
        ),
    }

    @classmethod
    def put(self, request, *args,):
        response = {}
        data = args[0]
        Book_id = request.GET.get('Book_id')
        if Book_id == "" or int(Book_id) <= 0:
            status_code = 400
            response["errors"] = "Please provide the supplier_id"
            response["status"] = status_code
            return Response(response, status=status_code)

        data.update({"Book_id": Book_id})

        data_validation = BookCreateSerializer(data=data)
        is_valid_data = data_validation.is_valid()

        if is_valid_data:
            data = data_validation.validated_data
            instance = CreateOrUpdate.BookCreateOrUpdate(
                self,
                data
            )
            response["id"] = instance.id
            response['message'] = "Book Updated sucessfully."
            status_code = 200

        else:
            status_code = 400
            errorlist = [data_validation.errors]
            response["errors"] = Errors.combine_allErrors(errorlist)
            response["status"] = status_code

        return Response(response, status=status_code)

    response_schema_dict = {
        "400": openapi.Response(
            description="custom 400 description",
            examples={
                "application/json": {
                    "error": "frontend error"
                }
            },
            schema=KeyErrorSerializer
        ),
        "200": openapi.Response(
            description="custom 200 description",
            examples={
                "application/json":
                    [
                        {
                            "Author_name": "",
                            "Book_Title":"",
                            "publication": "",
                            "book_Edition": "",
                            "Received_date": "",
                            "updated_date": "",
                            "Book_id": 0,
                            "is_active": True,
                            "is_deleted": False,
                            "message": "Book details fetched successfully."
                        }
                    ]
            },
            schema=BookDetailsSerializer
        ),
    }

    @classmethod
    def get(self, data, *args):
        response = {}
        data = args[0]

        data_validation = BookDetailsSerializer(data=data)
        is_valid_data = data_validation.is_valid()

        if is_valid_data:
            data = data_validation.validated_data
            response = BookInfo.BookDetails(
                self,
                data
            )
            status_code = 200

        else:
            status_code = 400
            errorlist = [data_validation.errors]
            response["errors"] = Errors.combine_allErrors(errorlist)
            response["status"] = status_code

        return Response(response, status=status_code)

    response_schema_dict = {
        "400": openapi.Response(
            description="custom 400 description",
            examples={
                "application/json": {
                    "error": "frontend error"
                }
            },
            schema=KeyErrorSerializer
        ),
        "200": openapi.Response(
            description="custom 200 description",
            examples={
                "application/json":
                    [
                        {

                            "is_deleted": True,
                            "message": "Book deleted successfully."
                        }
                    ],
            },
            schema=BookDetailsSerializer
        ),
    }

    @classmethod
    def delete(self, request, *args):
        response = {}
        data = args[0]
        Book_id = request.GET.get('Book_id')
        if Book_id == "" or int(Book_id) <= 0:
            status_code = 400
            response["errors"] = "Please provide the Book_id"
            response["status"] = status_code
            return Response(response, status=status_code)

        data.update({"Book_id": Book_id})

        data_validation = BookCreateSerializer(data=data)
        is_valid_data = data_validation.is_valid()

        if is_valid_data:
            data = data_validation.validated_data
            instance = CreateOrUpdate.BookCreateOrUpdate(
                self,
                data
            )
            response["id"] = instance.id
            response['message'] = "Book deleted sucessfully."
            status_code = 200

        else:
            status_code = 400
            errorlist = [data_validation.errors]
            response["errors"] = Errors.combine_allErrors(errorlist)
            response["status"] = status_code

        return Response(response, status=status_code)


