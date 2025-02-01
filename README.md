# BharatFD
# FAQ Management System

## Features
- Multilingual FAQ storage
- WYSIWYG editor support
- REST API with language selection
- Caching with Redis
- Auto-translation using Google Translate API
- Django Admin Panel

## Installation
```bash
git clone <repo-url>
cd faq_project
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
