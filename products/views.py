from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shelter
from django.utils import timezone

def home(request):
    shelter = Shelter.objects
    return render(request, 'products/home.html', {'shelter':shelter})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            shelter = Shelter()
            shelter.title = request.POST['title']
            shelter.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                shelter.url = request.POST['url']
            else:
                shelter.url = 'http://' + request.POST['url']
            shelter.icon = request.FILES['icon']
            shelter.image = request.FILES['image']
            shelter.pub_date = timezone.datetime.now()
            shelter.builder = request.user
            shelter.save()
            return redirect ('/products/' + str(shelter.id))
        else:
            return render(request, 'products/create.html', {'error':'All fields are required'})
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Shelter, pk=product_id)
    return render(request, 'products/detail.html', {'shelter':product})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        shelter = get_object_or_404(Shelter, pk=product_id)
        shelter.votes_total += 1
        shelter.save()
        return redirect ('/products/' + str(shelter.id))