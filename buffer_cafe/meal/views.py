from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import requests

def fetch_data_from_url(url):
    try:
        response = requests.get(url)
      
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON content from the response
            data = response.json()
            return data
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def home(request):
    json_url = "https://raw.githubusercontent.com/abdullahallnaim/batch3-week3-assignment3/main/meal.json"

    # Fetch data from the URL
    meal_data = fetch_data_from_url(json_url)

    # Check if data was successfully fetched
    if meal_data is not None:

        return render(request, 'base.html', context={'data': 'meal_data'})
    else:
        print("Failed to fetch data.")
        return render(request, 'base.html', context={'data': 'meal_data'})
