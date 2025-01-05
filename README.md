# Django Chatbot with OpenAI ChatGPT (Davinci-002 Model)

A Django-based chatbot application that integrates OpenAI's GPT model (Davinci-002) to provide intelligent and conversational interactions. This project demonstrates how to use OpenAI's API within a Django framework to create a scalable and customizable chatbot.

---

## Features
- 💬 **AI-Powered Conversations**: Powered by OpenAI's GPT models for dynamic responses.
- 🌐 **Web-Based Interface**: Built using Django, making it accessible via a web browser.
- 🔧 **Customizable**: Easily adjust conversation behavior, tone, and context.
- 📊 **Scalable**: Leverages Django's robustness for scaling with user demand.

---

## Prerequisites
1. An [OpenAI API Key](https://platform.openai.com/signup/).

---
## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/django-chatgpt-chatbot.git
cd django-chatgpt-chatbot
```

### 2. Set up a Virtual Environment
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
``` bash
API_KEY=<api_key>
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

