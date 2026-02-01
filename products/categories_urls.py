from django.urls import path
from . import views

urlpatterns=[
    path('',views.api_categories ,name='api-categories'),
    path('/<int:pk>',views.view_specific_category,name='view-specfic-category')
]