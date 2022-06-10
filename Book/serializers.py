from rest_framework import serializers
from models import Book


class KeyErrorSerializer(serializers.Serializer):
	error = serializers.CharField(
		required=False,
		help_text="Key error. Please check the error message"
	)

	@classmethod
	def validate(self, data):
		errors = {}

		if errors:
			raise serializers.ValidationError(errors)

		return super(KeyErrorSerializer, self).validate(self, data)


class BookCreateSerializer(serializers.Serializer):
	Book_id = serializers.IntegerField(
		required=False
	)
	Author_name = serializers.CharField(
		required=True
	)
	Book_Title = serializers.CharField(
		required=False
	)
	Book_Edition = serializers.CharField(
		required=False,
	)
	publication = serializers.CharField(
		required=False,
	)
	is_active = serializers.BooleanField(
		default=True,
		required=False
	)
	is_deleted = serializers.BooleanField(
		default=False,
		required=False
	)
	Received_date = serializers.DateTimeField(
		blank=False,
		null=False
	)
	updated_date = serializers.DateTimeField(
		blank=False,
		null=False
	)

	@classmethod
	def validate(self, data):

		errors = {}
		Book_id = data.get("Book_id")
		isExists = Book.objects.filter(Book_id=Book_id)

		if Book_id > 0:
			isExists = isExists.exclude(id=Book_id).exists()
		else:
			isExists = isExists.exists()

		if isExists:
			errors["Book"] = "Book already exists."

		if errors:
			raise serializers.ValidationError(errors)

		return super(BookCreateSerializer, self).validate(self, data)


class BookDetailsSerializer(serializers.Serializer):
	Book_id = serializers.IntegerField(
		required=True
	)

	@classmethod
	def validate(self, data):

		errors = {}
		Book_id = data.get("Book_id")
		if int(Book_id) <= 0 or Book_id == "":
			errors["Book"] = "Please select valid Book."
		item_exist = Book.objects.filter(id=Book_id).exists()
		if not item_exist:
			errors["supplier"] = "Book dose not exists."

		if errors:
			raise serializers.ValidationError(errors)

		return super(BookDetailsSerializer, self).validate(self, data)