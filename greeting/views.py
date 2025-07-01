from rest_framework import generics
from .models import GreetingCard, Message
from .serializers import MessageSerializer,GreetingCardSerializer
from rest_framework import generics
class GreetingCardDetailView(generics.RetrieveAPIView):
    queryset = GreetingCard.objects.all()
    serializer_class = GreetingCardSerializer
    lookup_field = 'slug'
    
    

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


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