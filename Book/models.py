from django.db import models

# Create your models here.
class Book(models.Model):
	Book_Title = models.CharField(max_length=100, blank=False, null=False)
	Author_name = models.CharField(max_length=100, blank=True, null=True)
	Book_Edition = models.CharField(max_length=100, blank=True, null=True)
	publication = models.CharField(max_length=100, blank=True, null=True)
	book_id = models.IntegerField()
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	Received_date = models.DateTimeField(blank=False, null=False)
	updated_date = models.DateTimeField(blank=False, null=False)