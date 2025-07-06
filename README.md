# 💌 Wedding Greeting Card - بطاقة تهنئة زفاف

مشروع بسيط وجميل لعمل كارت تهنئة تفاعلي للعريس والعروسة مع إمكانية إرسال تهاني وعرضها بشكل أنيق 🎉

---

## 🚀 الميزات

- تصميم مبهج يشبه فتح كتاب 📖
- إمكانية إرسال تهنئة من الزوار
- صفحة شكر بعد الإرسال ✅
- صفحات خاصة لعرض تهاني العريس أو العروسة فقط
- مشاركة البطاقة عبر واتساب وفيسبوك
- حماية عرض الرسائل (كل مستخدم يشوف اللي أرسل بس)
- يدعم الصور والكتابة بالعربية

---

## 📸 صورة من المشروع

![screenshot](https://via.placeholder.com/800x400.png?text=Wedding+Card+Preview)

---

## 🛠️ التقنيات المستخدمة

- Django 5.2.3
- Django REST Framework
- HTML/CSS & Vanilla JS
- Render for deployment

---

## 📦 خطوات التشغيل محليًا

```bash
# 1. استنساخ المشروع
git clone https://github.com/YourUsername/wedding-card.git
cd wedding-card

# 2. تثبيت المتطلبات
pip install -r requirements.txt

# 3. تهيئة القاعدة وتجهيز static
python manage.py migrate
python manage.py collectstatic

# 4. تشغيل الخادم المحلي
python manage.py runserver
