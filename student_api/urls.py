from django.urls import path

from .views import list_all_paths, add_new_path, get_one_path, update_one_path, delete_one_path, patch_path, list_all_students, add_new_student, get_one_student, update_one_student, delete_one_student, patch_student


urlpatterns = [
    # Paths
    path("paths/", list_all_paths),
    path("add_path/", add_new_path),
    path("path/<int:pk>", get_one_path),
    path("update_path/<int:pk>", update_one_path),
    path("delete_path/<int:pk>", delete_one_path),
    path("patch_path/<int:pk>", patch_path),

    # Students
    path("students/", list_all_students),
    path("add_student/", add_new_student),
    path("student/<int:pk>", get_one_student),
    path("update_student/<int:pk>", update_one_student),
    path("delete_student/<int:pk>", delete_one_student),
    path("patch_student/<int:pk>", patch_student),
]
