# BharatFD
# FAQ Management System
# 📖 Multilingual FAQ API

A Django REST framework-based API to store and manage **Frequently Asked Questions (FAQs)** with **multi-language support** using **Google Translate API** and **Redis caching**. The project includes **JWT authentication**, **WYSIWYG editor (CKEditor) integration**, and is Docker-ready for deployment.

---

## **🚀 Features**
- 🌍 **Multi-language support** for FAQs (English, Hindi, Bengali, etc.)
- ✍ **WYSIWYG editor** (`django-ckeditor`) for rich text formatting.
- 🔥 **Fast & cached translations** using **Redis**.
- 🔐 **JWT Authentication** for secure API access.
- 📡 **RESTful API** built with Django REST Framework (**DRF**).
- 📜 **Admin panel integration** for easy FAQ management.
- 🐳 **Docker support** for easy deployment.
- ✅ **Automated testing** with `pytest`.

---

## **📦 Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/ishan1915/multilingual-faq-api.git
cd multilingual-faq-api


 

```bash
git clone <repo-url>
cd faq_project
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
