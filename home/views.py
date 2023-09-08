from django.shortcuts import render
import json
from django.core.paginator import Paginator

def home(request):
    with open('data/model_info.json', 'r') as json_file:
        profiles_data = json.load(json_file)
    paginator = Paginator(profiles_data, 24)

    page_number = request.GET.get('page')

    page = paginator.get_page(page_number)
    context = {
        'profiles_data': page,
    }
    return render(request, 'home/home.html', context)

def profile_detail(request, username):
    with open('data/model_info.json', 'r') as json_file:
        profiles_data = json.load(json_file)

    profile = None
    for data in profiles_data:
        if data['cleaned_username'] == username:
            profile = data
            break
    context = {
        'profile': profile,
    }

    return render(request, 'home/profile_detail.html', context)

def search_results(request):
    query = request.GET.get('q', '')

    with open('data/model_info.json', 'r') as json_file:
        profiles_data = json.load(json_file)
    
    search_results = []
    for profile in profiles_data:
        if query.lower() in profile['username'].lower():
            search_results.append(profile)

    paginator = Paginator(search_results, 12)

    page_number = request.GET.get('page')

    page = paginator.get_page(page_number)
    context = {
        'query': query,
        'search_results': page,
    }

    return render(request, 'home/search_results.html', context)