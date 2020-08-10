from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
        
         path('account/', views.account, name = "account"),
         path('home/', views.home, name = "home"),
]