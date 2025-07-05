from django.urls import path
from .views import (
    GreetingCardDetailView,
    MessageCreateView,
    GroomMessagesView,
    BrideMessagesView,
    card_page_view,
    groom_messages_view,
    bride_messages_view,
    thank_you_view,
    groom_login_view,
    bride_login_view,
)

urlpatterns = [
    # API
    path('cards/<slug:slug>/', GreetingCardDetailView.as_view(), name='card-detail'),
    path('messages/send/', MessageCreateView.as_view(), name='send-message'),
    path('cards/<slug:slug>/groom/', GroomMessagesView.as_view(), name='api-groom-messages'),
    path('cards/<slug:slug>/bride/', BrideMessagesView.as_view(), name='api-bride-messages'),

    # HTML Pages
    path('cards-page/<slug:slug>/', card_page_view, name='card-page'),
    path('cards/<slug:slug>/thank-you/', thank_you_view, name='thank-you'),

    path('card/<slug:slug>/messages/groom/', groom_messages_view, name='groom-messages'),
    path('card/<slug:slug>/messages/bride/', bride_messages_view, name='bride-messages'),

    # Login Pages
    path('card/<slug:slug>/messages/groom/login/', groom_login_view, name='groom-login'),
    path('card/<slug:slug>/messages/bride/login/', bride_login_view, name='bride-login'),
]