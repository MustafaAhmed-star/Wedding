from django.db import models


from django.utils.text import slugify

class GreetingCard(models.Model):
    groom_name = models.CharField("اسم العريس", max_length=50)
    bride_name = models.CharField("اسم العروسة", max_length=50)
    slug = models.SlugField("الاسم المختصر للرابط", unique=True)
    groom_image = models.ImageField("صورة العريس", upload_to='groom_images/')
    bride_image = models.ImageField("صورة العروسة", upload_to='bride_images/')
    groom_code = models.CharField(max_length=10)
    bride_code = models.CharField(max_length=10)

    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.groom_name}_{self.bride_name}")
            unique_slug = base_slug
            counter = 1
            while GreetingCard.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs) 
    def __str__(self):
        return f"{self.groom_name} و {self.bride_name}"

    class Meta:
        verbose_name = "كارت تهنئة"
        verbose_name_plural = "كروت التهنئة"
        
class Message(models.Model):
    TO_CHOICES = (
        ('groom', 'العريس'),
        ('bride', 'العروسة'),
    )

    card = models.ForeignKey(GreetingCard, related_name="messages", on_delete=models.CASCADE, verbose_name="كارت التهنئة")
    text = models.TextField("نص التهنئة")
    sender_name = models.CharField("اسم المُرسل", max_length=50)
    to = models.CharField("إلى", max_length=10, choices=TO_CHOICES)
    created_at = models.DateTimeField("تاريخ الإرسال", auto_now_add=True)

    def __str__(self):
        return f"من {self.sender_name} إلى {self.get_to_display()}"

    class Meta:
        verbose_name = "رسالة تهنئة"
        verbose_name_plural = "رسائل التهنئة"