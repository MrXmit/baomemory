from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
# from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required 
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import Finch
# from .forms import FeedingForm
from django.contrib.auth.views import LoginView


class Home(LoginView):
  template_name = 'home.html'

# class FinchCreate(CreateView):
#   model = Finch
#   fields = ['name', 'breed', 'description', 'age']
#   success_url = '/finches/'

#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)

# class FinchUpdate(UpdateView):
#   model = Finch
#   fields = ['breed', 'description', 'age']

# class FinchDelete(DeleteView):
#   model = Finch
#   success_url = '/finches/' 

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# @login_required
# def finch_index(request):
#   finches = Finch.objects.filter(user=request.user)
#   return render(request, 'finches/index.html', { 'finches': finches })

# @login_required
# def finch_detail(request, finch_id):
#   finch = Finch.objects.get(id=finch_id)
#   toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
#   feeding_form = FeedingForm()
#   return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('finch-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)