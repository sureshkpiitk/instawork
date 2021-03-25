from django.urls import path

from team.views import TeamAPIView

urlpatterns = [
    path(r'/', TeamAPIView.as_view()),
    path(r'/<uuid:pk>/', TeamAPIView.as_view()),
]
