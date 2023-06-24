from allauth.account.forms import SignupForm


# class PendingAprrovalForm(SignupForm):
#     # To approve user in the admin panel
#     approval_status = forms.BooleanField(required=False)


# class CustomSignupForm(SignupForm):
#     def save(self, request)
#     user = super().save(request)
#     user.is_active = False
#     user.approval_status = self.cleaned_data['approval_status']
#     user.save()
#     return user
