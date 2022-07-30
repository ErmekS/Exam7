from django.urls import path
from django.views.generic import RedirectView

from webapp.views import IndexView, PollView, CreatePoll, UpdatePoll, DeletePoll
from webapp.views.choices import CreateAnswerView, UpdateAnswer, DeleteAnswer

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('poll/<int:pk>', PollView.as_view(), name='PollView'),
    path('poll/create/', CreatePoll.as_view(), name='CreatePoll'),
    path('poll/<int:pk>/update/', UpdatePoll.as_view(), name='UpdatePoll'),
    path('poll/<pk>/delete/', DeletePoll.as_view(), name='DeletePoll'),
    path('poll/<int:pk>/choice/add/', CreateAnswerView.as_view(), name="PollCreateAnswer"),
    path('answer/<int:pk>/update/', UpdateAnswer.as_view(), name="UpdateAnswer"),
    path('answer/<int:pk>/delete/', DeleteAnswer.as_view(), name="DeleteAnswer"),

]
