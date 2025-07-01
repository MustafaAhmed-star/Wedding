from django.urls import path
from .views import (
    GreetingCardDetailView,
    MessageCreateView,
    GroomMessagesView,
    BrideMessagesView,
)

urlpatterns = [
    path('cards/<slug:slug>/', GreetingCardDetailView.as_view(), name='card-detail'),
    path('messages/send/', MessageCreateView.as_view(), name='send-message'),
    path('cards/<slug:slug>/groom/', GroomMessagesView.as_view(), name='groom-messages'),
    path('cards/<slug:slug>/bride/', BrideMessagesView.as_view(), name='bride-messages'),
]