
from django .urls import path

from schoolapp import views
app_name='schoolapp'
urlpatterns = [
    path('',views.department,name='department'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('form/',views.form,name='form'),


]
