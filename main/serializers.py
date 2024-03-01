from rest_framework import serializers
from users.serializers import CohortSerializer, UserSerializer


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()


class ClassScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    start_date_and_time = serializers.DateTimeField()
    end_date_and_time = serializers.DateTimeField()
    repeat_frequency = serializers.CharField()
    meeting_type = serializers.CharField()
    organizer = UserSerializer(many=True)
    cohort = CohortSerializer(many=False)
    course = CourseSerializer(many=False)
    facilitator = UserSerializer()
    venue = serializers.CharField()
    date_created = serializers
