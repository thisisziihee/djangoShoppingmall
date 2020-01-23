from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm
from .models import Users
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, 'home.html', {'user' : request.session.get('user')})

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'
    
    def form_valid(self, form):
        user = Users(
            email = form.data.get('email'),
            password = make_password(form.data.get('password')),
            level = 'user'
        )
        user.save()

        return super().form_valid(form)