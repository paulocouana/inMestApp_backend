from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from main.models import *
from main.serializers import *
import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


    @api_view(["GET"])
    def fetch_cohorts(request):
        # 1. Retrieve from db all fetch actions:
        queryset = ClassSchedule.objects.all()

        # 2. Return queryset result as response
        # 2b. Transform/serialize the queryset result to json and send as response

        # 3. Respond to request 
        serializer = ClassScheduleSerializer(queryset, many=True)
        return Response({"data":serializer.data}, status.HTTP_200_OK)


    @api_view(["POST"])
    def create_class_schedule(request):
        title = request.data.get("title")
        description = request.data.get("description")
        start_date_and_time = request.data.get("start_date_and_time")
        end_date_and_time = request.data.get("end_date_and_time")
        cohort_id = request.data.get("cohort_id")
        venue = request.data.get("venue")
        facilitator_id = request.data.get("facilitator_id")
        is_repeated = request.data.get("is_repeated")
        repeat_frequency = request.data.get("repeat_frequency")
        course_id = request.data.get("course_id")
        meeting_type = request.data.get("meeting_type")

        if not title:
            return Response({"message":"My friend, send me te title"}, status.HTTP_400_BAD_REQUEST)

    
        cohort = None
        facilitator = None
        course = None

        # Validating the existence of records
        try:
            cohort = Cohort.objects.get(id=cohort_id)
        except Cohort.DoesNotExist:
            return Response({"message":"Attention, this Cohort does not exist"}, status.HTTP_400_BAD_REQUEST)
        
        try:
            facilitator = IMUser.objects.get(id=facilitator_id)
        except IMUser.DoesNotExist:
            return Response({"message":"Attention, this Facilitator does not exist"}, status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"message":"Attention, this Course does not exist"}, status.HTTP_400_BAD_REQUEST)
        
        # creating class schedule
        class_schedule = ClassSchedule.objects.create(
            title=title,
            description=description,
            venue=venue,
            is_repeated=is_repeated,
            repeat_frequency=repeat_frequency,
            facilitator=facilitator,
            start_date_and_time=datetime.datetime.now(),
            end_date_and_time=datetime.datetime.now(),
            cohort=cohort,
            course=course,
            organizer=facilitator
        )
        class_schedule.save()

        serializer = ClassScheduleSerializer(class_schedule, many=False)
        return Response({"message": "Schedule successfully created", "data": serializer.data}, status.HTTP_201_CREATED)

    # In Python we need to pass the context of the class in a function - for that we use the "self" keyword
    # Because the first argument is the context of the class and the second argument is the request, and any other thing we want
    # Anytime we are writing a View function inside a class in Python we need to bring the argument "self"

    def get(self, request):
        return JsonResponse({"result": self.queries})
    
    #We use POST to do user request data
    def post(self, request):
        return JsonResponse({"status": "Ok"})