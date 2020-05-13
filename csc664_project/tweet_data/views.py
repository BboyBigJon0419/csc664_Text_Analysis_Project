from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'tweet_data/index.html')

def twitter(request):
    return render(request, 'tweet_data/twitter.html')

def about(request):
    return render(request, 'tweet_data/about.html')

# File Structure on how it renders:
# tweet_data --> templates --> tweet_data --> .html 