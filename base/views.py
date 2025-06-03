import os
# import fitz  # PyMuPDF
from docx import Document
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Article
from django.shortcuts import render, redirect
from .forms import ArticleForm

# Create your views here.

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

def ArticleView(request, pk):
    article = get_object_or_404(Article, id=pk)

    # Get file extension
    file_path = article.content_file.path
    file_path = article.content_file.path
    print("File path:", file_path)  # Check what path Django sees

    extension = os.path.splitext(file_path)[1].lower()

    extracted_text = "Content preview not available."


    try:
        if extension == '.pdf':
            extracted_text = extract_text_from_pdf(file_path)
        elif extension == '.docx':
            extracted_text = extract_text_from_docx(file_path)
    except Exception as e:
        extracted_text = f"Error reading file: {e}"

    return render(request, 'read.html', {
        'article': article,
        'article_text': extracted_text
    })




@login_required
def Home(request):

    articles = Article.objects.all()
    
    query = request.GET.get('q')
    query_category = ''

    if query_category:
        articles = Article.objects.filter(cartegory__icontains=query_category)
        
    if query:
        articles = Article.objects.filter(title__icontains=query)

    else:

        articles = Article.objects.all().order_by('-published_at')
        # form = ArticleForm()
    return render(request, 'all.html', {'articles': articles})


@login_required
def UserProfile(request):
    articles = Article.objects.all().order_by('-published_at')
    return render(request, 'profile.html', {'articles': articles})



@login_required
def createArticle(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
        else:
            articles = Article.objects.all().order_by('-published_at')
            return render(request, 'all.html', {'form': form, 'articles': articles, 'error': 'An error occurred'})
    return redirect('home')





def Signout(request):
    logout(request)
    return redirect('signin')




def Signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html', {'error':'Invalid credentials'})
    
    return render(request, 'login.html')




def Signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirm-password']

        if password == confirmpassword:

            user = User.objects.create_user(username=username, email=email, last_name=lastname, first_name=firstname, password=password)
            user.save()
            return redirect('signin')  # or auto-login
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
    return render(request, 'signup.html')