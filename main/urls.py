from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', user_profile),
    path('say_hello/', say_hello),
    path('filter_queries/<int:query_id>/', filter_queries),
    path('queries/', QueryView.as_view(), name="query_view")
]