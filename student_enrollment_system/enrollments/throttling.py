from rest_framework.throttling import UserRateThrottle

class AdminRateThrottle(UserRateThrottle):
    rate = '1000/day'

class StudentRateThrottle(UserRateThrottle):
    rate = '100/day'