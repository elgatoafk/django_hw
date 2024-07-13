from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote
from django.views.generic.base import TemplateView
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin




@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})




@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})


def all_quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'all_quotes.html', {'quotes': quotes})



class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    html_email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('registration:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'registration/password_reset_subject.txt'


def author_detail_view(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'author_detail.html', {'author': author})
