from rest_framework.response import Response
from .backup import backup_database
from .throttling import AdminRateThrottle, StudentRateThrottle
from .tasks import send_welcome_email
from rest_framework import viewsets,status,generics
from .models import Student, Course, Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer
import threading

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited
    Inhertied from ModelViewSet which provides our view with all the actions like, GET, PUT, POST, DELETE
    """
    queryset = Student.objects.all()
    throttle_classes = [StudentRateThrottle, AdminRateThrottle]
    serializer_class = StudentSerializer
    def create(self, request):
        """
        Overrides the create method of ModelViewSet to add custom logic like backup database thread and send welcome email
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            send_welcome_email.delay(student.id)      #adds our task to RabbitMQ queue
            backup_thread = threading.Thread(target =backup_database)
            backup_thread.start()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited
    Inhertied from ModelViewSet which provides our view with all the actions like, GET, PUT, POST, DELETE
    """
    queryset = Course.objects.all()
    throttle_classes = [StudentRateThrottle, AdminRateThrottle]
    serializer_class = CourseSerializer

class EnrollmentListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows enrol;ments to be viewed or created
    Inhertied from generic ListCreateAPIView which provides our view with actions like, GET and POST
    Not using ModelViewSet here as only two actions are needed as per requirement
    """
    queryset = Enrollment.objects.all()
    throttle_classes = [StudentRateThrottle, AdminRateThrottle]
    serializer_class = EnrollmentSerializer