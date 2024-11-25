# from django.urls import path
# from . import views
# from .views import register_invitation

# urlpatterns = [
#     path('', views.task_list, name='task-list'),       # List tasks
#     path('create/', views.task_create, name='task-create'),  # Create task
#     path('<int:pk>/update/', views.task_update, name='task-update'),  # Update task
#     path('<int:pk>/delete/', views.task_delete, name='task-delete'),  # Delete task
#     path('register/<int:invitation_id>/', register_invitation, name='register_invitation'),
    
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.task_list, name='task-list'),  # List tasks
#     path('create/', views.task_create, name='task-create'),  # Create task
#     path('<int:pk>/update/', views.task_update, name='task-update'),  # Update task
#     path('<int:pk>/delete/', views.task_delete, name='task-delete'),  # Delete task
#     path('register/<int:invitation_id>/', views.register_invitation, name='register_invitation'),
#     path('send-invitation/', views.send_invitation, name='send-invitation'),  
#   # Registration via invitation
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('send-invitation/', views.send_invitation, name='send-invitation'),
#     path('register/<int:invitation_id>/', views.register_invitation, name='register_invitation'),
#     path('', views.task_list, name='task-list'),
#     path('create/', views.task_create, name='task-create'),
#     path('update/<int:pk>/', views.task_update, name='task-update'),
#     path('delete/<int:pk>/', views.task_delete, name='task-delete'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('update/<int:pk>/', views.task_update, name='task-update'),
    path('delete/<int:pk>/', views.task_delete, name='task-delete'),
    path('register/<int:invitation_id>/', views.register_invitation, name='register_invitation'),
]


