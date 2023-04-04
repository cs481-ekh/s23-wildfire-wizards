from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CSVUploadForm
from .models import AdminUser
from .utils import replace_data_with_csv

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})

        return render(request, 'admin_panel/login.html')

    
    
    @login_required
    def dashboard(request):
        if request.method == 'POST':
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                    replace_data_with_csv(request.FILES['file'])
                    # success message
                    return JsonResponse({'success': True})
            else:
                form = CSVUploadForm()

            return render(request, 'admin_panel/dashboard.html', {'form': form})