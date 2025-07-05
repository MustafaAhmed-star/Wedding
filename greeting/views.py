from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import GreetingCard, Message
from .serializers import MessageSerializer, GreetingCardSerializer

# ============= API Views =============

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


# ============= HTML Views =============

def card_page_view(request, slug):
    card = get_object_or_404(GreetingCard, slug=slug)
    return render(request, 'greetings/card.html', {'card': card})


def thank_you_view(request, slug):
    card = get_object_or_404(GreetingCard, slug=slug)
    return render(request, 'greetings/thank_you.html', {'card': card})


# ============= رسائل العريس والعروسة بعد تحقق الكود =============

def groom_messages_view(request, slug):
    card = get_object_or_404(GreetingCard, slug=slug)

    # التحقق من الجلسة
    if request.session.get(f'access_granted_groom_{slug}') != True:
        return redirect('groom-login', slug=slug)

    messages = Message.objects.filter(card=card, to='groom')
    return render(request, 'greetings/messages.html', {
        'messages': messages,
        'card': card,
        'to': 'العريس'
    })


def bride_messages_view(request, slug):
    card = get_object_or_404(GreetingCard, slug=slug)

    # التحقق من الجلسة
    if request.session.get(f'access_granted_bride_{slug}') != True:
        return redirect('bride-login', slug=slug)

    messages = Message.objects.filter(card=card, to='bride')
    return render(request, 'greetings/messages.html', {
        'messages': messages,
        'card': card,
        'to': 'العروسة'
    })


# ============= صفحات إدخال الرمز للعريس والعروسة =============

def groom_login_view(request, slug):
    card = get_object_or_404(GreetingCard, slug=slug)
    error = False

    if request.method == 'POST':
        code = request.POST.get('code')
        if code == card.groom_code:
            request.session[f'access_granted_groom_{slug}'] = True
            return redirect('groom-messages', slug=slug)
        else:
            error = True

    return render(request, 'greetings/login.html', {
        'card': card,
        'error': error,
        'to': 'العريس',
        'action_url': f'/api/card/{slug}/messages/groom/login/',
    })


def bride_login_view(request, slug):
    card = get_object_or_404(GreetingCard, slug=slug)
    error = False

    if request.method == 'POST':
        code = request.POST.get('code')
        if code == card.bride_code:
            request.session[f'access_granted_bride_{slug}'] = True
            return redirect('bride-messages', slug=slug)
        else:
            error = True

    return render(request, 'greetings/login.html', {
        'card': card,
        'error': error,
        'to': 'العروسة',
        'action_url': f'/api/card/{slug}/messages/bride/login/',
    })