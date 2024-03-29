from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Регистрирует нового пользователя"""
    if request.method != 'POST':
        # Показывать пустую форму регистрации
        form = UserCreationForm
    else:
        # Обработать заполненную форму
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Выполнить вход и перенаправить на домашнюю страницу приложения
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
