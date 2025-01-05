from django.shortcuts import render, redirect
from django.contrib import messages
import openai
import os
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from dotenv import load_dotenv
from .models import Code
load_dotenv('/Users/amanthakur/chatgpt-coder/codebot/codebot/.env')
API_KEY = os.environ.get("API_KEY")

# Create your views here.
def home(request):
    lang_list = ['aspnet', 'c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'docker', 'git', 'go', 'graphql', 'java', 'javascript', 'html', 'markup-templating', 'mongodb', 'php', 'plsql', 'python', 'ruby', 'rust', 'sql', 'typescript']
    if request.method =="POST":
        code = request.POST.get("code")
        lang = request.POST.get("lang")
        if lang == "Select any Programming Language":
            messages.success(request, "Hey, you forgot to pick any Programming Language!")
            return  render(request, 'home.html', {'languages': lang_list, 'code': code, 'lang': lang})
        openai.api_key = API_KEY
        openai.Model.list() # creates openai instance
        try:
            response = openai.Completion.create(
                engine = 'davinci-002',
                prompt = f'Respond only with code. Fix this {lang} code: {code}',
                temperature=0,
                max_tokens=1000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            response = (response["choices"][0]["text"]).strip()
            #save to database
            record = Code(user=request.user, question=code, answer=response, language=lang)
            record.save()
            return render(request, 'home.html', {'languages': lang_list, 'response': response, 'lang': lang})
        except Exception as e:
            return render(request, 'home.html', {'languages': lang_list, 'code': e, 'lang': lang})
    return render(request, 'home.html', {'languages': lang_list})

def suggest(request):
    lang_list = ['aspnet', 'c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'docker', 'git', 'go', 'graphql', 'java', 'javascript', 'html', 'markup-templating', 'mongodb', 'php', 'plsql', 'python', 'ruby', 'rust', 'sql', 'typescript']
    if request.method =="POST":
        code = request.POST.get("code")
        lang = request.POST.get("lang")
        if lang == "Select any Programming Language":
            messages.success(request, "Hey, you forgot to pick any Programming Language!")
            return  render(request, 'suggest.html', {'languages': lang_list, 'code': code, 'lang': lang})
        openai.api_key = API_KEY
        openai.Model.list() # creates openai instance
        try:
            response = openai.Completion.create(
                engine = 'davinci-002',
                prompt = f'Respond only with code. Fix this {lang} code: {code}',
                temperature=0,
                max_tokens=1000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            response = (response["choices"][0]["text"]).strip()
            #save to database
            record = Code(user=request.user, question=code, answer=response, language=lang)
            record.save()
            return render(request, 'suggest.html', {'languages': lang_list, 'response': response, 'lang': lang})
        except Exception as e:
            return render(request, 'suggest.html', {'languages': lang_list, 'code': e, 'lang': lang})
    return render(request, 'suggest.html', {'languages': lang_list})


def login_user(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in Successfully!")
            return redirect('home')
        else:
            messages.success(request, "Error Logging In")
            return redirect('home')
    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out!")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have Registered Successfully!")
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {"form": form})


def history(request):
    if request.user.is_authenticated:
        code = Code.objects.filter(user_id=request.user.id)
        return render(request, 'history.html', {'code': code})
    else:
        messages.success(request, "You Must be logged in to View History!")
        return redirect('home')

def delete_history(request, history_id):
    try:
        history = Code.objects.get(pk=history_id)
        history.delete()
        messages.success(request, "History Deleted Successfully!")
    except Code.DoesNotExist:
        messages.success(request, "Matching History Not Found!")
    except Exception as e:
        messages.success(request, f"Error: {e}")
    return redirect('history')
    