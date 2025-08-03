from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
import csv
import json
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Preference



# Create your views here.
def landing(requests):
    #return HttpResponse("HELLO WORLD")
    return render(requests,'landing.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(username = username).exists():
            messages.error(request,"username already taken")
            return redirect("signup")
        if User.objects.filter(email = email).exists():
            messages.error(request,"email is already signup")
            return redirect("signup")
        user = User.objects.create_user(username = username, email = email, password = password)
        user.save()
        messages.success(request,"account created successfully!")
        return redirect("signin")
    return render(request,"signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request,"Login successfull!!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('signin')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request,"logout successfull")
    return redirect('signin')

def home(request):
    deals = []  # your deal scraping logic
    preference_message = None

    if request.method == 'POST':
        category = request.POST.get('category')
        Preference.objects.update_or_create(user=request.user, defaults={'category': category})
        preference_message = f"We'll notify you when there's an offer on {category}s."

    return render(request, 'home.html', {
        'deals': deals,
        'preference_message': preference_message,
    })

from django.http import JsonResponse
import json

def set_preference(request):
    if request.method == 'POST' and request.user.is_authenticated:
        # For JSON requests, parse JSON body if sent as JSON
        try:
            data = json.loads(request.body)
            category = data.get('category')
        except json.JSONDecodeError:
            category = request.POST.get('category')

        if category:
            Preference.objects.update_or_create(user=request.user, defaults={'category': category})
            return JsonResponse({'message': f"We'll notify you when there's an offer on {category}s."})
        else:
            return JsonResponse({'message': 'Category is required!'}, status=400)
    return JsonResponse({'message': 'Invalid request'}, status=400)






#FLIPKART
def flipkart(request):
    return render(request, 'flipkart.html')

#F_WOMENS
def flipkartwomen(request):
    folder_path = os.path.join(settings.BASE_DIR, 'app', 'flipkart_csv')
    grouped_offers = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract middle part of filename (flipkart_dresses.csv -> dresses)
            parts = filename.split('_')
            if len(parts) > 1:
                category = parts[1].replace('.csv', '')
            else:
                category = filename.replace('.csv', '')

            offers = []
            with open(os.path.join(folder_path, filename), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    offers.append({
                        'product_link': row.get('Product Link', ''),
                        'product_name': row.get('Product Name', ''),
                        'image_url': row.get('Image URL', ''),
                        'price': row.get('Price', ''),
                        'original_price': row.get('Original Price', ''),
                        'discount': row.get('Discount', ''),
                    })

            grouped_offers[category] = offers

    return render(request, 'flipkart.html', {'grouped_offers': grouped_offers})

#F_SPORTS
def flipkartsports(request):
    folder_path = os.path.join(settings.BASE_DIR, 'app', 'flipkart_sports')
    grouped_offers = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract middle part of filename (flipkart_dresses.csv -> dresses)
            parts = filename.split('_')
            if len(parts) > 1:
                category = parts[1].replace('.csv', '')
            else:
                category = filename.replace('.csv', '')

            offers = []
            with open(os.path.join(folder_path, filename), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    offers.append({
                        'product_link': row.get('Product Link', ''),
                        'product_name': row.get('Product Name', ''),
                        'image_url': row.get('Image URL', ''),
                        'price': row.get('Price', ''),
                        'original_price': row.get('Original Price', ''),
                        'discount': row.get('Discount', ''),
                    })

            grouped_offers[category] = offers

    return render(request, 'flipkart.html', {'grouped_offers': grouped_offers})

#F_MENS
def flipkartmens(request):
    folder_path = os.path.join(settings.BASE_DIR, 'app', 'flipkart_mens')
    grouped_offers = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract middle part of filename (flipkart_dresses.csv -> dresses)
            parts = filename.split('_')
            if len(parts) > 1:
                category = parts[1].replace('.csv', '')
            else:
                category = filename.replace('.csv', '')

            offers = []
            with open(os.path.join(folder_path, filename), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    offers.append({
                        'product_link': row.get('Product Link', ''),
                        'product_name': row.get('Product Name', ''),
                        'image_url': row.get('Image URL', ''),
                        'price': row.get('Price', ''),
                        'original_price': row.get('Original Price', ''),
                        'discount': row.get('Discount', ''),
                    })

            grouped_offers[category] = offers

    return render(request, 'flipkart.html', {'grouped_offers': grouped_offers})

#F_HOME
def flipkarthome(request):
    folder_path = os.path.join(settings.BASE_DIR, 'app', 'flipkart_home')
    grouped_offers = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract middle part of filename (flipkart_dresses.csv -> dresses)
            parts = filename.split('_')
            if len(parts) > 1:
                category = parts[1].replace('.csv', '')
            else:
                category = filename.replace('.csv', '')

            offers = []
            with open(os.path.join(folder_path, filename), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    offers.append({
                        'product_link': row.get('Product Link', ''),
                        'product_name': row.get('Product Name', ''),
                        'image_url': row.get('Image URL', ''),
                        'price': row.get('Price', ''),
                        'original_price': row.get('Original Price', ''),
                        'discount': row.get('Discount', ''),
                    })

            grouped_offers[category] = offers

    return render(request, 'flipkart.html', {'grouped_offers': grouped_offers})

#F_ELEC
def flipkartelec(request):
    folder_path = os.path.join(settings.BASE_DIR, 'app', 'flipkart_elec')
    grouped_offers = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract middle part of filename (flipkart_dresses.csv -> dresses)
            parts = filename.split('_')
            if len(parts) > 1:
                category = parts[1].replace('.csv', '')
            else:
                category = filename.replace('.csv', '')

            offers = []
            with open(os.path.join(folder_path, filename), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    offers.append({
                        'product_link': row.get('Product Link', ''),
                        'product_name': row.get('Product Name', ''),
                        'image_url': row.get('Image URL', ''),
                        'price': row.get('Price', ''),
                        'original_price': row.get('Original Price', ''),
                        'discount': row.get('Discount', ''),
                    })

            grouped_offers[category] = offers

    return render(request, 'flipkart.html', {'grouped_offers': grouped_offers})



#AMAZON
def amazon(request):
    return render(request, 'amazon.html')

#A_WOMEN
def amazonwomen(request):

    folder_path = os.path.join(settings.BASE_DIR, 'app', 'amazon_women')
    grouped_offers = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract middle part of filename (flipkart_dresses.csv -> dresses)
            parts = filename.split('_')
            if len(parts) > 1:
                category = parts[1].replace('.csv', '')
            else:
                category = filename.replace('.csv', '')

            offers = []
            with open(os.path.join(folder_path, filename), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    offers.append({
                        'product_link': row.get('Product Link', ''),
                        'product_name': row.get('Product Name', ''),
                        'image_url': row.get('Image URL', ''),
                        'price': row.get('Price', ''),
                        'original_price': row.get('Original Price', ''),
                        'discount': row.get('Discount', ''),
                    })

            grouped_offers[category] = offers

    return render(request, 'amazon.html', {'grouped_offers': grouped_offers})

#A_MENS
def amazonmens(request):
    folder_path = os.path.join(settings.BASE_DIR, 'app', 'amazon_men')
    grouped_offers = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract middle part of filename (flipkart_dresses.csv -> dresses)
            parts = filename.split('_')
            if len(parts) > 1:
                category = parts[1].replace('.csv', '')
            else:
                category = filename.replace('.csv', '')

            offers = []
            with open(os.path.join(folder_path, filename), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    offers.append({
                        'product_link': row.get('Product Link', ''),
                        'product_name': row.get('Product Name', ''),
                        'image_url': row.get('Image URL', ''),
                        'price': row.get('Price', ''),
                        'original_price': row.get('Original Price', ''),
                        'discount': row.get('Discount', ''),
                    })

            grouped_offers[category] = offers

    return render(request, 'amazon.html', {'grouped_offers': grouped_offers})

#A_SPORTS
def amazonsports(request):
    folder_path = os.path.join(settings.BASE_DIR, 'app', 'amazon_sports')
    grouped_offers = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract middle part of filename (flipkart_dresses.csv -> dresses)
            parts = filename.split('_')
            if len(parts) > 1:
                category = parts[1].replace('.csv', '')
            else:
                category = filename.replace('.csv', '')

            offers = []
            with open(os.path.join(folder_path, filename), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    offers.append({
                        'product_link': row.get('Product Link', ''),
                        'product_name': row.get('Product Name', ''),
                        'image_url': row.get('Image URL', ''),
                        'price': row.get('Price', ''),
                        'original_price': row.get('Original Price', ''),
                        'discount': row.get('Discount', ''),
                    })

            grouped_offers[category] = offers

    return render(request, 'amazon.html', {'grouped_offers': grouped_offers})

#A_HOME
def amazonhome(request):
    
    folder_path = os.path.join(settings.BASE_DIR, 'app', 'amazon_home')
    grouped_offers = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract middle part of filename (flipkart_dresses.csv -> dresses)
            parts = filename.split('_')
            if len(parts) > 1:
                category = parts[1].replace('.csv', '')
            else:
                category = filename.replace('.csv', '')

            offers = []
            with open(os.path.join(folder_path, filename), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    offers.append({
                        'product_link': row.get('Product Link', ''),
                        'product_name': row.get('Product Name', ''),
                        'image_url': row.get('Image URL', ''),
                        'price': row.get('Price', ''),
                        'original_price': row.get('Original Price', ''),
                        'discount': row.get('Discount', ''),
                    })

            grouped_offers[category] = offers

    return render(request, 'amazon.html', {'grouped_offers': grouped_offers})

#A_ELEC
def amazonelec(request):
    folder_path = os.path.join(settings.BASE_DIR, 'app', 'amazon_elec')
    grouped_offers = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract middle part of filename (flipkart_dresses.csv -> dresses)
            parts = filename.split('_')
            if len(parts) > 1:
                category = parts[1].replace('.csv', '')
            else:
                category = filename.replace('.csv', '')

            offers = []
            with open(os.path.join(folder_path, filename), newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    offers.append({
                        'product_link': row.get('Product Link', ''),
                        'product_name': row.get('Product Name', ''),
                        'image_url': row.get('Image URL', ''),
                        'price': row.get('Price', ''),
                        'original_price': row.get('Original Price', ''),
                        'discount': row.get('Discount', ''),
                    })

            grouped_offers[category] = offers

    return render(request, 'amazon.html', {'grouped_offers': grouped_offers})

@csrf_exempt  # For simplicity; better to use CSRF tokens in production
def wishlist_action(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_name = data.get('product_name')
        product_link = data.get('product_link')
        image_url = data.get('image_url')
        price = data.get('price')
        original_price = data.get('original_price')
        discount = data.get('discount')

        if 'wishlist' not in request.session:
            request.session['wishlist'] = []

        wishlist = request.session['wishlist']

        # Check if product already in wishlist by product_link (unique)
        exists = any(item['product_link'] == product_link for item in wishlist)

        action = data.get('action')

        if action == 'add':
            if not exists:
                wishlist.append({
                    'product_name': product_name,
                    'product_link': product_link,
                    'image_url': image_url,
                    'price': price,
                    'original_price': original_price,
                    'discount': discount
                })
                request.session.modified = True
                return JsonResponse({'status': 'added'})
            else:
                return JsonResponse({'status': 'exists'})
        elif action == 'remove':
            new_wishlist = [item for item in wishlist if item['product_link'] != product_link]
            request.session['wishlist'] = new_wishlist
            request.session.modified = True
            return JsonResponse({'status': 'removed'})
        else:
            return JsonResponse({'status': 'unknown_action'}, status=400)

    return JsonResponse({'status': 'invalid_method'}, status=405)

def wishlist_view(request):

    wishlist = request.session.get('wishlist', [])
    context = {'wishlist': wishlist}
    return render(request, 'wishlist.html', context)

