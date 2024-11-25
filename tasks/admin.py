# from django.contrib import admin
# from .models import Task, GoogleOAuthKey, Invitation
# from django.core.mail import send_mail
# from django.urls import reverse
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse

# # Register Task and GoogleOAuthKey models
# admin.site.register(Task)

# @admin.register(GoogleOAuthKey)
# class GoogleOAuthKeyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'value', 'created_at', 'updated_at')
#     search_fields = ('name',)

# # Custom Admin for Invitation
# @admin.register(Invitation)
# class InvitationAdmin(admin.ModelAdmin):
#     list_display = ('email', 'invited_by', 'created_at', 'is_used')
#     actions = ['send_invitation_email']  # Add a custom action

#     def send_invitation_email(self, request, queryset):
#         """
#         Send an email invitation to the selected email addresses.
#         """
#         for invitation in queryset:
#             if not invitation.is_used:  # Only send to unused invitations
#                 registration_url = request.build_absolute_uri(
#                     reverse('register_invitation', args=[invitation.id])
#                 )

#     # Send email
#                 send_mail(
#                     subject='You are invited to join our platform',
#                     message=f'Please register using this link: {registration_url}',
#                     from_email='admin@example.com',  # Replace with your admin email
#                     recipient_list=[invitation.email],
#                 )
                
#         self.message_user(request, "Invitation emails sent successfully.")
#     send_invitation_email.short_description = "Send invitation email to selected users"


from django.contrib import admin
from .models import Task, GoogleOAuthKey, Invitation
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.urls import reverse

# Register Task and GoogleOAuthKey models
admin.site.register(Task)

@admin.register(GoogleOAuthKey)
class GoogleOAuthKeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created_at', 'updated_at')
    search_fields = ('name',)

# Custom Admin for Invitation
@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'invited_by', 'created_at', 'is_used')
    actions = ['send_invitation_email']  # Add a custom action

    def send_invitation_email(self, request, queryset):
        """
        Send an email invitation to the selected email addresses.
        """
        for invitation in queryset:
            if not invitation.is_used:  # Only send to unused invitations
                registration_url = request.build_absolute_uri(
                    reverse('register_invitation', args=[invitation.id])
                )
                
                try:
                    # Send email
                    send_mail(
                        subject='You are invited to join our platform',
                        message=f'Please register using this link: {registration_url}',
                        from_email='ranialpana38@gmail.com',  # Replace with your admin email
                        recipient_list=[invitation.email],
                        fail_silently=False
                    )
                    self.message_user(request, f"Invitation email sent to {invitation.email} successfully.")
                except BadHeaderError:
                    self.message_user(request, f"Invalid header for {invitation.email}.")
                except Exception as e:
                    self.message_user(request, f"An error occurred while sending the email to {invitation.email}: {e}")
                
        self.message_user(request, "Invitation emails processed.")
    send_invitation_email.short_description = "Send invitation email to selected users"
