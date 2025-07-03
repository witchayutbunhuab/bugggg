from django.urls import path

from myapp.views import data, home, info, pdf

# route
urlpatterns = [
    path('', home),
    path('students', students),
    path('info', info),
    path('data', data),
    path('pdf', pdf),
]
# winget install httpie