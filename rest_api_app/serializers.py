from rest_framework import serializers 
from rest_api_app.models import Student

#Serailizers 
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name'
                    , 'email', 'birth_date']
