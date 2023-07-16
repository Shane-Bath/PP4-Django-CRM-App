from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return "dashboard"

    def get_login_template_names(self):
        return ['account/login.html']
