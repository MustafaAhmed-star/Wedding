from rest_framework import generics
from .models import GreetingCard, Message
from .serializers import MessageSerializer,GreetingCardSerializer
from rest_framework import generics
class GreetingCardDetailView(generics.RetrieveAPIView):
    queryset = GreetingCard.objects.all()
    serializer_class = GreetingCardSerializer
    lookup_field = 'slug'
    
    

# class MessageCreateView(generics.CreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer


class GroomMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Message.objects.filter(card__slug=slug, to='groom')
        
class BrideMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Message.objects.filter(card__slug=slug, to='bride')
        
        
# greeting/views.py for rendering the card page (CRUD operations)
from django.shortcuts import render, get_object_or_404

def card_page_view(request, slug):
    card = get_object_or_404(GreetingCard, slug=slug)
    return render(request, 'greetings/card.html', {'card': card})
    
    
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer