from rest_framework import serializers
from .models import Student, Course, Enrollment
from datetime import date

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for Student model
    It serializes all the fields of the Student Model.
    """
    class Meta:
        model = Student
        fields = '__all__'
    def validate(self, data):
        """
        Validates the date of birth of the post or put request to check it should not be a date of the future
        """
        if 'date_of_birth' in data and data['date_of_birth'] > date.today():
            raise serializers.ValidationError({ 'date_of_birth': "Date of birth cannot be in the future."})
        return data
class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course model
    It serializes all the fields of the Course Model.
    """
    class Meta:
        model = Course
        fields = '__all__'
    def validate(self, data):
        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError("End date cannot be before start date.")
        return data

class EnrollmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Enrollment model
    It serializes all the fields of the Enrollment Model.
    """
    class Meta:
        model = Enrollment
        fields = '__all__'
   