from django.urls import path
from . import views


urlpatterns = [
    path("createBooks", views.createBooks),
    path("getBooks", views.getBooks),
    path("updateBooks/<str:book_id>", views.updateBooks),
    path("deleteBooks/<str:book_id>", views.deleteBooks)
]