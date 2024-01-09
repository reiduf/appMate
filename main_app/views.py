from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Connection, Job, Todo, Status, Interaction
from .forms import TodoForm, StatusForm, JobForm, InteractionForm, ConnectionForm


# Create your views here.
def home(request):
  jobs = Job.objects.filter(user = request.user)
  todos = Todo.objects.all()
  return render(request, 'home.html', {
    'jobs': jobs, 
    'todos': todos,
    })


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


@login_required
def jobs_index(request):
  jobs = Job.objects.filter(user = request.user)
  num_p = Job.objects.filter(progress = 'P').count()
  num_i = Job.objects.filter(progress = 'I').count()
  num_o = Job.objects.filter(progress = 'O').count()
  num_r = Job.objects.filter(progress = 'R').count()
  num_bookmarked = Job.objects.filter(bookmarked = True).count()

  results = None
  if request.GET.get('search_query'):
    query = request.GET.get('search_query')
    results = Job.objects.filter(company=query)

  return render(request, 'jobs/index.html', {
    'jobs' : jobs,
    'num_p' : num_p,
    'num_i' : num_i,
    'num_o' : num_o,
    'num_r' : num_r,
    'num_bookmarked' : num_bookmarked,
    'results': results,
  })




@login_required
def jobs_detail(request, job_id):
  job = Job.objects.get(id = job_id)
  todos = Todo.objects.filter(job = job_id)
  statuss = Status.objects.filter(job = job_id)
  todo_form = TodoForm()
  status_form = StatusForm()
  return render(request, 'jobs/detail.html', {
    'job' : job,
    'todos': todos,
    'statuss' : statuss,
    'todo_form': todo_form,
    'status_form': status_form
  })


class JobCreate(LoginRequiredMixin, CreateView):
  model = Job
  form_class = JobForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  

class JobUpdate(LoginRequiredMixin, UpdateView):
  model = Job
  form_class = JobForm
  

class JobDelete(LoginRequiredMixin, DeleteView):
  model = Job
  success_url = '/jobs'


@login_required
def add_todo(request, job_id):
  form = TodoForm(request.POST)
  if form.is_valid():
    new_todo = form.save(commit=False)
    # below could be an issue
    new_todo.job_id = job_id
    new_todo.save()
  return redirect('detail', job_id=job_id)


@login_required
def update_todo(request, job_id, todo_id):
  todo = Todo.objects.get(id = todo_id)
  if todo.done == False:
    todo.done = True
  else:
    todo.done = False
  todo.save()
  return redirect('detail', job_id=job_id)

@login_required
def delete_todo(request, job_id, todo_id):
  todo = Todo.objects.get(id = todo_id)
  todo.delete()
  return redirect('detail', job_id=job_id)


@login_required
def add_status(request, job_id):
  form = StatusForm(request.POST)
  if form.is_valid():
    new_status = form.save(commit=False)
    new_status.job_id = job_id
    new_status.save()
  return redirect('detail', job_id=job_id)


@login_required
def delete_status(request, job_id, status_id):
  status = Status.objects.get(id = status_id)
  status.delete()
  return redirect('detail', job_id=job_id)


@login_required
def connections_index(request):
  connections = Connection.objects.filter(user = request.user)
  return render(request, 'connections/index.html', {
    'connections' : connections
  })


@login_required
def connections_detail(request, connection_id):
  connection = Connection.objects.get(id = connection_id)
  interactions = Interaction.objects.filter(connection = connection_id)
  interaction_form = InteractionForm()
  return render(request, 'connections/detail.html', {
    'connection' : connection,
    'interactions' : interactions,
    'interaction_form' : interaction_form
  })


class ConnectionCreate(LoginRequiredMixin, CreateView):
  model = Connection
  form_class = ConnectionForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  

class ConnectionUpdate(LoginRequiredMixin, UpdateView):
  model = Connection
  fields = ['name', 'url', 'location', 'email', 'phone', 'company']
  

class ConnectionDelete(LoginRequiredMixin, DeleteView):
  model = Connection
  success_url = '/connections'


@login_required
def add_interaction(request, connection_id):
  form = InteractionForm(request.POST)
  if form.is_valid():
    new_interaction = form.save(commit=False)
    new_interaction.connection_id = connection_id
    new_interaction.save()
  return redirect('connections_detail', connection_id=connection_id)


@login_required
def delete_interaction(request, connection_id, interaction_id):
  interaction = Interaction.objects.get(id = interaction_id)
  interaction.delete()
  return redirect('connections_detail', connection_id=connection_id)