
from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', views.home, name = 'home'),

    path('about/', views.about, name = 'about'),

    path('academics/', views.academics, name = 'academics'),

    path('admission/', views.admission, name = 'admission'),

    path('contact/', views.contact_view, name = 'contact'),

    path('show/', views.show, name='show'),

    path('delete/<int:id>', views.delete),

    path('edit/<int:id>', views.edit),

    path('studentlife/', views.studentlife, name = 'studentlife'),

    path('facilities/', views.facilities, name = 'facilities'),
    
]
