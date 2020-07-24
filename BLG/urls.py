from django.urls import path
from BLG import views

urlpatterns = [
    path('blogs/', views.blogs, name="blogs"),
    path('addblogs/',views.add_blog,name="addblogs")
]
