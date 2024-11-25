"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import redirect

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('allauth.urls')),  # Google Login
#     path('tasks/', include('tasks.urls')),      # Your tasks app
#     path('', lambda request: redirect('task-list')),  # Redirect root URL to the task list
# ]


# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import redirect

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('allauth.urls')),  # Django Allauth URLs
#     path('tasks/', include('tasks.urls')), # Your app URLs
#     path('', lambda request: redirect('tasks/')), 
     
# ]
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from tasks import views  # Import views from the tasks app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Django Allauth URLs
    path('tasks/', include('tasks.urls')),  # Your app URLs


    #path('send-invite/', views.send_invitation, name='send_invite'),
    # path('register/<int:invitation_id>/', views.register_invitation, name='register_invitation'),

    path('', lambda request: redirect('tasks/')),  # Redirect to tasks page by default
]
