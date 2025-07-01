from rest_framework import serializers
from .models import GreetingCard, Message

class GreetingCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreetingCard
        fields = ['id', 'groom_name', 'bride_name', 'slug', 'groom_image', 'bride_image', 'created_at']
        read_only_fields = ['id', 'created_at']
        
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'card', 'text', 'sender_name', 'to', 'created_at']
        read_only_fields = ['id', 'created_at']
        
        
class GreetingCardSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = GreetingCard
        fields = [
            'id', 'groom_name', 'bride_name',
            'slug', 'groom_image', 'bride_image',
            'created_at', 'messages'
        ]