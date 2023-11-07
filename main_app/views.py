from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
# from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Memory
# from .forms import FeedingForm
from django.contrib.auth.views import LoginView


class Home(LoginView):
  template_name = 'home.html'

class MemoryCreate(CreateView):
  model = Memory
  fields = ['name', 'title', 'details']
  success_url = '/memories/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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
def memory_index(request):
  memories = Memory.objects.filter(user=request.user)
  return render(request, 'memories/index.html', { 'memories': memories })

# @login_required
def memory_detail(request, memory_id):
  memory = Memory.objects.get(id=memory_id)
  return render(request, 'memories/detail.html', { 'memory': memory})

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