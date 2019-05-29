from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model, login
from django.views.generic.edit import CreateView
from .forms import UserForm


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class UserCreate(CreateView):
    model = get_user_model()
    template_name = 'signup.html'
    form_class = UserForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('home')
