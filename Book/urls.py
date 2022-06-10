from django.urls import path, include
from .views import BookView

urlpatterns = [
	path(
		"Book",
		BookView.as_view(),
		name="book"
	),



	]