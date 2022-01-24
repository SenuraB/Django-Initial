from django.urls import path
from . import views

# URLConf
# urlpatterns special variables
urlpatterns = [
    # always end routes with /
    path('hello/', views.sayHello)
]