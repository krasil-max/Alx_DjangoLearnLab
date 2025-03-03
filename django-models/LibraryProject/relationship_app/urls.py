from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')), # Add this line
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # ... your other URL patterns ...
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='login'), name='logout'),
    # ... your other URL patterns ...
]

from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path("books/add/", views.add_book, name="add_book/"),
    path("books/edit/<int:pk>/", views.edit_book, name="edit_book/"),
    path("books/delete/<int:pk>/", views.delete_book, name="delete_book"),
]