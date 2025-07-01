from django.db import models


class GreetingCard(models.Model):
    groom_name = models.CharField(max_length=50)
    bride_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    groom_image = models.ImageField(upload_to='groom_images/')
    bride_image = models.ImageField(upload_to='bride_images/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.groom_name} & {self.bride_name}"
        
        
class Message(models.Model):
    TO_CHOICES = [
        ('G', 'Groom'),
        ('B', 'Bride'),
    ]
    card = models.ForeignKey(GreetingCard, related_name='messages', on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=50)
    message_text = models.TextField()
    to = models.CharField(max_length=1, choices=TO_CHOICES, default='G')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender_name} on {self.created_at}"