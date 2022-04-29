from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import SignupForm






class Register(CreateView):
    template_name = 'register.html'
    form_class = SignupForm
    success_url = reverse_lazy('/')
