from django.shortcuts import render,get_object_or_404, redirect
from core.forms import CricketerForm, collect_img_Form, registration_Form
from django.contrib.auth import authenticate, login, logout
from core.models import Cricketer, collect_img
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q 
from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings


def home(request):
    query = request.GET.get('q', '')  # Get search query from URL
    min_age = request.GET.get('min_age', '')
    max_age = request.GET.get('max_age', '')
    country = request.GET.get('country', '')
    is_captain = request.GET.get('is_captain', '')

    # Start with all cricketers
    data = Cricketer.objects.all()

    # Apply name search if provided
    if query:
        data = data.filter(Q(name__icontains=query) | Q(country__icontains=query))

    # Filter by age range
    if min_age:
        data = data.filter(age__gte=min_age)
    if max_age:
        data = data.filter(age__lte=max_age)

    # Filter by country
    if country:
        data = data.filter(country__iexact=country)

    # Filter by captain status (checkbox)
    if is_captain:
        data = data.filter(is_captain=True)

    # Apply pagination: limit 5 items per page
    paginator = Paginator(data, 5)
    page = request.GET.get('page')
    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_data = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        paginated_data = paginator.page(paginator.num_pages)

    return render(request, 'models/home.html', {
        'data': paginated_data,
        'query': query,
        'min_age': min_age,
        'max_age': max_age,
        'country': country,
        'is_captain': is_captain,
    })

def one_player_data(request, id):
    # data = Cricketer.objects.get(pk=3)
    # data = Cricketer.objects.get(name='Virat Kohli')
    data = Cricketer.objects.get(id=id)
    return render(request, 'models/home.html', {'onePlayerData': data})

@login_required
def cricketer_create_view(request):  
    if request.method == 'POST':
        form = CricketerForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()  # Saves the form data to the database
            return redirect('home')  # Redirect to the cricketer list page
            print(form)
    else:
        form = CricketerForm()
    
    return render(request, 'models/cricketer_form.html', {'form':form})

@login_required
def update_cricketer(request, id):
    cricketer = get_object_or_404(Cricketer, id=id)

    if request.method == 'POST':
        form = CricketerForm(request.POST, instance=cricketer)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CricketerForm(instance=cricketer)
    
    cache.clear() 
    return render(request, 'models/update_cricketer.html', {'form':form})

@login_required
def del_cricketer(request, id):
    queryset = Cricketer.objects.get(id=id)
    queryset.delete()
    return redirect('home')

@login_required
def upload_file(request):
    if request.method == 'POST':
        print(request.POST)  
        form = collect_img_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Saves the form data to the database
            return redirect('galary')
    else:
        form = collect_img_Form()
        return render(request, 'models/upload.html',{'form':form})

    cache.clear() 

    return render(request, 'models/upload.html',{'form':form})

def galary(request):
    data = collect_img.objects.all()
    print(data)
    
    return render(request, 'models/collection.html', {'data': data})

def login_view(request):
    print(request)

    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else:
            print("Form is invalid!")
    else:
        print("Rendering login page...")
        form = AuthenticationForm()

    cache.clear() 

    return render(request, 'models/login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    if request.method == 'POST':
        form = registration_Form(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return redirect('home')
    else:
        form = registration_Form()
        print('hi')

    cache.clear()

    return render(request, 'models/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('loginform') 

@login_required
def send_email(request):
    # send_email_to_client()
    subject = "this email is from django server with attchment."
    message = "this is our test message from django server to send attachment to other emails."
    recipent_list = ["ADD RECIPIENT EMAIL FROM"]
    file_path = f"{settings.MEDIA_ROOT}/files/sample-1.pdf"
    send_email_with_attachment(subject,message,recipent_list,file_path)
    return redirect('/')

@login_required
def clear_cache(request):
    cache.clear()
    return redirect(request.META.get('HTTP_REFERER', '/'))