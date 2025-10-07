from django.urls import path
from . import views

app_name = "videos"

urlpatterns = [
    path("", views.video_list, name="list"),                          # Read (list)
    path("video/<int:pk>/", views.video_detail, name="detail"),       # Read (detail)
    path("video/new/", views.video_create, name="create"),            # Create
    path("video/<int:pk>/edit/", views.video_update, name="update"),  # Update
    path("video/<int:pk>/delete/", views.video_delete, name="delete") # Delete
]
