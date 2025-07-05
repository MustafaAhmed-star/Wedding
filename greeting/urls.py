from django.urls import path
from .views import (
    GreetingCardDetailView,
    MessageCreateView,
    GroomMessagesView,
    BrideMessagesView,
    card_page_view,
    groom_messages_view,
    bride_messages_view
)

urlpatterns = [
    path('cards/<slug:slug>/', GreetingCardDetailView.as_view(), name='card-detail'),
    path('messages/send/', MessageCreateView.as_view(), name='send-message'),
    path('cards-page/<slug:slug>/', card_page_view, name='card_page'),
    path('cards/<slug:slug>/groom/', GroomMessagesView.as_view(), name='api-groom-messages'),
    path('cards/<slug:slug>/bride/', BrideMessagesView.as_view(), name='api-bride-messages'),
    path('card/<slug:slug>/messages/groom/', groom_messages_view, name='groom_messages'),
    path('card/<slug:slug>/messages/bride/', bride_messages_view, name='bride_messages'),
   
]


