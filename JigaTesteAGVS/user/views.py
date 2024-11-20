from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

class LogoutInterfaceView(LogoutView):
    template_name = 'user/logout.html'

class CustomLoginView(View):
    template_name = 'user/login.html'

    def get(self, request):
        # Renderiza a página inicial com os formulários vazios
        return render(request, self.template_name)

    def post(self, request):
        action = request.POST.get('action')

        if action == 'login':
            # Processar login
            username = request.POST.get('login_username')
            password = request.POST.get('login_password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redireciona para a página inicial
            else:
                return render(request, self.template_name, {
                    'error': 'Credenciais inválidas. Tente novamente.'
                })

        elif action == 'register':
            # Processar registro
            username = request.POST.get('register_username')
            email = request.POST.get('register_email')
            password = request.POST.get('register_password')

            if User.objects.filter(username=email).exists():
                return render(request, self.template_name, {
                    'error': 'Este email já está registrado.'
                })

            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)  # Faz login automático após registro
            return redirect('home')  # Redireciona para a página inicial

        # Se a ação não for válida
        return render(request, self.template_name, {
            'error': 'Ação inválida.'
        })
