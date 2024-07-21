from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, EnrollmentListCreateView

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('', include(router.urls)),
]