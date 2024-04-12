from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView, ListView,DetailView,DeleteView,TemplateView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin 
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.views import View
class HomeWorkList(ListView):
    model=HomeWork
    template_name='homework.html'
    context_object_name='homeworks'
    paginate_by=10

class CreateHomeWorkStudents(CreateView):
    model=HomeWork
    form_class=HomeWorkStudent
    template_name='homework_form.html'
    success_url=reverse_lazy('homework_list')

class CreateHomeWorkTeachers(CreateView):
    model=HomeWork
    form_class=HomeWorkFormTeacher
    template_name='homework_form.html'
    success_url=reverse_lazy('homework_list')

class DeleteHomeWork(DeleteView):
    model=HomeWork
    template_name='delete.html'
    success_url=reverse_lazy('homework_list')

class UpdateHomeWorkTeacher(UpdateView):
    model=HomeWork
    form_class=HomeWorkFormTeacher
    template_name='homework_form.html'
    success_url=reverse_lazy('homework_list')

class UpdateHomeWorkStudent(UpdateView):
    model=HomeWork
    form_class=HomeWorkStudent
    template_name='homework_form.html'
    success_url=reverse_lazy('homework_list')
class HomeWorkDetail(DetailView):
    model=HomeWork
    template_name='homework_detail.html'
    context_object_name='homework'
    success_url=reverse_lazy('homework_list')
class BookList(ListView):
    model=Book
    template_name='book.html'
    context_object_name='books'
    paginate_by=10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = Subject.objects.filter(teacher=self.request.user)
        return context

    

class BookDetail(DetailView):
    model=Book
    template_name='book_detail.html'
    context_object_name='book'

class CreateBook(CreateView):
    model=Book
    form_class=BookForm
    template_name='book_form.html'
    success_url=reverse_lazy('book_list')


class DeleteBook(DeleteView):
    model=Book
    template_name='delete.html'
    success_url=reverse_lazy('book_list')

class UpdateBook(UpdateView):
    model=Book
    form_class=BookForm
    template_name='book_form.html'
    success_url=reverse_lazy('book_list')



class Logout(LogoutView):
  next_page=reverse_lazy('home')


class Home(TemplateView):
    template_name='home.html'
class Index(ListView):
    model=CustomUser
    template_name='index.html'
    context_object_name='users'
class VerifyEmailView(View):
    def get(self, request, user_pk, token):
        user = CustomUser.objects.get(pk=user_pk)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your email has been verified')
            return redirect('home')
        else:
            messages.error(request, 'Invalid verification link')
            return redirect('home')
class Login(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('index')
    success_message = 'You are logged in successfully'
class Search(ListView):
    template_name='book.html'
    context_object_name='books'
    paginate_by=5

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get('q'))
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['q']=self.request.GET.get('q')
        return context

class Search1(ListView):
    template_name='homework.html'
    context_object_name='homeworks'
    paginate_by=5

    def get_queryset(self):
        return HomeWork.objects.filter(Title__icontains=self.request.GET.get('q'))
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['q']=self.request.GET.get('q')
        return context

class SingUpView(SuccessMessageMixin, CreateView):
   model=CustomUser
   form_class=SignUpForm
   success_url=reverse_lazy('home')
   template_name='registration.html'
   success_message = 'Account created successfully'
    
   def send_verification_email(self, user):
        token = default_token_generator.make_token(user)
        verify_url = self.request.build_absolute_uri(f'/verify/{user.pk}/{token}/')
        subject = 'Verify your email'
        message = f'Hello {user.username}, please click the link below to verify your email:\n\n{verify_url}'
        send_mail(subject, message, 'studentshub@example.com', [user.email])

   def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object  
        user.is_active = False
        user.save()
        self.send_verification_email(self.object)
        return response


class ProfileView(TemplateView):
    template_name = 'profile.html'

class Mark(TemplateView):
    template_name = 'mark.html'

class Exam(TemplateView):
    template_name = 'exam.html'

class Schedules(TemplateView):
    template_name = 'schedules.html'