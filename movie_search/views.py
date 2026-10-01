from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

import os
from dotenv import load_dotenv

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")




from django.contrib.auth.decorators import login_required
from .models import MovieSearch


@login_required
def movie_info(request):
    movie_info = None
    
    if request.method == 'POST':
        movie_name = request.POST.get('movie_name', '')  
        
        if movie_name:
            
            url = f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_KEY}"
            try:
                response = requests.get(url)
                data = response.json()  
                
                if data.get('Response') == 'True':
                    movie_info = data

                   
                    MovieSearch.objects.create(user=request.user, movie_name=movie_name)
                else:
                    movie_info = {'error': 'Movie not found'}
            except Exception as e:
                movie_info = {'error': f'Error fetching data: {str(e)}'}
    
    return render(request, 'index.html', {'movie_info': movie_info})



from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')









class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['movie_searches'] = MovieSearch.objects.filter(user=self.request.user).order_by('-search_time')
        return context

