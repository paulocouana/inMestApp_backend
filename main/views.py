from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.

def say_hello(request):
    return HttpResponse("<h1>Hello Paulo</h1>")

# Write a View Function named user_profile. The View Function should return a JsonResponse. 
# The JsonResponse data should include:
# name: your name, email: your email, phone_number: your phone number
# And register the View Function on the path called profile

def user_profile(request):
    user_details = {
        "Name": "Paulo",
        "E-mail": "paulo.ouana@meltwater.org",
        "Phone number": "+27 (079) 410 6235"
    }

    return JsonResponse(user_details)
    # The JsonResponse can also be returned like the code below:
    # return JsonResponse({"Name": "Paulo", "E-mail": "paulo.ouana@meltwarer.org", "Phone number": "+27 (079) 410 6235"})


# 1. Write a View Simple Function called filter_queries
# 1.a. The view function should receive query_id through the url
# 1.b. Return a JsonResponse data with the following data: id, title, description, status, and submitted_by
# 1.c. The id should be the id received through the url

def filter_queries(request, query_id):
    query = {
        "id": query_id,
        "title": "Get to know Paulo Ouana",
        "description": "Paulo, the 1st Mozambican in MEST AFRICA",
        "status": "ACCEPTED",
        "submitted_by": "Owusua"
    }
    return JsonResponse(query)

class QueryView(View):
    queries = [
        {"id": 1, "title": "Adama declined Val shots"},
        {"id": 2, "title": "Samsom accepted Val shots"}
    ]

    # In Python we need to pass the context of the class in a function - for that we use the "self" keyword
    # Because the first argument is the context of the class and the second argument is the request, and any other thing we want
    # Anytime we are writing a View function inside a class in Python we need to bring the argument "self"

    def get(self, request):
        return JsonResponse({"result": self.queries})
    
    #We use POST to do user request data
    def post(self, request):
        return JsonResponse({"status": "Ok"})