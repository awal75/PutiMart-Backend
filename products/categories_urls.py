from django.urls import path
from . import views

urlpatterns=[

    path('/<int:pk>',views.view_specific_category),
]