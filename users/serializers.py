from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()

class CohortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    year = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    author = UserSerializer(many=False) # To indicate the relationship many to 1, we use "many=False". In this case we expect to get an object and not a list of author

class CohortMemberSerializer(serializers.Serializer):
    
    # There is a special thing we can do here: do we need to have the Cohort inside the Cohort Member? The answer is No.
    # cohort = CohortSerializer(many=True)
    member = UserSerializer(many=False)
    
    # Do you need each Cohort to 

