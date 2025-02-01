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









📝 API Documentation
Authentication
Method	Endpoint	Description
POST	/api/token/	Get JWT token
POST	/api/token/refresh/	Refresh JWT token
Example Request (Token Generation)

 
Edit
{
  "username": "admin",
  "password": "yourpassword"
}

FAQ Endpoints
Method	Endpoint	Description
GET	/api/faqs/	List all FAQs
POST	/api/faqs/	Create a new FAQ
GET	/api/faqs/{id}/	Retrieve an FAQ
PUT	/api/faqs/{id}/	Update an FAQ
DELETE	/api/faqs/{id}/	Delete an FAQ


Get FAQs in Different Languages
 
GET /api/faqs/?lang=hi  # Fetch FAQs in Hindi
GET /api/faqs/?lang=bn  # Fetch FAQs in Bengali
Example Response

 
{
  "id": 1,
  "question": "What is Django?",
  "answer": "<p>Django is a Python web framework.</p>",
  "translated_question": "डिजैंगो क्या है?"
}
🛠 Running Tests
Run tests using pytest:
pytest
