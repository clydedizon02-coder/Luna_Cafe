# Luna Café – Django Final Project

A multi-page café website built with **Django Templates** for the DMMMSU-NLUC College of Information Technology Final Project (Django Templates & GitHub).

## Project Overview

**Luna Café** is a fictional student-friendly café near the DMMMSU North La Union Campus.  
The website showcases the café’s story, menu, atmosphere, and contact information using clean, responsive design and proper Django template practices.

**Problem it solves:** Provides an online presence for a local café so students and visitors can easily view the menu, learn about the place, and find contact details.

**Target users:** DMMMSU students, local residents, and café visitors in North La Union.

## Features

- 5 complete pages: Home, About, Menu, Gallery, Contact
- Template inheritance with `base.html` and `{% block %}` / `{% extends %}`
- Reusable navbar and footer via `{% include %}`
- Named URL patterns with `{% url %}` tags (no hard-coded paths)
- Static files (CSS) loaded with `{% load static %}` and `{% static %}`
- Fully responsive design (works on mobile, tablet, and desktop)
- Clean project structure ready for demonstration

## Tech Stack

- Python 3
- Django 4.2+ / 5.x / 6.x
- HTML5 + CSS3 (custom responsive stylesheet)
- Google Fonts (Playfair Display + Inter)

## Project Structure

```
luna_cafe/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── luna_cafe/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── main/               # Main app
    ├── views.py
    ├── urls.py
    ├── templates/main/
    │   ├── base.html
    │   ├── navbar.html
    │   ├── footer.html
    │   ├── home.html
    │   ├── about.html
    │   ├── menu.html
    │   ├── gallery.html
    │   └── contact.html
    └── static/main/css/
        └── style.css
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/clydedizon02-coder/Luna_Cafe.git
   cd Luna_Cafe
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** (creates the database)
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to:  
   **http://127.0.0.1:8000/**

## Pages

| Page     | URL          | Description                          |
|----------|--------------|--------------------------------------|
| Home     | `/`          | Hero section + features + CTA        |
| About    | `/about/`    | Story, mission, vision, stats        |
| Menu     | `/menu/`     | Coffee, pastries, and refreshers     |
| Gallery  | `/gallery/`  | Visual placeholders of the café      |
| Contact  | `/contact/`  | Location, hours, and contact form    |

## AI Tools & Tutorials Acknowledgement

This project was developed with assistance from AI tools (including Grok by xAI) for code structure, template best practices, and CSS design.  
All code has been reviewed and understood by the student. The student is fully responsible for explaining every part of the implementation.

## Author

Student – College of Information Technology  
Don Mariano Marcos Memorial State University – North La Union Campus  
Final Project: Django Templates & GitHub

---

*Built with ❤️ and Django*
