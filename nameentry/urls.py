from django.urls import path
import nameentry.views

urlpatterns = [
    path('', nameentry.views.index)
]
