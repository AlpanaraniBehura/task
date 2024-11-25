from django.db import models
from django.contrib.auth.models import User

class GoogleOAuthKey(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Client ID" or "Client Secret"
    value = models.TextField()  # Store the key value
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link task to a user
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Invitation(models.Model):
    email = models.EmailField(unique=True)  # Email of the invited user
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invitations')  # Admin who sent the invite
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)  # Mark if the invitation was used

    def __str__(self):
        return f"Invitation to {self.email}"
