from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def news_portal_view(request):
    # Fetch the API data
    api_url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-08-27&sortBy=publishedAt&apiKey=164bfd6f2217443a80395da07ad74e52'  # Replace with actual API URL
    response = requests.get(api_url)
    data = response.json()  # Parsing the JSON response
    
    # Extract the articles from the JSON response
    articles = data.get("articles", [])
    
    # Pass the articles to the template
    return render(request, 'news_portal.html', {'articles': articles})
